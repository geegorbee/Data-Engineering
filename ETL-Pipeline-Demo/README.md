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

