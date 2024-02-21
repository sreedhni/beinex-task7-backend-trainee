# Write a Python program to read a file line by line store it into a variable.
file_path = input("Enter the path to the file: ")#C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt

file=open(file_path,'r')
file_content = file.readlines()
if file_content:
    print("File contents stored in a variable:")
    print("contents in the file= ",file_content)
else:
    print("no contents in the file")
