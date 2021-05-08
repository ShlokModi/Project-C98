def swapFileData():
    file1 = input("Write the First File Name")
    file2 = input("Write the Second File Name")
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)
    print("First File : " + data_a)
    print("Second File : " + data_b)
swapFileData()
