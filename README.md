# AEO/GEO Prompt Audit

## Problem Statement
As students increasingly turn to Artificial Intelligence Answer Engines (like ChatGPT, Perplexity, Gemini, and Google AI Overviews) for advice on colleges and coding programs, it is critical for educational platforms to understand their AI visibility. This experiment measures how often AI engines mention the target platform, cite its official or third-party properties, and accurately describe its offerings. The goal is to identify gaps in AI Overviews (AEO) and Generative Engine Optimization (GEO) to ensure prospective students receive accurate and helpful information.

## Method
* **Setup:** All queries were run on the same day (2026-09-28) using a fresh incognito session to minimize personalization.
* **Engines Tested:** ChatGPT, Gemini
* **Prompting:** The exact wording of each prompt was used, and only the first generated answer was analyzed.
* **Evaluation Criteria:**
  * **Mentioned:** Did the engine explicitly name the platform or its specific programs?
  * **Accurate:** Was the description of the platform's programs, fees, and outcomes factually correct?
  * **Official Cited:** Did the engine cite a direct link to the official website?
  * **Third-Party Cited:** Did the engine cite reviews, articles, or other external sites mentioning the platform?

## How to Reproduce
1. Clone this repository: `git clone https://github.com/HARI24VEDHA/AEO_GEO_Prompt_Audit.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your manual evaluation results to `data/results.csv`.
4. Run the analysis script: `python src/analyze.py`
5. Generate the charts: `python src/charts.py`
6. Check the `outputs/` folder for generated CSV summaries and PNG charts.

## Findings
*(Based on 10 manually evaluated responses across 5 prompts × 2 engines, run on 2026-09-28)*

### Engine Summary

| Engine  | Answers Logged | Visibility Share (%) | Accuracy Rate (%) | Official Page Cited | Third-Party Cited |
|---------|---------------|---------------------|------------------|--------------------|--------------------|
| ChatGPT | 5             | 100%                | 100%             | 0                  | 0                  |
| Gemini  | 5             | 80%                 | 75%              | 0                  | 0                  |

### Visibility Share by Category

| Category     | ChatGPT | Gemini |
|--------------|---------|--------|
| Brand        | 100%    | 100%   |
| Placement    | 100%    | 0%     |
| Fees & Details | 100% | 100%   |

### Top Competitors Surfaced by AI Engines
1. Scaler Academy (most frequent)
2. Coding Ninjas
3. Crio.do
4. Masai School
5. AlmaBetter
6. Newton School
7. PW Skills
8. LogicMojo

### Most-Cited Domains
Neither ChatGPT nor Gemini cited any external URLs or the official website in any of the 10 responses tested.

### Key Observations
1. **ChatGPT** mentions and accurately describes the platform in 100% of brand, placement, and fees queries — but **never links to the official website**.
2. **Gemini** completely omits the platform from a generic "best coding programs for placements" query — a significant visibility gap.
3. **Gemini's response to "Is it legit?"** contains unverified negative claims (e.g., alleging paid reviews) presented as facts — a potential reputation risk.
4. **Neither engine ever cited the official website** across all 10 responses, meaning students have no direct path to official information from AI answers.
5. **Scaler Academy** is the most frequently surfaced competitor across both engines.

## Recommended Fixes

| Gap Identified | Hypothesis | Recommended Page Change |
|---|---|---|
| Official website never cited by either engine | AI engines cite sources they can crawl and verify; the official site may lack structured, crawlable FAQ content | Add dedicated FAQ pages on the official site with direct answers to common student questions (e.g., "Is NxtWave legit?", "What are the fees?") using structured data / schema markup |
| Gemini omits the platform from generic placement queries | The platform is under-represented on third-party review and comparison sites that Gemini trusts as sources | Get listed on credible review and comparison sites (e.g., Shiksha, AmbitionBox, G2, Coursera reviews) that AI engines already trust and cite |
| Gemini's "legit" response contains unverified negative claims | AI engines aggregate user-generated content from Reddit, forums, and blogs; negative forum threads are being weighted heavily | Publish well-documented, factual case studies and placement outcome reports on the official site to provide credible counter-sources for AI engines to reference |
| No third-party citations in any response | Independent blog posts, YouTube reviews, and news articles about the platform may be sparse or poorly indexed | Encourage authentic student testimonials and press coverage; ensure third-party content mentions the official domain for citation linking |

*(Note: Only legitimate optimizations are recommended — rewriting direct-answer content, correcting outdated facts, and improving listings on review sites that engines already trust.)*

## Limitations
* **Sample Size:** The current test set covers 5 prompts × 2 engines = 10 data points. The full audit covers 30 prompts × 4 engines.
* **Variability:** AI engine responses may vary by time, location, and slight differences in prompt phrasing.
* **Personalization:** Despite using incognito mode, completely isolating the query from systemic personalization algorithms is difficult.
* **Snapshot in Time:** Results reflect a single-day run on 2026-09-28 and may not represent long-term AI behaviour.

## Next Steps
1. Complete testing across all 30 prompts and remaining engines (Perplexity, Google AI Overviews).
2. Implement the recommended fixes (FAQ pages, structured data, third-party listings).
3. Re-run the exact same prompts after fixes and compare new visibility and accuracy scores against this baseline.
