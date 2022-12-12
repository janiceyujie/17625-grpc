from inventory_client import InventoryServiceClient

def get_book_titles(client, isbns):
    """
        taking a list of ISBNs, 
        calling GetBook RPC to retrieve corresponding titles, 
        and return them as a list.
    """
    titles = []
    for isbn in isbns:
        title = client.get_book_titles(isbn)
        titles.append(title)
    return titles
        

if __name__ == '__main__':
    # create an instance of client api object with reasonable defaults to access the server
    client = InventoryServiceClient(address = "localhost", port = "50051")
    # call the defined function using two hardcoded ISBNs as a parameter
    isbns = ["ISBN1", "ISBN2"]
    titles = get_book_titles(client, isbns)
    # print returned titles to standard output
    print(titles)