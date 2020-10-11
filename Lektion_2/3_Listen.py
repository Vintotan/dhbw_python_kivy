a = [1, "Hallo", 12.5]
print(a)

b = range(1, 10, 1)
print(b)

for i in b:
    print(i)

c = [2, 4, 6, 8]

d = [a, c]
print(d)

# Indizes
print(a[1])
print(d[0][1])  # -> "Hallo"

print(d[1][2]) # -> 6

c.append(10)
print(c)