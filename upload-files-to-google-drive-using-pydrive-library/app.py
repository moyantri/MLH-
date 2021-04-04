from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})  

file1.SetContentString('Hello World!') 

file1.Upload()
