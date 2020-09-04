# 1: 10 students:
# this program is to assign the grades to the students having some marks in english
#and also help teachers to calculate the grades of students
def assign_grade(marks):
    
    grade = []
    for i in range(10):
        if marks[i]>= 90:
            grade.append('A')
        elif marks[i]>= 80:
            grade.append('B')
        elif marks[i]>65:
            grade.append('C')
        elif marks[i]>=40:
            grade.append('D')
        elif marks[i]<40:
            grade.append('E')
    
    print("Grades of Students with respecto to their marks: ",grade)
    return grade

def main():
    print("Enter the marks of students: \n")
    marks = [0]*10
    
    for i in range(10):
        marks[i] = int(input())
        
    print("Entered marks of student: ",marks)
    assign_grade(marks)
main()
