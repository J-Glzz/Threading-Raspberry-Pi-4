import threading
import concurrent.futures
import RPi.GPIO as GPIO
import time
import sys

# Establecemos que vamos a trabjar en modo BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Led's Output
led1 = 14
led2 = 15
led3 = 10
led4 = 9
led5 = 11
# Boton Input
boton1 = 18
boton2 = 23
boton3 = 24
boton4 = 25
boton5 = 8
botonParo = 7


def btn1():
    GPIO.setup(boton1, GPIO.IN)
    GPIO.setup(led1, GPIO.OUT)
    while True:
        btn_state = GPIO.input(boton1)
        if btn_state == False:
            print("Encendido led 1")
            GPIO.output(led1, GPIO.HIGH)
        Rojo1 = GPIO.PWM(led1, 5)
        Rojo1.start(5)
        time.sleep(0.5)
        break


while True:
    btn_state = GPIO.input(boton1)
    if btn_state == False:
        print("Apagado led 1")
        GPIO.output(led1, GPIO.LOW)
        time.sleep(0.5)
        break


def btn2():
    GPIO.setup(boton2, GPIO.IN)
    GPIO.setup(led2, GPIO.OUT)
    while True:
        btn_state = GPIO.input(boton2)
        if btn_state == False:
            print("Encendido led 2")
            GPIO.output(led2, GPIO.HIGH)
        Verde1 = GPIO.PWM(led2, 10)
        Verde1.start(10)
        time.sleep(0.5)
        break


while True:
    btn_state = GPIO.input(boton2)
    if btn_state == False:
        print("Apagado led 2")
        GPIO.output(led2, GPIO.LOW)
        time.sleep(0.5)
        break


def btn3():
    GPIO.setup(boton3, GPIO.IN)
    GPIO.setup(led3, GPIO.OUT)
    while True:
        btn_state = GPIO.input(boton3)
        if btn_state == False:
            print("Encendido led 3")
            GPIO.output(led3, GPIO.HIGH)
        azul = GPIO.PWM(led3, 15)
        azul.start(15)
        time.sleep(0.5)
        break


while True:
    btn_state = GPIO.input(boton3)
    if btn_state == False:
        print("Apagado led 3")
        GPIO.output(led3, GPIO.LOW)
        time.sleep(0.5)
        break


def btn4():
    GPIO.setup(boton4, GPIO.IN)
    GPIO.setup(led4, GPIO.OUT)
    while True:
        btn_state = GPIO.input(boton4)
        if btn_state == False:
            print("Encendido led 4")
            GPIO.output(led4, GPIO.HIGH)
        Verde2 = GPIO.PWM(led4, 25)
        Verde2.start(25)

        time.sleep(0.5)
        break


while True:
    btn_state = GPIO.input(boton4)
    if btn_state == False:
        print("Apagado led 4")
        GPIO.output(led4, GPIO.LOW)
        time.sleep(0.5)
        break


def btn5():
    GPIO.setup(boton5, GPIO.IN)
    GPIO.setup(led5, GPIO.OUT)
    while True:
        btn_state = GPIO.input(boton5)
        if btn_state == False:
            print("Encendido led 5")
            GPIO.output(led5, GPIO.HIGH)


Rojo2 = GPIO.PWM(led4, 50)
Rojo2.start(50)
time.sleep(0.5)
break

while True:
    btn_state = GPIO.input(boton5)
    if btn_state == False:
        print("Apagado led 5")
        GPIO.output(led5, GPIO.LOW)
        time.sleep(0.5)
        break


def btnp():
    GPIO.setup(botonParo, GPIO.IN)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.setup(led4, GPIO.OUT)
    GPIO.setup(led5, GPIO.OUT)
    while True:
        btn_state = GPIO.input(botonParo)
        if btn_state == False:
            print("Apagados")
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.LOW)
            GPIO.output(led4, GPIO.LOW)
            GPIO.output(led5, GPIO.LOW)
            time.sleep(0.5)
            break
    GPIO.cleanup(0)


while True:
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = []
        futures.append(executor.submit(btn1, ))
        futures.append(executor.submit(btn2, ))
        futures.append(executor.submit(btn3, ))
        futures.append(executor.submit(btn4, ))
        futures.append(executor.submit(btn5, ))
        futures.append(executor.submit(btnp, ))
        for future in concurrent.futures.as_completed(futures):
            future.result()
