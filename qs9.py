# Write a Python program that takes a text file as input and returns the number of words of a given text file. 
# Note: Some words can be separated by a comma with no space. 

file_path = input("Enter the path to the text file: ")#C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt

word_count = 0
read_file=open(file_path,'r')
for line in read_file:
    words = line.replace(',', ' ').split()  
    word_count += len(words)
print("Total number of words in the file:", word_count)

read_file.close()
