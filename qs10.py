# Write a Python program to create a file where all letters of English alphabet are listed by specified 
# number of letters on each line. 

write_file=open("alphabet.txt", "w")
letters_per_line =int(input("enter the no of letter per line"))
for i in range(0, 26, letters_per_line):
    line = ' '.join(chr(ord('a') + index_of_the_letter) for index_of_the_letter in range(i, min(i + letters_per_line, 26)))
    write_file.write(line + '\n')
print("alphabets are added into the file as per the rule")
write_file.close()
