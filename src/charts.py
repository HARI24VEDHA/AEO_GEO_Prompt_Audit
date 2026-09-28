import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib.parse
from collections import Counter

def main():
    results_path = "data/results.csv"
    prompts_path = "data/prompts.csv"
    
    if not os.path.exists(results_path) or not os.path.exists(prompts_path):
        print("Data files missing. Cannot generate charts.")
        return

    try:
        results = pd.read_csv(results_path, dtype=str)
        prompts = pd.read_csv(prompts_path, dtype=str)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if results.empty:
        print("Results file is empty. Skipping charts generation.")
        return

    os.makedirs("outputs", exist_ok=True)
    df = results.merge(prompts[['prompt_id', 'category']], on='prompt_id', how='left')

    # Visibility by engine
    engines = df['engine'].unique()
    engine_shares = []
    for engine in engines:
        edf = df[df['engine'] == engine]
        mentions = len(edf[edf['nxtwave_mentioned'] == 'Yes'])
        share = (mentions / len(edf) * 100) if len(edf) > 0 else 0
        engine_shares.append((engine, share))
    
    if engine_shares:
        e_df = pd.DataFrame(engine_shares, columns=['Engine', 'Visibility'])
        e_df.set_index('Engine').plot(kind='bar', legend=False, color='skyblue', edgecolor='black')
        plt.title('Visibility Share by Engine')
        plt.ylabel('Visibility Share (%)')
        plt.tight_layout()
        plt.savefig('outputs/visibility_by_engine.png')
        plt.close()
        print("Saved outputs/visibility_by_engine.png")

    # Visibility by category
    categories = df['category'].dropna().unique()
    cat_shares = []
    for cat in categories:
        cdf = df[df['category'] == cat]
        mentions = len(cdf[cdf['nxtwave_mentioned'] == 'Yes'])
        share = (mentions / len(cdf) * 100) if len(cdf) > 0 else 0
        cat_shares.append((cat, share))
        
    if cat_shares:
        c_df = pd.DataFrame(cat_shares, columns=['Category', 'Visibility'])
        c_df.set_index('Category').plot(kind='bar', legend=False, color='lightgreen', edgecolor='black')
        plt.title('Visibility Share by Category')
        plt.ylabel('Visibility Share (%)')
        plt.tight_layout()
        plt.savefig('outputs/visibility_by_category.png')
        plt.close()
        print("Saved outputs/visibility_by_category.png")

    # Most cited domains
    all_domains = []
    for _, row in df.iterrows():
        if pd.notna(row['sources_cited']) and row['sources_cited'].strip():
            urls = [u.strip() for u in row['sources_cited'].split(',')]
            for url in urls:
                try:
                    domain = urllib.parse.urlparse(url).netloc
                    if domain:
                        all_domains.append(domain)
                except:
                    pass
    
    if all_domains:
        domain_counts = Counter(all_domains).most_common(10)
        domains, counts = zip(*domain_counts)
        plt.barh(domains, counts, color='coral', edgecolor='black')
        plt.title('Most-Cited Domains')
        plt.xlabel('Citation Count')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('outputs/most_cited_domains.png')
        plt.close()
        print("Saved outputs/most_cited_domains.png")

if __name__ == "__main__":
    main()
