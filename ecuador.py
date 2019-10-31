# -*- coding: utf-8 -*-
#!/usr/bin/env python
import socket
import time
import onionGpio
import json

##time.sleep(30)

gpioNum1 = 17
gpioNum2 = 11
gpioObj1 = onionGpio.OnionGpio(gpioNum1)
gpioObj2 = onionGpio.OnionGpio(gpioNum2)
status1  = gpioObj1.setInputDirection()
status2  = gpioObj2.setInputDirection()


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
            out = {
            	"GPIO17":value1,
            	"GPIO11":value2
            }
            out = json.dumps(out)
            obj.send(out)

            ##print (mens)
            time.sleep(1)

        obj.close()
        print("Conexión cerrada")
    except Exception as e:
        time.sleep(5)
        print( e )

    finally:
        pass
