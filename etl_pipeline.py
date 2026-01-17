"""
Sales ETL Pipeline
==================
Automated ETL script for processing sales data.

Author: Piyush Nirmal
GitHub: https://github.com/piyush-nirmal

Usage:
    python etl_pipeline.py
"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from Excel file.
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        DataFrame with raw data
    """
    logger.info(f"Extracting data from {file_path}...")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    df = pd.read_excel(file_path)
    logger.info(f"Extracted {len(df)} rows")
    
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform and clean the data.
    
    Transformations:
        - Remove duplicate rows
        - Fix date format issues
        - Remove rows with null dates
        - Calculate Profit column
        - Extract Year and Month from dates
    
    Args:
        df: Raw DataFrame
        
    Returns:
        Cleaned and transformed DataFrame
    """
    logger.info("Starting data transformation...")
    initial_count = len(df)
    
    # Step 1: Remove duplicates
    df = df.drop_duplicates()
    after_dedup = len(df)
    logger.info(f"Removed {initial_count - after_dedup} duplicate rows")
    
    # Step 2: Fix date column
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    
    # Step 3: Remove rows with null dates
    df = df.dropna(subset=['Order_Date'])
    after_null_removal = len(df)
    logger.info(f"Removed {after_dedup - after_null_removal} rows with invalid dates")
    
    # Step 4: Feature Engineering
    df['Profit'] = df['Sales'] - df['Cost']
    df['Year'] = df['Order_Date'].dt.year
    df['Month'] = df['Order_Date'].dt.month
    
    logger.info(f"Transformation complete. Final row count: {len(df)}")
    
    return df


def load_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Load data to CSV file.
    
    Args:
        df: Transformed DataFrame
        output_path: Path for output CSV file
    """
    logger.info(f"Saving to CSV: {output_path}")
    df.to_csv(output_path, index=False)
    logger.info("CSV export complete")


def load_to_mysql(df: pd.DataFrame, connection_string: str, table_name: str) -> int:
    """
    Load data to MySQL database.
    
    Args:
        df: Transformed DataFrame
        connection_string: SQLAlchemy connection string
        table_name: Target table name
        
    Returns:
        Number of rows loaded
    """
    logger.info(f"Loading data to MySQL table: {table_name}")
    
    try:
        engine = create_engine(connection_string)
        rows_loaded = df.to_sql(
            name=table_name, 
            con=engine, 
            if_exists='replace', 
            index=False
        )
        logger.info(f"Successfully loaded {rows_loaded} rows to MySQL")
        return rows_loaded
    except Exception as e:
        logger.error(f"Failed to load to MySQL: {str(e)}")
        raise


def run_etl_pipeline(
    source_file: str = "sales_raw_500.xlsx",
    output_csv: str = "sales_cleaned.csv",
    mysql_connection: str = None,
    mysql_table: str = "sales_data"
) -> dict:
    """
    Run the complete ETL pipeline.
    
    Args:
        source_file: Path to source Excel file
        output_csv: Path for output CSV file
        mysql_connection: MySQL connection string (optional)
        mysql_table: MySQL table name
        
    Returns:
        Dictionary with ETL summary
    """
    start_time = datetime.now()
    logger.info("=" * 50)
    logger.info("Starting ETL Pipeline")
    logger.info("=" * 50)
    
    # Extract
    raw_df = extract_data(source_file)
    
    # Transform
    clean_df = transform_data(raw_df)
    
    # Load to CSV
    load_to_csv(clean_df, output_csv)
    
    # Load to MySQL (if connection provided)
    if mysql_connection:
        load_to_mysql(clean_df, mysql_connection, mysql_table)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    summary = {
        "status": "SUCCESS",
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "duration_seconds": duration,
        "rows_extracted": len(raw_df),
        "rows_loaded": len(clean_df),
        "rows_removed": len(raw_df) - len(clean_df),
        "output_file": output_csv
    }
    
    logger.info("=" * 50)
    logger.info("ETL Pipeline Complete!")
    logger.info(f"Duration: {duration:.2f} seconds")
    logger.info(f"Rows processed: {len(clean_df)}")
    logger.info("=" * 50)
    
    return summary


if __name__ == "__main__":
    # Run ETL Pipeline
    # Uncomment and modify MySQL connection string to enable database loading
    
    result = run_etl_pipeline(
        source_file="sales_raw_500.xlsx",
        output_csv="sales_cleaned.csv",
        # mysql_connection="mysql+pymysql://user:password@localhost:3306/salesdb",
        # mysql_table="sales_data"
    )
    
    print("\nETL Summary:")
    for key, value in result.items():
        print(f"  {key}: {value}")
