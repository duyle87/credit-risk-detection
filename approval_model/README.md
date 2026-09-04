# Approval Model – LendingClub Underwriting Analytics

## 1. Project overview

This project builds an interpretable model that predicts whether a LendingClub loan application is **accepted (funded)** or **rejected**, using historical application data.

**Key outcome:**  
A logistic regression model that estimates the probability of approval, plus a Tableau dashboard that lets users explore approval patterns and test “what‑if” scenarios.

---

## 2. Business question

**Primary question:**  
Given an applicant’s profile and loan request characteristics, how likely is LendingClub to fund the application?

**Why it matters:**  
- Demonstrates understanding of credit underwriting and selection.  
- Shows ability to turn raw data into a decision‑support tool.  
- Provides a transparent, interpretable model suitable for risk‑focused roles.

---

## 3. Data sources

- **Accepted loans dataset** – all loans funded by LendingClub.  
- **Rejected applications dataset** – all applications declined by LendingClub.  

Both datasets are combined and restricted to **shared columns only** (e.g., requested amount, credit score/risk score, DTI, employment length, state, application date).

> Note: This reflects historical LendingClub decisions, not their current policy.

Raw data files (stored in the repo’s `data/` folder, ignored by Git):

- `../data/accepted.csv`  
- `../data/rejected.csv`

---

## 4. Project structure

```text
approval_model/
│
├── README.md                     # This file
│
├── notebook/
│   └── 01_approval_model_walkthrough.ipynb
│
├── src/
│   ├── 01_combine_data.py
│   ├── 02_clean_features.py
│   ├── 03_train_model.py
│   └── 04_export_tableau_artifacts.py
│
└── outputs/
    ├── lendingclub_combined_raw.csv
    ├── lendingclub_clean.csv
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

Ensure the raw LendingClub files exist in the repo’s `data/` folder:

- `data/accepted.csv`  
- `data/rejected.csv`

The code in this project loads from `../data/`.

### 5.4 Run the pipeline

Option A – Notebook (recommended):

```bash
# From repo root
jupyter notebook approval_model/notebook/01_approval_model_walkthrough.ipynb
```

Option B – Scripts:

```bash
python approval_model/src/01_combine_data.py
python approval_model/src/02_clean_features.py
python approval_model/src/03_train_model.py
python approval_model/src/04_export_tableau_artifacts.py
```

These steps generate all files in `approval_model/outputs/`.

---

## 6. What to inspect (recruiter checklist)

### 6.1 Business framing

- This README: **Section 2 – Business question**  
  - Is the target clearly defined (accepted vs. rejected)?  
  - Are scope and limitations stated?

### 6.2 Data preparation

- Notebook or `src/01_combine_data.py`  
  - How accepted and rejected files are loaded.  
  - How shared columns are identified and selected.  
  - How the `accepted` label is created.

- Output: `outputs/lendingclub_combined_raw.csv`  
  - Check that both accepted and rejected rows are present.  
  - Verify feature list matches the description.

### 6.3 Feature selection & cleaning

- Notebook or `src/02_clean_features.py`  
  - Which columns are kept/dropped and why.  
  - How missing values are handled.  
  - Any transformations (e.g., FICO mid, employment length).

- Output: `outputs/lendingclub_clean.csv`

### 6.4 Modeling approach

- Notebook or `src/03_train_model.py`  
  - Why logistic regression was chosen (interpretability, scorecard‑style).  
  - Train/test split strategy (random vs. time‑based).  
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
  - Used in Tableau to show which factors increase/decrease approval odds.

### 6.7 Scored dataset

- Output: `outputs/lendingclub_scored.csv`  
  - Contains:
    - Key features (FICO, DTI, loan amount, employment length, state, year, etc.)  
    - `actual_accepted` (0/1)  
    - `p_accepted` (predicted probability)  

This file powers most of the analytics in the Tableau dashboard.

### 6.8 Tableau dashboard

- File: `../tableau/approval_dashboard.twbx` (or published link)

Key views:

1. **Model performance**
   - AUC and other metrics.  
   - ROC curve.  
   - Confusion matrix at a chosen threshold.

2. **Approval probability calculator**
   - Interactive parameters for FICO, DTI, loan amount, employment length.  
   - Displays predicted probability of approval using the model coefficients.

3. **Acceptance rate analytics**
   - Acceptance rate by FICO band, DTI band, state, and year.  
   - Filters to slice the population.

4. **Model logic**
   - Coefficient / odds ratio chart.  
   - Short explanation of direction and magnitude of effects.

---

## 7. Modeling details (summary)

- **Model type:** Logistic regression (L2 regularization).  
- **Target:** `accepted` (1 = funded, 0 = rejected).  
- **Features (examples):**
  - `fico_mid` (midpoint of FICO range)  
  - `dti`  
  - `loan_amnt`  
  - `emp_length`  
  - `addr_state`  
  - `year` / `month` of application  

- **Validation:**
  - Train/test split (time‑based or random).  
  - Primary metric: AUC‑ROC.  
  - Secondary metrics: accuracy, precision, recall, F1, Brier score.

Full details are in the notebook and modeling script.

---

## 8. Key findings (placeholders – replace with your results)

- Higher credit scores are strongly associated with higher odds of approval.  
- Higher DTI reduces the likelihood of acceptance.  
- Larger requested loan amounts slightly reduce approval odds, all else equal.  
- Acceptance rates have changed over time, reflecting evolving underwriting standards.  
- The model achieves an AUC‑ROC of **X.XX** on the test set.

---

## 9. Limitations

- The data reflects **historical** LendingClub decisions, not current policy.  
- Some important underwriting variables may be missing or inconsistently defined across accepted/rejected files.  
- The model is designed for **demonstration and learning**, not for real lending decisions.  
- Geographic and demographic fairness analysis is limited by available fields.

---

## 10. How this project maps to role expectations

This project demonstrates:

- **Data engineering:** Combining and cleaning large CSVs, documenting transformations.  
- **Modeling:** Building and evaluating an interpretable classification model.  
- **Risk thinking:** Understanding selection, underwriting, and probability outputs.  
- **Communication:** Clear README, structured notebook, and recruiter checklist.  
- **Visualization:** Tableau dashboard that translates model outputs into interactive business insights.

---

## 11. Next steps

Potential extensions:

- Add calibration analysis and fairness checks.  
- Incorporate more advanced features (e.g., credit history aggregates).  
- Deploy the dashboard (Tableau Public or hosted) and link it here.