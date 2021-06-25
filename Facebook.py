i=1
cs=11111111111
xd=1000
f=open('id.txt')
while i < 9999:
 print xd+cs
 f.write(xd+cs)
 cs+=1
 f.close()
