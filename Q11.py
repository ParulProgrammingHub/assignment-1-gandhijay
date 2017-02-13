   pri = float(input(" Enter the principal "))
   rate = float(input(" Enter the interest rate "))
   years= float(input(" Enter the number of years "))
   def compound_interest(pri,rate,years):
       if years<=0:
           return pri
      else:
            return compound_interest(pri+pri*rate/100,rate,years-1)
    print(" Compount is ", compound_interest(pri,rate,years))
