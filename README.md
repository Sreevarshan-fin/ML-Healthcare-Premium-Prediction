# 🩺 Health Insurance Premium Prediction Model

## 📙 Project Summary
A complete machine learning workflow to predict **annual health insurance premiums** using customer demographics, lifestyle indicators, and medical history.  
The final model is deployed as a **Streamlit web app**, enabling underwriters and customers to generate fast, consistent, and risk-based premium estimates.

---

## 🌟 Highlights
- **Custom Health Risk Score** engineered from medical history.
- **Context-aware outlier handling** for age and income using IQR + quantile capping.
- **Multicollinearity review** with Correlation Heatmaps and VIF.
- **Model comparison:** Linear Regression, Ridge Regression, and XGBoost.
- **Final chosen model:** Tuned XGBoost Regressor  
  - **Test R²:** 0.9812  
  - **RMSE:** 1,162.60 (≈50% lower error than Linear/Ridge)
- **Streamlit Web App** built for real-time premium prediction.

---

## 🛠 Tools & Technologies
**Languages:** Python  
**Libraries:** Pandas, NumPy, Scikit-learn, XGBoost  
**Visualization:** Matplotlib, Seaborn  
**App Framework:** Streamlit  
**Environment:** Jupyter Notebook, VS Code  
**Version Control:** Git, GitHub  
**Deployment:** Streamlit Cloud  

---

## 📁 Project Structure

Each notebook represents a **separate experiment**, making the workflow easier  to review

premium_prediction_project/
│
├── notebooks/
│   ├── 00_premium_full_analysis.ipynb        → Full workflow
│   ├── 01_seg_premium_lt25.ipynb             → Premium < 25
│   ├── 02_seg_premium_gt25.ipynb             → Premium > 25
│   ├── 03_seg_genetic_lt25.ipynb             → Genetic Score < 25
│   └── 04_seg_genetic_gt25.ipynb             → Genetic Score > 25
│
├── README.md
└── other project files…


---


## 🚀 Launch the Application
**Streamlit App:** ***[![Open in Streamlit](https://img.shields.io/badge/Launch%20App-Streamlit-%23FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge&labelColor=FF4B4B)](https://ml-healthcare-premium-prediction-7qrpw78zqct4zhdm7u8v2d.streamlit.app/)**

---

## 📝 Detailed Documentation

### 1️⃣ Project Overview
This project builds a predictive model for estimating health insurance premiums using variables such as:
- Age  
- BMI  
- Income (lakhs)  
- Number of dependants  
- Smoking status  
- Region  
- Policy type  
- Medical history  

The model is integrated into a **Streamlit application** for real-time use.

---

### 2️⃣ Scope of Work
**Objectives**
- Build a high-accuracy model (**R² > 97%**)  
- Keep prediction error below **10% for ≥95%** of customers  
- Deploy the model on the cloud  
- Provide a user-friendly web interface  

**Project Stages**
- Data collection + validation  
- Outlier detection + treatment  
- Feature engineering + encoding  
- EDA + statistical checks  
- Model development + comparison  
- Deployment + testing  

---

### 3️⃣ Data Collection
Dataset includes anonymized, PII-safe fields:
- Age  
- BMI  
- Children  
- Smoker  
- Region  
- Charges (target)  

---

### 4️⃣ Data Preprocessing
Performed:
- Duplicate removal  
- Outlier detection  
- Capping extreme incomes  
- Removing unrealistic ages (>100)  
- Retaining valid high-income customers  

---

### 5️⃣ Data Visualization
Insights:
- Older customers → higher premiums  
- Income shows no direct correlation  
- Dependants have minimal impact  
- Premium distribution is right-skewed  

---

### 6️⃣ Feature Engineering
- **Ordinal encoding** for policy type & income groups  
- **Label encoding** for non-ordinal features  
- **Custom Health Risk Score (0–1)**  
- Removed redundant engineered columns  
- Improved dataset consistency  

---

### 7️⃣ Multicollinearity Checks
- Correlation heatmap  
- VIF calculation  
- Removed income_level or income_lakhs (high VIF > 10)  

---

### 8️⃣ Feature Scaling
Used **Min-Max Scaling** for:
- Faster convergence  
- Balanced feature importance  
- Improved model performance  

---

### 9️⃣ Model Evaluation
**Linear / Ridge Regression**
- R² ≈ 0.93  
- RMSE ≈ 2,273  

**XGBoost (Initial)**
- Slight underfitting  

**XGBoost (Tuned)**
- **Test R²:** 0.9812  
- **RMSE:** 1,162.60  
- Excellent generalization  

**Final Model:** Tuned XGBoost Regressor

---

### 🔟 Model Error Analysis
- Residuals centered around 0%  
- Right-skew reveals overprediction cases  
- Extreme errors (40–90%) tied to demographic imbalance  
- Dataset dominated by customers aged 18–25  
- Underperformance for age 30+ due to sparse training examples  

---





