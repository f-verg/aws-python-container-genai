import sys
from langchain_community.llms import Bedrock

def handler(event, context):
    # Simple test of psycopg2
    # conn = psycopg2.connect("dbname=test user=postgres password=postgres")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'