student_scores = input().split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_numb = 0
for score in student_scores:
    if score > max_numb:
        max_numb = score
print(f"The highest score in the class {max_numb}")
