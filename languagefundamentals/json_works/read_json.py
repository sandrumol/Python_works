from json import load
f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\json_works\\students.json","r")
data=load(f)
# print(data)
# print(type(data))


# print all emp names

all_names=[emp.get("name") for emp in data]
# print(all_names)


# print all departments

all_depts={emp.get("department") for emp in data} # duplicate not allowed in set
# print(all_depts)


# highest salary employee

max_salary=max(data,key=lambda d:d.get("salary"))
print(max_salary)
print(max_salary.get("name"))

