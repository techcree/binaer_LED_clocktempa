# Temperaturanzeige

#The LED on the Pico board is the LED PIN 25
#
#                Stu                                Min                               Sek
#  80 ()            8 (GP27/led19)    80 ()            8 (GP11/led11)    80 (GP15/led07)  8 (GP3/led03)
#  40 (GP22/led22)  4 (GP18/led18)    40 (GP14/led14)  4 (GP10/led10)    40 (GP28/led06)  4 (GP2/led02)
#  20 (GP21/led21)  2 (GP17/led17)    20 (GP13/led13)  2 (GP9/led09)     20 (GP5/led05)   2 (GP1/led01)
#  10 (GP20/led20)  1 (GP16/led16)    10 (GP12/led12)  1 (GP8/led08)     10 (GP4/led04)   1 (GP0/led00)
#
#
import machine 
import utime
from machine import ADC #Mainboard Sensor
from machine import Pin
import time, random
import change

#sekunden Einer
led00 = Pin(0, Pin.OUT) # sek1 gruen (1)
led01 = Pin(1, Pin.OUT) # sek1 gruen (2)
led02 = Pin(2, Pin.OUT) # sek1 gruen (4)
led03 = Pin(3, Pin.OUT) # sek1 gruen (8)
#sekunden Zehner
led04 = Pin(4, Pin.OUT) # sek10 gruen (1) 
led05 = Pin(5, Pin.OUT) # sek10 gruen (2)
#Pin6 wird vom RTC Modul benötigt###
led06 = Pin(28, Pin.OUT) # sek10 gruen (4)
# Pin7 wird vom RTC Modul benötigt###
led07 = Pin(15, Pin.OUT) # sek10 gruen (8)
# Minuten Einer
led08 = Pin(8, Pin.OUT) # min rot (1)
led09 = Pin(9, Pin.OUT) # min rot (2)
led10 = Pin(10, Pin.OUT) # min rot (4)
led11 = Pin(11, Pin.OUT) # min rot (8)
#Minuten Zehner
led12 = Pin(12, Pin.OUT) # min rot (1)
led13 = Pin(13, Pin.OUT) # min rot (2)
led14 = Pin(14, Pin.OUT) # min rot (4)
# min10 (8) rot wird nicht benötigt
#Stunden Einer
led16 = Pin(16, Pin.OUT) # std1 gelb (1)
led17 = Pin(17, Pin.OUT) # std1 gelb (2)
led18 = Pin(18, Pin.OUT) # std1 gelb (4)
led19 = Pin(27, Pin.OUT) # std1 gelb (8)
#Stunden Zehner
led20 = Pin(20, Pin.OUT) # std10 gelb (1)
led21 = Pin(26, Pin.OUT) # std10 gelb (2)
led22 = Pin(22, Pin.OUT) # std10 gelb (4)
# std10 (8) gelb wird nicht benötigt
#led26 = Pin(26, Pin.OUT) # std10 gelb (4)


#Alle aus RESET
led00.value(0)
led01.value(0)
led02.value(0)
led03.value(0)
led04.value(0)
led05.value(0)
led06.value(0)
led07.value(0)
led08.value(0)
led09.value(0)

led10.value(0)
led11.value(0)
led12.value(0)
led13.value(0)
led14.value(0)

led16.value(0)
led17.value(0)
led18.value(0)
led19.value(0)

led20.value(0)
led21.value(0)
led22.value(0)

#Pause


#


# Setup Temperaturmessung und Konvertierung
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535) 


while True:
        loop = 0
        while loop <= 2:
            h = 0
            o = 0
            reading = sensor_temp.read_u16() * conversion_factor
            temperature = round(27 - (reading - 0.706) / 0.001721)
            tempa=temperature
            print("TEMPERATUR")
            print (tempa)
            #print("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 7)
            utime.sleep(3)
        
#LED zeigen Temperaturbereiche an    
            if tempa == 0:
                led22.value(1)    
            
            if tempa == 1:
                led00.value(1)
            
            if tempa == 2:
                led01.value(1)

            if tempa == 3:
                led00.value(1)
                led01.value(1)
           
            if tempa == 4:
                led02.value(1)
          
            if tempa == 5:
                led00.value(1)
                led02.value(1)
                
            if tempa == 6:
                led01.value(1)
                led02.value(1)  
          
            if tempa == 7:
                led00.value(1)
                led01.value(1)
                led02.value(1)
          
            if tempa == 8:
                led03.value(1)
 
            if tempa == 9:
                led00.value(1)
                led03.value(1)
          
            if tempa == 10:
                led04.value(1)
          
            if tempa == 11:
                led00.value(1)
                led04.value(1)
          
            if tempa == 12:
                led01.value(1)
                led04.value(1)
          
            if tempa == 13:
                led00.value(1)
                led01.value(1)
                led04.value(1)

            if tempa == 14:
                led02.value(1)
                led04.value(1)
          
            if tempa == 15:
                led00.value(1)
                led02.value(1)
                led04.value(1)
          
            if tempa == 16:
                led01.value(1)
                led02.value(1)
                led04.value(1)
          
            if tempa == 17:
                led00.value(1)
                led01.value(1)
                led02.value(1)
                led04.value(1)

            if tempa == 18:
                led03.value(1)
                led04.value(1)
          
            if tempa == 19:
                led00.value(1)
                led03.value(1)
                led04.value(1)
          
            if tempa == 20:
                led05.value(1)
          
            if tempa == 21:
                led00.value(1)
                led05.value(1)
          
            if tempa == 22:
                led01.value(1)
                led05.value(1)
          
            if tempa == 23:
                led00.value(1)
                led01.value(1)
                led05.value(1)

            if tempa == 24:
                led02.value(1)
                led05.value(1)
          
            if tempa == 25:
                led00.value(1)
                led02.value(1)
                led05.value(1)
          
            if tempa == 26:
                led01.value(1)
                led02.value(1)
                led05.value(1)
          
            if tempa == 27:
                led00.value(1)
                led01.value(1)
                led02.value(1)
                led05.value(1)
          
            if tempa == 28:
                led03.value(1)
                led05.value(1)
          
            if tempa == 29:
                led01.value(1)
                led03.value(1)
                led05.value(1)
          
            if tempa == 30:
                led04.value(1)
                led05.value(1)
          
            if ((tempa>= 31) and (tempa<= 50)):
                led00.value(1)
 
            utime.sleep(5)

            #Reset
            led00.value(0)
            led01.value(0)
            led02.value(0)
            led03.value(0)
            led04.value(0)
            led05.value(0)
            led06.value(0)
            led07.value(0)
            led08.value(0)
            led09.value(0)
            led10.value(0)
            led11.value(0)
            led12.value(0)
            led13.value(0)
            led14.value(0)
            led16.value(0)
            led17.value(0)
            led18.value(0)
            led19.value(0)
            led20.value(0)
            led21.value(0)
            led22.value(0)
            
            loop = loop + 1
            
        if loop >= 3:
            exec(open('change.py').read())