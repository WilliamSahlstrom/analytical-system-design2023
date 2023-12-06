# bash commands
# crontab -e
# 0 0 * * 1-5 /path/to/your/python /path/to/your/cron_script.py

# set via "Task Scheduler" on Windows
# set trigger to "Daily" and "Recur every" field to 1 day

from main import job, schedule_job
import time

# Function to run scheduler loop
def run_schedule():
    schedule_job()
    while True:
        job()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()