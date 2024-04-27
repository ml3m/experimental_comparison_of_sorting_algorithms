import random


list_len = 100

output_line = []
a = []


# RANDOM LIST GENERATION
    # FULL RANGE RANDOM
for i in range(list_len):
    a.append(i)
random.shuffle(a)
print(f"shuffled:\n\n{a}")

a = []
    # ALMOST SORTED
for i in range(list_len):
    a.append(i)
mm = random.choice(a)
mn = random.choice(a)
nn = a[mm]
a[mm] = a[mn]
a[mn] = nn
print(f"almost sorted:\n\n{a}")

a = []
    # REVERSE SORTED
for i in range(list_len):
    a.append(list_len-i-1)
print(f"Reverse sorted:\n\n{a}")

    # SORTED

a = []

for i in range(list_len):
    a.append(i)
print(f"sorted:\n\n{a}")
