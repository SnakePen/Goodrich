import sys
data = []
print(f'Size of the empty list: {sys.getsizeof(data)}')
for k in range(5):
    a = len(data)
    b = sys.getsizeof(data)
    print(f'Length: {a:3d}: Size in bytes: {b:4d}')
    data.append(None)
