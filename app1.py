

import os
from google.cloud import storage
from datetime import timedelta
import sys

#print(sys.argv[1])
# Initiate names
project_id  =  'oceanfriends-71bae' # Your Project ID
bucket_name =  'oceanfriends-71bae.appspot.com' # Name of bucket


# Set Credential
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'iamKey.json'


# Initialise a client
client = storage.Client(project_id)

# Create a bucket object for our bucket
bucket = client.get_bucket(bucket_name)

# Create a blob object from the filepath
bucket_file = 'thermalCamera/rawdata1667013943_23.pgm'

blob = bucket.blob(bucket_file)

local_file = './images/rawdata1667013943_23.pgm'

# Upload the file to a destination
blob.upload_from_filename(local_file)


print("done")






