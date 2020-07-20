import logging
import random
import string
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    listletters = []
    for i in range(5):
        listletters.append(random.choice(string.ascii_letters))
    newletters="".join(listletters)
    return str(newletters)