import grpc

from grpc_server.pkg.grpc_server_pb2 import GetUsersRequest
from grpc_server.pkg.grpc_server_pb2_grpc import MyAwesomeServiceStub


def get_users_response(client):
    response = client.GetUsers(GetUsersRequest())
    print(response)


if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = MyAwesomeServiceStub(channel)
        get_users_response(stub)
