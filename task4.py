class Student:
    def __init__(self, name, age, group_number, average_score):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.average_score = average_score

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_scholarship(self):
        if self.average_score == 5.0:
            return 6000
        elif 0 < self.average_score < 5.0:
            return 4000
        else:
            return 0

    def print_scholarship(self):
        scholarship = self.get_scholarship()
        print(f"Scholarship: {scholarship} Rubles")

    def compare_scholarship(self, other):
        return self.get_scholarship() > other.get_scholarship()


class PostGraduate(Student):
    def __init__(self, name, age, group_number, average_score, research_project):
        # Call parent class constructor
        super().__init__(name, age, group_number, average_score)
        self.research_project = research_project

    def print_info(self):
        super().print_info()
        print(f"Research Project: {self.research_project}")

    def get_scholarship(self):
        if self.average_score == 5.0:
            return 8000
        elif 0 <= self.average_score < 5.0:
            return 6000
        else:
            return 0


def main():
    # Create a student object
    test_student = Student("Tang Mengkai", 20, "5132704/30701", 4.8)
    # Create a postgraduate object
    test_postgraduate = PostGraduate("Makcum", 25, "12345", 5.0, "AI Algorithm Research")

    print("=== Student Info ===")
    test_student.print_info()
    test_student.print_scholarship()

    print("=== Postgraduate Info ===")
    test_postgraduate.print_info()
    test_postgraduate.print_scholarship()

    print("=== Scholarship Comparison ===")
    if test_student.compare_scholarship(test_postgraduate):
        print(f"{test_student.name}'s scholarship is greater than {test_postgraduate.name}'s")
    else:
        print(f"{test_student.name}'s scholarship is less than {test_postgraduate.name}'s")


if __name__ == "__main__":
    main()
