import argparse
import os
import shutil

from constantes import data_dir, dest_dir
from lectura_data import metadata

parser = argparse.ArgumentParser()
parser.add_argument(
    '--binary', 
    dest='binary', 
    action='store_const',
    const=True, 
    default=False,
    help='Whether to sort images for binary classification.'
)

label = metadata["label"].unique()

for i in label:
    os.mkdir(dest_dir + "/" + str(i))
    imagenes = metadata.loc[metadata['label'] == i, 'image_id']
    for id in imagenes:
        shutil.copyfile((data_dir + "/" + id + ".jpg"), 
                        (dest_dir + "/" + str(i) + "/" + id + ".jpg"))
