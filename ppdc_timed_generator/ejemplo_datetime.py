import datetime as dt

# Date
t1 = dt.date(2025, 10, 17)
despues = dt.date(2025, 10, 20)
print(t1, type(t1))

res = despues - t1
print("Resta:", res, type(res))

# Datetime
t2 = dt.datetime.now()
t4 = dt.datetime(2025, 1, 1, 7, 00)
print(t2, type(t2))
print(t4, type(t4))

res = t2 - t4
print()
print("Resta: ", res, ":", type(res))

# Time
t3 = dt.time(23, 00, 00)
print(t3, type(t3))


# Datetime con deltas
current = dt.datetime.now()
print()
print(current)
for i in range(10):
    current -= dt.timedelta(days=1)
    print(current)
