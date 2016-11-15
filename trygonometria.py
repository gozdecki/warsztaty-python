def sin(x):
   if x == 90:
      res = 1
   elif x == 60:
      res = (3**(0.5))/2
   elif x == 45:
      res = (2**(0.5))/2
   elif x == 30:
      res = 0.5
   elif x == 0:
      res = 0
   else:
      res = False
   return res

print(sin(90), sin(45), sin(20))
