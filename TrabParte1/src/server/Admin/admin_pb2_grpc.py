# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import admin_pb2 as admin__pb2


class PortalAdminStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createUser = channel.unary_unary(
                '/helloworld.PortalAdmin/createUser',
                request_serializer=admin__pb2.Request.SerializeToString,
                response_deserializer=admin__pb2.Response.FromString,
                )
        self.updateUser = channel.unary_unary(
                '/helloworld.PortalAdmin/updateUser',
                request_serializer=admin__pb2.Request.SerializeToString,
                response_deserializer=admin__pb2.Response.FromString,
                )
        self.deleteUser = channel.unary_unary(
                '/helloworld.PortalAdmin/deleteUser',
                request_serializer=admin__pb2.Request.SerializeToString,
                response_deserializer=admin__pb2.Response.FromString,
                )
        self.getUser = channel.unary_unary(
                '/helloworld.PortalAdmin/getUser',
                request_serializer=admin__pb2.Request.SerializeToString,
                response_deserializer=admin__pb2.Response.FromString,
                )


class PortalAdminServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createUser(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PortalAdminServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createUser': grpc.unary_unary_rpc_method_handler(
                    servicer.createUser,
                    request_deserializer=admin__pb2.Request.FromString,
                    response_serializer=admin__pb2.Response.SerializeToString,
            ),
            'updateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.updateUser,
                    request_deserializer=admin__pb2.Request.FromString,
                    response_serializer=admin__pb2.Response.SerializeToString,
            ),
            'deleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteUser,
                    request_deserializer=admin__pb2.Request.FromString,
                    response_serializer=admin__pb2.Response.SerializeToString,
            ),
            'getUser': grpc.unary_unary_rpc_method_handler(
                    servicer.getUser,
                    request_deserializer=admin__pb2.Request.FromString,
                    response_serializer=admin__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.PortalAdmin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PortalAdmin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.PortalAdmin/createUser',
            admin__pb2.Request.SerializeToString,
            admin__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.PortalAdmin/updateUser',
            admin__pb2.Request.SerializeToString,
            admin__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.PortalAdmin/deleteUser',
            admin__pb2.Request.SerializeToString,
            admin__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.PortalAdmin/getUser',
            admin__pb2.Request.SerializeToString,
            admin__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
