import shutil
import os
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.constants import LEFT, TOP

# path to source directory
src_dir = r'C:\Data\VPE Tune\testData'
  
# path to destination directory root
# (today's date will be added)
dest_dir = r'C:\Backup'

# get today's date to create desination directory
from datetime import datetime
timestamp = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

# dest_dir = dest_dir + '\\' + timestamp
dest_dir = os.path.join(dest_dir,timestamp)

# set up display
window = tk.Tk()
window.geometry("600x200")
window.title("Backup Files")
fontsize = ('Arial 10')

label01 = tk.Label(window, text ='Source Directory: '+src_dir, font = fontsize) 
label01.pack(pady=0, side=TOP, anchor="w")
label02 = tk.Label(window, text ='Destination Directory: '+dest_dir, font = fontsize) 
label02.pack(pady=0, side=TOP, anchor="w")
  
# getting all the files in the source directory
files = os.listdir(src_dir)

# check that destination directory doesn't already exist
if not os.path.exists(dest_dir):
    # recursive copy
    shutil.copytree(src_dir, dest_dir)
else:
    mb.showerror("Backup Error", "Backup folder already exists!")

# count copied files to verify success
noOfFiles = 0
noOfDir = 0

for base, dirs, files in os.walk(dest_dir):
    print('Looking in : ',base)
    for directories in dirs:
        noOfDir += 1
    for Files in files:
        noOfFiles += 1

statusstring = "Backup Success! " + str(noOfFiles) + " files copied in " + str(noOfDir) + " folders."
label_status = tk.Label(window, text =statusstring, font = fontsize) 
label_status.pack(pady=0, side=TOP, anchor="w")

window.mainloop()