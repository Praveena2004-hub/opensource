x,y,z=map(int,input().split())
total_time=x*y
total_available=z*24*60
if total_time <= total_available:
    print("YES")
else:
    print("NO")
