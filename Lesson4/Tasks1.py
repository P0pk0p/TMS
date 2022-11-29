import requests

my_list = list(range(1, 51))
result = []

for x in my_list:
    result.append(x)
result = result[::-1]

print(result)


# my_list = list(range(1, 51))
#
# result = [x for x in my_list ]
# print(result[::-1])

#my_list = list(range(1, 51))
#result = list(reversed(my_list))

#print(my_list)
#print(result)