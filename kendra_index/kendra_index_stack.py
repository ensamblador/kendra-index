from aws_cdk import (
    # Duration,
    Stack,
)
from constructs import Construct

from kendra_constructs import (KendraIndex, KendraCrawlerV2Datasource,KendraCrawlerDatasource )
class KendraIndexStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        index = KendraIndex(self, "I")
        
        connect_docs_ds = KendraCrawlerDatasource(
            self, "ConnectDocs",
            index_id= index.index_id,
            role_arn=index.role.arn,
            name = "connect-docs",
            seed_urls=["https://docs.aws.amazon.com/connect/latest/adminguide/"],
            url_inclusion_patterns=[".*amazon.com/connect/latest/adminguide/.*"],
            url_exclusion_patterns=[".*connect/latest/adminguide/API_.*"]
        )
    
