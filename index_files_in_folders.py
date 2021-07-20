import os
import sys
import datetime

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

def work(path):
    start= datetime.datetime.now()
    list = os.listdir(path) # lists all folders and files contained in the specified path
    print(list)

 # constructs a stack where if its a folder add subfolders to the stack 
 # else index the file
 # limitation subfolders of subfolders may cause problems currently
    for i in list:
        if os.path.isdir(i) == False:
            print(os.system('opensemanticsearch-index-file -v -f '+str(path+"/"+i)))
            print("--------------------------------------------------------------------")
        else:
            print(os.listdir(str(path+"/"+i)))
            work(path + "/" + i)

    print(str(start) + " -- " + str(datetime.datetime.now()) + " --- Time elapsed: " + str(datetime.datetime.now()-start))

usage_msg = "Usage: " + sys.argv[0] + " \n -h Print this message" + " \n -c go with current folder" + " \n -p PATH goes through the provided path" + " \n -f reads specified file and works with the data passed line break means new location" + " \n Args folders path to index"

if "-h" in opts:
    print(usage_msg)

elif "-c" in opts:
    print("Starting with current directory")
    work(os.getcwd())

elif "-p" in opts:
    print("looking at provided path" + args)
    work(args[0])

elif "-f" in opts:
    with open(args[0],"r", encoding="UTF-8") as input:
        for line in input.readlines():
            work(line)
elif len(args) < 1:
    print("Please pass a folder location to start with.")
else:
    raise SystemExit(f"Usage: {sys.argv[0]} {usage_msg}")