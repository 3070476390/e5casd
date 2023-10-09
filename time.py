import time
import os

def focus_timer(work_minutes, break_minutes):
    while True:
        # Work phase
        print(f"Focus for {work_minutes} minutes.")
        time.sleep(work_minutes * 60)  # Convert minutes to seconds

        # Break phase
        os.system("notify-send 'Take a break!'")  # Linux notification, adjust for your OS
        print(f"Take a {break_minutes} minutes break.")
        time.sleep(break_minutes * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    work_time = 25  # minutes
    break_time = 5   # minutes

    focus_timer(work_time, break_time)
