###coding:utf-8
import random
while 1:
   secret=random.randint(1000,9999)
   a=secret/1000
   b=(secret/100)%10
   c=(secret/10)%10
   d=secret%10
   if not(a==b or a==c or a==d or b==c or b==d or c==d):
     break
while 1:
   while 1:
      try:
         i=int(raw_input("please enter a four-digit number "))
      except:
         print "you must enter a number"
         continue
      a1=i/1000
      b1=(i/100)%10
      c1=(i/10)%10
      d1=i%10
      if a1==0 or a1==b1 or a1==c1 or a1==d1 or b1==c1 or b1==d1 or c1==d1 or a1>=10:
         print "your number is not a four-digit number or it has repeated digits."
      elif b1==0 or c1==0 or d1==0:
         print "number 0 should not be entered"   
      else:
         break
   C=0
   A=0
   if a1 in (a,b,c,d) :
      C+=1
   if b1 in (a,b,c,d) :
      C+=1
   if c1 in (a,b,c,d) :
      C+=1
   if d1 in (a,b,c,d) :
      C+=1
   if a1==a:
      A+=1
   if b1==b:
      A+=1
   if c1==c:
      A+=1
   if d1==d:
      A+=1
   B=C-A
   print A, "A",B,"B"
   if A==4:
      break
   print "please guess again"
print"Congratulations!You 've got the number"

