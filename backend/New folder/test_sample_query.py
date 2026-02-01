import os
import pandas as pd
from database import db_manager

# Setup minimal logging to stdout
import logging
logging.basicConfig(level=logging.INFO)

# User's query
user_query = "SELECT * FROM SAMPLE_BT WHERE ROWNUM <= 100"
limit = 100
offset = 0

# Wrappers used in services.py
paginated_query = f"""
            SELECT * FROM (
                SELECT a.*, ROWNUM rnum FROM (
                    {user_query}
                ) a WHERE ROWNUM <= {limit + offset}
            ) WHERE rnum > {offset}
            """

print(f"Executing query:\n{paginated_query}")

try:
    df = db_manager.execute_query_pandas(paginated_query, timeout=10)
    print("Query success!")
    print(df.head())
    print("Columns:", df.columns)
except Exception as e:
    print(f"Query failed: {e}")
    import traceback
    traceback.print_exc()
