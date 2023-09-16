from aws_cdk import (
    # Duration,
    Stack,
    CustomResource,
)
from constructs import Construct

from kendra_constructs import (
    KendraIndex,
    KendraCrawlerV2Datasource,
    CRKendraCrawlerV2Datasource,
    KendraCrawlerDatasource,
)
from s3_cloudfront import S3Deploy
from lambdas import Lambdas


class KendraIndexStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        index = KendraIndex(self, "I")
        # enterprise_index = KendraIndex(self, "IE", edition="ENTERPRISE_EDITION")

        Fn = Lambdas(self, "Fn")

        s3_deploy = S3Deploy(self, "urls", "urls", "s3_urls")

        connect_docs_ds = KendraCrawlerDatasource(
            self,
            "ConnectDocs",
            index_id=index.index_id,
            role_arn=index.role.arn,
            name="connect-docs",
            seed_urls=["https://docs.aws.amazon.com/connect/latest/adminguide/"],
            url_inclusion_patterns=[".*amazon.com/connect/latest/adminguide/.*"],
            url_exclusion_patterns=[".*connect/latest/adminguide/API_.*"],
        )

        connect_Blogs_100 = CRKendraCrawlerV2Datasource(
            self, "Blogs100",
            service_token=Fn.data_source_creator.function_arn,
            index_id= index.index_id,
            role_arn=index.role.arn,
            name = "connect-blogs-100",
            description = "100 Primeros Blogs de Connect",
            seed_urls=None,
            #seed_urls=["https://aws.amazon.com/blogs/contact-center/aws-recognized-as-a-leader-in-2023-gartner-magic-quadrant-for-contact-center-as-a-service-with-amazon-connect/"],
            s3_seed_url = f"s3://{s3_deploy.bucket.bucket_name}/s3_urls/connect_blogs_1.txt",
            url_inclusion_patterns=["*.aws.amazon.com/blogs/contact-center/.*"],
            url_exclusion_patterns=["*./tag/.*"]
        )

        connect_Blogs_200 = CRKendraCrawlerV2Datasource(
            self, "Blogs200",
            service_token=Fn.data_source_creator.function_arn,
            index_id= index.index_id,
            role_arn=index.role.arn,
            name = "connect-blogs-200",
            description = "Blogs de 100 a 200",
            seed_urls=None,
            #seed_urls=["https://aws.amazon.com/blogs/contact-center/aws-recognized-as-a-leader-in-2023-gartner-magic-quadrant-for-contact-center-as-a-service-with-amazon-connect/"],
            s3_seed_url = f"s3://{s3_deploy.bucket.bucket_name}/s3_urls/connect_blogs_2.txt",
            url_inclusion_patterns=["*.aws.amazon.com/blogs/contact-center/.*"],
            url_exclusion_patterns=["*./tag/.*"]
        )
        
 
        connect_workshops = CRKendraCrawlerV2Datasource(
            self, "Workshops",
            service_token=Fn.data_source_creator.function_arn,
            index_id= index.index_id,
            role_arn=index.role.arn,
            name = "connect-workshops",
            description = "workshops",
            seed_urls=None,
            #seed_urls=["https://aws.amazon.com/blogs/contact-center/aws-recognized-as-a-leader-in-2023-gartner-magic-quadrant-for-contact-center-as-a-service-with-amazon-connect/"],
            s3_seed_url = f"s3://{s3_deploy.bucket.bucket_name}/s3_urls/connect_workshops.txt",
            url_inclusion_patterns=["*.aws.amazon.com/blogs/contact-center/.*"],
            url_exclusion_patterns=["*./tag/.*"]
        )
        
 