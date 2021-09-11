import logging;

from server.Admin.admin_pb2_grpc import PortalAdminStub;
from server.Admin.admin_pb2 import Request;

import grpc
class admin():
    def getActivity():
        channel = grpc.insecure_channel('localhost:50051')
        stub = PortalAdminStub(channel)
        while not(activity == 5):
            print('What activity would you like to do?')
            print('1 - get all activities')
            print('2 - create an activity')
            print('3 - update an activity')
            print('4 - delete an activity')
            print('5 - quit')
            activity = int(input('What user would you like to do?'))

            if(activity == 1):
                response = stub.getUser()
                print('Id do usuario',response.message)

            if(activity == 2):
                PersonName = input("What's your name? ")
                response = stub.createUser(Request(name=PersonName))
                print('Id do usuario',response.message)

            if(activity == 3):
                PersonName = input("What's the name of the person would like to update? ")
                response = stub.updateUser(Request(name=PersonName)) # i have to pass the new name of the person
                print('Usuario atualizado',response.message)

            if(activity == 4):
                PersonName = input("What's the name of the person would like to update? ")
                response = stub.deleteUser(Request(name=PersonName)) 
                print('Usuario atualizado',response.message)

            if(activity == 5):
                print('bye')
                return 1

            if(activity > 5 or activity < 1):    
                print('user does not exists')

if __name__ == '__main__':
    logging.basicConfig()
    admin.getActivity()