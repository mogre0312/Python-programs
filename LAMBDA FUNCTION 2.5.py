x=[1,2,3,4,5]
y=list(map(lambda num:num*num,x))
print(y)

z=list(filter(lambda num:num%2==0,x))
print(z)

u=['ashu','ankit','pooja']
s=list(map(lambda u:u[0],u))
print(s)

t=list(filter(lambda u:u[0]=='p',u))
print(t)