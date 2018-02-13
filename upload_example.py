from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('gs://realcamera-e0491.appspot.com')
blob = bucket.blob('raspi.jpg')
blob.upload_from_string('this is test')
