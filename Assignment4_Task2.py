#Write and append data to a file

filename = 'Output.txt'
try:
    FileContent = input('Enter the text to write to the file: ')
    file = open(filename, 'w+')
    contents=file.write(FileContent)
    print('Data successfully written to ',format(filename))

    FileAppened = input('Enter the additional text to append: ')
    appends=file.write(FileAppened)
    print('Data successfully appended.')
    file.close()

    ReadContents = open(filename, 'r')
    print('Final content of ', format(filename))
    print(ReadContents.read())
    ReadContents.close()

except FileNotFoundError:
    print('File {} does not exist', format(filename))

