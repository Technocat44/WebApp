import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    '''
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.   f
    
    '''

    def handle(self):
        # self.request is the TCP socket connected to the client
        received_data = self.request.recv(1024).strip()
        print(self.client_address[0] + "is sending data: ") #self.client_address gives us the info about the requester
        print(received_data.decode()) # this turns the data into a string
        print("\n\n")
        
        self.request.sendall("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 17\r\n\r\nWhat's up world!!".encode())

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C

    server = socketserver.ThreadingTCPServer((host, port), MyTCPHandler)
    server.serve_forever()

