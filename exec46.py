'''
FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESIVA PARA O
ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 A 0 COM UMA PAUSA DE 1 SEG ENTRE ELES
'''

import time

for n in range(10, -1, -1):
    print(n)
    time.sleep(1)

print("""
                                   .''.       
       .''.      .        *''*    :_/_:     . 
      :_/_:   _/_  .:.*_*   : / :  .'.:.'.
  .''.: / :   ./)   ':'* / * :  '..'.  -=:o:=-
 :_/_:'.:::.    ' *''*    * '.'/.' _.':'.'
 : / : :::::     *_/_*     -= o =-  /)    '  
  '..'  ':::'     * / *     .'/.'.   '
      *            *..*         :
""")