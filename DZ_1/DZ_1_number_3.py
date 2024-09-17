length = int(input())
width = int(input())
size = int(input())

if size <= length * width and (size % length == 0 or size % width == 0):
    print(True)
else:
    print(False)
