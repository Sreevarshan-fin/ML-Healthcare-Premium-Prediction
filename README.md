

# 🏥 **Health Insurance Premium Prediction**


I built a machine learning system that predicts health insurance premiums with **99% accuracy**. 

When I started this project, my goal was simple: build something that actually works in a real insurance workflow, not just a model with a high score. The project started with **50,000 raw insurance records**, and I handled everything—from cleaning messy data to deploying a working Streamlit app that real users can interact with.

---

#  **Key Achievements & What I Delivered**

* Achieved **R² = 0.99** and reduced RMSE by **~50%** after tuning XGBoost with RandomizedSearchCV
* Built **4 specialized models** using age segmentation + a custom **Genetic Risk Score**, dropping young customer errors from **73% → 2.7%**
* Deployed a **Streamlit app** with real-time predictions, refined based on feedback from insurance professionals
  
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


**Segment Performance:**  
Only **2.49%** of young customers exceeded the 10% error threshold—meaning **97.51%** of predictions hit the target. The Genetic Risk Score made the difference here.

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

**Segment Performance:**  
Only **0.3%** exceeded the 10% threshold—meaning **99.7%** were accurate. No additional segmentation was needed for this group.

---

### **Overall Summary**

* Both age groups meet the **<10% business requirement**
* The Genetic Risk Score improved under-25 accuracy dramatically, while the 25+ group was already stable
---

# **How I Built This**


### **The Challenge**

Insurance premiums depend on factors like age, medical history, lifestyle, and hereditary risks. The dataset had quality issues, and different age groups behaved completely differently—making accurate prediction tricky.

My goal was to build a system that kept **residual error below 10%** for every customer segment, not just overall.

---

#### **Task 1: Cleaning & Understanding the Data**

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

#### **Task 2: Feature Engineering**

I improved the dataset with:

* Label Encoding + One-Hot Encoding
* Scaling for numeric features
* **VIF-based feature selection** to avoid multicollinearity
* Created a **Health Risk Score** by converting medical text (like “diabetes”, “high BP”) into a numerical value
* Tuned the scoring weights to improve model performance

These steps helped the model understand real medical risk patterns.

---

#### **Task 3: Selecting the Right Algorithm**

I tested:

* Linear Regression
* Ridge Regression
* XGBoost

Linear models struggled because health risks don’t increase in a straight line.
**XGBoost** handled the non-linear relationships much better.

Using **RandomizedSearchCV**, I tuned:

 `max_depth = 5`
 `n_estimators = 50`
 `learning_rate = 0.1`

After tuning:

* R² improved to **0.99**
* RMSE reduced by **~50%**
* Performance was stable on the 70/30 split

---

#### **Task 4: Fixing the High Error in Young Customers (<25)**

During error analysis, I found a major issue:

* Young customers (<25) had **73% error**
* Adults (25+) had **0.3% error**
* The dataset had **more young customers**, causing imbalance

Because this failed the <10% requirement, I needed a deeper solution.

##### **Step 1: Age Segmentation**

I split the dataset into:

* Under 25
* 25 and above

This helped a bit, but the young group still had high errors.

##### **Step 2: Genetic Risk Score (Main Fix)**

Younger customers' premiums were strongly influenced by hereditary health factors.

So I created a **Genetic Risk Score** representing:

* Family disease history
* Hereditary health tendencies
* Early-age risk patterns

For adults (25+):

* No genetic data available
* So I set **Genetic Risk Score = 0**
* The model still performed well

##### **Final Result**

| Age Group      | Before Fix     | After Segmentation + Genetic Score |
| -------------- | -------------- | ---------------------------------- |
| **< 25 Years** | **73% error**  | **2.7% error**                     |
| **≥ 25 Years** | **0.3% error** | **0.3% error (no change needed)**  |


---

#### **Task 5: Making It Usable**

I built a **Streamlit web app** that shows instant predictions.

To make it practical:

* Collected feedback from insurance experts
* Simplified UI labels to match underwriting terminology
* Improved workflow for non-technical users
* Optimized backend for **sub-second predictions**

This turned the project into something insurance teams could actually use, not just a model.

---

## 📈 **Business Impact**

* Fixed the young customer error rate from **73% → 2.7%**, eliminating the biggest risk area
* Met the **<10% error requirement** across all customer groups
* Built a deployed **Streamlit app** that insurance teams can use for real-time predictions
  
---


## **What I Learned:**

The biggest lesson? High overall accuracy doesn't mean every group is predicted well. I could've spent weeks tuning hyperparameters, but the real breakthrough came from **understanding that young customers' premiums are driven by hereditary factors**—not from a better algorithm.

I also learned that building a usable product matters as much as building an accurate model. Getting feedback from insurance professionals showed me which features actually mattered to users.



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
