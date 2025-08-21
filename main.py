"""Reading and Writing Files in Python"""
with open(
    'C:\\Users\\jobmu\\Desktop\\cRaZy\\Python_Assignments\\file_handling_and_exception_handling\\input.txt', 'r',
    encoding='utf-8'
) as read_file:

    content = read_file.read()

print('File read successfully')
print("Input file content:\n", content)


