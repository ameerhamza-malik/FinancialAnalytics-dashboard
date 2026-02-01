import sys
import os
import logging

# Configure logging to stdout
logging.basicConfig(level=logging.INFO)

# Add the parent directory (root of backend) to path
sys.path.append(os.getcwd())

from database import db_manager
from services import ProcessService

def debug_run():
    try:
        print("Testing DB Connection...")
        # Force connection to initialize output handler
        with db_manager.get_connection() as conn:
            print(f"Connected to {conn.version}")

        print("Attempting to run Process 1...")
        # Mock running process 1
        # process_1 exists in DB (id=1) 
        output = ProcessService.run_process(1, {})
        print("Process Output:")
        print(output)
        
    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_run()
