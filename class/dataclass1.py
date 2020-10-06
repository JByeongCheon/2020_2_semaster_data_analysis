# def is_prime2(num):
#     if num != 1:
#         for x in range(2, num):
#             if num % x == 0:
#                 return False
#     else:
#         return False
#
#     return num
#
# def is_prime():
#     for i in range(1, 1001):
#         if is_prime2(i):
#             print(i,',',end='')
#
#
# def  sum_digits(num_input):
#     num_size = len(str(num_input))
#     ten_sum = 10 ** (num_size - 1)
#     num_input = int(num_input)
#     sum = 0
#
#     while(num_input != 0):
#         sum += num_input // ten_sum
#         num_input = num_input % ten_sum
#         ten_sum = ten_sum / 10
#     print(sum)
# #/////////////////////////2020-09-14//////////////////////////////////////////////
#
# def sum_f(lst, f):
#     sum = 0
#     for v in lst:
#         sum += f(v)
#     return sum
# def sq(x):
#     return x**2





