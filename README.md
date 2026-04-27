# 🚀 Titanic Data Cleaning & Preprocessing

## 📖 Problem Statement
The goal of this project is to clean and preprocess the Titanic dataset to improve data quality and make it suitable for analysis and machine learning.

---

## 📂 Dataset
- Source: Kaggle Titanic Dataset  
- File Used: `titanic.csv`  
- Contains passenger details such as age, gender, class, and survival status  

---

## ⚙️ Data Cleaning Steps Performed

### 1️⃣ Handling Missing Values
- Filled missing values in **Age** column using median  
- Filled missing values in **Embarked** column using mode  

👉 This ensures no null values affect analysis

---

### 2️⃣ Removing Unnecessary Columns
- Dropped **Cabin** column (if present)  
👉 Reason: Too many missing values, not useful for analysis

---

### 3️⃣ Removing Duplicate Records
- Checked and removed duplicate rows  
👉 Ensures data consistency and avoids bias

---

### 4️⃣ Data Standardization
- Ensured correct data types  
- Cleaned dataset for better readability  

---

### 5️⃣ Saving Cleaned Data
- Final cleaned dataset saved as:
```plaintext
cleaned_titanic.csv
