student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# total_exam_scores = sum(student_scores)
# print(total_exam_scores)

# total_scores = 0

# for score in student_scores:
#     total_scores += score
# print(total_scores)
largest_number = student_scores[0]
for score in student_scores:
    if score > largest_number:
        largest_number = score
print(largest_number)