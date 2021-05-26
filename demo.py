list_a = ["dog_a", "dog_a", "dog_a", "dog_a"]

list_b = ["dog_b", "dog_b", "dog_b", "dog_b"]

list_c = []

n = len(list_a) + len(list_b)

for i in range(n):
    if i % 2 == 1 and len(list_a) > 0:
        list_c.append(list_a[0])
        list_a = list_a[1:]
    else:
        list_c.append(list_b[0])
        list_b = list_b[1:]

print(list_c)
