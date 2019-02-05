choice=input("enter number 1,2,3,4:")
x=int(input("enter the number"))
y=int (input("enter the nunber"))
if choice==1:
  z=x+y
  print (z)
elif choice==2:
  z=x-y
  print (z)
elif choice==3:
  z=x*y
  print (z)
elif choice==4:
  if(y==0): 
   print("zero value")
  else:
   z=x/y  
   print (z)
else: 
  print ("invalid input")
