from time import sleep
import os

# Console colors
White = '\033[0m'
Red = '\033[31m' 
Green = '\033[32m' 
Orange = '\033[33m'
Blue = '\033[34m'  
Purple = '\033[35m'
Cyan = '\033[36m' 
Gray = '\033[37m'  


Delay = int(input(Orange + "Enter Delay between executions (in seconds) : " + White))

print(Blue + "Files in this directory are mentioned below: " + White)
# code to list files
files = []
for file in os.listdir():
    if file == "File_Autorun_Delay.py":
        continue
    if os.path.isfile(file):
        files.append(file)
# print files
i = 1
for file in files:
    print(str(i)+".  " + file)
    i+=1

print(Blue + "Press Ctrl + C to EXIT " + White)
extension = input(Orange + "Enter extension (type \"all\" to run all files) : " + White).strip()
#fixing if "." is not present
if extension[0] != ".":
    extension = "." + extension

# count files to be executed
num_files = 0
for file in files:
    if extension == file[-(len(extension)):len(file)] or extension == ".all":
        num_files += 1

if num_files == 0:
    print(Red + f"error : NO FILES WITH {extension} ARE PRESENT" + White)
    sleep(10)
    exit()


# executing files
print(Green + f"EXECUTING {num_files} FILES..." + White)

x = 0
for file in files:
    if extension == file[-(len(extension)):len(file)] or extension == ".all":
        os.startfile(file)
        x += 1
        print(Green + "Launched : " + str(int(x/num_files*100)) + "% : " + White + file)
        if x == num_files:
            print(Green + f"EXECUTED {num_files} FILES SUCCESSFULLY" + White)
            sleep(10)
            exit()
        sleep(Delay)


