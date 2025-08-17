# End-to-End Sales Analysis for Superstore

---<img width="1318" height="741" alt="Screenshot 2025-08-17 125757" src="https://github.com/user-attachments/assets/cf332c8a-7bdf-4138-a37a-1904d51b69f6" />

### Project Overview

This project provides an end-to-end analysis of sales data for a fictional superstore. The goal was to process and analyze the data to identify key performance indicators, uncover sales trends, and deliver actionable insights to improve profitability.

---

### Tools Used

* **Python:** For data cleaning and preparation (ETL).
    * **Libraries:** Pandas
* **SQL:** For data exploration and analysis.
    * **Database:** SQLite (managed with DB Browser for SQLite)
* **Power BI / Tableau:** For creating the final interactive dashboard.

---

### The Process

1.  **Data Cleaning & Preparation (ETL):** The initial dataset contained several inconsistencies. A Python script was developed to:
    * Handle encoding errors and load the data correctly.
    * Parse and standardize highly mixed date formats (e.g., `DD-MM-YYYY`, `M/D/YYYY`).
    * Create new features like `Profit Margin`, `Order Year`, and `Order Month` to enable deeper analysis.

2.  **Exploratory Data Analysis (EDA) with SQL:** After loading the cleaned data into an SQLite database, I wrote SQL queries to answer key business questions related to overall performance, product profitability, customer segments, and geographical trends.

3.  **Data Visualization:** The insights from the SQL analysis were visualized in an interactive dashboard to communicate the findings effectively to non-technical stakeholders.

---

### Key Findings & Recommendations

This is a fantastic and professional-looking dashboard! You've successfully visualized all the key insights from the data and created a powerful analytical tool. This is the perfect final product for your portfolio.

The final step in any data analysis project is to interpret the dashboard and present a clear, concise summary with actionable recommendations. This is where you demonstrate your value as an analyst by translating data into business strategy.

#### Executive Summary
Overall business performance is strong, with total sales reaching $2.30M and a healthy total profit of $286.4K.
However, our analysis reveals a critical weakness in the Furniture category, which is severely undermining the company's overall profitability.
By addressing specific unprofitable products and regions, we have a significant opportunity to increase our profit margins.


#### **Key Findings:**
* Overall business performance is strong, with total sales reaching **$2.30M** and a healthy profit of **$286.4K**.
* The **Furniture category** is a major underperformer, generating significant sales but minimal profit.
* **Tables** and **Bookcases** are the primary loss-making sub-categories.
* States like **Texas, Pennsylvania, and Illinois** are major loss centers.

#### **Actionable Recommendations:**
* **Investigate 'Tables':** Conduct an urgent review of the 'Tables' sub-category's end-to-end costs, especially in unprofitable states.
* **Re-evaluate Discount Strategy:** Test a reduction in discounts for Furniture in one of the loss-making states to measure the impact on profitability.
* **Focus on Strengths:** Allocate more marketing resources to high-performing categories and the crucial 'Consumer' segment.
