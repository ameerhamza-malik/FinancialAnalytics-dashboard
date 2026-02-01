import time
import sys
import datetime

def main():
    print(f"[{datetime.datetime.now()}] Starting Sample Process 1...")
    
    total_steps = 5
    for i in range(1, total_steps + 1):
        # Simulate work
        time.sleep(1)
        progress = (i / total_steps) * 100
        print(f"[{datetime.datetime.now()}] Step {i}/{total_steps} completed. Progress: {progress:.0f}%")
        sys.stdout.flush() 

    print(f"[{datetime.datetime.now()}] Process 1 finished successfully!")

if __name__ == "__main__":
    main()
