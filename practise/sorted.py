
# string_ = 'hello python01239%# -='
# print(sorted(string_)) # returns in the form of list containing each character sorted
# list_ = [10008,22,3]
# print(sorted(list_))
# set_ = {546,58,630}
# print(sorted(set_))
# dict_ = {'d': 78, 'b':60, 'c':1008}
# print(sorted(dict_)) #sorts based on keys and return only keys after sorted
# print(sorted(dict_.values())) # sorts based on values and returns only values after soted
# print(sorted(dict_.items())) # sorts based on keys and returns list containing tuples of keys and value
"""when we performing sorted on dictionaries if sorted argument is of keys all keys are of same data type only
or when we performing sorted based on values all values must be of same data type"""
"""sorted return data type is always list only"""
# print(sorted(dict_, reverse = True))
# print(sorted(dict_.values(), reverse=True))

"""find the largest and smallest words"""
# string_ = 'hello python world become polution of current affairs'
# res = sorted(string_.split(), key = len)
# print(res[0])
# print(res[-1])

"""to print largest and smallest words along with their lenths in the below sentence"""
sentence = 'kasi is a python language'
res = sorted(sentence.split(), key = len)
print(res[0], len(res[0]))
print(res[-1], len(res[-1]))

# """using unpacking"""
# shortest,*res,longest = sorted(sentence.split(), key = len)
# print(shortest, len(shortest))
# print(longest, len(longest))

"""wap to sort the below list based on the last character of the each string"""
list_ = ['kasi','is','guntur','person','bangalore']
for