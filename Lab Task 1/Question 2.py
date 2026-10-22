class Student:
    def __init__(self, score, document_completeness, attendance_percentage, assignment_status):
        self.score = score
        self.document_completeness = document_completeness
        self.attendance_percentage = attendance_percentage
        self.assignment_status = assignment_status

    def result(self):
        if (self.score >= 70 and self.document_completeness == "Yes" and self.attendance_percentage >= 75 and selfassignment_status == "Yes"):
            return "Pass"
        else:
            return "Fail"

    def final_result(self, expected):
        result = self.result()
        
#Printing Complete Result
        print(f"Input: Score: {self.score}, Document: {self.document_completeness},
              Attendance: {self.attendance_percentage}, Assignment: {self.assignment_status}")

        print("Expected Result:", expected)
        print("Actual Result:", result)
        
#Students Pass Conditions 
        if result == "Pass":
            print("Reason: All conditions are satisfied.")
        elif self.score < 70:
            print("Reason: Score is below 70.")
        elif self.document_completeness != "Yes":
            print("Reason: Document is not complete.")
        elif self.attendance_percentage < 75:
            print("Reason: Attendance Percentage is below 75%.")
        elif self.assignment_status != "Yes":
            print("Reason: Assignment is not submitted.")


# Case 1
student1 = Student(80, "Yes", 80, "Yes")
student1.final_result("Pass")

# Case 2
student2 = Student(80, "Yes", 60, "Yes")
student2.final_result("Fail")

# Case 3
student3 = Student(80, "Yes", 80, "No")
student3.final_result("Fail")

# Case 4
student4 = Student(70, "Yes", 75, "Yes")
student4.final_result("Pass")
