'''class Student:
    def __init__(self,name):
        self.name=name
        self.quizzes = []
        self.total_score = 0
        self.num_quizzes = 0
        
    def getName(self):
        return self.name
    def addQuiz(self,score):
        if score<0:
            raise ValueError("Quiz score cannot be negative")
        self.quizzes.append(score)
        self.total_score += score
        self.num_quizzes += 1
    def getTotalScore(self):
        return self.total_score
    def getAverageScore(self):
        if self.num_quizzes == 0:
            raise ValueError("No quizzes taken")
        return self.total_score/self.num_quizzes   
     
name=input("Enter Student Name: ")
student = Student(name)

# Adding quizzes
while True:
    try:
        score = float(input("Enter quiz score (or a negative number to stop): "))
        if score < 0:
            break
        student.addQuiz(score)
    except ValueError as e:
        print(e)

# Displaying results
print("\nStudent Information:")
print("Name:", student.getName())
print("Total Score:", student.getTotalScore())
try:
    print("Average Score:", student.getAverageScore())
except ValueError as e:
    print(e)


        
                '''
                
class Grade:
    GRADE_MAPPING = {
        "A+": 4.3, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }

    def __init__(self, grade):
        self.grade = grade

    def getNumericValue(self):
        return Grade.GRADE_MAPPING.get(self.grade, 0.0)


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.total_score = 0.0
        self.num_grades = 0

    def getName(self):
        return self.name

    def addGrade(self, grade_str):
        grade = Grade(grade_str)
        self.grades.append(grade)
        self.total_score += grade.getNumericValue()
        self.num_grades += 1

    def getGPA(self):
        if self.num_grades == 0:
            raise ValueError("No grades available to calculate GPA")
        return self.total_score / self.num_grades


# Example usage
name = input("Enter Student Name: ")
student = Student(name)

# Adding grades
while True:
    grade_str = input("Enter a grade (or 'exit' to stop): ")
    if grade_str.lower() == 'exit':
        break
    try:
        student.addGrade(grade_str)
    except ValueError as e:
        print(e)

# Displaying results
print("\nStudent Information:")
print("Name:", student.getName())
try:
    print("GPA:", student.getGPA())
except ValueError as e:
    print(e)
                