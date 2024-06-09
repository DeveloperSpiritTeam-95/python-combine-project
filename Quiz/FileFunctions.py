# this is only read the data from file
"""
print("This is First state of printing:")
file = open("Quiz\demo.txt",'r')
data = file.read()
print(data)
print(type(data))

file.close()
"""
# this is replace and print the file data
"""
file = open("Quiz\demo.txt",'r')
data = file.read()
print(data.replace("prabhakar","harsha"))
print(data)

file.close()
"""

# file = open("Quiz\Test1.py","r")
# data = file.read()
# print(data)
# file.close()

# this is the function which is executed with main
"""
print("This is second state of printing using main: ")
def read_entire_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("Reading entire file:")
            print(data)
            file.close()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = 'Quiz\demo.txt'
    read_entire_file(filename)
"""

# this is only read the line by line every time
"""
file = open("C:\PythonProjects\core-project\Quiz\demo.txt","r")

line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)

line3 = file.readline()
print(line3)

file.close()
"""

# this is only for write mode the data inside the file
"""
file = open("Quiz\demo.txt","w")
file.write("This is prabhakar learning ReactJs.")

file.close()
"""

# this is only append the statements inside the file

# file = open("Quiz\demo.txt","a")
# file.write("\nI want to learn java later.")
# file.close()

# create a file inside the folder using write mode

# file = open("Quiz\sample.txt","w")
# file.write("This is sample file")
# file.close()

# create a file inside the folder using append mode

# file = open("Quiz\demo1.txt","a")
# file.write("This is append mode")
# file.close()


# override the text in starting mode is r+

# file = open("Quiz\demo1.txt","r+")
# file.write("abc")
# print(file.read())
# file.close()

# file = open("Quiz\demo1.txt","w+")
# file.write("abc")
# print(file.read())
# file.close()


# file = open("Quiz\demo1.txt","x")
# file.write("abc")
# file.close()

# file = open("Quiz\demo1.txt","w+")
# file.write("abc")
# print(file.read())
# file.close()

#  no need to clode file with keyword clode the file for you
with open("Quiz\demo1.txt","w+") as file:
    file.write("This is prabhakar")
    print(file.read())
    

