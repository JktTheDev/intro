n = int(input("Enter the number:"))
i=1
a= int(input("Enter the lower limit:"))
b= int(input("Enter the upper limit:"))
y=int((a-(a%n))/n)
while(n*y<b):
   if n*y>=a:
         print(n*y)
   y=y+1