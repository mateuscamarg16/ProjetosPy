from playsound import playsound
from datetime import datetime
import time

hora_acordar = input('INFORME AS HORAS NO MODELO (00:00): ')

while True:
    hora_atual = datetime.now().strftime('%H:%M')
    
    if hora_atual == hora_acordar:
        playsound(r"C:\Users\Mateus\Downloads\acorda.mp3.mp3")
        break
    
    time.sleep(30)


