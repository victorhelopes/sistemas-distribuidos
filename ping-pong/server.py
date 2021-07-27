import socket                               # Import socket module

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)                                 # Now wait for client connections.
c, addr = s.accept()                     # Establish connection with client.
print('Got connection from', addr)

c.send('Thank you for connecting'.encode())
data = c.recv(1024)
print('Start connection:',data)
while True:
   x=''
   data = ''
   data = c.recv(1024)
   print('mensagem recebida: ', data.decode())
   if (data.decode() == 'sair'):
      c.send('Come back often'.encode())
      c.close   
      break   
   while x =='':
      x = input('Envie uma mensagem: ')
   c.send(x.encode())
   if(x == 'sair'):
      data = c.recv(1024)
      print(data.decode())
      c.close 
      break
      
