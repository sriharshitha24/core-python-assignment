def calculate_averages(students):
    averages = {}
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        averages[name] = round(average, 2)
    return averages

def find_top_performer(students):
    top_student = None
    highest_average = 0
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        if avg > highest_average:
            highest_average = avg
            top_student = name
    return top_student

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

average_marks = calculate_averages(students)
top_performer = find_top_performer(students)

print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
