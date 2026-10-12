def check_result(score, document, attendance, assignment):
    if score >= 70 and document == "Yes" and attendance >= 75 and assignment == "Yes":
        return "Pass"
    else:
        return "Fail"


def print_reason(score, document, attendance, assignment, result):
    if result == "Pass":
        print("Reason: All conditions are satisfied.")
    elif score < 70:
        print("Reason: Score is below 70.")
    elif document != "Yes":
        print("Reason: Document is not complete.")
    elif attendance < 75:
        print("Reason: Attendance is below 75%.")
    else:
        print("Reason: Assignment is not submitted.")


def Final_result(score, document, attendance, assignment, expected):
    result = check_result(score, document, attendance, assignment)

    print(f"Input: Score = {score}, Document = {document}, Attendance = {attendance}, Assignment = {assignment}")
    print(f"Expected Result: {expected}")
    print(f"Actual Result: {result}")

    print_reason(score, document, attendance, assignment, result)


Final_result(80, "Yes", 80, "Yes", "Pass")

Final_result(80, "Yes", 60, "Yes", "Fail")

Final_result(80, "Yes", 80, "No", "Fail")

Final_result(70, "Yes", 75, "Yes", "Pass")
