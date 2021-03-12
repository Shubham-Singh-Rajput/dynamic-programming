n=5
oldspace=1
oldbuilding=1
for i in range(2,n+1):
    space=oldbuilding
    building=oldspace+oldbuilding
    oldbuilding=building
    oldspace=space
print((oldspace+oldbuilding)**2)