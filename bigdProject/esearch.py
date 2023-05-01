from opensearchpy import OpenSearch

# Connect to OpenSearch
opensearch = OpenSearch(["http://localhost:9200"])

# Define the search query
query = {"query": {"match": {"content": "Vaishnavi"}}}

# Execute the search and print the results
response = opensearch.search(index="lorem_ipsum_ind", body=query)
for hit in response["hits"]["hits"]:
    print(hit["_source"]["filename"])
