import socket 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates server
server.bind(('0.0.0.0', 9999))  # http://localhost:9999/

server.listen()

while True:    
    client_connection, client_address = server.accept()

    request = client_connection.recv(1024).decode()
    print(request)

   # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':      # http://localhost:9999/
        filename = '/index.html'      
    elif filename == '/aboutus':     # http://localhost:9999/aboutus.html
        filename = '/aboutus.html'
    else : 
        filename = '/page_not_fount.html'

    fin = open('htdocs' + filename)
    content = fin.read()
    fin.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
# server.close()


''' 
server.bind() :  The bind() method takes a single argument: a tuple containing the host (IP address) and port number. 
host:
'127.0.0.1' or 'localhost': Binds the socket so it can only accept connections from within the same machine (loopback interface).
'0.0.0.0' or an empty string '': Binds the socket to all available IPv4 interfaces, allowing connections from other computers on the network.

'''