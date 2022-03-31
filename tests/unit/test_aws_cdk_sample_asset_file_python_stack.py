import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_sample_asset_file_python.aws_cdk_sample_asset_file_python_stack import AwsCdkSampleAssetFilePythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_sample_asset_file_python/aws_cdk_sample_asset_file_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkSampleAssetFilePythonStack(app, "aws-cdk-sample-asset-file-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
