# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:05:28 2021

@author: anaka
"""



import psycopg2

class Connection:

        def _init_(self):
            self.connection = None
            
        def openConnection(self):
            try:
               
                self.connection = psycopg2.connect(host="localhost",port="5432",dbname="Tokyo2020",user="postgres" ,password="canino123")
                print('La conexión se realizó exitosamente')
            except Exception as e:
                print (e)

        def closeConnection(self):
            self.connection.close()



