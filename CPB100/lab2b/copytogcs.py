from google.cloud import storage


def upload_blob():
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    bucket_name = "<バケット名>"
    # The path to your file to upload
    source_file_name = "/home/<ユーザー名>/training-data-analyst/CPB100/lab2b/earthquakes.png"
    # The ID of your GCS object
    destination_blob_name = "latest_earthquake.png"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
upload_blob()