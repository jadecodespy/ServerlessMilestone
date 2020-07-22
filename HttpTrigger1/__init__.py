import logging
import random
import requests
import azure.functions as func
from azure.cosmos import CosmosClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    getnumbers = requests.get('https://jadeazfunction.azurewebsites.net/api/HttpTrigger2?code=rFIbZDWG04Um4U1tQ1LtZkVuOrUda13UrMc7buN3nHCBu/BEGoniug==')
    getletters = requests.get('https://jadeazfunction.azurewebsites.net/api/HttpTrigger3?code=3vYSLRruH2cdxNqFDmH1OW56C0BNmJpnENKhpuk08uwWR4bGbhU2Ig==')
    
    numbers = getnumbers.text 
    letters = getletters.text
    answer = []


    for i in range(5):
        answer.append(numbers[i])
        answer.append(letters[i])
    finalans="".join(answer)
    
    key = "nvzumL7YLMAIS9H6P3Ya2aID31eY0n4yvwzkioiIgPXLw8Tvy9KGt8RX4EPFi81PN4fgN5nQ4LxMTio8S6XmWA=="
    endpoint = "https://serverlessmilestone-1.documents.azure.com:443/;AccountKey=nvzumL7YLMAIS9H6P3Ya2aID31eY0n4yvwzkioiIgPXLw8Tvy9KGt8RX4EPFi81PN4fgN5nQ4LxMTio8S6XmWA==;"
    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    client.create_database_if_not_exist(id=database_name)
    
    container_name= "UsernameContainer"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path/"id"), offer_throughput=400
    )
    
    return str(finalans)


 