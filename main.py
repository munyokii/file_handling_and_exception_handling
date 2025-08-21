"""Reading and Writing Files in Python"""
with open(
    'C:\\Users\\jobmu\\Desktop\\cRaZy\\Python_Assignments\\file_handling_and_exception_handling\\input.txt', 'r',
    encoding='utf-8'
) as read_file:

    content = read_file.read()

print('File read successfully')
print("Input file content:\n", content)

in_upper = content.upper()

with open(
  'C:\\Users\\jobmu\\Desktop\\cRaZy\\Python_Assignments\\file_handling_and_exception_handling\\output.txt', 'w',
  encoding='utf-8'
) as write_file:
    new_content = in_upper
    write_file.write(new_content)

print('File written successfully with uppercase content')
print("File written successfully with uppercase content:\n", new_content)

try:
    file_name = input("Enter the file name to read: ").strip().lower()
    with open(file_name, 'r', encoding='utf-8') as read_file:
        content = read_file.read()
        print('File read successfully')
        print(f"{file_name} file content:\n", content)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except IOError:
    print("Unable to read the file. Please try again!")
