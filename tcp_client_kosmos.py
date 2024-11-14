import socket


def start_kosmos_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'dev.kosmos_server'
    port = 5000

    try:
        client_socket.connect((host, port))

        while True:
            message = input("Ingrese su mensaje (Escriba 'DESCONEXION' para desconectarte del servidor): ")

            if message.upper() == "DESCONEXION":
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
                if data.decode() == "DESCONECTADO":
                    print("Desconectado del servidor.")
                    break
            else:
                if message:
                    client_socket.sendall(message.encode())
                    data = client_socket.recv(1024)
                    print(f"Recibido: {data.decode()}")
                else:
                    print("Por favor ingresa un mensaje válido.")

    except ConnectionRefusedError:
        print("Error: El servidor no esta activo.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Conexión cerrada.")


if __name__ == "__main__":
    start_kosmos_client()

