# Liquor Sales Data Analysis in Python

Data analysis and visualization project for liquor sales (2016–2019).  
Includes **data cleaning**, **exploratory analysis**, and **insightful visualizations** using Python.

---

## 📊 **About**

This project analyzes liquor sales data to:
1. Identify the most popular product in each postal area (**zip_code**)
2. Calculate each store's share of total sales

---

## 🗂️ **Dataset**

- Original data: CSV file with 24 columns and records from 2012–2020
- Analysis focuses on 2016–2019
- Missing values handled, data types corrected:
  - `date` → datetime
  - `zip_code` → int
  - `bottles_sold` → int
  - `sales_dollars` → float

---

## ⚙️ **Methodology**

✅ **1. Data Loading & Cleaning**
- Load CSV, preview features
- Filter dates: 2016–2019
- Drop rows with missing values (`dropna()`)
- Convert types for accurate calculations

✅ **2. Popular Product per Zip Code**
- Group by `zip_code` and `item_number`
- Aggregate `bottles_sold`
- Use `idxmax()` to find top-selling product in each area
- Visualize with **scatter plot** (Seaborn / Matplotlib)

✅ **3. Store Sales Share**
- Calculate % share of total sales per store
- Visualize with horizontal **bar chart** (Plotly)

---

## 📚 **Tech Stack**

- 🐍 **Python**
- 📊 **Pandas**
- 🎨 **Seaborn**
- 📈 **Matplotlib**
- 📊 **Plotly**

---

## ✅ **Results**

- Data cleaned and filtered to ~60 records without missing values
- Popular product found for each area
- Store-wise sales distribution identified
- Visual dashboards help reveal high-selling products and top stores

---

## 🔍 **Key Insights**

- Clear understanding of liquor sales trends per area and store
- Supports business decisions for inventory and marketing
