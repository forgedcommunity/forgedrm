import uuid
import pyminizip
import os

def drmID():
    return uuid.uuid4()

def packageWithID(folder_path, output_zip):
    id = drmID()
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    
    pyminizip.compress_multiple(files, [], output_zip, str(id), 5)
    return id
