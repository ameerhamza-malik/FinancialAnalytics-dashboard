import sys
import os

# Add the parent directory (root of backend) to path
sys.path.append(os.getcwd())

from database import db_manager
from services import ProcessService

def debug_processes():
    try:
        print("Testing DB Connection...")
        db_manager.get_connection()
        print("Connection OK.")
        
        print("Running Query...")
        sql = "SELECT id, name, description, script_path, role, is_active, created_at FROM app_processes WHERE is_active = 1 ORDER BY name"
        rows = db_manager.execute_query(sql)
        print(f"Rows found: {len(rows)}")
        
        if rows:
            print("First row keys:", rows[0].keys())
            print("First row values:", rows[0])
            
            roles = rows[0].get("role")
            print(f"Role value: '{roles}'")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_processes()
