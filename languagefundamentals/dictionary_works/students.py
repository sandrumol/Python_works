students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btech"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btech"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
   
    
]

# total number of students

# print(f"Total number of students={len(students)}")


# print all students name

# for std in students:
#     print(std.get("name"))

# OR

all_students_name=[stud.get("name") for stud in students ]
# print(all_students_name)


# print students name whose experience > 1

# for stud in students:
#     if stud.get("exp")>1:
#         print(stud.get("name"))

students_exp_greater_than_one=[stud.get("name") for stud in students if stud.get("exp")>1]
# print(students_exp_greater_than_one)


# print students name whose skills contain both java,python

# for stud in students:
#     if "java" in stud.get("skills") and "python" in stud.get("skills"):
#         print(stud.get("name"))


# print mca students name

# for stud in students:
#     if stud.get("qualification")=="mca":
#         print(stud.get("name"))

mca_students=[stud.get("name") for stud in students if stud.get("qualification")=="mca"]
# print(mca_students)


# print most experienced student

most_experienced=max(students,key=lambda d:d.get("exp")) 
# print(most_experienced) #dict
highest_exp=most_experienced.get("exp")
exp_studs=[stud.get("name") for stud in students if stud.get("exp")==highest_exp]
# print(exp_studs)


# print students names having skills >2

# for stud in students:
#     if len(stud.get("skills")) > 2:
#         print(stud.get("name"))

skills_gt_two=[stud.get("name") for stud in students if len(stud.get("skills"))>2]
# print(skills_gt_two)


# print students name starts with 'j'

# for stud in students:
#     if stud.get("name").startswith("j"):
#         print(stud.get("name"))

name_startswith_j=[stud.get("name") for stud in students if stud.get("name").startswith("j")]
# print(name_startswith_j)


# print skill taken by most students

skill_count={}
for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)
# count_lst=[]
# for s in skill_count:
#     count_lst.append(skill_count.get(s))
# max_count=max(count_lst)
# max_skill=[sk for sk in skill_count if skill_count.get(sk)==max_count]
# print(f"The skill that most of the students have is {max_skill}")
max_skill=max(skill_count,key=lambda k:skill_count.get(k))
print(f"The skill that most of the students have is {max_skill}")

