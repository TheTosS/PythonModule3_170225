# client.py
import socket

HOST = '127.0.0.1'  # Тот же IP, что и у сервера
PORT = 8080  # Тот же порт, что и у сервера


def run_client():
    # Создаем сокет клиента
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Подключаемся к серверу

        message = "Привет, сервер!"
        s.sendall(message.encode('utf-8'))  # Отправляем сообщение серверу

        print(f"Отправлено: '{message}'")

        # Получаем ответ от сервера
        data = s.recv(1024)
        print(f"Получено от сервера:\n{data.decode('utf-8')}")


if __name__ == '__main__':
    run_client()
