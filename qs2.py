# Write a Python program to read first n lines of a file
file_path = "C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt"
file_read = open(file_path, 'r')
number_of_lines = int(input("Enter the number of lines you want to read: "))
for i in range(number_of_lines):
    line = file_read.readline().rstrip()  
    if line:
        print(line)
    else:
        print("No content in the file")
        break
file_read.close()

