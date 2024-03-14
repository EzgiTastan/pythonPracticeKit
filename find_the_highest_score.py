# Let's write a program that calculates the highest score from a List of scores.


student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Initialize a variable to store the highest score
highest_score = student_scores[0]

# Iterate through the scores to find the highest one
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
