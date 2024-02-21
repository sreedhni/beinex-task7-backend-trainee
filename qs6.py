# Write a Python program to read a random line from a file. 
random_line_number =int(input("enter the line numbr: "))

file_read = open("C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt", 'r')

current_line = 1

for line in file_read:
    if(current_line==random_line_number):
        print(line)
        break
    current_line = current_line +1 

file_read.close()