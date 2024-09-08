import psutil
import logging

# Setup logging
logging.basicConfig(filename='/var/log/system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 75
MEMORY_THRESHOLD = 70
DISK_THRESHOLD = 85

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        alert(f"High memory usage detected: {memory.percent}%")
    return memory.percent

def check_disk():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alert(f"Low disk space detected: {disk.percent}%")
    return disk.percent

def alert(message):
    logging.info(message)
    print(f"ALERT: {message}")

if __name__ == '__main__':
    cpu_usage = check_cpu()
    memory_usage = check_memory()
    disk_usage = check_disk()

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
