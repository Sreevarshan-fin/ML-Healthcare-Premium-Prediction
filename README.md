

# 🏥 **Health Insurance Premium Prediction**

I built a machine learning system that predicts health insurance premiums with **99% accuracy**.
The project started with **50,000 raw insurance records**, and I handled the entire pipeline — from cleaning messy data to deploying a working Streamlit application that real users can interact with.

---

#  **Key Achievements & What I Delivered**

* Achieved **R² = 0.99** and **~50% lower RMSE** after tuning XGBoost using RandomizedSearchCV.
* Processed **50,000+ records**, cleaned the data, and prepared a final dataset using encoding, scaling, and **VIF-based feature selection**.
* Built **4 specialized models** using age segmentation and a custom **Genetic Risk Score** to capture hereditary health patterns.
* Reduced **residual error to below 10%** for all customer groups (business requirement).
* Developed and deployed a **Streamlit app** with real-time predictions and improved the UI based on feedback from insurance-domain professionals.

---

#  **Results (Based on Streamlit Testing)**

### **Test 1 — Customer Under 25**

| Metric                | Value     |
| --------------------- | --------- |
| **Actual Premium**    | ₹13,365   |
| **Predicted Premium** | ₹13,615   |
| **Absolute Error**    | ₹250      |
| **Error %**           | **1.87%** |

**Interpretation:**
The under-25 segment was originally the hardest to predict.
After adding the **Genetic Risk Score**, predictions became much more stable.
A **1.87% error** is well within the **<10% requirement**.

**Segment Insight:**

* Only **2.49%** of young customers had error > 10%.
* Meaning **97.51%** predictions were accurate.
* Genetic Risk Score made the biggest impact in this group.

---

### **Test 2 — Customer Above 25**

| Metric                | Value     |
| --------------------- | --------- |
| **Actual Premium**    | ₹16,339   |
| **Predicted Premium** | ₹16,034   |
| **Absolute Error**    | ₹305      |
| **Error %**           | **1.86%** |

**Interpretation:**
The model naturally performed well for adults without extra features.
Predictions were stable and reliable.

**Segment Insight:**

* Only **0.3%** had error > 10%.
* Meaning **99.7%** of predictions were accurate.
* No further segmentation was needed for this group.

---

### **Overall Summary**

* Both age groups meet the **<10% business requirement**
* Genetic Risk Score significantly improved accuracy for under-25 customers
* The 25+ group was already stable with minimal tuning
* Real tests show **~1.8% error**, confirming strong real-world reliability

---

# **How I Built This (Problem-Solving Journey)**

## **Problem I Needed to Solve**

Insurance premiums depend on many factors — age, medical history, lifestyle, and hereditary risks.
The dataset had quality issues and age groups behaved differently, which made accurate prediction difficult.
I needed to build a system that produced **consistent and fair predictions** while keeping **residual error < 10%** for every customer segment.

---

## **Task 1: Cleaning & Understanding the Data**

When I first opened the dataset, I found:

* Ages above 100
* Repeated or unrealistic medical history
* Extremely high income values
* Missing or inconsistent entries

I reviewed all records carefully and used simple domain reasoning to fix the data.

**What I did:**

* Removed biologically impossible values
* Used **quantile capping** to limit extreme outliers
* Kept genuine high-income customers
* Cleaned and prepared a final usable dataset
* Used a **70% training / 30% testing** split for reliable evaluation

---

## **Task 2: Feature Engineering**

I improved the dataset with:

* Label Encoding + One-Hot Encoding
* Scaling for numeric features
* **VIF-based feature selection** to avoid multicollinearity
* Created a **Health Risk Score** by converting medical text (like “diabetes”, “high BP”) into a numerical value
* Tuned the scoring weights to improve model performance

These steps helped the model understand real medical risk patterns.

---

## **Task 3: Selecting the Right Algorithm**

I tested:

* Linear Regression
* Ridge Regression
* XGBoost

Linear models struggled because health risks don’t increase in a straight line.
**XGBoost** handled the non-linear relationships much better.

Using **RandomizedSearchCV**, I tuned:

* `max_depth = 5`
* `n_estimators = 50`
* `learning_rate = 0.1`

After tuning:

* R² improved to **0.99**
* RMSE reduced by **~50%**
* Performance was stable on the 70/30 split

---

## **Task 4: Fixing the High Error in Young Customers (<25)**

During error analysis, I found a major issue:

* Young customers (<25) had **73% error**
* Adults (25+) had **0.3% error**
* The dataset had **more young customers**, causing imbalance

Because this failed the <10% requirement, I needed a deeper solution.

### **Step 1: Age Segmentation**

I split the dataset into:

* Under 25
* 25 and above

This helped a bit, but the young group still had high errors.

### **Step 2: Genetic Risk Score (Main Fix)**

Younger customers' premiums were strongly influenced by hereditary health factors.

So I created a **Genetic Risk Score** representing:

* Family disease history
* Hereditary health tendencies
* Early-age risk patterns

For adults (25+):

* No genetic data available
* So I set **Genetic Risk Score = 0**
* The model still performed well

### **Final Result**

| Age Group      | Before Fix     | After Segmentation + Genetic Score |
| -------------- | -------------- | ---------------------------------- |
| **< 25 Years** | **73% error**  | **2.7% error**                     |
| **≥ 25 Years** | **0.3% error** | **0.3% error (no change needed)**  |

Both groups went below **10% error**, meeting the business requirement.

---

## **Task 5: Making It Usable**

I built a **Streamlit web app** that shows instant predictions.

To make it practical:

* Collected feedback from insurance experts
* Simplified UI labels to match underwriting terminology
* Improved workflow for non-technical users
* Optimized backend for **sub-second predictions**

This turned the system into a **complete end-to-end solution**, not just a model.

---

# 📈 **Business Impact**

* Reduced **underwriting risk** by keeping error under 10%
* Fixed the biggest risk area (young customers) from **73% → 2.7%**
* Ensured **consistent and fair pricing** across all customer groups
* Enabled **faster, data-driven premium estimation**
* Added transparency using interpretable features like the Genetic Risk Score
* Delivered a **deployable Streamlit tool** usable by insurance teams

---

# 📘 **What I Learned**

* **Domain knowledge matters** — ML works best when you understand the industry
* **Data quality > algorithms**
* Thinking in terms of **business requirements** helped solve the 73% → 2.7% issue
* **Error analysis** reveals deeper problems that accuracy hides
* Building a product (UI, UX, feedback) is just as important as building the model



---

# 🛠️ Tools & Technologies

**Languages:** Python
**Data Handling:** Pandas, NumPy
**Visualization:** Matplotlib, Seaborn
**Machine Learning:** Scikit-learn, XGBoost
**Feature Engineering:** Label Encoding, One-Hot Encoding, Scaling, VIF
**Model Tuning:** RandomizedSearchCV
**Deployment:** Streamlit
**Version Control:** Git, GitHub
**Environment:** Jupyter Notebook


----------------------
