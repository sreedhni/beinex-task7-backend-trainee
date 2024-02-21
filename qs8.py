# Write a Python program to write a list to a file
user_input = input("Enter elements of the list separated by spaces: ")
my_list = user_input.split()
file_path = "output_list.txt"
read_file=open(file_path,'w')
read_file.write(str(my_list))

print("List has been written to", file_path)

read_file.close()
