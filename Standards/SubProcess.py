

import subprocess

def SubProcess_initialize(functions):
    subprocess.run(functions, shell=True)

def SubProcess_parallel_initialize(functions):
    subprocess.Popen(functions, shell=True)

def SubProcess_return_initialize(functions):
    output = subprocess.run(
        functions,
        shell=True,
        capture_output=True, 
        text=True
    )
    return output.stdout.strip()


