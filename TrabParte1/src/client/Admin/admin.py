from server.User.PortalCliet import PortalClient
from server.Admin.PortalAdmin import PortalAdmin

class admin:
    def getActivity():
        print('What activity would you like to do?')
        print('1 - get all activities')
        print('2 - create an activity')
        print('3 - update an activity')
        print('4 - delete an activity')
        print('5 - quit')
        activity = int(input('What user would you like to do?'))

        if(activity == 1):
            admin.getUser()
        if(activity == 2):
            admin.createUser()
        if(activity == 3):
            admin.updateuser()
        if(activity == 4):
            admin.deleteUser()
        if(activity == 5):
            print('bye')
            return 1
        if(activity > 5 or activity < 1):    
            print('user does not exists')

    def createUser():
        name = input('Qual o nome do novo usuario: ')
        return PortalAdmin.createUser(name)
    
    def updateUser(name):
        name = input('Qual o nome do novo usuario: ')
        return(PortalAdmin.updateUser(name))


    def deleteUser():
        name = input('Qual o nome do novo usuario: ')
        return(PortalAdmin.updateUser(name))

    def getUser():
        name = input('Qual o nome do novo usuario: ')
        return(PortalAdmin.getUser(name)) 
