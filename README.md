# Stats_CAT_2.1

Comprehensive, reproducible solution notebook for the MSTA 6102 CAT (Statistics). The notebook combines manual epidemiological derivations, executable Python code, regression modelling, and publication-ready outputs.

## Getting started

1. Create/activate a Python 3 environment with write access to this repository.
2. Launch JupyterLab/Jupyter Notebook and open `MSTA_6102_CAT_Stats.ipynb`.
3. Run all cells from top to bottom. The setup cell checks for required packages and reports any that need installation (`numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `sklearn`, `ipywidgets`, `nbconvert`, `weasyprint`, `fpdf`).
4. All artefacts are written to the `outputs/` directory.

## Key notebook features

- Manual LaTeX derivations and code-verification for Questions 1–2.
- Logistic and Poisson/Negative Binomial modelling pipeline for Question 3 with diagnostics (ROC, calibration, VIF, dispersion checks).
- Bootstrap alternatives, sensitivity simulation, optional widgets, and clean-up helper.
- Automated tests to verify published point estimates.
- Auto-export of reveal.js slides and a one-page results brief (Markdown + PDF).

## Generated artefacts

Running the notebook produces (non-exhaustive list):

- `outputs/q1_summary_measures.csv` — Risk difference, relative risk, odds ratio with CIs for Question 1.
- `outputs/q1_inference_tests.csv` — Chi-square, Fisher, and phi statistics.
- `outputs/q1_fatality_prevalence.png`, `outputs/q1_residual_heatmap.png`, `outputs/q1_forest_plot.png`, `outputs/q1_rr_or_sensitivity.png` — Visual diagnostics and sensitivity figure.
- `outputs/q2_summary_measures.csv` — Case–control odds ratio/CI summary.
- `outputs/q3_logistic_or_table.csv`, `outputs/q3_model_coefficients.csv`, `outputs/q3_results.md` — Logistic modelling outputs.
- `outputs/results_one_page.md`, `outputs/results_one_page.pdf` — Publication-style summary.
- `outputs/MSTA_6102_CAT_Slides.html` — Reveal.js slide deck (if `EXPORT_SLIDES=True`).
- `outputs/outputs_index.csv` — Catalog of files produced in the latest run.

Use the optional clean-up cell inside the notebook to archive or reset the `outputs/` directory once you have collected the desired artefacts.
