from aws_cdk import Stack, CfnOutput, aws_ssm as ssm
from constructs import Construct

from kendra_constructs import KendraIndex



class KendraIndexStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # self.index = KendraIndex(self, "I")
        self.index = KendraIndex(self, "IE", edition="ENTERPRISE_EDITION")
        self.create_ssm_param("kendra-index-id", self.index.index_id)
        CfnOutput(self, "output_index_id", value=self.index.index_id)

    def create_ssm_param(self, name, value):
        ssm.StringParameter(
            self,
            f"ssm-{name}",
            parameter_name=f"/gen-ai-apps/{name}",
            string_value=value,
        )