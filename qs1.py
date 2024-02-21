# Write a Python program to read an entire text file.

read_file=open("C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt",'r')
contents_in_hello_txt_file = read_file.read()
if contents_in_hello_txt_file:
    print(contents_in_hello_txt_file)
else:
    print("The text file is empty")

read_file.close()



















