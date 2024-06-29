# score = 59
# A_score = 90
# B_score = 80
# C_score = 70
# D_score = 60
# if score >= A_score:
#     print('Your grade is A.')
# else:
#     if score >= B_score:
#         print('Your grade is B.')
#     else:
#         if score >= C_score:
#             print('Your grade is C.')
#         else:
#             if score >= D_score:
#                 print('Your grade is D.')
#             else:
#                 print('Your grade is F.')


# Write a for loop that displays the following set of numbers:

# 0, 10, 20, 30, 40, 50 . . . 1000


my_list = []
for n in range(0, 1001, 10):
    my_list.append(n)
print(my_list)

# my_list = []
for n in range(0, 1001, 10):
    if n == 1000:
        print(n)
    else:
        print(n, end=", ")

# Write an if-else statement that displays 'Speed is normal' if the speed variable is 
# within the range of 24 to 56. If the speed variable’s value is outside this range, display 'Speed is abnormal'.

# speed = int(input("How fast were you going? "))
# if speed > 24 and speed < 56:
#     print("Speed is normal")
# else:
#     print("Speed is abnormal")

# my_string = "Hello World"
# my_string[0] = "X"
# print(my_string)