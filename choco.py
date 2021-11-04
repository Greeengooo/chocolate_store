import boto3


def lambda_handler(event, context):
    ls = []
    k = int(event["budget"])
    res = k
    while k != 0:
        ls.append(k % 3)
        k = k // 3
        res += k
    reminder = sum(ls) // 3
    maximum_number = res + reminder
    return {
        'statusCode': 200,
        'body': maximum_number
    }