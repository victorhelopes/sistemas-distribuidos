import socket

from server.User.PortalCliet import PortalClient

class user:
    CID = 0
    def getActivity():
        print('What task would you like to do?')
        print('1 - get all activities')
        print('2 - create an activity')
        print('3 - update an activity')
        print('4 - delete an activity')
        print('5 - delete all activities')
        print('6 - quit')
        Task = int(input('What task would you like to do?'))
        if(Task == 1):
            user.getTask()
        if(Task == 2):
            user.createTask()
        if(Task == 3):
            user.updateTask()
        if(Task == 4):
            user.deleteTask()
        if(Task == 5):
            return [5]
        if(Task == 6):
            print('bye')
            return 6
        if(Task > 5 or Task < 1):    
            print('task does not exists')

    def getTask():
        return [1]

    def createTask(self):
        title = input("What is the title of the activity would you like to create? ")
        description = input("What is the description of the activity? ")  
        return([2,{self.CID, title, description}])

    def updateTask(self):
        title = input("What is the title of the activity would you like to update? ")
        description = input("What is the description of the activity? ")  
        return([3,{self.CID, title, description}])

    def deleteTask(self):
        title = input("What is the title of the activity would you like to delete? ")
        return([4,{self.CID, title}])

    def __main__():
        s = socket.socket()
        host = socket.gethostname()
        port = int(input())
        s.connect((host, port))
        login = 0
        while(login == 0):
            name = input("What is your name? ")
            s.send(0,' ',name)
            login = s.recv(1024)  

        user.CID = login
        while(sair):
            response = user.getActivity()
            if response == 5: sair = False
            s.send(response)
            print(s.recv(1024))


