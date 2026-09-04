# Credit Risk Detection – LendingClub Models

This repository contains two complementary credit-risk and underwriting modeling projects built with historical LendingClub loan-application data.

1. **Approval Model** – Predicts whether a loan application is accepted (funded) or rejected.  
2. **Default Model** – Predicts whether a funded loan will default versus be fully paid.

Both projects use the same LendingClub data source but answer different business questions. Each project has separate documentation, code, modeling outputs, and Tableau reporting artifacts.

---

## Projects

### 1. Approval Model – Underwriting Analytics

- **Folder:** [`approval_model/`](./approval_model)  
- **Business question:** Given applicant and loan-request characteristics, how likely is LendingClub to fund the application?  
- **Data:** Accepted and rejected applications, limited to fields available in both datasets.  
- **Model:** Interpretable logistic regression.  
- **Planned outputs:** Model metrics, coefficients, ROC curve, scored dataset, and Tableau underwriting dashboard.

[View the Approval Model documentation →](./approval_model/README.md)

---

### 2. Default Model – Credit Risk Scorecard

- **Folder:** [`default_model/`](./default_model)  
- **Business question:** Given a funded loan’s characteristics at origination, how likely is it to default versus be fully paid?  
- **Data:** Funded LendingClub loans only.  
- **Model:** Interpretable logistic regression using a scorecard-style approach.  
- **Planned outputs:** Model metrics, coefficients, ROC curve, scored dataset, and Tableau credit-risk dashboard.

[View the Default Model documentation →](./default_model/README.md)

---

## Data Setup

The full raw LendingClub datasets are excluded from version control because they are several gigabytes in size.

Download the historical LendingClub accepted and rejected loan-application files independently, then store them locally using this structure:

```text
data/
└── raw/
    ├── accepted_2007_to_2018Q4.csv
    └── rejected_2007_to_2018Q4.csv
```

The `data/` directory is excluded through `.gitignore`. This means the source data remains local and is not uploaded to GitHub.

---

## Tech Stack

- **Language:** Python  
- **Core libraries:** pandas, numpy, scikit-learn  
- **Interactive reporting:** Tableau  
- **Version control:** Git and GitHub  

---

## Repository Structure

```text
credit-risk-detection/
│
├── README.md
├── .gitignore
│
├── data/                         # Local only; excluded from Git
│   └── raw/
│       ├── accepted_2007_to_2018Q4.csv
│       └── rejected_2007_to_2018Q4.csv
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

## Project Principles

- Use **separate modeling pipelines** for approval and default prediction.  
- Use only information available at the relevant decision point to avoid data leakage.  
- Prioritize interpretable logistic-regression models over black-box approaches.  
- Evaluate models on held-out data using discrimination and probability-quality metrics.  
- Translate outputs into interactive Tableau dashboards for business users.  
- Treat all results as historical analytical demonstrations, not lending recommendations or current LendingClub policy.

---

## Author

Damien Le  
[LinkedIn](YOUR_LINKEDIN_URL)  
[Portfolio](YOUR_PORTFOLIO_URL)