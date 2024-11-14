import socket


def start_kosmos_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = '0.0.0.0'
    port = 5000
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida con el cliente: {client_address}")

        while True:
            data_client = client_socket.recv(1024)
            if not data_client:
                break
            message_client = data_client.decode()
            if message_client.upper() == "DESCONEXION":
                print(f"Cliente {client_address} pidió desconectar. Cerrando conexión.")
                response = "DESCONECTADO"
                client_socket.sendall(response.encode())
                break
            print(f"Recibido: {message_client}")
            response = message_client.upper()
            client_socket.sendall(response.encode())
        client_socket.close()
        print(f"Conexión con el cliente {client_address} cerrada.")


if __name__ == '__main__':
    start_kosmos_server()
