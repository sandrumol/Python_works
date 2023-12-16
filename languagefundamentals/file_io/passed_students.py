# print passed students from students.txt and failed.txt
 
path_students="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\students.txt"
path_failed="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\failed.txt"
f_students=open(path_students,"r")
f_failed=open(path_failed,"r")

# all_students_set=set()
# failed_students_set=set()
# for st in f_students:
#     student=st.rstrip("\n")
#     all_students_set.add(student)

# for st in f_failed:
#     failed=st.rstrip("\n")
#     failed_students_set.add(failed)
# passed_students=all_students_set.difference(failed_students_set)
# print(passed_students)

# OR

# set comprehension
all_students_set={st.rstrip("\n") for st in f_students}
failed_students_set={st.rstrip("\n") for st in f_failed}
passed_students=all_students_set-failed_students_set
print(passed_students)

