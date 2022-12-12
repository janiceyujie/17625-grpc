from unittest.mock import Mock
import unittest
import inventory_client
from get_book_titles import get_book_titles

class TestInventory(unittest.TestCase):

    @unittest.mock.patch('get_book_titles.InventoryServiceClient.get_book_titles', return_value = 'title1')
    def test_without_running_server(self, mock_client):
        client = inventory_client.InventoryServiceClient(address = "localhost", port = "50051")
        isbns = ["ISBN1"]
        titles = get_book_titles(client, isbns)
        self.assertEqual(1, len(titles))
        self.assertEqual("title1", titles[0])

    def test_with_running_server(self):
        client = inventory_client.InventoryServiceClient(address = "localhost", port = "50051")
        isbns = ["ISBN1", "ISBN2"]
        titles = get_book_titles(client, isbns)
        self.assertEqual(2, len(titles))
        self.assertEqual("title1", titles[0])
        self.assertEqual("title2", titles[1])


if __name__ == '__main__':
    unittest.main()
    

# create a mock of InventoryServiceClient
# write a unit test for business logic defined in `client/get_book_titles.py
# pass the newly created mock object as a client API accessor
# Make sure tests can be run without a server running