#!/usr/bin/env python3
import os, time, shutil

"""
dont have fb, sorry 
subcribed by code house
"""

def get_file_name():
    mypath1=input("Enter the file: ")
    mypath = r"{}".format(mypath1)
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    return (onlyfiles, mypath)

def into_folder_year(get_file_name,mypath):
    """
    Given file name with Created date details list
    Make new folder or exist folder using Created date in file details
    """
    count = 0
    for i in get_file_name:
        # needed path in photo_file
        photo_file = f"{mypath}\{i}"
        #get the Created date in file
        time1 = os.path.getmtime(photo_file)
        #get the Year(Created date) in file
        year_file = time.strftime("%Y",time.localtime(time1))
        # get the path in year 
        create_folder_year = f"{mypath}\{year_file}"
        # check the dir exist or not
        if not os.path.isdir(create_folder_year):
            os.mkdir(create_folder_year)
        # make copy into folder
        shutil.copy2(photo_file,f"{create_folder_year}\{i}")
        count += 1
        print(i, " Count: ", count)

        
def into_folder_month(get_file_name,mypath):
    """
    Given file name with Created date details list
    Make new folder or exist folder using Created date in file details
    """
    count = 0
    for i in get_file_name:
        # needed path in photo_file
        photo_file = f"{mypath}\{i}"
        #get the Created date in file
        time1 = os.path.getmtime(photo_file)
        #get the Yeamontheated date) in file
        month_file = time.strftime("%m",time.localtime(time1))
        # get the path in month 
        create_folder_month = f"{mypath}\{month_file}"
        # check the dir exist or not
        if not os.path.isdir(create_folder_month):
            os.mkdir(create_folder_month)
        # make copy into folder
        shutil.copy2(photo_file,f"{create_folder_month}\{i}")
        count += 1
        print(i, " Count: ", count)


def main():
    get_file_name1 , mypath = get_file_name()

    print("""
    Please choose which date:
    1) Month
    2) Year
    """)
    ch = int(input("Choose the number : "))

    if ch == 1:
        into_folder_month(get_file_name1,mypath)
    elif ch ==2:
        into_folder_year(get_file_name1,mypath)
    else:
        print("Error Choose Wrong Number")

if __name__ == "__main__":
    main()
