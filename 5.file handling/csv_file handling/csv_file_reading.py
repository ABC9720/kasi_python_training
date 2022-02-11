import csv
from collections import defaultdict

path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\kasi.csv"

"file reading"
# with open(path,'r') as csv_file:
#     read_obj = csv.reader(csv_file)
#     for row in read_obj: # reads each row as a list
#         print(row)
"""file reader using Dict Reader"""
"file reading (using dictionary method)"
# with open(path,'r') as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:  # reads each row as a dictionary and key will be header (first row eleme)
#         print(row)


# "file writing"
# with open(path,'w') as csv_:
#     write_obj = csv.writer(csv_)
#     write_obj.writerow(['x','y','z'])
#     write_obj.writerows([('kasi','rao','mohan'),('a','b','c')])
#
# "file reading (using dictionary method)"
# "file writing"
# with open(path,'w') as csv_:
#     dictwriter_obj = csv.DictWriter(csv_.writer(["x","y","z"]))

"""write a program to read all the employees in employee table"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\employees.csv"
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if row:
#             print(row[0])


"""write program to print only the names with salaries > 7000"""
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if int(row[-1]) > 7000:
#             print(row[0])


"""wap to group male and female names""" "(using default dict)"
# with open(path) as csv_file:
#     dd = defaultdict(list)
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         dd[row[1]] += [row[0]]
#     print(dd)

"""wap to gropu employees based on their temas"""
# with open(path) as csv_file:
#     dd = defaultdict(list)
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if row:  # if any row is empty it wil raise error so that we have to check if empty or not
#             dd[row[2]] += [row[0]]   # row.strip() will wont work because row is not a string for that we directly taken row in if
#     print(dd)  # so if row empty the condition give false else if data is there in row it gives true

"""sort the shares in tes.csv file based on the share prices"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\test.csv"
# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     l = list(read_obj)
#     res = sorted(l, key = lambda d: float(d['price']))
#     print(list(res))

"""writer a program to add alll the shares in test.scv file"""
with open(path) as csv_file:
    add = 0
    read_obj = csv.DictReader(csv_file)
    for row in read_obj:
        add += float(row['price'])
    print(add)