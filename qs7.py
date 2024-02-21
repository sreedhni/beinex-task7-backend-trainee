# Write a Python program to assess if a file is closed or not
file_path = input("Enter the path to the text file: ")

file = open(file_path,'r')

if file.closed:
    print("File is closed.")
else:
    print("File is not closed.")
    
file.close()

