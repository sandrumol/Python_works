employee={"id":1000,"name":"hari","department":"developer"}

# update department as senior developer
employee["department"]="senior developer"
print(employee)


if "salary" not in employee:
    employee["salary"]=45000
else:
    employee["salary"]+=1000
print(employee)