     p = float(input(" Enter the principal "))
     r = float(input(" Enter the interest rate "))
     y= float(input(" Enter the number of years "))
     def simple_interest(p,r,y):
              simple_interest=float((p*r*y/100))
              return simple_interest
     print(" Simple interest is ", simple_interest(p,r,y))
