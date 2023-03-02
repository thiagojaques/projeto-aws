import aws_cdk as core
import aws_cdk.assertions as assertions

from projeto_aws.projeto_aws_stack import ProjetoAwsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in projeto_aws/projeto_aws_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjetoAwsStack(app, "projeto-aws")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
