# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:08:05 2021

@author: anaka
"""
import psycopg2
from configparser import ConfigParser
import bd


#!/usr/bin/python

 
def config(archivo='visualizar.ini', seccion='postgresql'):
    # Crear el parser y leer el archivo
    parser = ConfigParser()
    parser.read(archivo)
 
    # Obtener la sección de conexión a la base de datos
    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))


def conectar():
    """ Conexión al servidor de pases de datos PostgreSQL """
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()
 
        # Conexion al servidor de PostgreSQL
        print('Conectando a la base de datos PostgreSQL...')
        conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
 
        # creación del cursor
        cur = conexion.cursor()
        
        # Ejecución de una consulta con la version de PostgreSQL
        print('La version de PostgreSQL es la:')
        cur.execute('SELECT version()')
 
        # Ahora mostramos la version
        version = cur.fetchone()
        print(version)
       
        # Cierre de la comunicación con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')
 
 
if __name__ == '__main__':
    conectar()
    

def discipline():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM discipline;")
            # Hacer un while, mientras fetchone no regrese None
            disciplina= cursor.fetchone()
            while disciplina:
                print(disciplina)
                disciplina = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()
        
def athletes():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM athlete;")
            # Hacer un while, mientras fetchone no regrese None
            atleta= cursor.fetchone()
            while atleta:
                print(atleta)
                atleta = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()

def coach():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM coach;")
            # Hacer un while, mientras fetchone no regrese None
            coach= cursor.fetchone()
            while coach:
                print(coach)
                coach = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()

def event_team():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM event_team;")
            # Hacer un while, mientras fetchone no regrese None
            event= cursor.fetchone()
            while event:
                print(event)
                event = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()

def event():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM event;")
            # Hacer un while, mientras fetchone no regrese None
            ev= cursor.fetchone()
            while ev:
                print(ev)
                ev = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()
        
def team():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM discipline;")
            # Hacer un while, mientras fetchone no regrese None
            team= cursor.fetchone()
            while team:
                print(team)
                team = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()

def country():
    conexion = psycopg2.connect("dbname=Olympics user=postgres password=canino123")
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM discipline;")
            # Hacer un while, mientras fetchone no regrese None
            country= cursor.fetchone()
            while country:
                print(country)
                country = cursor.fetchone()
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()
        
        
#EJECUTAR PARA VISUALIZAR LAS TABLAS:
#Descomentar para ejecutar.
  
discipline()
#athletes()
#coach()
#event_team()
#event()
#team()
#country()
