#!/usr/bin/python3.8


'''
Tar användar -input och sparar i variabeln 'nutemp'
Evaluerar nutemp och skriver ut:
-'slå på vrme' om nutemp<25
-'stäng av värme om nutemp >24

'''

NuTemp = int(input('Vilken temperatur är det?')))
if NuTemp <25:
  print(f'Temperaturen är {NuTemp} -grader. Slå på värmen!!')
elif NuTemp >24:
  print(f'Du svarade {NuTemp} -grader. Sänk värmen!!')
else:
  print('Förstår ej svar')
print('***slut på programmet***')


#läs user-input
'''
nuTemp = read('Ange nuTemp:')
NuTemp = input('Vilken temperatur är det?')
if NuTemp == <=25:
  print(f'Temperaturen är {NuTemp} -grader. Slå på värmen!!')
elif NuTemp == >24:
  print(f'Du svarade {NuTemp} -grader. Sänk värmen!!')
else:
  print('Förstår ej svar')
print('***slut på programmet***')
'''
