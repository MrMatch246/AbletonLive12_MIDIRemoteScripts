import os

def main():
    #iterate over all the files in the current directory and subdirectories
    for root, dirs, files in os.walk("./MIDIRemoteScripts"):
        for file in files:
            if file.endswith(".pyc"):
                #print the name of the file
                print(os.path.join(root, file))
                #run the uncompyle6 command
                os.system("python3.9 python-uncompyle6/uncompyle6/bin/uncompile.py " + os.path.join(root, file) + " > " + os.path.join(root, file)[:-1])



if __name__ == '__main__':
    main()


