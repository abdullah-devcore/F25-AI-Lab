def result_checking(score, document, attendance, assignment):
    if score >= 70 and document == "Yes" and attendance >= 75 and assignment == "Yes":
        return "Pass"
    else:
        return "Fail"

# Case 1
score = 80
document = "Yes"
attendance = 80
assignment = "Yes"

result = result_checking(score, document, attendance, assignment)

print("Case 1")
print(f"Input: Score : {score}, Document : {document}, Attendance : {attendance}, Assignment : {assignment}")
print("Expected Result: Pass")

if result == "Pass":
    print("Actual Result: Pass")
    print("Reason: All conditions are satisfied.")
else:
    print("Actual Result: Fail")
    if score < 70:
        print("Reason: Score is below 70.")
    elif document != "Yes":
        print("Reason: Document is not complete.")
    elif attendance < 75:
        print("Reason: Attendance is below 75%.")
    elif assignment != "Yes":
        print("Reason: Assignment is not submitted.")


# Case 2
score = 80
document = "Yes"
attendance = 60
assignment = "Yes"

result = result_checking(score, document, attendance, assignment)

print("Case 2")
print(f"Input: Score : {score}, Document : {document}, Attendance : {attendance}, Assignment : {assignment}")
print("Expected Result: Fail")

if result == "Pass":
    print("Actual Result: Pass")
    print("Reason: All conditions are satisfied.")
else:
    print("Actual Result: Fail")
    if score < 70:
        print("Reason: Score is below 70.")
    elif document != "Yes":
        print("Reason: Document is not complete.")
    elif attendance < 75:
        print("Reason: Attendance is below 75%.")
    elif assignment != "Yes":
        print("Reason: Assignment is not submitted.")



# Case 3
score = 80
document = "Yes"
attendance = 80
assignment = "No"

result = result_checking(score, document, attendance, assignment)

print("Case 3")
print(f"Input: Score : {score}, Document : {document}, Attendance : {attendance}, Assignment : {assignment}")
print("Expected Result: Fail")

if result == "Pass":
    print("Actual Result: Pass")
    print("Reason: All conditions are satisfied.")
else:
    print("Actual Result: Fail")
    if score < 70:
        print("Reason: Score is below 70.")
    elif document != "Yes":
        print("Reason: Document is not complete.")
    elif attendance < 75:
        print("Reason: Attendance is below 75%.")
    elif assignment != "Yes":
        print("Reason: Assignment is not submitted.")


# Case 4
score = 70
document = "Yes"
attendance = 75
assignment = "Yes"

result = result_checking(score, document, attendance, assignment)

print("Case 4")
print(f"Input: Score : {score}, Document : {document}, Attendance : {attendance}, Assignment : {assignment}")
print("Expected Result: Pass")

if result == "Pass":
    print("Actual Result: Pass")
    print("Reason: Score and attendance meet the required limits.")
else:
    print("Actual Result: Fail")
    if score < 70:
        print("Reason: Score is below 70.")
    elif document != "Yes":
        print("Reason: Document is not complete.")
    elif attendance < 75:
        print("Reason: Attendance is below 75%.")
    elif assignment != "Yes":
        print("Reason: Assignment is not submitted.")