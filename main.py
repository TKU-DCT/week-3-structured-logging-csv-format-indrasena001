import psutil
from datetime import datetime
import csv
import os

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get CPU usage percentage
    cpu = psutil.cpu_percent(interval=1)
    
    # Get memory usage percentage
    memory = psutil.virtual_memory().percent
    
    # Get disk usage percentage for the root drive
    disk = psutil.disk_usage('/').percent
    
    return [now, cpu, memory, disk]

def write_log(data):
    filename = "log.csv"
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow(['Timestamp', 'CPU', 'Memory', 'Disk'])
        
        # Write the data row
        writer.writerow(data)

if __name__ == "__main__":
    row = get_system_info()
    write_log(row)
    print("Logged:", row)
