import os
#from unpyc37.unpyc3 import decompile
def main():
    #iterate over all the files in the current directory and subdirectories
    print("decompiling files ...")
    multi_decompile_files("./MIDIRemoteScripts")
    return
    for root, dirs, files in os.walk("./MIDIRemoteScripts"):
        for file in files:
            if file.endswith(".pyc"):
                #print the name of the file
                print(os.path.join(root, file))
                #run the uncompyle6 command
                #os.system("python3.9 python-uncompyle6/uncompyle6/bin/uncompile.py " + os.path.join(root, file) + " > " + os.path.join(root, file)[:-1])
                #os.system("decompyle3 " + os.path.join(root, file) + " > " + os.path.join(root, file)[:-1])
                #decompile(os.path.join(root, file), os.path.join(root, file)[:-1])

                decompiled = multi_decompile(os.path.join(root, file))
                with open(os.path.join(root, file)[:-1], "w") as f:
                    f.write(decompiled)


# use multiprocessing to decompile the files in parallel
def multi_decompile_files(folder_path):
    files_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pyc"):
                files_paths.append(os.path.join(root, file))

    # use multiprocessing to decompile the files in parallel
    print("decompiling files in parallel ... " + str(len(files_paths)) + " files")
    from multiprocessing import Pool
    with Pool(10) as p:
        p.map(multi_decompile, files_paths)




def multi_decompile(filepath):
    parse_error = "Parse error at or near"
    stack_start = "--"
    stack_end = "from __future__ import"

    output_decompile3 = os.popen("decompyle3 " + filepath).read()
    output_decompile6 = os.popen("uncompyle6 " + filepath).read()

    decompilations = [output_decompile3, output_decompile6]
    clean_decompilations = []
    for decompilation in list(decompilations):
        if parse_error not in decompilation:
            clean_decompilations.append(decompilation)


    final_decompilation = None

    if len(clean_decompilations) == 0:
        best_decompilation = None
        offset = 0
        for decompilation in list(decompilations):
            error_offset_str = decompilation.split(parse_error)[1].split("\n")[0].split("offset ")[1]
            error_offset = int(error_offset_str)
            print("error_offset: ", error_offset)
            if error_offset > offset:
                offset = error_offset
                best_decompilation = decompilation
        start = best_decompilation.find(stack_start)
        end = best_decompilation.rfind(stack_end)
        print("start: ", start)
        print("end: ", end)
        best_decompilation = best_decompilation[:start] + best_decompilation[end:]
        final_decompilation = best_decompilation
    else:
        final_decompilation = clean_decompilations[0]
    with open(filepath[:-1], "w") as f:
        f.write(final_decompilation)
    print("decompiled: ", filepath)


#function that executes command in the shell and returns the output
def execute_command(command):
    #run the command
    result = os.popen(command).read()
    #return the result
    return result


if __name__ == '__main__':
    main()


