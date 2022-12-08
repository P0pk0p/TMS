from datetime import datetime

# def decorator(func):
#     def wrapper(*args, **kvargs):
#         time = datetime.now()
#         result = func(*args, **kvargs)
#         print("Used time:", datetime.now() - time)
#         return result
#     return wrapper
#
#
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
#
# gcd(a,b)
# gcd(a,b)
# gcd(a,b)

# print(gcd)

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@counter
def f():
    print("Hello")


f()
f()
f()

print(f.count)


