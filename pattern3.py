for i in range(5):
   for j in range(5):
       if i in [0,4]:
           print("-",end="")
       else:
           if j in [0,4]:
               print("|",end="")
           else:
               print(" ",end="")
   print()
               
