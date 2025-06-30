from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.mobile import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from diagrams.aws.analytics import Athena, Glue
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import Client

with Diagram(
    name="Complex Serverless Event-Driven AWS Architecture",
    show=False,
    filename="serverless_architecture",
    outformat="png"
):
    user = Client("User")
    auth = Cognito("User Auth")
    api = APIGateway("API Gateway")
    
    # Lambda Layers
    auth_lambda = Lambda("Authorizer Lambda")
    main_lambda = Lambda("Main Lambda")
    worker_lambda = Lambda("Worker Lambda")
    
    # Messaging
    sns = SNS("Event Topic")
    sqs = SQS("Worker Queue")
    
    # Storage & Database
    s3 = S3("Raw File Storage")
    db = Dynamodb("Application DB")
    
    # Analytics
    glue = Glue("Glue ETL")
    athena = Athena("Athena Query")
    
    # Monitoring
    logs = Cloudwatch("CloudWatch Logs")

    # Connections
    user >> auth >> api >> auth_lambda
    api >> main_lambda
    main_lambda >> [sns, s3, db, logs]
    sns >> sqs >> worker_lambda >> db
    s3 >> glue >> athena
