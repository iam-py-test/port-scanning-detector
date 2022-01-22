from http.server import BaseHTTPRequestHandler, HTTPServer
import time

try:
	hostname = input("Enter a hostname to use: ")
	serverPort = int(input("Enter a port to use: "))
except:
	print("Invalid hostname or port")
	input()
	import sys
	sys.exit()

class ps_detect(BaseHTTPRequestHandler):
	def do_GET(self):
		print(self)
		self.send_response(404)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(bytes("not found", "utf-8"))


if __name__ == "__main__":        
	webServer = HTTPServer((hostname, serverPort), ps_detect)
	print("Server started http://%s:%s" % (hostname, serverPort))
	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass
	webServer.server_close()
	print("Server stopped.")