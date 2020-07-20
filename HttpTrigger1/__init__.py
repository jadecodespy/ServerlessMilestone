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


    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    client.create_database_if_not_exist(id=database_name)
    return str(finalans)
 