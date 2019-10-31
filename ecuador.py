# -*- coding: utf-8 -*-
#!/usr/bin/env python
import socket
import time
import onionGpio

time.sleep(30)

gpioNum = 17
gpioObj = onionGpio.OnionGpio(gpioNum)
status  = gpioObj.setInputDirection()


while True:
    try :
        obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        obj.connect(("192.168.20.1", 8850))
        print("Conectado al servidor")



        while True:
            value = gpioObj.getValue()
            ##print 'GPIO%d input value: %d'%(gpioNum, int(valor))
            ##mens = value
            ##byt=mens.encode()
            obj.send(value)

            ##print (mens)
            time.sleep(0.5)

        obj.close()
        print("Conexión cerrada")
    except Exception as e:
        time.sleep(5)
        print( e )

    finally:
        pass

