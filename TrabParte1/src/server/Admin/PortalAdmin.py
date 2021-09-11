import sys
sys.path.append("..\..\server")

from data import data 

from concurrent import futures
import logging

import admin_pb2
import admin_pb2_grpc

import grpc

class PortalAdmin(admin_pb2_grpc.PortalAdminServicer):

    def createUser(name):
        if(hash(name) > len(data.user)):
            for i in range(0,len(data.user) - hash(name)):
                data.user.append(0)
        data.user[hash(name)] = {hash(name), name}
        return admin_pb2.Response(hash(name))

    def updateUser(name):
        if(data.user[hash(name)] == 0):
            return 'error'
        data.user[hash(name)] = {hash(name), name}
        return admin_pb2.Response('OK')

    def deleteUser(name):
        if(data.user[hash(name)] == 0):
            return 'error'
        data.user[hash(name)]
        data.user[hash(name)] = 0
        return admin_pb2.Response('removed')
    def getUser(name):
        return admin_pb2.Response(data.user[hash(name)])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_PortalAdminServicer_to_server(PortalAdmin(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.baseConfig()
    serve()