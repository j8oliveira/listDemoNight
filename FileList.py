my_file = open("requiredCS.txt", 'r')
all_lines = my_file.readlines()
for line in all_lines:
    upper_case_line = line.upper()
#    upper_case_line = upper_case_line.strip()
    course_and_name = upper_case_line.split(' : ')
    print(course_and_name[0])
    print(course_and_name[1])
print("Those are the required COMP courses for the major")