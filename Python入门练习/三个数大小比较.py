x=int(input('input x:'))
y=int(input('input y:'))
z=int(input('input z:'))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    z,y=y,z
print('from small to small:  ')
print(x,y,z)
