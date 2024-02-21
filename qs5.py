# Write a Python program to copy the contents of a file to another file

first_file_path = input("Enter the path to the source file: ") #C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt
copy_file_path = input("Enter the path to the destination file: ") #C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\\copy_file.txt
first_file = open(first_file_path, 'r')

copy_of_the_file = open(copy_file_path, 'w')

for line in first_file:
    copy_of_the_file.write(line)

first_file.close()
copy_of_the_file.close()

print("Contents copied successfully from 1st file  to second file go copy_file.txt and confirm it")
