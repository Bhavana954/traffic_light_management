import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(21,GPIO.IN)
GPIO.setup(26,GPIO.IN)
GPIO.setup(19,GPIO.IN)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)


while True:
    if (GPIO.input(17)==0 and GPIO.input(21)==0 and GPIO.input(19)==0 and GPIO.input(26)==0):
        GPIO.output(14,True)
        GPIO.output(4,True)
        GPIO.output(20,True)
        GPIO.output(10,True)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
        GPIO.output(11,True)
        GPIO.output(12,True)
        GPIO.output(18,True)
        GPIO.output(2,True)
        GPIO.output(10,False)
        GPIO.output(9,False)
        GPIO.output(3,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(20,False)
        GPIO.output(15,False)
        GPIO.output(14,False)
        time.sleep(3)
        print ("Object Detected in all lanes")
        time.sleep(0.1)
    elif(GPIO.input(17)==0 and GPIO.input(19)==0 and GPIO.input(26)==0 and GPIO.input(21)!=0):
        GPIO.output(14,True)
        GPIO.output(4,True)
        GPIO.output(16,True)
        GPIO.output(10,True)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,False)
        GPIO.output(3,False)
        print("Lane 1 and Lane 2 and lane 3")
        time.sleep(0.1)
    elif(GPIO.input(17)==0 and GPIO.input(19)==0 and GPIO.input(26)!=0 and GPIO.input(21)==0):
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,True)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
        GPIO.output(14,True)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,True)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,True)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,True)
        print("Lane 2 and Lane 3 and lane 4")
        time.sleep(0.1)
    elif(GPIO.input(17)==0 and GPIO.input(19)!=0 and GPIO.input(26)==0 and GPIO.input(21)==0):
        GPIO.output(14,True)
        GPIO.output(4,True)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,True)
        GPIO.output(12,False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,True)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,True)
        GPIO.output(3,False)
        print("Lane 3 and Lane 4 and lane 1")
        time.sleep(0.1)
    elif(GPIO.input(17)==0 and GPIO.input(19)!=0 and GPIO.input(26)==0 and GPIO.input(21)==0):
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,True)
        GPIO.output(3,False)
        time.sleep(3)
        GPIO.output(14,False)
        GPIO.output(4,True)
        GPIO.output(16,False)
        GPIO.output(10,True)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,True)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        print("Lane 4 and Lane 1 and lane 2")
        time.sleep(0.1)
    #2conditions
    elif(GPIO.input(17)!=0 and GPIO.input(19)==0 and GPIO.input(26)==0 and GPIO.input(21)!=0):
        print("Lane 1 and lane 2")
        GPIO.output(14,False)
        GPIO.output(4,True)
        GPIO.output(16,True)
        GPIO.output(10,True)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,True)
        GPIO.output(3,False)
        time.sleep(3)
    elif(GPIO.input(19)!=0 and GPIO.input(17)==0 and GPIO.input(26)==0 and GPIO.input(21)!=0):
        print("Lane 1 and lane 3")
        GPIO.output(14,True)
        GPIO.output(4,True)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
    elif(GPIO.input(17)!=0 and GPIO.input(19)!=0 and GPIO.input(26)==0 and GPIO.input(21)==0):
        print("Lane 4 and Lane 1")
        GPIO.output(14,False)
        GPIO.output(4,True)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,True)
        GPIO.output(12,False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,True)
        GPIO.output(3,False)
        time.sleep(3)
    elif(GPIO.input(17)==0 and GPIO.input(19)==0 and GPIO.input(26)!=0 and GPIO.input(21)!=0):
        print("Lane 3 and lane 2")
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,True)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
        GPIO.output(14,True)
        GPIO.output(4,False)
        GPIO.output(16,True)
        GPIO.output(10,True)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
    elif(GPIO.input(17)!=0 and GPIO.input(19)==0 and GPIO.input(26)!=0 and GPIO.input(21)==0):
        print("Lane 4 and lane 2")
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
    elif(GPIO.input(17)==0 and GPIO.input(19)!=0 and GPIO.input(26)!=0 and GPIO.input(21)==0):
        print("Lane 4 and lane 3")
        GPIO.output(14,True)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,True)
        GPIO.output(12,False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,True)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
    elif(GPIO.input(17)!=0 and GPIO.input(19)!=0 and GPIO.input(26)==0 and GPIO.input(21)!=0):
        print("Lane 1")
        GPIO.output(14,False)
        GPIO.output(4,True)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,False)
        time.sleep(3)
    elif(GPIO.input(17)!=0 and GPIO.input(19)==0 and GPIO.input(26)!=0 and GPIO.input(21)!=0):
        print("Lane 2")
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,False)
        GPIO.output(11,True)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
    elif(GPIO.input(17)==0 and GPIO.input(19)!=0 and GPIO.input(26)!=0 and GPIO.input(21)!=0):
        print("Lane 3")
        GPIO.output(14,True)
        GPIO.output(4,False)
        GPIO.output(16,True)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,False)
        GPIO.output(20,False)
        GPIO.output(12,False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
    elif(GPIO.input(17)!=0 and GPIO.input(19)!=0 and GPIO.input(26)!=0 and GPIO.input(21)==0):
        print("Lane 4")
        GPIO.output(14,False)
        GPIO.output(4,False)
        GPIO.output(16,False)
        GPIO.output(10,False)
        GPIO.output(18,False)
        GPIO.output(15,True)
        GPIO.output(20,False)
        GPIO.output(12,True)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(3)
    else:
        print("No vechile")
        GPIO.output(10, False)
        GPIO.output(9,True)
        GPIO.output(11,False)
        GPIO.output(15,True)
        GPIO.output(18, False)
        GPIO.output(14,False)
        GPIO.output(20,False)
        GPIO.output(16,True)
        GPIO.output(12, False)
        GPIO.output(2,False)
        GPIO.output(4,False)
        GPIO.output(3,True)
        time.sleep(0.1)
        