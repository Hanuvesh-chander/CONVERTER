print("THIS IS A CONVETER ")
print("AVAILABLE DATAS FOR CONVERSION ARE :-")
print("weight")
print("temperature")
print("length")
data=input("enter the type of data you want to convert :-  " )
if data=="weight":
     print("Type of weights for conversion are: ")
     print("pounds")
     print("kilograms")
     print("ounce")
     print("stones")
     weight=input("enter the type of weight to convert :- ")
     if weight=="pounds":
          weight=float(input("what's the weight in pounds ? \n  "))
          print("Weight is "+ str(weight)+" pounds")
          kilograms=0.453592* weight
          print("So  weight in  kilograms is  "+ str(kilograms)) 
          ounce=16*weight
          print("and weight in ounce is  "+ str(ounce))              
         

           stones=0.071429*weight	            
          print("and weight in stones is  "+ str(stones))              
     elif weight=="kilograms":
          weight=float(input("what's the weight in kilograms ? \n "))
          print("Weight is  "+str(weight)+" kilograms")
          pounds=2.204623*weight
          print("so weight in pounds is  "+str(pounds))   
          ounce=35.27396*weight
          print("and  weight in ounce is  "+ str(ounce))           
          stones=0.157473*weight
          print("and weight in stones is   "+ str(stones))                     
     elif weight=="ounce":
          weight=float(input("what's the weight in ounce ?  "\n))
          print("Weight in ounce is  "+ str(weight))
          pounds=0.0625*weight
          print("so weight in pounds is  "+ str(pounds))                
          kilograms=0.02835*weight
          print("and weight in kilograms is   "+ str(kilograms))           .
          stones=0.004464*weight
          print("and weight in stones is  "+ str(stones))                   
     elif weight=="stones":
          weight=float(input("what's the weight in stones ?  "\n))
          print("Weight in stones is  "+ str(weight))
          kilograms=6.350293*weight
          print("so weight in kilograms is   "+str(kilograms))              
          pounds=14*weight
          print("and weight in pounds is  "+ str(pounds))                
          ounce=224*weight
          print("and weight in ounce is  "+str(ounce))                      
      else:
          print("we don't have any more weight types")
elif data=="temperature":
     print("The types of temperature for conversion are :-")
     print("celsius")
     print("kelvin")
     print("farenheit")	
     temperature=input("enter the type of temperature to convert  :-  ")
     if temperature=="celsius":
          temperature=float(input("What's  the temperature in celsius ?  \n  "))
          print("The tempertaure in celsius is " + str(temperature))
          farenheit=32+(9/5*temperature)
          print("so temperature in farenheit is " +str(farenheit))
          kelvin=273.15+temperature
          print("and temperature in kelvin is " + str(kelvin))
     elif temperature=="kelvin":
          temperature=float(input("What's  the temperature in Kelvin?   ")
         print("The tempertaure in kelvin is " + str(temperature))
          farenheit=32+9/5*(temperature-273.15)
          print("so temperature in farenheit is " +str(farenheit))
          celsius=temperature-273.15
          print("and temperature in Celsius is " + str(celsius))              
     elif temperature=="farenheit":
          temperature=float(input("what's the temperature in farenheit ?   "))
          print("The temperature in farenheit is"+ str(temperature))
          celsius=-17.777+0.555*temperature
          print("so temperature in celsius is"+str(celsius))
          kelvin=255.372+0.555*temperature
          print("and temperature in kelvin is"+str(kelvin))
     else :
          print("Try something else")

elif  data=="length":
     print("The types of length for conversion are :-")
     print("cm")
     print("km")
     print("millimeters")
     print("foot")
     print("inches")
     print("metre")
     length=input("enter the type of length to convert :-")
     if length=="cm":
          cm=float(input("What's the length in cm ?  \n"))
          print("The length in cm is"+ str(cm))
          metres=0.01*cm
          print("So  length in  meters  is  "+ str(metres))  
          feet=0.0328084*cm
          print("and length in  feets is  "+ str(feet))        
          inches=0.393701*cm
          print("and length  in inches is  "+ str(inches))           
          km=cm/100000
          print("and length in km is    "+ str(km))
          millimetre=10*cm
          print("and length in mm is   "+str(millimetre))
     elif length=="km":
          km=float(input("What's the length in km ?  \n"))
          print("The length in km is"+ str(km))
          metres=1000*km
          print("So  length in  meters  is  "+ str(metres))  
          feet=3280.84*km
          print("and length in  feets is  "+ str(feet))        
          inches=39370.1*km
          print("and length  in inches is  "+ str(inches))            
          cm=km*100000
          print("and length in cm is    "+ str(cm))
          millimetre=1000000*km
          print("and length in mm is   "+str(millimetre))          
     elif length=="metre":
          metre=float(input("What's the length in metres ?  \n"))
          print("so" + str(metre)+"is the length in metres")
          km=metre/1000
          print("So  length in  meters  is  "+ str(km))  
          feet=3.28084*metre
          print("and length in  feets is  "+ str(feet))        
          inches=39.37*metre
          print("and length  in inches is  "+ str(inches))           
          cm=metre*100	
          print("and length in cm is    "+ str(cm))
          millimetre=1000*metre
          print("and length in mm is   "+str(millimetre))           
     elif length=="feet":
          feet=float(input("What's the length in foot ?  \n"))
          print("so the length in feet is"+str(feet))
          metres=foot/3.281
          print("So  length in  meters  is  "+ str(metres))  
          km=feet/0.0003048
          print("and length in kilometres is  "+ str(km))        
          inches=12*feet
          print("and length  in inches is  "+ str(inches))           
          cm=feet*30.48
          print("and length in cm is    "+ str(cm))
          millimetre=304.8*feet
          print("and length in mm is   "+str(millimetre))           
     elif length=="inches":
          inches=float(input("What's the length in inches ?  \n"))
          print("so the length in inches is"+str(inches))
          metres=inches/39.37
          print("So  length in  meters  is  "+ str(metres))  
          feet=inches/12
           print("and length in  feets is  "+ str(feet))        
          kilometres=inches/39370.079
          print("and length  in kilometres is  "+ str(kilometers))           
          cm=2.54*inches
          print("and length in cm is    "+ str(cm))
          millimetre=25.4*inches
          print("and length in mm is   "+str(millimetre))           
     elif length=="millimetres":
          millimetres=float(input("What's the length in millimetres ?  "))
          print("so the length in millimetres is"+str(millimetres))
          metres=millimetres/1000
          print("So  length in  meters  is  "+ str(metres))
          feet=millimetres/304.8
          print("and length in  feets is  "+ str(feet))        
          inches=millimetres/25.4
          print("and length  in inches is  "+ str(inches))           
          cm=millimetres/10
          print("and length in cm is    "+ str(cm))
          km=millimetres/1000000
          print("and length in km is   "+str(km))           
     else:
          print("try something else")    
     
else:
     print("Thanks for using me")

