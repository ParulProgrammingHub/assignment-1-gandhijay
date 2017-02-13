      s1=float(input( " Enter Marks of subject 1 "))
      s2=float(input( " Enter Marks of subject 2 "))
      s3=float(input( " Enter Marks of subject 3 "))
      s4=float(input( " Enter Marks of subject 4 "))
      s5=float(input( " Enter Marks of subject 5 "))
      tot=(s1+s2+s3+s4+s5)
      mean=(tot)/5 
      print ( " mean ",mean) 
      per=(tot*100)/500
      print ( " Per ",per)
      if per  <= 35 :
              print( " Fail ")
      else :
            print( " Pass ")
