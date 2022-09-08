#!/usr/bin/python3.8

#leta primtalargetsnumber

#ange maxtal att prova

numberstotest =int(input('hur många tal vill du undersöka?:'))
#yttre loop prova samtliga tal till numerstotest

for i in range(1,numberstotest+1):

    #inre loop - provar om talet i är jämt delbart med något annat än 1 och i
   #då är  det inte ett primtal

   provennotprime = False
   for k in range(2,i):
      if i % k == 0:
         print(f'    {i} är ej ett primtal')
         provennotprime = True
         break
# Om vi lämnat den inre loopen utan att sätta provennotprime så har vi  funnit ett primtal.
   if provennotprime == False:
      print(f'{i} Är ett Primtal!')
      
