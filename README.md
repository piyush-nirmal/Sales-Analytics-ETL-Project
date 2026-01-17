# 📊 End-to-End ETL Pipeline | Sales Data Analytics

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-Data%20Source-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

**A complete data engineering project demonstrating ETL (Extract, Transform, Load) pipeline development with Python, MySQL, and Power BI visualization.**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Results](#-results)

</div>

---

## 🎯 Project Overview

This project implements a **production-ready ETL pipeline** that extracts raw sales data from Excel, performs comprehensive data cleaning and transformation using Python/Pandas, loads the processed data into a MySQL database, and visualizes insights through an interactive Power BI dashboard.

### Business Problem
Organizations often have raw sales data scattered across Excel files with quality issues like duplicates, missing values, and inconsistent formatting. This project solves that by automating the data cleaning process and creating a centralized, queryable database for analytics.

---

## ✨ Features

- 🔄 **Automated Data Extraction** from Excel files
- 🧹 **Data Cleaning & Validation** (duplicate removal, null handling, date formatting)
- 🔧 **Feature Engineering** (Profit calculation, Year/Month extraction)
- 💾 **Database Integration** with MySQL for centralized storage
- 📈 **Interactive Dashboard** built with Power BI
- 📋 **Export Capabilities** to CSV for portability

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ETL PIPELINE ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐             │
│   │   EXTRACT    │    │    TRANSFORM     │    │     LOAD     │             │
│   │              │    │                  │    │              │             │
│   │  Excel File  │───▶│  Python/Pandas   │───▶│    MySQL     │             │
│   │  (.xlsx)     │    │  • Duplicates    │    │   Database   │             │
│   │              │    │  • Null Values   │    │              │             │
│   │  520 rows    │    │  • Date Fixing   │    │  482 rows    │             │
│   │              │    │  • New Features  │    │              │             │
│   └──────────────┘    └──────────────────┘    └──────┬───────┘             │
│                                                      │                      │
│                                                      ▼                      │
│                                               ┌──────────────┐             │
│                                               │  VISUALIZE   │             │
│                                               │              │             │
│                                               │  Power BI    │             │
│                                               │  Dashboard   │             │
│                                               │              │             │
│                                               └──────────────┘             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
End-to-End ETL Pipeline/
│
├── 📊 sales_raw_500.xlsx      # Source data (raw Excel file)
├── 📓 cleaning.ipynb          # Jupyter notebook with ETL logic
├── 📄 sales_cleaned.csv       # Transformed output data
├── 📈 Dashboard.pbix          # Power BI dashboard file
└── 📖 README.md               # Project documentation
```

---

## 🔧 Tech Stack

| Category | Technology |
|----------|------------|
| **Programming** | Python 3.11 |
| **Data Processing** | Pandas, NumPy |
| **Database** | MySQL 8.0 |
| **ORM/Connector** | SQLAlchemy, PyMySQL |
| **Visualization** | Power BI, Matplotlib |
| **Environment** | Jupyter Notebook |
| **Data Source** | Microsoft Excel |

---

## 📊 Data Schema

### Input Data (Raw - 7 Columns)

| Column | Type | Description |
|--------|------|-------------|
| Order_ID | INT | Unique order identifier |
| Order_Date | DATE | Date of order |
| Customer | VARCHAR | Customer name |
| Region | VARCHAR | Geographic region (North/South/East/West) |
| Product | VARCHAR | Product category |
| Sales | INT | Sales amount (₹) |
| Cost | INT | Cost amount (₹) |

### Output Data (Cleaned - 10 Columns)

| Column | Type | Description |
|--------|------|-------------|
| *...original columns...* | | |
| **Profit** | INT | Calculated: Sales - Cost |
| **Year** | INT | Extracted from Order_Date |
| **Month** | INT | Extracted from Order_Date |

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- MySQL Server
- Power BI Desktop (for dashboard)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/end-to-end-etl-pipeline.git
   cd end-to-end-etl-pipeline
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas numpy matplotlib sqlalchemy pymysql openpyxl jupyter
   ```

3. **Setup MySQL Database**
   ```sql
   CREATE DATABASE salesdb;
   ```

4. **Update database credentials** in the notebook
   ```python
   engine = create_engine('mysql+pymysql://username:password@localhost:3306/salesdb')
   ```

---

## 💻 Usage

### Run ETL Pipeline

1. **Open Jupyter Notebook**
   ```bash
   jupyter notebook cleaning.ipynb
   ```

2. **Execute all cells** to run the complete pipeline

3. **View results** in:
   - `sales_cleaned.csv` - Cleaned data file
   - MySQL `salesdb.sales_data` - Database table
   - `Dashboard.pbix` - Power BI visualizations

---

## 📈 Data Transformation Summary

| Step | Operation | Impact |
|------|-----------|--------|
| 1 | Load raw data | 520 rows imported |
| 2 | Remove duplicates | ~20 rows removed |
| 3 | Fix date format | Invalid dates → NaT |
| 4 | Remove null dates | 18 rows removed |
| 5 | Calculate Profit | New column added |
| 6 | Extract Year/Month | 2 new columns added |
| **Final** | **Clean dataset** | **482 rows, 10 columns** |

**Data Quality Improvement: 7.3% bad data identified and handled**

---

## 📊 Sample Insights

After running the pipeline, the data enables analysis such as:

- 📍 **Regional Performance** - Sales & Profit by North/South/East/West
- 📦 **Product Analysis** - Top performing product categories
- 📅 **Time Trends** - Monthly/Yearly sales patterns
- 👥 **Customer Insights** - Top customers by revenue
- 💰 **Profitability** - Profit margins across segments

---

## 🖼️ Dashboard Preview

The Power BI dashboard includes:

- **KPI Cards** - Total Sales, Profit, Orders
- **Regional Map** - Geographic distribution
- **Trend Charts** - Monthly/Yearly patterns
- **Product Breakdown** - Category-wise analysis
- **Top Customers** - Customer ranking table

---

## 🛠️ Key Skills Demonstrated

- ✅ **ETL Development** - End-to-end pipeline design
- ✅ **Data Cleaning** - Handling real-world data quality issues
- ✅ **Python Programming** - Pandas, NumPy for data manipulation
- ✅ **SQL & Databases** - MySQL integration with SQLAlchemy
- ✅ **Data Visualization** - Power BI dashboard creation
- ✅ **Feature Engineering** - Creating derived columns
- ✅ **Documentation** - Clear project documentation

---

## 🔮 Future Enhancements

- [ ] Add automated scheduling (Windows Task Scheduler / Cron)
- [ ] Implement incremental loading
- [ ] Add data validation checks with Great Expectations
- [ ] Create ETL logging and monitoring
- [ ] Deploy dashboard to Power BI Service
- [ ] Add unit tests for data transformations

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!

---

<div align="center">

**Built with ❤️ using Python, MySQL & Power BI**

</div>
