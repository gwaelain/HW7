with open('recips.txt', 'w+', encoding='utf8') as f:
    #file.write(" ")
    #file.seek(0)
    #print(file.read())
    #lines= f.readLines()
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline() == '')
    print(f.readline() is None)
