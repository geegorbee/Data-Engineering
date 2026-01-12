# ETL Pipeline Demonstration

**Author:** Gerald Brown  
**Date:** January 2026  
**Purpose:** Portfolio demonstration of data engineering ETL workflow concepts

---

## Overview

This project demonstrates a complete **Extract-Transform-Load (ETL)** pipeline built with Python and Pandas, simulating the type of batch data processing performed by AWS Glue jobs in production data engineering environments.

---

## What It Does

### 📥 **Extract Phase**
- Reads raw transaction data from CSV file
- Simulates data ingestion from source systems
- In production: would connect to S3, RDS, APIs, or streaming sources

### 🔄 **Transform Phase**

**Data Quality Checks:**
- Validates data integrity (null checks, type validation)
- Filters invalid transactions (pending/failed status)
- Converts data types (string dates → datetime objects)

**Business Logic:**
- Aggregates daily transaction metrics (count, total, average, max)
- Summarizes spending by merchant category
- Creates analytics-ready datasets

### 📤 **Load Phase**
- Writes cleaned transaction data to CSV
- Exports aggregated daily summaries
- Saves category analysis results
- In production: would write to Redshift, S3 data lake, or RDS

---

## Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and aggregation
- **ETL Design Patterns** - Industry-standard workflow architecture
- **Data Quality Validation** - Production-grade checks

---

## Project Structure

ETL-Pipeline-Demo/
├── README.md                  # This file
├── etl_pipeline.py            # Main ETL script
├── sample_data.csv            # Input: Raw transaction data
├── transactions_clean.csv     # Output: Cleaned transactions (generated)
├── daily_summary.csv          # Output: Daily aggregated metrics (generated)
└── category_summary.csv       # Output: Category spending analysis (generated)

---

## How to Run

**Requirements:**
```bash
pip install pandas

python etl_pipeline.py

Expected Output:
	∙	Console shows Extract → Transform → Load phases
	∙	Creates 3 new CSV files with processed data

Sample Output
************************************************************
ETL PIPELINE EXECUTION START
Timestamp: 2026-01-13 10:30:00
************************************************************

============================================================
EXTRACT PHASE: Loading raw transaction data
============================================================
✓ Successfully loaded 10 records from sample_data.csv
✓ Columns: transaction_id, user_id, amount, transaction_date, status, merchant_category

Sample data (first 3 rows):
   transaction_id  user_id  amount transaction_date     status merchant_category
0            1001      101  125.50       2026-01-08  completed          groceries
1            1002      102   45.00       2026-01-08  completed             dining
2            1003      101  200.00       2026-01-08    pending           shopping

============================================================
TRANSFORM PHASE: Data Quality Validation
============================================================
✓ No null values found
✓ Filtered to completed transactions: 8 records
  (Removed 2 pending/failed transactions)
✓ Converted transaction_date to datetime format

============================================================
TRANSFORM PHASE: Aggregation & Analytics
============================================================
✓ Created daily transaction summary
  Metrics: count, total, average, maximum per day
✓ Created merchant category summary

============================================================
LOAD PHASE: Writing processed data
============================================================
✓ Saved transactions_clean.csv (8 records)
✓ Saved daily_summary.csv (4 records)
✓ Saved category_summary.csv (4 categories)

✓ All data successfully written to output files

************************************************************
PIPELINE EXECUTION COMPLETE - SUCCESS
************************************************************

📊 DAILY SUMMARY RESULTS:
                transaction_count  total_amount  avg_amount  max_amount
transaction_date                                                        
2026-01-08                      2        170.50       85.25      125.50
2026-01-09                      2        165.24       82.62       89.99
2026-01-10                      3        522.50      174.17      300.00
2026-01-11                      1         95.75       95.75       95.75

📊 CATEGORY SUMMARY RESULTS:
                   total_spent  transaction_count
merchant_category                                 
shopping                300.00                  1
entertainment           269.99                  2
groceries               167.75                  2
dining                  216.00                  3

Key Concepts Demonstrated
✅ ETL Workflow Design - Standard Extract-Transform-Load pattern✅ Data Quality Validation - Null checks, filtering, type conversion✅ Business Logic Implementation - Aggregation, grouping, sorting✅ Pipeline Orchestration - Phase coordination and error handling✅ Production Readiness - Logging, error handling, documentation

Real-World Applications
This demonstration shows understanding of:
	∙	AWS Glue ETL jobs - Batch data processing in cloud environments
	∙	Data pipeline monitoring - Quality checks and validation logic
	∙	Data warehousing concepts - Preparing data for analytics (Redshift, Snowflake)
	∙	Data engineering workflows - Production-grade code structure


Skills Demonstrated
For Data Engineering Roles:
	∙	Python data manipulation (Pandas)
	∙	ETL pipeline design and implementation
	∙	Data quality validation and monitoring
	∙	Aggregation and transformation logic
	∙	Code documentation and organization
For Interviews:
	∙	Can explain Extract-Transform-Load workflow
	∙	Understands data quality concepts
	∙	Knows how to aggregate and summarize data
	∙	Can discuss production considerations (error handling, logging)

Future Enhancements
Potential improvements for expanded portfolio:
	∙	Add database connectivity (PostgreSQL/MySQL)
	∙	Implement AWS S3 integration for cloud storage
	∙	Create data quality metrics dashboard
	∙	Add incremental load logic (process only new/changed data)
	∙	Integrate with Apache Airflow for scheduling
	∙	Add unit tests and error handling
	∙	Implement logging framework


About This Project
Built as part of a data engineering portfolio to demonstrate practical ETL development skills for junior data engineer roles. This project showcases the ability to design, implement, and document data pipelines using Python and industry-standard patterns.
Training Completed:
	∙	AWS Skill Builder: Introduction to AWS Glue
	∙	AWS Skill Builder: Introduction to Amazon Redshift
	∙	Coursera: Advanced SQL Joins
	∙	Coursera: SQL Syntax Fundamentals


Contact
Gerald Brown CBS, NL, Canada
Email: gerald.brown@alumni.utoronto.caLinkedIn: linkedin.com/in/gerald-brown-63168223aPortfolio: github.com/geegorbee

Related Projects:
	∙	Cybersecurity Portfolio - AWS security, IAM, GRC
	∙	AI Portfolio - Berg’s AI Ordering System
