# -*- coding: utf-8 -*-
#!/usr/bin/env python
 
#Se importa el módulo
import socket

while True:
    try:
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        ser.bind((socket.gethostbyname("192.168.20.185"), 8855))
        ser.settimeout(5)
        ser.listen(1)
        servidor, addr = ser.accept()
    

        while True:
            peticion= servidor.recv(1024)
            print (peticion)
            
        servidor.close()
        
    except Exception as e:
        print(e)
        servidor.close()
        del ser
