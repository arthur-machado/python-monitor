import psutil, time, platform

#import socket

# retorna a porcentagem de uso da CPU no intervalo de 1 segundo
def get_cpu_usage():

    return str(psutil.cpu_percent(interval=1))

# retorna a porcentagem de uso da memória
def get_mem_usage():
    
    mem = psutil.virtual_memory()

    return str(mem.percent)

# está retornando o endereço local (127.0.0.1) 
#def get_IP():
    #hostname = socket.gethostname()
    #ip = socket.gethostbyname(hostname)

    #return ip

# quanto espçao de disco está ocupando na raíz (para sistemas Linux) 
def get_disk():
    
    return str(psutil.disk_usage('/').percent)


# boas-vindas
print("\nWelcome to the Python Monitor! :)\nBy Arthur Machado (github.com/arthur-machado) \n\n")

# imprime informações da máquina no início do programa
print("CPU model: " + platform.processor())
print ("OS: " + platform.platform())


# desenha o cabeçalho do monitor
print("=" * 59)
print("||      CPU      ||      MEMORY       ||      DISK       ||")
print("=" * 59)

#imprime as informações enquanto o programa rodar
while True:
    print("||     "+ get_cpu_usage()+"%      ||      "+get_mem_usage()+"%        ||      "+get_disk()+"%      ||")
    print("-"*59)
    time.sleep(1)
