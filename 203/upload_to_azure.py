from prefect import flow
from prefect.filesystems import Azure


@flow()
def upload_to_azure() -> None:
    """The main flow function to upload taxi data"""

    az_block = Azure.load("azure-demo")
    az_block.put_directory(local_path="data", to_path="data")


if __name__ == "__main__":
    upload_to_azure()
