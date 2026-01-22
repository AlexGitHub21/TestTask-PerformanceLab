import sys

file_path_1 = sys.argv[1]
file_path_2 = sys.argv[2]

with open(file_path_1, 'r') as f1:
    lines = f1.readlines()
    h, k = map(int, lines[0].split())
    rx, ry = map(int, lines[1].split())

with open(file_path_2, 'r') as f2:
    list_coord = []
    for line in f2:
        x, y = map(int, line.split())
        list_coord.append((x, y))


for x, y in list_coord:
    l = ((x - h) ** 2 / rx ** 2) + ((y - k) ** 2 / ry ** 2)
    if l > 1: print(2)
    if l == 1: print(0)
    if l < 1: print(1)

print("Центр эллипса: ",h, k)
print("Радиус: ", rx, ry)
print("Координаты точек: ", list_coord)