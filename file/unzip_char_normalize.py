import sys
from unicodedata import normalize
import os

def change_nfc_all_dir(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        os.rename(before_filename, after_filename)

        if os.path.isdir(before_filename):    
            change_nfc_all_dir(before_filename)

# main
if __name__ == "__main__":
    change_nfc_all_dir("/data/image-work/agency-image")
