def my_func(n):
    if n == 0:
        return 1
    return my_func(n - 1) * n


print(my_func(4))