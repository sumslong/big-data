import logging
import os
import cloudstorage as gcs
import webapp2

#from google.appengine.api import app_identity

import csv
from io import StringIO

from google.cloud import storage

def read_csv_from_cloud(BUCKET_NAME, FILE_NAME)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(BUCKET_NAME)

    blob = bucket.blob(FILE_NAME)
    blob = blob.download_as_string()
    blob = blob.decode('utf-8')

    blob = StringIO(blob)  #tranform bytes to string here

    names = csv.reader(blob)  #then use csv library to read the content

    #for name in names:
     #   print(f"First Name: {name[0]}")

    return names
    






# def get(self):
#     bucket_name = "big-data-project_storage-bucket" #os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())

#     self.response.headers['Content-Type'] = 'text/plain'
#     self.response.write('Demo GCS Application running from Version: '
#                       + os.environ['CURRENT_VERSION_ID'] + '\n')
#     self.response.write('Using bucket name: ' + bucket_name + '\n\n')


# def create_file(self, filename):
#     """Create a file.

#     The retry_params specified in the open call will override the default
#     retry params for this particular file handle.

#     Args:
#       filename: filename.
#     """
#     self.response.write('Creating file %s\n' % filename)

#     write_retry_params = gcs.RetryParams(backoff_factor=1.1)
#     gcs_file = gcs.open(filename,
#                       'w',
#                       content_type='text/plain',
#                       options={'x-goog-meta-foo': 'foo',
#                                'x-goog-meta-bar': 'bar'},
#                       retry_params=write_retry_params)
#     gcs_file.write('abcde\n')
#     gcs_file.write('f'*1024*4 + '\n')
#     gcs_file.close()
#     self.tmp_filenames_to_clean_up.append(filename)


# def read_file(self, filename):
#     self.response.write('Reading the full file contents:\n')
#     #gs://big-data-project_storage-bucket/med_data.csv

#     gcs_file = gcs.open(filename)
#     contents = gcs_file.read()
#     gcs_file.close()
#     self.response.write(contents)