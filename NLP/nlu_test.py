# import IBM API key from ibm-credentials.env
import os
from dotenv import load_dotenv
# import necessary libraries for IBM Cloud
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions

load_dotenv('ibm-credentials.env')
API_KEY = os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_APIKEY')

authenticator = IAMAuthenticator(API_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

url = 'https://www.locanto.ie/Labour/606/'

natural_language_understanding.set_service_url(url)

response = natural_language_understanding.analyze(
    url='https://www.locanto.ie/Labour/606/',
    features=Features(entities=EntitiesOptions(sentiment=True, limit=1))).get_result()

print(json.dumps(response, indent=2))
