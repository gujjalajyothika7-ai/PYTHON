#16 LPA question
def greet(n,start,temp,end):
   if n==1:
        print("Disc1 moves from",start,"to",end)
   else:
        greet(n-1,start,end,temp)
        print("Disc",n,"moves from",start,"to",end)
        greet(n-1,temp,start,end)
greet(3,'A','B','C')