a=121
if str(a)==str(a)[::-1]:
    print(a,"Pallandrome")
else:
    print(a,"not pallandrome")




a=list(range(-25,26))
b=[]
c=[]
zero=[]
for i in a:
    if i > 0:
      b.append(i)
    elif  i < 0:
      c.append(i)
    else:
      zero.append(i)
print("Positive numbers",b)
print("negative numbers",c)
print(zero)
