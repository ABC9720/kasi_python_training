
# a = [10,12,14,16,18]
# b =[20,22,24,26,28]
# if b[0] - a[-1] == 2:
#     temp = b[0]
#     for item in b[1::]:
#         if item - temp == 2:
#             temp = item
#         else:
#             print(f"{b} is not have continuous sequence of {a}")
#             break
#     else:
#         print(f"{b} is a continous sequence with {a}")
# else:
#     print(f"{b} doesnt start with contnuity of {a}")



# # write a comprehension to filter all languages which start's with p
# languages = ['python','java','peri','PHP','Python','JS','C++','Python']
# res = [item for item in languages if item[0].lower() == 'p']
# print(res)

# # write a comprehension to filter all out those names which are less than 6 characters
# names = ['apple','google','gmail','yahoo','flipkart','instagram']
# res = [item for item in names if len(item) < 6]
# print(res)

# # write a list comprehension to reverse the item of a list if the  item is of odd length string otherwise
# # keep them as it is
# names = ['apple','google','yahoo','facebook','yield','flipkart']
# res = [item[::-1] if len(item) % 2 !=0 else item for item in names]
# print(res)

# # write a comprehension to raise the elements in the list to the power of their index
# a = [1,2,3,4,5]
# res = [item ** index for index,item in enumerate(a)]
# print(res)
#
#
# # build a list of tuples with string and it;s length pair using list comprehension
# names = ['apple','google','yahoo','facebook','yelp','flipkart']
# res = [(item,len(item)) for item in names]
# print(res)

# # write a program to print all numeric values in a list using list comprehension
# items = ['apple', 1.2, 'google', '12.60', 26, 50+50j, '100']
# var = [item for item in items if isinstance(item, (int, float, complex))]
# print(var)

