min_max = lambda x, y: (x,y) if x < y else (y,x)
a = 5
b = 10

print("Minimum and Maximum:", min_max(a,b))