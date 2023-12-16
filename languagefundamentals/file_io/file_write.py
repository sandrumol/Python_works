# copy the path of folder and add file name on it as 'years.txt'

# path="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\years.txt"
# f=open(path,"w")
# f.write("hello") # only accept string values



# write colors from list to colors.txt

# path="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\colors.txt"
# f=open(path,"w")

# colors=["red","green","blue"]
# for c in colors:
#     f.write(c+"\n") # write each colors in line by line



# write all century years from 1800 to 2024 into century_years.txt

# path="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\century_years.txt"
# f=open(path,"w")
# for year in range(1800,2025):
#     if year%100==0:
#         f.write(str(year)+"\n")




# write all years from 1800 to 2024 into years.txt

# path="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\years.txt"
# f=open(path,"w")
# for year in range(1800,2025):
#     f.write(str(year)+"\n")



# read all years from years.txt and print leap years
# write all leap years into leap_years.txt

read_path="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\years.txt"
fr=open(read_path,"r")
write_path="C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\leap_years.txt"
fw=open(write_path,"w")
for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        # print(year)
        fw.write(str(year)+"\n")


