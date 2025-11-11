try:
    num=int("abc")
    print("This will not be printed")
except ValueError as e:
    print(e)
    
    
file_path="non_existing_file.txt"
try:
    print(f"Attempting to open {file_path}..")
    f=open(file_path,'r')
    content=f.read()
except FileNotFoundError as e:
    print(e)
else:
    print("File Read successfully")
    print(content)
finally:
    Print("Finished Execution")