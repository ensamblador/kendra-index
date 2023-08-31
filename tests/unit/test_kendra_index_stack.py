import aws_cdk as core
import aws_cdk.assertions as assertions

from kendra_index.kendra_index_stack import KendraIndexStack

# example tests. To run these tests, uncomment this file along with the example
# resource in kendra_index/kendra_index_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = KendraIndexStack(app, "kendra-index")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
