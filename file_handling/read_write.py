
def only_read(file_path):
    file = open('sample_file.txt','r') # type of file = _io.TextIOWrapper
    for each_line in file:
        print(each_line)

def lets_write(file_path):
    file = open(file_path,'w')
    file.write("This is my first line")
    file.close()

def lets_append(file_path):
    file = open(file_path,'a')
    file.write("My second line")
    file.close()



def lets_use_with(file_path):
    with open(file_path) as file:
        print(file.read())
    #for write
    #file.write("your text")


file_path = "sample_file.txt"

#only_read(file_path)

#lets_write("my_first_file.txt")

#lets_append("my_first_file.txt")

#lets_use_with(file_path)

