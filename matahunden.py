#!/usr/bin/python3.8 


'''
fråga användare om hunden är hungrig.
Skriv ut 'mata hunden' om svar et är Ja
skri ut hunden mätt om svar nej.
annars skriv ut förstår ej.
'''
svar=input('Är hunden hungrig?')
if svar.lower() == 'ja':
  print(f'Du svarade {svar} - Mata hunden!!')
elif svar.lower() == 'nej':
  print(f'Du svarade {svar} - Hunden är alltså mätt!!')
else:
  print('Förstår ej svar')
print('***slut på programmet***')

 

