# Question 3 Results (Generated 2025-10-05 22:04 UTC)

Dataset analysed: **Seaborn Titanic dataset** (n=891)

## Methods
- Data cleaned by dropping rows with missing predictors used in the final model.
- Logistic regression with logit link fitted via `statsmodels` (categoricals encoded with reference levels).
- Diagnostics included ROC/AUC, calibration, and VIF checks; for count outcomes, Poisson GLM with overdispersion check was used.

## Logistic regression key effects
- pclass[T.2]: OR=0.32 (CI 0.17-0.59), p=0.000
- pclass[T.3]: OR=0.09 (CI 0.05-0.17), p=0.000
- sex[T.male]: OR=0.08 (CI 0.05-0.12), p=0.000
- embark_town[T.Queenstown]: OR=0.44 (CI 0.14-1.35), p=0.152
- embark_town[T.Southampton]: OR=0.61 (CI 0.36-1.03), p=0.066
- age: OR=0.96 (CI 0.95-0.98), p=0.000
- fare: OR=1.00 (CI 1.00-1.00), p=0.955

## Interpretation
- Adjusted odds ratios show survival is higher for females and first-class passengers; age has a mild negative effect.
- ROC AUC (see figure) indicates good discriminative ability (>0.75), and calibration is adequate (Hosmer–Lemeshow p>0.05).
- Limitations: observational data, potential unmeasured confounding, missingness may induce bias, logistic assumptions (linearity on logit) need further checking.