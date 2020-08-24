import psutil
import time
import socket

def get_cpu_usage():

    return psutil.cpu_percent(interval=1)
        

def get_mem_usage():
    
    mem = psutil.virtual_memory()

    return mem.percent

def get_IP():
    print (socket.getfqdn(socket.gethostname()))

    
    
     
# =========================================================

print("=" * 39)
print("||      CPU      ||      MEMORY       ||")
print("=" * 39)
get_IP()
while True:
    print("||     "+str(get_cpu_usage())+"%      ||      "+str(get_mem_usage())+"%       ||")
    print("-"*39)
    time.sleep(1)