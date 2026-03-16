

import os

def OS_exit_Main():
    os.sys.exit()

def OS_environment(ANY_TAG, ANY_VALUE):
    os.environ[ANY_TAG] = ANY_VALUE

def OS_initialize_directory(directory_path):
    os.makedirs(directory_path)

def OS_return_boolean_filesystem(filesystem_path):
    return os.path.exists(filesystem_path)

def OS_return_boolean_file(file_path):
    return os.path.isfile(file_path) 

def OS_return_boolean_directory(directory_path):
    return os.path.isdir(directory_path)

def OS_return_list_of_directory_files(directory_path):
    return os.listdir(directory_path)

def OS_delete_file(file_path):
    os.remove(file_path)

def OS_return_path_of_home_user():
    return os.path.expanduser("~")

def OS_return_absolute_path(relative_path_of_filesystem):
    return os.path.abspath(relative_path_of_filesystem)

def OS_return_resolution_path_of_symbolic_link(relative_path_of_symbolic_link):
    return os.path.realpath(relative_path_of_symbolic_link)

def OS_return_function_parameters():
    return os.sys.argv

def OS_return_last_part_of_path(filesystem_path):
    return os.path.basename(filesystem_path)


