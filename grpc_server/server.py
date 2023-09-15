import grpc
import logging

from concurrent import futures

from grpc_server.pkg.grpc_server_pb2 import GetUsersResponse

from grpc_server.pkg.grpc_server_pb2_grpc import MyAwesomeServiceServicer, add_MyAwesomeServiceServicer_to_server


class MyAwesomeServer(MyAwesomeServiceServicer):
    def GetUsers(self, request, context):
        users = [
            {
                'user_id': 1,
                'user_name': "user_1",
            },
            {
                'user_id': 2,
                'user_name': "user_2",
            },
            {
                'user_id': 3,
                'user_name': "user_3",
            },
        ]

        users_response = [
            GetUsersResponse.User(user_id=u['user_id'], user_name=u['user_name']) for u in users
        ]

        return GetUsersResponse(users=users_response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MyAwesomeServiceServicer_to_server(
        MyAwesomeServer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
