import grpc
from protos.InventoryService_pb2_grpc import InventoryServiceStub
from protos.InventoryService_pb2 import getBookRequest

class InventoryServiceClient:

    def __init__(self, address, port):

        self.address = address
        self.port = port
        self.channel = grpc.insecure_channel(self.address + ":" + self.port)
        self.stub = InventoryServiceStub(self.channel)

    def get_book_titles(self, isbn):

        # call rpc to get the book title given isbn
        try:
            bookReply = self.stub.GetBook(getBookRequest(ISBN = isbn))
            return bookReply.book.title
        except:
            return ""

        

