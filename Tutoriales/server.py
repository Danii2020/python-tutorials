import socket
import threading as tr
import pyttsx3
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 1234))

def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()

def handle_connection(connection, address):
    conectado = True
    while conectado:
        message = connection.recv(1024).decode('utf-8')
        if message == 'desconectado':
            conectado = False
        talk(message)
        connection.send("Mensaje recibido!".encode('utf-8'))
    connection.close()


def start_connection():
    s.listen(2)
    while True:
        connection, address = s.accept()
        thread = tr.Thread(target=handle_connection, args=(connection, address))
        thread.start()
        print("Iniciando conexión...")
        print(f"Conexiones activas {tr.activeCount() - 1}")

if __name__ == '__main__':
    print("Servidor escuchando..")
    start_connection()