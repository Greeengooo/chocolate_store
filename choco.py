import boto3

if __name__ == '__main__':
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName='chocolate',
        InvocationType='RequestResponse'
    )
    print(response['Payload'].read())