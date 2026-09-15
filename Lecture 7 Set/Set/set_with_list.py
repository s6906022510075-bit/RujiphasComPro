attendance_week = [
["Alice", "Bob", "Charlie", "David"], # Day 1
["Alice", "Charlie", "David"], # Day 2
["Alice", "Bob", "David"],#day 3
["Alice", "David", "Eve"], # Day 4
["Bob", "Charlie", "David"] # day 5
]

#convert each day's attendance list to a set
attendance_set = [set(day) for day in attendance_week]
print("Attendance for each day as sets:", attendance_set)


# 1. determine students who were present on all days
present_all_days = set.intersection(*attendance_set)
print("Students present all days:", present_all_days)

# 2. determine students who were absent on at least one day
all_students = set.union(*attendance_set)
absent_at_least_one_day = all_students - present_all_days
print("Students absent on at least one day:", absent_at_least_one_day)#output: {'Bob', 'Charlie', 'Eve'}

# 3. Create a list of students who were present on the first day but absent on the last day
first_day_set = attendance_set[0]
last_day_set = attendance_set[-1]
first_day_present_last_day_absent = first_day_set - last_day_set
print("Students present on the first day but absent on the last day:", first_day_present_last_day_absent) #output: {'Bob', 'Charlie'}

# 4. Calculate the total number of unique students who attended at least one day
unique_students = len(all_students)
print("Total number of unique students who attended at least one day:", unique_students) #output: 5