#mini project for log file analysis using iterators and generators

import itertools
from contextlib import contextmanager

def create_large_log_file(filename,line=1000000):
    with open(filename,"w") as f:
        for i in range(line):
            level="INFO" if i%2==0 else "ERROR"
            f.write(f"{level}: This is log message number {i}\n")
    print(f"Created log file '{filename}' with {line} lines.")
    

@contextmanager
def file_reader(filename):
    print(f"Opening file '{filename}' for reading.")
    try:
        f_obj = open(filename, "r")
        yield f_obj
    finally:
        print(f"Closing file '{filename}'.")
        f_obj.close()
        
        
def find_errors_in_log(log_file_iterator):
    for line in log_file_iterator:
        if "ERROR" in line:
            yield line.strip()
            
            
log_filename="app.log"

create_large_log_file(log_filename)


print("\n Starting log analysis...\n")

error_lines_gerenartor = find_errors_in_log(log_filename)
first_5_errors = itertools.islice(error_lines_gerenartor, 5)

print("Found ERROR lines:")
for error in first_5_errors:  
    print(error)


