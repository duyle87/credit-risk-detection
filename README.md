# Credit Risk Detection – LendingClub Models

Credit and risk analytics for LendingClub-style loan portfolio analysis, including probability-of-default modeling, underwriting analytics, vintage performance, concentration risk, and recession stress testing.

This repository contains two complementary modeling projects using LendingClub data:

1. **Approval Model** – Predicts whether a loan application is accepted (funded) or rejected.  
2. **Default Model** – Predicts whether a funded loan will default (vs. be fully paid).

Both projects share the same underlying data source but answer different business questions and use separate code, documentation, and outputs.

---

## Projects

### 1. Approval Model (Underwriting Analytics)

- **Folder:** [`approval_model/`](./approval_model)  
- **Question:** Given applicant and loan-request characteristics, how likely is LendingClub to fund the application?  
- **Data:** Accepted + rejected applications, restricted to shared columns.  
- **Model:** Interpretable logistic regression.  
- **Outputs:** Model metrics, coefficients, ROC curve, scored dataset, Tableau dashboard.

👉 Start here: [`approval_model/README.md`](./approval_model/README.md)

---

### 2. Default Model (Credit Risk Scorecard)

- **Folder:** [`default_model/`](./default_model)  
- **Question:** Given a funded loan, how likely is it to default (vs. be fully paid)?  
- **Data:** Accepted (funded) loans only.  
- **Model:** Interpretable logistic regression (scorecard-style).  
- **Outputs:** Model metrics, coefficients, ROC curve, scored dataset, Tableau dashboard.

👉 Start here: [`default_model/README.md`](./default_model/README.md)

---

## Shared Data

- Raw LendingClub CSVs are stored in:  
  - `data/accepted.csv` – funded loans  
  - `data/rejected.csv` – declined applications  

These files are typically large and are ignored by Git (see `.gitignore`). Each project’s scripts load from this `data/` folder.

---

## Tech Stack

- **Language:** Python  
- **Libraries:** pandas, numpy, scikit-learn  
- **Visualization / Dashboard:** Tableau  
- **Version Control:** Git + GitHub

---

## Repository Structure

```text
credit-risk-detection/
│
├── README.md                     # This file
├── .gitignore
│
├── data/
│   ├── accepted.csv
│   └── rejected.csv
│
├── approval_model/
│   ├── README.md
│   ├── notebook/
│   ├── src/
│   └── outputs/
│
├── default_model/
│   ├── README.md
│   ├── notebook/
│   ├── src/
│   └── outputs/
│
└── tableau/
    ├── approval_dashboard.twbx
    └── default_dashboard.twbx
```

---

## Author

Damien Le  
[Your LinkedIn / Portfolio Link]  
[Your Email]