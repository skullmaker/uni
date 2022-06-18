#Q1
n=int (input(""))
n= n*4 
b=str(input(""))
print ("Your heart beats",n, "in 1 minute")
Boom=str(n*b)

print( "Heart sound:",Boom)
#Q2
x = str(input(""))
y=str(input(""))
y1=x[0]
x=x.replace( x[0], y )
 
print(x.replace( x[0], y1,1 )) 

#Q3
x=str(input(''))
x= x[0:1].upper() + x[1:(len(x)-1)//2] + x[(len(x)-1)//2:(len(x)+2)//2].upper() + x[(len(x)+2)//2:len(x)-1] + x[len(x)-1:len(x)].upper()
print (x)

#Q4

lst = [] 

while True :
    x=(input())
    if x=="":
        break
    lst.append(x) 
 #a

Sum=0
 
for ele in range(0, len(lst)):
    Sum = int(Sum) + int(lst[ele])
 
 
print(Sum)
   
#b
lst.sort()
print(lst)

lst.reverse()
print(lst)
#C
positve = list(filter(lambda x: (int(x) >= 0), lst)) 

print(positve) 






#d
print (max(lst),min(lst))

#e
x = len(lst) 
if x % 2 == 0: 
    median1 = lst[x//2] 
    median2 = lst[x//2 - 1] 
    median = (int(median1) + int(median2))/2
else: 
    median = lst[x//2] 
print(median)

#f
for even in lst: 

    if int(even) % 2 == 0: 
        print((even), end = " ") 
print("")
#g


for odd in lst: 
    if int(odd) % 2 != 0: 
      
        print ( odd,end= " ") 

print("")
#h
l=5
add = list(map(lambda x : int(x) + l, lst)) 


print (str(add)) 


           
        