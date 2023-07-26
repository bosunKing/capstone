
from mylib.getchar import Getchar
import serial

sp  = serial.Serial('COM3', 115200, timeout=1) #serial통신을 위한 객체 생성 timeout=> 1초동안 기다려도 수신되는게없을시 넘어감.

pan = _pan = 75  
tlt = _tlt = 75

def send_pan(pan):
    tx_dat = "pan" + str(pan) + "\n" #tx_dat 전송할 데이터
    sp.write(tx_dat.encode())        #인코드 해야함     
    print(tx_dat)

def send_tilt(tlt):
    tx_dat = "tilt" + str(tlt) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

def main(args=None):
    global pan; global _pan; global tlt; global _tlt;
    send_pan(75)
    send_tilt(75)
    kb = Getchar()
    key = ''
    
    while key!='Q':
    
        key = kb.getch()
            ####################################################### tilt control ########################################
        if key == 'w': 
            if tlt - 1 >= 25:
                tlt = tlt - 1
            else:
                tlt = 25
            print("tilt up,   pan = %s, tilt = %s."%(pan, tlt))
            send_tilt(tlt)
        elif key == 's':
            if tlt + 1 <= 125:
                tlt = tlt + 1
            else:
                tlt = 125
                
            print("tilt down, pan = %s, tilt = %s."%(pan, tlt))
            send_tilt(tlt)
            ####################################################### pan control ########################################
        elif key == 'a': # pan left
            if pan + 1 <= 125:
                pan = pan + 1
            else:
                pan = 125
            print("pan left,  pan = %s, tilt = %s."%(pan, tlt))
            send_pan(pan)
        if key == 'd': # pan right
            if pan - 1 >= 25:
                pan = pan - 1
            else:
                pan = 25
            print("panright,  pan = %s, tilt = %s."%(pan, tlt))
            send_pan(pan)
        else:   pass
        
        #send_pan(pan)
        #send_tilt(tlt)
        

if __name__ == '__main__':
    main()

