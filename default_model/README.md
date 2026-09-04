# Default Model – LendingClub Credit Risk Scorecard

## 1. Project overview

This project builds an interpretable model that predicts whether a **funded** LendingClub loan will **default** (vs. be fully paid). The approach mimics a bank‑style credit risk scorecard using logistic regression.

**Key outcome:**  
A logistic regression model that estimates the probability of default, plus a Tableau dashboard that shows risk segmentation, model performance, and key drivers of default.

---

## 2. Business question

**Primary question:**  
Given a funded loan’s characteristics at origination, how likely is it to default (vs. be fully paid)?

**Why it matters:**  
- Directly relevant to credit risk, financial analysis, and risk‑modeling roles.  
- Demonstrates ability to define a meaningful risk target from loan status.  
- Provides an interpretable, scorecard‑style model aligned with industry practice.

---

## 3. Data sources

- **Accepted loans dataset** – all loans funded by LendingClub.  

Only funded loans are used, because only they have a realized outcome (paid vs. default).

> Note: This reflects historical loan performance, not future guarantees.

Raw data file (stored in the repo’s `data/` folder, ignored by Git):

- `../data/accepted.csv`

---

## 4. Project structure

```text
default_model/
│
├── README.md                     # This file
│
├── notebook/
│   └── 01_default_model_walkthrough.ipynb
│
├── src/
│   ├── 01_load_accepted.py
│   ├── 02_define_default_label.py
│   ├── 03_clean_features.py
│   ├── 04_train_model.py
│   └── 05_export_tableau_artifacts.py
│
└── outputs/
    ├── lendingclub_accepted_clean.csv
    ├── lendingclub_scored.csv
    ├── model_coefficients.csv
    ├── model_metrics.csv
    ├── roc_curve.csv
    └── calibration_curve.csv
```

---

## 5. How to run this project

### 5.1 Requirements

- Python 3.9+  
- Required packages (example `requirements.txt` in repo root or here):

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
```

### 5.2 Setup

```bash
# From repo root
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 5.3 Data placement

Ensure the raw LendingClub accepted file exists:

- `data/accepted.csv`

The code in this project loads from `../data/accepted.csv`.

### 5.4 Run the pipeline

Option A – Notebook (recommended):

```bash
# From repo root
jupyter notebook default_model/notebook/01_default_model_walkthrough.ipynb
```

Option B – Scripts:

```bash
python default_model/src/01_load_accepted.py
python default_model/src/02_define_default_label.py
python default_model/src/03_clean_features.py
python default_model/src/04_train_model.py
python default_model/src/05_export_tableau_artifacts.py
```

These steps generate all files in `default_model/outputs/`.

---

## 6. What to inspect (recruiter checklist)

### 6.1 Business framing

- This README: **Section 2 – Business question**  
  - Is the default target clearly defined?  
  - Are scope and limitations stated?

### 6.2 Data preparation

- Notebook or `src/01_load_accepted.py` and `src/02_define_default_label.py`  
  - How `accepted.csv` is loaded.  
  - How `loan_status` is mapped to a binary default label (e.g., Charged Off / Fully Paid).  
  - How ongoing/current loans are handled (excluded or treated separately).

- Output: `outputs/lendingclub_accepted_clean.csv`  
  - Check that the target definition matches the description.

### 6.3 Feature selection & cleaning

- Notebook or `src/03_clean_features.py`  
  - Which columns are kept/dropped and why.  
  - How missing values are handled.  
  - Any transformations (e.g., FICO mid, DTI bins, income bins).

### 6.4 Modeling approach

- Notebook or `src/04_train_model.py`  
  - Why logistic regression was chosen (interpretability, scorecard‑style).  
  - Train/test split strategy (random vs. time‑based by origination date).  
  - Regularization settings.

### 6.5 Model evaluation

- Output: `outputs/model_metrics.csv`  
  - AUC‑ROC, accuracy, precision, recall, F1, Brier score, etc.

- Output: `outputs/roc_curve.csv`  
  - Used in Tableau to plot the ROC curve.

- (Optional) `outputs/calibration_curve.csv`  
  - Used to assess probability calibration.

### 6.6 Model interpretation

- Output: `outputs/model_coefficients.csv`  
  - Feature names, coefficients, odds ratios.  
  - Used in Tableau to show which factors increase/decrease default odds.

### 6.7 Scored dataset

- Output: `outputs/lendingclub_scored.csv`  
  - Contains:
    - Key features (FICO, DTI, loan amount, employment length, grade, purpose, etc.)  
    - `actual_default` (0/1)  
    - `p_default` (predicted probability)  

This file powers most of the analytics in the Tableau dashboard.

### 6.8 Tableau dashboard

- File: `../tableau/default_dashboard.twbx` (or published link)

Key views:

1. **Model performance**
   - AUC and other metrics.  
   - ROC curve.  
   - Confusion matrix at a chosen threshold.

2. **Risk segmentation**
   - Distribution of predicted default probabilities.  
   - Actual default rate by predicted risk bucket.

3. **Feature insights**
   - Coefficient / odds ratio chart.  
   - Default rates by grade, purpose, FICO band, DTI band, etc.

4. **What‑if analysis (optional)**
   - Sliders for key features showing impact on predicted default probability.

---

## 7. Modeling details (summary)

- **Model type:** Logistic regression (L2 regularization).  
- **Target:** Binary default indicator derived from `loan_status`  
  - `default = 1` for statuses like “Charged Off”, “Default”, severe delinquency.  
  - `default = 0` for “Fully Paid”, “Paid Off”.  
- **Features (examples):**
  - `fico_mid`  
  - `dti`  
  - `loan_amnt`  
  - `int_rate`  
  - `grade` / `sub_grade` (encoded)  
  - `purpose`, `home_ownership`, `emp_length`, etc.

- **Validation:**
  - Train/test split (ideally time‑based by origination date).  
  - Primary metric: AUC‑ROC.  
  - Secondary metrics: accuracy, precision, recall, F1, Brier score.

Full details are in the notebook and modeling script.

---

## 8. Key findings (placeholders – replace with your results)

- Lower credit scores and higher DTI are strongly associated with higher default risk.  
- Higher interest rates and risk grades correspond to higher predicted and actual default rates.  
- The model achieves an AUC‑ROC of **X.XX** on the test set, indicating good discrimination between paid and defaulted loans.  
- Predicted risk buckets show monotonic increases in actual default rates.

---

## 9. Limitations

- The data reflects **historical** loan performance, not future guarantees.  
- Some loans may still be “Current” at the time of extraction; handling of these loans affects labels.  
- The model is designed for **demonstration and learning**, not for real lending decisions.  
- Certain borrower‑level details (e.g., full credit history) are not available.

---

## 10. How this project maps to role expectations

This project demonstrates:

- **Data engineering:** Cleaning and labeling loan data with a clear risk definition.  
- **Modeling:** Building and evaluating an interpretable credit risk model.  
- **Risk thinking:** Translating loan status into a meaningful default target and risk score.  
- **Communication:** Clear README, structured notebook, and recruiter checklist.  
- **Visualization:** Tableau dashboard that communicates risk segmentation and model logic.

---

## 11. Next steps

Potential extensions:

- Refine default definition (e.g., include severe delinquency, exclude very recent loans).  
- Add score scaling (e.g., 300–850 score) and policy‑based cutoffs.  
- Incorporate more advanced features or time‑to‑event modeling.  
- Deploy the dashboard (Tableau Public or hosted) and link it here.