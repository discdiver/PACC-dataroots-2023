from flows import pipe
from prefect.deployments import Deployment
from prefect.filesystems import Azure

az_block = Azure.load("azure-demo")

deploy = Deployment.build_from_flow(
    flow=pipe,
    name="Azure Example",
    storage=az_block,
)


if __name__ == "__main__":
    deploy.apply()
