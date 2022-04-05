import shutil
import subprocess
import os

BASE_PATH = '/usr/bin/'
JAVA_PATH_COMPILE = BASE_PATH + 'javac'
JAVA_PATH_EXEC = BASE_PATH + 'java'
PYTHON_EXEC = BASE_PATH + 'python3'
GCC_EXEC = BASE_PATH + 'gcc'
NPM_EXEC = BASE_PATH + 'npm'

def save_file(file,filepath,file_name):
    new_file = open(filepath+"/"+file_name, "wb")
    shutil.copyfileobj(file, new_file)

def start_compile(exec_type, file, file_name, box_id):
    # create box
    if os.path.isdir('/var/local/lib/'+str(box_id)):
        pass
    else:
        os.makedirs('/var/local/lib/'+str(box_id))
    save_file(file, '/var/local/lib/'+str(box_id),file_name)
    exec_command = ''
    if exec_type == 'python':
        os.popen("sh ./init_isolate_py.sh "+str(box_id)+" "+exec_command+" "+file_name)
    elif exec_type == 'java':
        os.popen("sh ./init_isolate_java.sh "+str(box_id)+" "+exec_command+" "+file_name)
    elif exec_type == 'gcc':
        os.popen("sh ./init_isolate_gcc.sh "+str(box_id)+" "+exec_command+" "+file_name)
    else:
        return None
    box = "/var/local/lib/isolate/"+str(box_id) + "/box"
    return read_outout(box,exec_type)

def read_outout(box_path,exec_type):
    if exec_type == 'python':
        pass
    elif exec_type == 'java':
        pass
    elif exec_type == 'gcc':
        pass
    return "success"
# with open('/app/constants.py','rb') as file:
#     print(start_compile('python',file, 'constants.py','100'))