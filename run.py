import psutil, time, platform

#import socket

# retorna a porcentagem de uso da CPU no intervalo de 1 segundo
def get_cpu_usage():

    use = psutil.cpu_percent(interval=1)
    use_str = str(use)

    if use < 45:
        return u"\u001b[32;1m" + use_str
    
    elif use >= 45 and use <= 83.9:
        return u"\u001b[33m" + use_str

    elif use >= 84:
        return u"\033[1;31;40m" + use_str

# retorna a porcentagem de uso da memória
def get_mem_usage():
    
    mem_total = psutil.virtual_memory().total / (1024 ** 3) # converte para GB
    mem_used = psutil.virtual_memory().used / (1024 ** 3)
    percent = round((mem_used * 100 / mem_total), 1) # calcula porcentagem e arredonda
    mem_str = str(percent)

    if percent < 45.0:
        return u"\u001b[32;1m" + mem_str
    
    elif percent >= 45 and percent <= 84.9:
        return u"\u001b[33m" + mem_str

    elif percent >= 85:
        return u"\033[1;31;40m" + mem_str



# está retornando o endereço local (127.0.0.1) 
#def get_IP():
    #hostname = socket.gethostname()
    #ip = socket.gethostbyname(hostname)

    #return ip

# quanto espçao de disco está ocupando na raíz (para sistemas Linux) 
def get_disk():
    
    return str(psutil.disk_usage('/').percent)


# boas-vindas
print("\nWelcome to the Python Monitor! :)\nBy Arthur Machado (github.com/arthur-machado) \n")

# imprime informações da máquina no início do programa
print("CPU model: " + platform.processor())
print ("OS: " + platform.platform())
print("Disk usage: " + get_disk()+"%\n")


# desenha o cabeçalho do monitor
print(u"\u001b[37;1m=" * 40)
print(u"\u001b[37;1m||      CPU       ||      MEMORY      ||")
print(u"\u001b[37;1m=" * 40)

#imprime as informações enquanto o programa rodar
while True:
    try:
        print(u"\u001b[37;1m||     "+ get_cpu_usage()+"%      \u001b[37;1m||      "+get_mem_usage()+"%        \u001b[37;1m||")
        print(u"\u001b[37;1m-"*40)
        time.sleep(0.8)
    
    except KeyboardInterrupt:
        print("\nPrograma finalizado!")
        break