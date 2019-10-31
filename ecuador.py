# -*- coding: utf-8 -*-
#!/usr/bin/env python
import socket
import time
import onionGpio

time.sleep(30)

gpioNum1 = 17
gpioNum2 = 11
gpioObj1 = onionGpio.OnionGpio(gpioNum1)
gpioObj2 = onionGpio.OnionGpio(gpioNum2)
status  = gpioObj.setInputDirection()


while True:
    try :
        obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        obj.connect(("192.168.20.1", 8850))
        print("Conectado al servidor")



        while True:
            value1 = gpioObj1.getValue()
            value2 = gpioObj2.getValue()
            ##print 'GPIO%d input value: %d'%(gpioNum, int(valor))
            ##mens = value
            ##byt=mens.encode()
            obj.send(value1,value2)

            ##print (mens)
            time.sleep(0.5)

        obj.close()
        print("Conexión cerrada")
    except Exception as e:
        time.sleep(5)
        print( e )

    finally:
        pass
