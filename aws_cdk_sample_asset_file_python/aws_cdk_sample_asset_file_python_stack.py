from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ecs as ecs,
)
from constructs import Construct

config_path = ""
container_path = ""


class AwsCdkSampleAssetFilePythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        task_definition = ecs.Ec2TaskDefinition(self, id="ec2_task")
        env_file = ecs.AssetEnvironmentFile.from_asset(path=config_path)
        container_image = ecs.ContainerImage.from_asset(directory=container_path)

        cluster = ecs.Cluster(self, id="cluster")
        container_definition = ecs.ContainerDefinition(
            self,
            "container",
            task_definition=task_definition,
            environment_files=[env_file],
            image=container_image,
        )
        ecs_service = ecs.Ec2Service(
            self, "service", task_definition=task_definition, cluster=cluster
        )
