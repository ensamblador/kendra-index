from aws_cdk import (
    Stack,
    CfnOutput
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
        
        files_es = S3Deploy(self, "files_es","files_es", "files_es")
    
        
        s3_files_es_ds = CRKendraS3Datasource(
            self, "S3_pdf_es_reinvent_v3",
            service_token=Fn.data_source_creator.function_arn,
            index_id= index.index_id,
            role_arn=index.role.arn,
            name = "files-reinvent-v3",
            description = "",
            bucket_name=files_es.bucket.bucket_name,
            language_code = 'en',
            inclusion_prefixes=["files_es/reinvent/"],
            #metadata_files_prefix = "files_es/metadata/",
            inclusion_patterns = []
        )
        CfnOutput(self, "output_index_id", value=index.index_id,export_name= "REINVENT-INDEX-ID")
        
        
        


        
