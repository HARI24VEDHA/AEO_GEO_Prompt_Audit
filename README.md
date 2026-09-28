# AEO/GEO Prompt Audit: NxtWave

## Problem Statement
As students increasingly turn to Artificial Intelligence Answer Engines (like ChatGPT, Perplexity, Gemini, and Google AI Overviews) for advice on colleges and coding programs, it is critical for educational platforms to understand their AI visibility. This experiment measures how often AI engines mention NxtWave, cite its official or third-party properties, and accurately describe its offerings. The goal is to identify gaps in AI Overviews (AEO) and Generative Engine Optimization (GEO) to ensure prospective students receive accurate and helpful information.

## Method
* **Setup:** All queries were run on the same day using a fresh or incognito session to minimize personalization.
* **Prompting:** The exact wording of each prompt was used, and only the first generated answer was analyzed.
* **Evaluation Criteria:**
  * **Mentioned:** Did the engine explicitly name "NxtWave" or "CCBP"?
  * **Accurate:** Was the description of NxtWave's programs, fees, and outcomes factually correct?
  * **Official Cited:** Did the engine cite a direct link to `ccbp.in`?
  * **Third-Party Cited:** Did the engine cite reviews, articles, or other external sites mentioning NxtWave?

## How to Reproduce
1. Clone this repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your manual evaluation results to `data/results.csv`.
4. Run the analysis script: `python src/analyze.py`
5. Generate the charts: `python src/charts.py`
6. Check the `outputs/` folder for generated CSV summaries and PNG charts.

## Findings
* **Visibility Share:** [TO BE FILLED AFTER RUN]
* **Accuracy Rate:** [TO BE FILLED AFTER RUN]
* **Most Cited Domains:** [TO BE FILLED AFTER RUN]
* **Top Competitors Shown:** [TO BE FILLED AFTER RUN]

## Recommended Fixes
| Gap Identified | Hypothesis | Recommended Page Change |
| --- | --- | --- |
| [TO BE FILLED AFTER RUN] | [TO BE FILLED AFTER RUN] | [TO BE FILLED AFTER RUN] |

*(Note: We will only recommend legitimate optimizations such as rewriting direct-answer content, correcting outdated facts on our own site, and improving listings on review sites that the engines already trust.)*

## Limitations
* **Sample Size:** The test set is limited to 30 prompts.
* **Variability:** AI engine responses may vary by time, location, and slight differences in prompt phrasing.
* **Personalization:** Despite using incognito mode, completely isolating the query from systemic personalization algorithms is difficult.

## Next Steps
After implementing the recommended fixes, we plan to re-run the exact same prompts and compare the new visibility and accuracy scores against the baseline established here.
