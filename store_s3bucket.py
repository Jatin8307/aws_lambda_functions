import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='s3bucket2111'
#my bucket name is s3bucket2111
	transactionToUpload = {}
	transactionToUpload['transactionId'] = '12345'
	transactionToUpload['type'] = 'PURCHASE'
	transactionToUpload['amount'] = 23874682734
	transactionToUpload['customerId'] = 'to_be_uploaded'

	fileName = 'to_be_uploaded' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Put Complete')
