grade1 = int(input("Enter your score for the first exam: \033[1m"))
grade2 = int(input("Enter your score for the second exam: \033[1m"))
grade3 = int(input("Enter your score for the third exam: \033[1m"))
average = (grade1 + grade2 + grade3) / 3
print("Your average score is:", average)
if average > 95:
    print("Congratulations!" "\n" "That is a great average!")