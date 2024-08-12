# filename: read_file.py

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

read_file('adaVoiceTest.py')