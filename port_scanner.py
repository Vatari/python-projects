import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Въведете ip address или домейн: ')

HOST = socket.gethostbyname(target)
print(f'Сканиране на {HOST}....')


def port_scan(port):
    try:
        s.connect((HOST, port))
        return True
    except:
        return False


start = time.time()


for port in range(80, 86):
    if port_scan(port):
        print(f'порт {port} е отворен')
    else:
        print(f'порт {port} е затворен')

end = time.time()
print(f'Време на изпълнение: {end - start:.2f} секунди')
