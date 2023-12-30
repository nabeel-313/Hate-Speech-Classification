import os
from hate.logger import logging
import urllib.request as req




class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_url,filepath,destination):
        
        #I am makig changes in code because dont have gcp account, I will downlaod locally from url
        #command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        #os.system(command)
        
        
        logging.info("downloading started...")
        logging.info(f"URL is :{gcp_bucket_url} filepath is  \n{filepath}")
        filename, headers = req.urlretrieve(gcp_bucket_url, filepath)
        logging.info(f"filename:{filename} created with info \n{headers}")
        
            
            