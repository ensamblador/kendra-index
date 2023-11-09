from aws_cdk import (
    Stack
)
from constructs import Construct

from kendra_constructs import (
    KendraIndex, CRKendraCrawlerV2Datasource,
    KendraCrawlerDatasource, CRKendraS3Datasource
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
        '''
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
            description = "Blogs de 101 a 162",
            seed_urls=None,
            s3_seed_url = f"s3://{s3_deploy.bucket.bucket_name}/s3_urls/connect_blogs_2.txt",
            url_inclusion_patterns=["*.aws.amazon.com/blogs/contact-center/.*"],
            url_exclusion_patterns=["*./tag/.*"]
        )
        '''
        
        files_es = s3_deploy.deploy("files_es","files_es", "files_es")
        
        s3_files_es_ds = CRKendraS3Datasource(
            self, "S3_pdf_es",
            service_token=Fn.data_source_creator.function_arn,
            index_id= index.index_id,
            role_arn=index.role.arn,
            name = "files-es",
            description = "documentos en español",
            bucket_name=s3_deploy.bucket.bucket_name,
            language_code = 'es',
            inclusion_prefixes=["documents/"],
            metadata_files_prefix = "metadata/",
            inclusion_patterns = []

        )
        
        


        
