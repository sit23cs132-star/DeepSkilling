from azure.storage.blob import BlobServiceClient

client = BlobServiceClient.from_connection_string("CONNECTION_STRING")
container = client.get_container_client("mycontainer")
with open("data.txt", "rb") as data:
    container.upload_blob("data.txt", data)
