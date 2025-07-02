#Create a dictionary of Student Marks

dict = {'Vinod': '95', 'Kishore': '65', 'Mike': '75', 'Kiran': '57'}
try:
    student = input('Enter the student\'s name: ').capitalize()
    marks = dict[student]
    print('{}\'s marks: {}'.format(student, marks))

except KeyError:
    print('Student not found')
