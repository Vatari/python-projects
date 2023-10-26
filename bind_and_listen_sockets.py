import socket
import sys

HOST = "10.10.101.22"
PORT = int(input("Въведете порт: "))

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((HOST, PORT))

except socket.error as message:

    print('Bind failed. Error Code : '
          + str(message[0]) + ' Message '
          + message[1])
    sys.exit()

print(f"Сървъра e стартиран на: {HOST}:{PORT}")

soc.listen()

while True:
    try:
        conn, address = soc.accept()
        print('Свързване от ' + address[0] + ':' + str(address[1]))

        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Клиент {address[0]}:{str(address[1])} прекъсна връзката.")
                break
            print(data.decode())
            server_data = input()
            conn.send(server_data.encode())



    except Exception as e:
        print("Връзката е прекъсната!")
        break
