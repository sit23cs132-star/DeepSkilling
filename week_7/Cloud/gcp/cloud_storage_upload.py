from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket("mybucket")
blob = bucket.blob("data.txt")
blob.upload_from_filename("data.txt")
