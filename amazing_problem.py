points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
points = sorted(points)
points =  [x[0] for x in points]
out = 0
print(points)

for i in range(1, len(points)):
    out = max(out,(points[i]- points[i-1]))

print(out)