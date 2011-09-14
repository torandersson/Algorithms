""" 
Todo: 
	Change method of input
	Add modulus
	Add the testcases

Tor Andersson:
site: http://www.alltheissues.com

I implemented this algorithm in Java back in school and wanted to try again, parsing is always fun 

Idiotic to implement this in python since python has one builtin

python 
>>> 3*2+4*5
26

Example:

expression = ["3","*","2","+","4","*","5"]
calculator = Calculator(expression)
calculator.parse()

Grammar:

E -> T { (  "+" | "-"  ) T}
T -> F {( "*" | "/" ) F}
F -> P ["^" F]
P -> v | "(" E ")" | "-" T	       
"""

#Importing for 5/2 = 2.5 and not 2
from __future__ import division

class Calculator(object):
	def __init__(self,expression):
		self.expression = expression
		self.pos = -1	
	
	def parse(self):
		t = self.E()
		print t
	
	def E(self):
		t = self.T()
		while self.next() == "+" or self.next() == "-":
			operand = self.next()
			self.advance_next()
			t1 = self.T()
			if operand == "+":
				t =  float(t)+float(t1)
			else:	
				t =  float(t)-float(t1)
		return float(t)
		
	def T(self):
		t = self.F()
		while self.next() == "*" or self.next() == "/":
			operand = self.next()
			self.advance_next()
			t1 = self.F()
			if operand == "*":
				t = float(t) * float(t1)
			else:
				t = float(t) / float(t1)
		return float(t)
		
	def F(self):
		t = self.P()
		if self.next() == "^":
			t1 = self.F()
			return t**t1
			self.advance_next()
		return t
		
	def P(self):
		if self.isNumber(self.next()):
			t = self.next()
			self.advance_next()
			return t
		elif self.next() == "(":
			self.advance_next()
			t = self.E()
			expext(")")
			return t
 		elif self.next() == "-":
			self.advance_next()
			t = self.F()
			return (-1)*t
		else:
			raise Exception("Unknown token -->"+self.next()+ "at position "+ str(self.pos))
			
	def isNumber(self,char):
		return char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0" 
	
	def expect(self,tok):
		if self.next() == tok:
			self.advance_next()
		else:
			raise Exception("Expected an other token!")
	
	def advance_next(self):
		if self.pos >= len(expression):
			return None
		self.pos +=1
		return self.expression[self.pos]
				
	def current(self):
		return self.expression[self.pos]
	
	def next(self):
		if self.has_next():
			return self.expression[self.pos+1]
		return ""
	
	def has_next(self):
		return self.pos+1 < len(expression)
		
