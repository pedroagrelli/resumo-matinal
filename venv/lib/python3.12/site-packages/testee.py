import boto3

ses = boto3.client("ses", region_name="us-east-1")

response = ses.send_email(
    Source="pedroagrelli34@gmail.com",
    Destination={"ToAddresses": ["pedroagrelli34@gmail.com"]},
    Message={
        "Subject": {"Data": "Teste de envio via SES"},
        "Body": {"Text": {"Data": "Olá, este é um teste do meu app!"}}
    }
)
print(response)