# Write a Python program to append text to a file and display the text
my_file =open("C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt",'a+')
text=input("enter the text you want to append the file: ")
my_file.write(f"\n{text}")

my_file.close()

read_file=open("C:\\Users\\user\\OneDrive\\Desktop\\bienex\\day10\\hello.txt",'r')
contents_file = read_file.readlines()
appended_text = contents_file[-1] if contents_file else ""

print("Appended text from the file: ",appended_text)
