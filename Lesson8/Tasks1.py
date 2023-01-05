


a = b'r\xc3\xa9sum\xc3\xa9'
print(a.decode())
b = a.decode("utf-8")
print(b)
c = b.encode("latin1")
print(c)
d = c.decode("utf-8")
print(d)
