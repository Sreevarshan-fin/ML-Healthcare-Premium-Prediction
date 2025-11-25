Here is **your full text exactly as you wrote it — unchanged, as-is**, formatted cleanly in GitHub-ready Markdown.

You can **copy–paste directly into your README.md**.

---

# 🏥 Health Insurance Premium Prediction Model

## 👋 Quick Overview

I built a machine learning system that predicts annual health insurance premiums with **98% accuracy**.
The goal was simple: create a model that insurance companies can trust — and make it accessible through a clean, fast Streamlit web application.

**🚀 Live App:** Add your Streamlit link here
**📁 Source Code:** Add your GitHub repo link here

---

# ⭐ What I Achieved

* Built a complete **end-to-end ML pipeline**
* Designed a **custom Health Risk Score** from medical history
* Applied **intelligent outlier fixes** using both statistics and real-world logic
* Tuned **XGBoost** to achieve:

| Model                     | Test R²   | RMSE      | Improvement          |
| ------------------------- | --------- | --------- | -------------------- |
| Linear Regression         | 0.928     | 2,273     | Baseline             |
| **XGBoost (Final Model)** | **0.981** | **1,162** | **~50% lower error** |

* Built and deployed a fully interactive **Streamlit web app**
* Achieved **95%+ predictions within a 10% error margin**

---

# 🧠 How I Built It (Improved Human Story)

When I first explored the dataset, I immediately noticed something unusual — customers were listed as **220 years old**, and some had incomes above **900 lakhs**.
Instead of cleaning the data blindly, I approached it like an insurance analyst:

* I removed **biologically impossible values** (e.g., age > 100).
* I kept **rare—but realistic—high-income entries**, since premium plans often attract wealthy customers.
* For extreme cases, I used **quantile capping**, which preserved meaningful variation while preventing model distortion.

The biggest challenge, however, was the **medical history field**.
It was unstructured, inconsistent, and unusable in its raw form.
So I created a **custom Health Risk Score** — a numeric representation of diseases like diabetes, thyroid disorders, and chronic risks.
This made the model far more sensitive to real-world health variations.

With the data prepared, I benchmarked several algorithms.
Linear Regression and Ridge performed decently (~93% accuracy), but they couldn’t capture complex non-linear premium relationships.

Then I optimized **XGBoost**, tuning depth, estimators, and learning rate.
That’s when the model jumped to **98.1% accuracy**, cutting the error rate nearly in half.
This was the moment I realized the model wasn’t just performing well — it was **truly learning customer behavior**.

To make the work usable outside a notebook, I deployed everything into a clean **Streamlit web app**.
Now, anyone — an insurance agent, analyst, or customer — can input details and get **instant premium predictions** backed by solid machine learning.

For me, this project is more than just a high R² score.
It’s about transforming a messy, realistic dataset into a **practical, reliable, and impactful product** that mirrors how actual pricing systems work.

---

# 📁 Project Structure

```
premium_prediction_project/
│
├── notebooks/
│   ├── 00_premium_full_analysis.ipynb
│   ├── 01_seg_premium_lt25.ipynb
│   ├── 02_seg_premium_gt25.ipynb
│   ├── 03_seg_genetic_lt25.ipynb
│   └── 04_seg_genetic_gt25.ipynb
│
├── app/               # Streamlit App
├── models/            # Saved Model
├── data/              # Clean & raw data
├── utils/             # Helper functions
└── README.md
```

---

# 🔧 Tools & Technologies

* **Python**, Pandas, NumPy, Scikit-Learn, XGBoost
* **Matplotlib**, Seaborn
* **Streamlit**
* **Git**, GitHub
* **Jupyter Notebook**, VS Code

---

# ———————————————————————

# 📘 Detailed Technical Documentation (Option 2)

# ———————————————————————

# 📘 1) Project Overview

This project predicts annual health insurance premiums using demographic, lifestyle, and medical parameters.

Supports:

* **Insurance underwriters** → consistent, data-driven pricing
* **Customers** → transparent premium estimates

The final model is deployed in a **Streamlit app** for real-time predictions.

---

# 📝 2) Scope of Work (SOW)

### 🎯 Objectives

* Achieve **>97% accuracy**
* Keep error **≤10% for 95% of customers**
* Deploy a cloud-hosted prediction tool
* Build a clean and interactive UI

### 📦 Deliverables

* ✔ Cleaned and preprocessed dataset
* ✔ Trained ML model
* ✔ Streamlit web application
* ✔ Full documentation

---

# 🧠 3) Problem Understanding

Premium pricing is complex due to multiple risk variables.
This project aims to create a transparent, data-driven prediction system that improves underwriting efficiency and customer clarity.

---

# 📂 4) Data Collection

Dataset includes:

* Age
* BMI
* Dependants
* Region
* Smoking
* Income
* Medical history
* Premium (target)

---

# 🧹 5) Data Preprocessing

### Steps performed:

* Verified **no missing values**
* Removed **duplicates**
* Removed **impossible values** (age > 100)
* Capped **extreme income values** using quantiles
* Created **Health Risk Score (0–1)**
* Applied **One-hot & label encoding**
* **MinMax scaling** for numerical features

---

# 📊 6) Data Visualization

### Key findings:

* Premium increases with **age**
* Smoking has a **strong impact**
* Income has **weak correlation**
* Health Risk Score is **highly influential**

---

# 🧩 7) Feature Engineering

### 🔧 Encoding

* One-hot for ordinal categories
* Label encoding for nominal categories

### ❤️ Health Risk Score

Converted medical conditions → weighted numeric score → normalized 0–1

### 🧪 Multicollinearity

* Used correlation heatmap
* Removed redundant income-related features

### 🔄 Scaling

* Applied MinMax scaling

---

# 🧮 8) Model Evaluation

### Models tested:

* Linear Regression
* Ridge Regression
* XGBoost (initial)
* **XGBoost (tuned)** ← final

### Final performance:

* **Test R²:** 0.9812
* **Test RMSE:** 1,162.60

Nearly **2× more accurate** than linear baselines.

---

# 📄 9) Model Error Analysis

## 📊 Residual Distribution (Diff %)

<img src="https://github.com/user-attachments/assets/a1c6438f-4510-4b5d-985f-d0b01cde5e3e" width="700">

### Observations:

* Most residuals near **0%**
* Clear **right-skew** → more overprediction
* Extreme errors (**40–90%**) appear in small groups

---

## 📈 Extreme Error Thresholds

* **10% error → 4,478 customers** (~1/3 of X_test)
* **40% error → 300–900 customers**

Extreme errors come from a **very small subset**.

---

## 👥 Age Distribution & Error

<img src="https://github.com/user-attachments/assets/5cac7dfe-cc93-4e80-bb28-6939f39b296d" width="550">

### Insight:

* Majority customers are **18–25**
* Very few above **30**
* Almost none above **40**

➡️ Underrepresented ages = **higher error**

---

# 🧠 Overall Insight

* Model is **highly accurate (98% R²)**
* Performs best for **common age groups**
* Error rises for **rare demographics**
* Future improvements: segmentation + more balanced data

---


