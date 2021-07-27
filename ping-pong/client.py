import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.

s.connect((host, port))
data = s.recv(1024)
s.send('Thank you for connecting'.encode())
while True:
   x=''
   while x=='':
      x = input('Envie uma mensagem: ')
   s.send(x.encode()) 
   if(x == 'sair'):
      data = s.recv(1024)
      print(data.decode())
      s.close 
      break
   data = ''
   data = s.recv(1024)
   if (data.decode() == 'sair'):
      s.send('Come back often'.encode())
      s.close 
      break
   print('mensagem recebida: ',data.decode())