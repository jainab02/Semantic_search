from elasticsearch import Elasticsearch
from utils.embeddings import embed_text

# Initialize Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

def search_documents(query):
    query_embedding = embed_text(query)
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_embedding}
            }
        }
    }
    response = es.search(index="documents", query=script_query)
    results = [hit["_source"]["filename"] for hit in response["hits"]["hits"]]
    return results
