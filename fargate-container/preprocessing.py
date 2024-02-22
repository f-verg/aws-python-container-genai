from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.image import partition_image
import sys
import os
import boto3
 
s3 = boto3.client('s3')
s3_bucket = os.environ['BUCKET_NAME']
file_key = os.environ['FILE_KEY']
local_pdf_file_path = '/tmp/downloaded_file.pdf'  # Use /tmp directory in Lambda for temporary files

if __name__ == "__main__":
    # Download the PDF file from S3
    s3.download_file(s3_bucket, pdf_file_key, local_pdf_file_path)

    elements = partition_pdf(local_pdf_file_path, strategy='hi_res', include_page_breaks=True, languages=['deu'])
    
    response =  {
        "statusCode" : 200,
        "body" : {"message": "Hello from Fargate", "list" : elements}
    }

    print(json.dumps(response))
