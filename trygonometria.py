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


def cos2(x):
   if x == 0:
      res = 1
   elif x == 30:
      res = (3**(0.5))/2
   elif x == 45:
      res = (2**(0.5))/2
   elif x == 60:
      res = 0.5
   elif x == 90:
      res = 0
   else:
      res = False
   return res

def cos(x):
   return sin(90-x)

def tg(x):
   return sin(x)/cos(x)

print(sin(90), sin(45), sin(20))
print(cos(90), cos(45), cos(20))
print(cos2(90), cos2(45), cos2(20))
print(tg(0), tg(45), tg(30))
print(tg(90))
