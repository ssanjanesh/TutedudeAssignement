#Read a file and handle errors
Lineno=0
filename = 'Sample.txt'
try:
    file = open(filename, 'r')
    contents = file.readlines()
    #print(contents)
    for i in contents:
        Lineno+=1
        print('Line {}: {}'.format(Lineno, i.strip()))
        #print('Line {}',format(Lineno))
        #print(i)
    file.close()

except FileNotFoundError:
    print('The file {} does not exist'.format(filename))