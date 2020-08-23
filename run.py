import psutil
import time


def get_cpu_usage(duration):
    timeout = time.time() + duration

    while True:
        print (psutil.cpu_percent(interval=1))
        #time.sleep(1)

        if time.time() > timeout:
            break

def get_mem_usage(duration):
    timeout = time.time() + duration
    mem = psutil.virtual_memory()

    while True:
        print (mem.percent)
        time.sleep(1)

        if time.time() > timeout:
            break

# =========================================================

print( "O que você quer monitorar?" )
action = int(input( "1-CPU; 2-Memória; 3-Disco:   "))

length = float(input("Por quanto tempo você quer monitorar(segundos)?: "))

if action == 1:
    get_cpu_usage(length)
elif action == 2:
    get_mem_usage(length)

