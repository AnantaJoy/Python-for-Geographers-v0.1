try:
    # context manager
    # file will be closed automatically
    # even if exception occurs
    # __enter__ and __exit__ methods are called automatically
    with open('file.log') as file, open('file.log') as file2:
        read_data = file.read()
except:
    print("Could not open file.log")
else:
    print(read_data)
    