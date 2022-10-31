import os
from google.cloud import storage
from datetime import timedelta
import sys

print(sys.argv[1])
# Initiate names
project_id  =  'oceanfriends-71bae' # Your Project ID
bucket_name =  'oceanfriends-71bae.appspot.com' # Name of bucket

##bucket_file =  'file.txt' # Location of the file on Bucket
#local_file  =  'file.txt' # Location of downloaded file on your PC

# Set Credential
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'iamKey.json'

timeS = sys.argv[1]

for i in range(100) :

    # Initialise a client
    client = storage.Client(project_id)

    # Create a bucket object for our bucket
    bucket = client.get_bucket(bucket_name)

    # Create a blob object from the filepath
    # Create a blob object from the filepath
    bucket_file = 'thermalCamera/IM_' + timeS + '_'+str(i) +'.bmp'
    blob = bucket.blob(bucket_file)
	#./images/IM_%s_%d.bmp
    local_file = './images/IM_'  + timeS + '_'+str(i) +'.bmp'
    # Upload the file to a destination
    blob.upload_from_filename(local_file)
    print(local_file+" Uploaded" )


print("done")
