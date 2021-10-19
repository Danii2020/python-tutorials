import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.100.16", 1234)) #remember to change the IP for your server's IP

def send_messages(message):
    msg = message.encode('utf-8')
    client.send(msg)
    print(client.recv(1024).decode('utf-8'))

def run():
    while True:
        message = input("Escribe un mensaje: ")
        send_messages(message)
        if message == 'q':
            send_messages("desconectado")
            break

if __name__ == '__main__':
    run()