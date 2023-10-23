import requests
import os

def database_get(path: str):
    url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

    headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return str(response.json())
    else:
        return f"Request failed with status code {response.status_code}"
        

def database_post(path: str, data: dict):
    url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

    headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=data, headers=headers)
    
    return str(response.json())
        
def database_delete(path: str):
    url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

    headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return str(response.json())
    else:
        return f"Request failed with status code {response.status_code}"