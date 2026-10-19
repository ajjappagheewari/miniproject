
from pathlib import Path
import os

def createfile():
    try:
        name=input("enter your file name  ")
        file_path=Path(name)
        if not file_path.exists():
            with open(file_path,"w")as fc:
                        data=input("write what you want to write")
                        fc.write(data)
        else:
             print("ERROR FILE already exist")
    except Exception as err:
         print(f"an error occure {err}")

def readingfile():
    try:
         name=input("enter your file name")
         file_path=Path(name)
         if file_path.exists():
              with open(file_path,"r")as fr:
                   content=fr.read()
                   print(content)
         else:
              print(" file not exist")
    except Exception as err:
         print(f"ERROR {err}")
                           
def updatingfile():
     try:
          name=input("enter your file name ")
          file_path=Path(name)
          if file_path.exists():
               print("operatons")
               print("1 for renaming the file")
               print("2 appending the file")
               print("3 rewriting the file")
               
               choice=int(input("enter your operation number"))
               if choice==1:
                    new_name=input("enter your new file name")
                    new_path=Path(new_name)
                    if not new_path.exists():
                         file_path.rename(new_path)
                         print("file name is renamed")
               elif choice==2:
                    with open(file_path,"a")as fx:
                         data=input("enter what you want to append")
                         fx.write(data)
               elif choice==3:
                    with open(file_path,"w")as fz:
                         data=input("rewrite here")
                         fz.write(data)
          else:
               print(" file not exist to update")
     except Exception as err:
          print(f"ERROR OF {err}")
       
def deletingfile():
     try:
          name=input("enter your file name")
          file_path=Path(name)
          if file_path.exists:
               file_path.unlink()
               print("file deleted successfully")
          else:
               print("file dont exist to delete")
     except Exception as err:
          print(f"ERROR of {err}")

          
   
print("1 for creating  a file")
print("2 for reading  a file")
print("3 for updating  a file")
print("4 for deleting  a file")

num=int(input("enter a number "))

if num==1:
    createfile()
if num==2:
    readingfile()
if num==3:
    updatingfile()
if num==4:
    deletingfile()

