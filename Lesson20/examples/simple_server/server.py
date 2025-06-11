# server.py
import socket

HOST = '127.0.0.1'  # Стандартный IP-адрес для localhost (твой компьютер)
PORT = 8080         # Порт, на котором будет работать сервер

def run_server():
    # Создаем сокет (интерфейс для сетевого соединения)
    # socket.AF_INET - используем IPv4
    # socket.SOCK_STREAM - используем TCP (для надежной передачи данных)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # Привязываем сокет к адресу и порту
        s.listen()            # Начинаем слушать входящие соединения

        print(f"Сервер слушает на {HOST}:{PORT}")

        while True:
            # Принимаем входящее соединение
            # conn - новый сокет для обмена данными с клиентом
            # addr - адрес клиента
            conn, addr = s.accept()
            with conn:
                print(f"Подключился клиент: {addr}")

                # Получаем данные от клиента (максимум 1024 байта)
                data = conn.recv(1024)
                print(f"Получено: {data.decode('utf-8').strip()}")

                # Отправляем ответ клиенту
                response = "HTTP/1.1 200 OK\nContent-Type: text/plain; charset=utf-8\n\nПривет от сервера!"
                conn.sendall(response.encode('utf-8'))

                print("Ответ отправлен.")

if __name__ == '__main__':
    run_server()