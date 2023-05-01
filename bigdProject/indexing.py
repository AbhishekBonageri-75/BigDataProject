from opensearchpy import OpenSearch
import chardet


# Connect to OpenSearch
opensearch = OpenSearch(["http://localhost:9200"])

# Define the index mapping
mapping = {
    "mappings": {
        "properties": {"filename": {"type": "keyword"}, "content": {"type": "text"}}
    }
}

# Create the index with the mapping
opensearch.indices.create(index="lorem_ipsum_ind2", body=mapping)

# Read the file contents and index them in OpenSearch
with open("Lorem_Ipsum.txt", "rb") as f:
    content = f.read()
    result = chardet.detect(content)
    file_encoding = result["encoding"]
    content = content.decode(file_encoding)

doc = {"filename": "Lorem_Ipsum.txt", "content": content}
opensearch.index(index="lorem_ipsum_ind", body=doc)
