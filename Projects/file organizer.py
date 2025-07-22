import os
import shutil


files = os.listdir("/home/gautam/Downloads")
videos = []
images = []
zip_files = []
wallpapers = []
installers = []
documents = []
#print(files)

def sorting():

    for file_ in files:
        if 'wallpaper' in file_ or 'Wallpaper' in file_:
            wallpapers.append(file_)
        elif '.png' in file_ or '.jpg' in file_ or '.jpeg' in file_:
            images.append(file_)
        elif '.mp4' in file_ or '.mov' in file_ :
            videos.append(file_)
        elif '.zip' in file_ or '.rar' in file_ :
            zip_files.append(file_)
        elif '.deb' in file_ or '.AppImage' in file_:
            installers.append(file_)
        elif '.pdf' in file_ or '.csv' in file_ or '.excel' in file_:
            documents.append(file_)
        else: 
            continue

def moving():
    for video in videos:
        shutil.move('/home/gautam/Downloads/'+video, '/home/gautam/Downloads/Videos')

    for image in images:
        shutil.move('/home/gautam/Downloads/'+image, '/home/gautam/Downloads/Images')
    
    for document in documents:
        shutil.move('/home/gautam/Downloads/'+document, '/home/gautam/Downloads/documents')

    for zip_file in zip_files:
        shutil.move('/home/gautam/Downloads/'+zip_file, '/home/gautam/Downloads/Zip-files')

    for installer in installers:
        shutil.move('/home/gautam/Downloads/'+installer, '/home/gautam/Downloads/Installers')
    
    for wallpaper in wallpapers:
        shutil.move('/home/gautam/Downloads/'+wallpaper, '/home/gautam/Downloads/Wallpapers')


sorting()
moving()
