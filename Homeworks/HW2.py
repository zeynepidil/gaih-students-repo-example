#Explain your work

#Day1Homework
studentsname_list=["Jenny Black","Edward Column","John Newman","Jessica Marley","Bernard Steven"]
print(studentsname_list)
name=input("Please enter student name")
print("Name:{}".format(name))
y1=input('midtermgrade:')
y2=input('finalgrade:')
y3=input('homeworkgrade:')
average=((float(y1)+float(y2)+float(y3))/3)
print("Average:{}".format(average))



gradeslist=[[75,90,85],[60,70,87],[65,76,89],[80,50,55],[85,95,100]]
grades_dictionary={"Jenny Black":83.33,"Edward Column":72.33,"John Newman":76.67,"Jessica Marley":61.64,"Bernard Steven":93.33}
print(grades_dictionary)
print(grades_dictionary["Bernard Steven"])

if(average>77.46):
    print("Congratulations,you're above average")
else:
   print("You're under the average")
