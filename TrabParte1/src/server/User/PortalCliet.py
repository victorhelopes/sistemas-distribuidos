from socket import socket
from data.data import data 
from client.Admin.admin import admin

class PortalClient:
    def login(name):
        return data.user[admin.getUser(name)]

    def createTask(CID, title, description):
        if(hash(title) > len(data.task)):
            for i in range(0,len(data.task) - hash(title)):
                data.task.append(0)
        data.task[hash(title)] = {CID, title, description}
        return (CID, title, description)

    def updateTask(CID, title, description):
        if(data.task[hash(title)] == 0):
            return 'error'
        data.task[hash(title)] = {hash(title), title, description}
        return'OK'

    def deleteTask(CID, title):
        if(data.task[hash(title)] == 0):
            return 'error'
        removed = data.task[hash(title)]
        data.task[hash(title)] = 0
        return 'removed'

    def deleteAllTasks(CID):
        for i in range(0,data.task):
            if data.task[i] != 0:
                if( data.task[i].CID == CID):
                    data.task[i] = 0
        return 'success'

    def __main__():
        s = socket()               
        host = socket.getsockname()         
        port = int(input())                  
        s.bind((host, port))                

        s.listen(5)                         
        c, addr = s.accept()                
        print('Got connection from', addr)

        c.send('Thank you for connecting'.encode())
        info = c.recv(1024)
        if(len(data.user) < hash(info)):
            info = PortalClient.login(info)
            if(info  != 0):
                return info
            return 0
        info = c.recv(1024)
        if(info[0] == 1):
            return 1
        if(info[0] == 2):
            PortalClient.createTask(info[1])
            return 'success'
        if(info[0] == 3):
            PortalClient.updateTask(info[1])
        if(info[0] == 4):
            PortalClient.deleteTask(info[1])
        if(info[0] == 5):
            PortalClient.deleteAllTasks()