#! /usr/bin/env python3

import os
from os.path import basename, dirname, exists
from urllib.request import urlretrieve
from zipfile import ZipFile
from pathlib import Path
from shutil import rmtree


def download_zip(from_url=None, to_dir=None, leave_zip=False):
    Path(dirname(to_dir)).mkdir(parents=True, exist_ok=True)
    zip_path = to_dir + '.zip'
    urlretrieve(from_url, zip_path)
    zip_file = ZipFile(zip_path, 'r')
    zip_file.extractall(to_dir)
    zip_file.close()
    if not leave_zip:
        os.remove(zip_path)


LISA_URL = 'http://cvrr.ucsd.edu/LISA/Datasets/signDatabasePublicFramesOnly.zip'
BTSC_TRAINING_URL = 'https://btsd.ethz.ch/shareddata/BelgiumTSC/BelgiumTSC_Training.zip'
BTSC_TESTING_URL = 'https://btsd.ethz.ch/shareddata/BelgiumTSC/BelgiumTSC_Testing.zip'

print('Cleaning ./data ... ',
      end='', flush=True)
if exists('./data'):
    rmtree('./data')
Path('./data').mkdir()
print('Done.')

# print('Downloading LISA Dataset to ./data/lisa ...',
#       end='', flush=True)
# download_zip(
#     from_url=LISA_URL,
#     to_dir='./data/lisa',
# )
# print('Done.')

print('Downloading BelgiumTSC Training Dataset to ./data/btsc/training ... ',
      end='', flush=True)
download_zip(
    from_url=BTSC_TRAINING_URL,
    to_dir='./data/btsc/training',
)
print('Done.')

print('Downloading BelgiumTSC Testing Dataset to ./data/btsc/testing ... ',
      end='', flush=True)
download_zip(
    from_url=BTSC_TESTING_URL,
    to_dir='./data/btsc/testing',
)
print('Done.')
