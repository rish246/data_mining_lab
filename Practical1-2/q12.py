class Student:

    def __init__(self, name):
        self.marks = []
        self.name = name


    def __str__(self) -> str:

        if len(self.marks) == 0:
            average_marks = 0
        else:
            average_marks = sum(self.marks) / len(self.marks)
        return f'{self.name}\t:\t{average_marks}\n'

    def add_marks(self, marks : int):
        self.marks.append(marks)

    def get_average_marks(self):
        return sum(self.marks) / len(self.marks)


def assign_marks(subject_marks, students):
    for subj_marks in subject_marks:

        for idx, marks in enumerate(subj_marks):
            students[idx].add_marks(marks)




def main():
    # create 5 students
    s1 = Student('student 1')
    s2 = Student('student 2')
    s3 = Student('student 3')
    s4 = Student('student 4')
    s5 = Student('student 5')
    

    subj_one_marks = [10, 32, 23, 11, 32]
    subj_two_marks = [14, 52, 63, 17, 35]
    subj_three_marks = [6, 72, 43, 31, 42]
    subj_four_marks = [16, 12, 13, 51, 34]
    subj_five_marks = [8, 34, 15, 14, 36]


    students = [s1, s2, s3, s4, s5]
    subject_marks = [subj_one_marks, subj_two_marks, subj_three_marks, subj_four_marks, subj_five_marks]

    assign_marks(subject_marks, students)


    # get max and min average score
    average_scores = [x.get_average_marks() for x in students]

    min_marks_loc = average_scores.index(min(average_scores))
    max_marks_loc =average_scores.index(max(average_scores))
    
    print('Student Name\tAverage Marks')
    for student in students:
        print(student)

    print(f"Max average achieved by student: {students[max_marks_loc]}")
    print(f"Min average achieved by student: {students[min_marks_loc]}")

main()