# 1)

# * * *
# * * *
# * * *


# for row in range(1,4):
#     for col in range(1,4):
#         print("*",end="\t")
#     print()#newline


# 2)

# * * *
# * * *
# * * *
# * * *

# for row in range(1,5):
#     for col in range(1,4):
#         print("*",end="\t")
#     print()


# 3)

#
#   #
#   #   #
#   #   #   #

# for row in range(1,5):
#     for col in range(1,row+1):
#         print("#",end="\t")
#     print()


# 4)

# 1
# 2   2
# 3   3   3
# 4   4   4   4
# 5   5   5   5   5

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(row,end="\t")
#     print()


# 5)

# 1 
# 1   2
# 1   2   3
# 1   2   3   4

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="\t")
#     print()


#6)

#   #   #   #
#   #   #
#   #
#

# for row in range(7,1,-1):
#     for col in range(row,1,-1):
#         print("#",end="\t")
#     print()

#OR

# for row in range(1,5):
#     for col in range(row,5):
#         print("#",end="\t")
#     print()


#7)

# O   
# O E
# O E  O
# O E  O   E
# O E  O   E   O

# for row in range(1,6):
#     for col in range(1,row+1):
#         print("O" if col%2!=0 else "E",end="\t")
#         # if col%2!=0:
#         #     print("O",end="\t")
#         # else:
#         #     print("E",end="\t")
#     print()


# 8)

#           *        
#         *   *   
#       *   *   *
#     *   *   *   *
#   *   *   *   *   *
# *   *   *   *   *   *

for row in range(1,7):
    for space in range(row,6):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end=" ")
    print()