"""task 3"""
import requests

file_path = r"C:\pictures\pic.jpg"

def foo(directory, file_name):

    f = open(directory, 'rb')
    upload_files = {'file': (file_name, f, 'image/jpeg')}
    response = requests.post('https://postman-echo.com/post', files=upload_files)

    return len(response.text.encode('utf8'))


print(foo(file_path, "pic.jpg"))
