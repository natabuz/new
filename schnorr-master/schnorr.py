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
	tmp = lint.Lint()


	if len(sys.argv) !=7:
		print ("wrong count of argument!!!")
		print ("USAGE : python ./schnorr.py p.txt q.txt g.txt w.txt r.txt e.txt")
		sys.exit (-1)
	
	p = lint.Lint(tmp.read(sys.argv[1]))#read p
	q = lint.Lint(tmp.read(sys.argv[2]))#read q
	g = lint.Lint(tmp.read(sys.argv[3]))#read g
	w = lint.Lint(tmp.read(sys.argv[4]))#read w
	r = lint.Lint(tmp.read(sys.argv[5]))#read r
	e = lint.Lint(tmp.read(sys.argv[6]))#read e
	
	inv_g = inv(g, p)

	y = p.powmod(inv_g, w, p)
	
	x = p.powmod(g, r, p)
	
	print "Ключи считаны\n"
	
	print "Алиса отсылает x =", x, "Бобу\n"
	
	print "Боб отсылает e =", e, "Алисе\n"

	s = (r + w * e) % q

	print "Алиса отсылает s =", s, "Бобу\n"

	m1 = p.powmod(g, s, p)
	m2 = p.powmod(y, e, p)

	m = (m1 * m2) % p

	if m == x:
		print "Боб идентифицировал Алису, так как x =", m, "\n"
	else:
		print "Не удалось идентифицировать\n"
