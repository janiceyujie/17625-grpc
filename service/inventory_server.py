from concurrent import futures
import grpc
import protos.inventory_pb2 as inventory_pb2
import protos.InventoryService_pb2_grpc as InventoryService_pb2_grpc
import protos.InventoryService_pb2 as InventoryService_pb2 

class InventoryServiceServer(InventoryService_pb2_grpc.InventoryServiceServicer):

    def __init__(self):

        self.books = {
            "ISBN1": inventory_pb2.Book(ISBN = "ISBN1", title = "title1", author = "author1", genre = 0, publishing_year = 2000),
            "ISBN2": inventory_pb2.Book(ISBN = "ISBN2", title = "title2", author = "author2", genre = 1, publishing_year = 2001),
            "ISBN3": inventory_pb2.Book(ISBN = "ISBN3", title = "title3", author = "author3", genre = 2, publishing_year = 2002)
        }

    def CreateBook(self, request, context):
        """
            given the book details, create and store the book object.
            Data is stored in a dictionary with the ISBN being the keys, 
            and the book object being the values.
        """
        isbn = request.ISBN
        title = request.title
        author = request.author
        genre = request.genre
        year = request.publishing_year

        if isbn == "" or title == "" or author == "" or year == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Missing fields")
        
        new_book = inventory_pb2.Book(ISBN = isbn, title = title, author = author, genre = genre, publishing_year = year)
        self.books[isbn] = new_book

        return InventoryService_pb2.createReply(code = 0, message = "Success")

    def GetBook(self, request, context):
        
        """
            given the ISBN, return the book object
        """
        isbn = request.ISBN

        if isbn not in self.books.keys():
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No book found for the specified ISBN")

        book = self.books[isbn]

        return InventoryService_pb2.getBookReply(code = 0, message = "Success", book = book)

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    InventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServiceServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()