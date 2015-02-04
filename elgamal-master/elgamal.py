#!/usr/bin/python
# -*- coding: utf-8 -*-

import lint
import sys

def xgcd(a, b):								#Расширенный алгоритм Евклида
	if a == lint.Lint("0"):
		return 0, 1, b

	if b == lint.Lint("0"):
		return 1, 0, a

	px = lint.Lint("0")
	ppx = lint.Lint("1")
	py = lint.Lint("1")
	ppy = lint.Lint("0")

	while b > lint.Lint("0"):
		q = a / b
		a, b = b, a % b
		x = ppx - q * px
		y = ppy - q * py
		ppx, px = px, x
		ppy, py = py, y

	return ppx, ppy, a

def inv(a, p):								#Число в -1 степени по модулю p
	x, y, g = xgcd(a, p)
	return (x % p + p) % p

if __name__ == "__main__":

	if len(sys.argv) !=6:
		print ("wrong count of argument!!!")
		print ("USAGE : python ./elgamal.py mes.txt p.txt g.txt x.txt k.txt")
		sys.exit (-1)

	f = open(sys.argv[1])

	mes = int(f.read())

	f.close()
	
	mes = lint.Lint(str(mes))
	
	p = lint.Lint(mes.read(sys.argv[2]))# read p
	g = lint.Lint(mes.read(sys.argv[3]))#read g
	x = lint.Lint(mes.read(sys.argv[4]))#read x
	k = lint.Lint(mes.read(sys.argv[5]))#read k
	
	y = p.powmod(g, x, p)
	
	a = p.powmod(g, k, p)                   #Шифровка

	b = p.powmod(y, k, p)                   #Шифровка
	
	b = (mes * b) % p
	
	#Расшифровка 
	decode = p.powmod(a, x, p)   			#a^x mod p       	
	
	decode = inv(decode, p)					#(a^x)^(-1) mod p
	
	decode = (decode * b) % p

	f = open("decode.txt", "w")

	f.write(decode.trim().toString())

	f.close()
