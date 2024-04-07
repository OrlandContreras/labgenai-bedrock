import json
import boto3

boto3_bedrock = boto3.client("bedrock")
response = json.dumps(boto3_bedrock.list_foundation_models())
print(response)
