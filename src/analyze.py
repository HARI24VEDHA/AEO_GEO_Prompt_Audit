import pandas as pd
import sys
import os
from collections import Counter
import urllib.parse

def main():
    results_path = "data/results.csv"
    prompts_path = "data/prompts.csv"
    
    if not os.path.exists(results_path) or not os.path.exists(prompts_path):
        print("Error: Required data files not found.")
        return

    try:
        results = pd.read_csv(results_path, dtype=str)
        prompts = pd.read_csv(prompts_path, dtype=str)
    except Exception as e:
        print(f"Error loading CSV files: {e}")
        return

    if results.empty:
        print("Results file is empty. Please add data to data/results.csv to see the analysis.")
        return

    # Validation
    yes_no_cols = ['nxtwave_mentioned', 'official_page_cited', 'third_party_site_cited']
    yes_no_na_cols = ['described_accurately']
    
    errors = []
    
    for col in yes_no_cols:
        if col in results.columns:
            invalid = results[~results[col].isin(['Yes', 'No', pd.NA]) & results[col].notna()]
            if not invalid.empty:
                errors.append(f"Invalid values in {col}. Must be Yes or No.")
                
    for col in yes_no_na_cols:
        if col in results.columns:
            invalid = results[~results[col].isin(['Yes', 'No', 'NA', pd.NA]) & results[col].notna()]
            if not invalid.empty:
                errors.append(f"Invalid values in {col}. Must be Yes, No, or NA.")

    unknown_prompts = set(results['prompt_id']) - set(prompts['prompt_id'])
    if unknown_prompts:
        errors.append(f"Unknown prompt_ids found in results: {unknown_prompts}")

    duplicates = results.duplicated(subset=['prompt_id', 'engine'])
    if duplicates.any():
        errors.append("Duplicate prompt_id + engine combinations found.")

    if errors:
        print("Validation errors found in data/results.csv:")
        for error in errors:
            print(f"- {error}")
        return

    # Merge categories
    df = results.merge(prompts[['prompt_id', 'category', 'prompt']], on='prompt_id', how='left')

    # Compute metrics per engine
    engines = df['engine'].unique()
    summary = []
    
    gaps = []
    all_competitors = []
    all_domains = []

    for engine in engines:
        edf = df[df['engine'] == engine]
        answers_logged = len(edf)
        mentions = edf[edf['nxtwave_mentioned'] == 'Yes']
        mention_count = len(mentions)
        visibility_share = (mention_count / answers_logged * 100) if answers_logged > 0 else 0
        
        accuracy_count = len(mentions[mentions['described_accurately'] == 'Yes'])
        accuracy_rate = (accuracy_count / mention_count * 100) if mention_count > 0 else 0
        
        official_cited = len(edf[edf['official_page_cited'] == 'Yes'])
        third_party_cited = len(edf[edf['third_party_site_cited'] == 'Yes'])

        summary.append({
            'Engine': engine,
            'Answers Logged': answers_logged,
            'NxtWave Mentioned': mention_count,
            'Visibility Share (%)': round(visibility_share, 2),
            'Accuracy Rate (%)': round(accuracy_rate, 2),
            'Official Page Cited': official_cited,
            'Third-Party Cited': third_party_cited
        })
        
        # Gaps
        for _, row in edf.iterrows():
            if row['nxtwave_mentioned'] == 'No' or row['described_accurately'] == 'No':
                gaps.append({
                    'engine': engine,
                    'prompt_id': row['prompt_id'],
                    'category': row['category'],
                    'prompt': row['prompt'],
                    'issue': 'Not mentioned' if row['nxtwave_mentioned'] == 'No' else 'Inaccurate'
                })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv("outputs/summary.csv", index=False)
    
    print("\n### Engine Summary ###\n")
    print(summary_df.to_markdown(index=False))

    if gaps:
        gaps_df = pd.DataFrame(gaps)
        gaps_df.to_csv("outputs/gaps.csv", index=False)
        print(f"\nGenerated outputs/gaps.csv with {len(gaps)} gap(s).")

    # Visibility share by category
    print("\n### Visibility Share by Category ###\n")
    cat_summary = []
    for cat in df['category'].dropna().unique():
        cdf = df[df['category'] == cat]
        mentions = len(cdf[cdf['nxtwave_mentioned'] == 'Yes'])
        share = (mentions / len(cdf) * 100) if len(cdf) > 0 else 0
        cat_summary.append({'Category': cat, 'Visibility Share (%)': round(share, 2)})
    
    cat_df = pd.DataFrame(cat_summary)
    print(cat_df.to_markdown(index=False))

    # Competitors and Domains
    for _, row in df.iterrows():
        if pd.notna(row['competitors_shown']) and row['competitors_shown'].strip():
            comps = [c.strip() for c in row['competitors_shown'].split(',')]
            all_competitors.extend(comps)
        
        if pd.notna(row['sources_cited']) and row['sources_cited'].strip():
            urls = [u.strip() for u in row['sources_cited'].split(',')]
            for url in urls:
                try:
                    domain = urllib.parse.urlparse(url).netloc
                    if domain:
                        all_domains.append(domain)
                except:
                    pass

    print("\n### Top Competitors ###")
    comp_counts = Counter(all_competitors)
    for comp, count in comp_counts.most_common(10):
        print(f"- {comp}: {count}")

    print("\n### Most-Cited Domains ###")
    domain_counts = Counter(all_domains)
    for domain, count in domain_counts.most_common(10):
        print(f"- {domain}: {count}")

if __name__ == "__main__":
    main()
