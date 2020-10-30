#https://www.facebook.com/sukarna.jana.9/posts/861280437944655
#Subscribed by Sukarna Jana

#install module using pip install zipfile36 / pip install zipfile37
from zipfile import ZipFile as zf

#specifying the zip file name or path
# we are using \\ because we are running code in python 3.8.1
file_name="C:\\Users\\VAIO\\Desktop\\Raspbian_TempGUI-master.zip"

#opening the zip file in read mode
with zf(file_name,'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
    # extracting all the files
    print('Extracting files, please wait processing....')
    zip.extractall()
    print('Done!')
