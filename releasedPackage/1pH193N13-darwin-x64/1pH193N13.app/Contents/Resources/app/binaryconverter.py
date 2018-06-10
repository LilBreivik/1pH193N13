import binascii
import os 

from tkinter import filedialog

workingDirectory = os.getcwd()

file_path_to_password = os.path.join(workingDirectory , "assets" , "key" + "." + "txt")

file_pth_to_binary_converted_password = os.path.join(workingDirectory , "assets" , "key" + "." + "bin")

x = ""

with open(file_path_to_password, 'rb') as f:

    for chunk in iter(lambda: f.read(32), b''):
        
        x += str(binascii.hexlify(chunk)).replace("b","").replace("'","")
 
print(x)
 
with open(file_pth_to_binary_converted_password , 'wb') as f:
    f.write(x.encode('utf-8'))

