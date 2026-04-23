import uuid
import pyzipper
import os

def drmID():
    return uuid.uuid4()

def packageWithID(folder_path, output_zip):
    id = drmID()
    with pyzipper.AESZipFile(output_zip, 'w', encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(str(id).encode())
        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                arcname = os.path.relpath(filepath, folder_path)  # preserves structure
                zf.write(filepath, arcname)
    return id
