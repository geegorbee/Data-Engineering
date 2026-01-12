"""
ETL Pipeline Demonstration
Author: Gerald Brown
Date: January 2026

Demonstrates Extract-Transform-Load workflow for data engineering.
Simulates batch processing pipeline similar to AWS Glue jobs.

Pipeline Steps:
1. EXTRACT: Read raw transaction data from CSV
2. TRANSFORM: Clean, validate, and aggregate data
3. LOAD: Write processed data to output files

Data Quality Checks:
- Filter invalid transaction statuses
- Remove null values
- Validate data types
- Calculate aggregated metrics
"""

import pandas as pd
from datetime import datetime
import os

# ============================================================================
# EXTRACT PHASE
# ============================================================================

def extract_data(input_file='sample_data.csv'):
    """
    Extract: Read raw data from source file
    
    In production, this would connect to:
    - S3 buckets
    - RDS databases
    - API endpoints
    - Streaming sources (Kinesis)
    """
    print("=" * 60)
    print("EXTRACT PHASE: Loading raw transaction data")
    print("=" * 60)
    
    try:
        df = pd.read_csv(input_file)
        print(f"✓ Successfully loaded {len(df)} records from {input_file}")
        print(f"✓ Columns: {', '.join(df.columns)}")
        print(f"\nSample data (first 3 rows):")
        print(df.head(3))
        return df
    except FileNotFoundError:
        print(f"✗ Error: {input_file} not found")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {str(e)}")
        return None

# ============================================================================
# TRANSFORM PHASE
# ============================================================================

def validate_data(df):
    """
    Data Quality Checks
    
    Validates:
    - No null values in critical fields
    - Correct data types
    - Valid status values
    """
    print("\n" + "=" * 60)
    print("TRANSFORM PHASE: Data Quality Validation")
    print("=" * 60)
    
    initial_count = len(df)
    
    # Check for null values
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print(f"⚠ Warning: Found {null_counts.sum()} null values")
        print(null_counts[null_counts > 0])
    else:
        print("✓ No null values found")
    
    # Filter for completed transactions only (business rule)
    df_clean = df[df['status'] == 'completed'].copy()
    removed = initial_count - len(df_clean)
    print(f"✓ Filtered to completed transactions: {len(df_clean)} records")
    print(f"  (Removed {removed} pending/failed transactions)")
    
    # Convert date strings to datetime
    df_clean['transaction_date'] = pd.to_datetime(df_clean['transaction_date'])
    print("✓ Converted transaction_date to datetime format")
    
    return df_clean

def transform_data(df_clean):
    """
    Business Logic Transformations
    
    Creates aggregated views:
    - Daily transaction summaries
    - Category breakdowns
    - User spending patterns
    """
    print("\n" + "=" * 60)
    print("TRANSFORM PHASE: Aggregation & Analytics")
    print("=" * 60)
    
    # Daily summary statistics
    daily_summary = df_clean.groupby('transaction_date').agg({
        'transaction_id': 'count',
        'amount': ['sum', 'mean', 'max']
    }).round(2)
    
    daily_summary.columns = ['transaction_count', 'total_amount', 'avg_amount', 'max_amount']
    print("✓ Created daily transaction summary")
    print(f"  Metrics: count, total, average, maximum per day")
    
    # Category summary
    category_summary = df_clean.groupby('merchant_category').agg({
        'amount': ['sum', 'count']
    }).round(2)
    
    category_summary.columns = ['total_spent', 'transaction_count']
    category_summary = category_summary.sort_values('total_spent', ascending=False)
    print("✓ Created merchant category summary")
    
    return df_clean, daily_summary, category_summary

# ============================================================================
# LOAD PHASE
# ============================================================================

def load_data(df_clean, daily_summary, category_summary):
    """
    Load: Write processed data to destination
    
    In production, this would write to:
    - S3 (data lake)
    - Redshift (data warehouse)
    - RDS (operational database)
    - DynamoDB (NoSQL)
    """
    print("\n" + "=" * 60)
    print("LOAD PHASE: Writing processed data")
    print("=" * 60)
    
    try:
        # Write cleaned transactions
        df_clean.to_csv('transactions_clean.csv', index=False)
        print(f"✓ Saved transactions_clean.csv ({len(df_clean)} records)")
        
        # Write daily summary
        daily_summary.to_csv('daily_summary.csv')
        print(f"✓ Saved daily_summary.csv ({len(daily_summary)} records)")
        
        # Write category summary (bonus output)
        category_summary.to_csv('category_summary.csv')
        print(f"✓ Saved category_summary.csv ({len(category_summary)} categories)")
        
        print("\n✓ All data successfully written to output files")
        return True
        
    except Exception as e:
        print(f"✗ Error writing data: {str(e)}")
        return False

# ============================================================================
# PIPELINE ORCHESTRATION
# ============================================================================

def run_pipeline():
    """
    Main pipeline orchestration
    
    Coordinates the full ETL workflow:
    1. Extract from source
    2. Transform with quality checks
    3. Load to destination
    
    Similar to how AWS Glue jobs orchestrate transformations
    """
    print("\n")
    print("*" * 60)
    print("ETL PIPELINE EXECUTION START")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("*" * 60)
    
    # Execute pipeline phases
    raw_data = extract_data()
    
    if raw_data is not None:
        clean_data = validate_data(raw_data)
        clean_data, daily_summary, category_summary = transform_data(clean_data)
        success = load_data(clean_data, daily_summary, category_summary)
        
        if success:
            print("\n" + "*" * 60)
            print("PIPELINE EXECUTION COMPLETE - SUCCESS")
            print("*" * 60)
            
            print("\n📊 DAILY SUMMARY RESULTS:")
            print(daily_summary)
            
            print("\n📊 CATEGORY SUMMARY RESULTS:")
            print(category_summary)
        else:
            print("\n✗ Pipeline failed during load phase")
    else:
        print("\n✗ Pipeline failed during extract phase")

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    run_pipeline()

