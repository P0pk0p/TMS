
my_list = [9, 5, 1, 3, 5, 3, 1, 2, 7, 1, 7, 9]

def my_func():

    rez = {}
    for i in my_list:
        if rez.get(i, None):
            rez[i] += 1
        else:
            rez[i] = 1

my_func()

print(my_func)


# lst = [9, 13, 1, 3, 7, 3, 1, 1, 7, 1, 7, 9]
# rez = {}
#
# for el in lst:
#     if rez.get(el, None):
#         rez[el] += 1
#     else:
#         rez[el] = 1
#
# print(rez)
#
# rez_sorted = sorted(rez.items(), key=lambda x: x[1], reverse=True)
# print(dict(rez_sorted))