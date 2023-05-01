import unittest
from opensearchpy import OpenSearch


class TestSearchForWordInDocument(unittest.TestCase):
    def setUp(self):
        self.opensearch = OpenSearch()
        self.index_name = "lorem_ipsum_ind2"
        self.doc_id = "1"
        self.doc = {
            "title": "lorem_ipsum.txt",
            "content": "This is a test document for search",
            "tags": ["test", "search", "document"],
        }

        self.opensearch.index(index=self.index_name, id=self.doc_id, body=self.doc)

    # def tearDown(self):
    #     self.opensearch.delete(index=self.index_name, id=self.doc_id)

    def word_exists_test(self):
        query = {"query": {"match": {"content": "lorem"}}}
        result = self.opensearch.search(index=self.index_name, body=query)
        self.assertEqual(result["hits"]["total"]["value"], 1)

    def word_does_not_exist_test(self):
        query = {"query": {"match": {"content": "hello"}}}
        result = self.opensearch.search(index=self.index_name, body=query)
        self.assertEqual(result["hits"]["total"]["value"], 0)

    def multiple_terms_test(self):
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"content": "test"}},
                        {"match": {"title": "document"}},
                    ]
                }
            }
        }
        result = self.opensearch.search(index=self.index_name, body=query)
        self.assertEqual(result["hits"]["total"]["value"], 1)
