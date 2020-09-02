import psutil
import time
import socket

def get_cpu_usage():

    return str(psutil.cpu_percent(interval=1))
        

def get_mem_usage():
    
    mem = psutil.virtual_memory()

    return str(mem.percent)

def get_IP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return ip

def get_disk():
    return str(psutil.disk_usage('/').percent)


print("=" * 59)
print("||      CPU      ||      MEMORY       ||      DISK       ||")
print("=" * 59)

while True:
    print("||     "+ get_cpu_usage()+"%      ||      "+get_mem_usage()+"%       ||      "+get_disk()+"%      ||")
    print("-"*59)
    time.sleep(1)
