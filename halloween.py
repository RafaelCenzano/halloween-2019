import random
import os
from time import sleep as delay

def hacker1():
	for nums in range(0,101):
		delay(0.05)
		print(f'Hacking NASA; status: {nums}%')

def hacker2():
	for nums in range(0,random.randint(100,300)):
		delay(0.007)
		newnums = nums ** random.randint(4,20)
		print(f'compute hash: {newnums}')

def hacker3():
	for nums in range(0,101):
		delay(0.009)
		print(f'Cracking firewall 1; status: {nums}%')
	print('------------------\nFirewall 1 cracked\n------------------')
	delay(1)
	for nums in range(0,101):
		delay(0.009)
		print(f'Cracking firewall 2; status: {nums}%')
	print('------------------\nFirewall 2 cracked\n------------------')
	delay(1)
	for nums in range(0,101):
		delay(0.009)
		print(f'Cracking firewall 3; status: {nums}%')
	print('------------------\nFirewall 3 cracked\n------------------')
	delay(1)
	for nums in range(0,101):
		delay(0.009)
		print(f'Cracking firewall 4; status: {nums}%')
	print('------------------\nFirewall 4 cracked\n------------------')
	delay(1)
	for nums in range(0,101):
		delay(0.009)
		print(f'Cracking firewall 5; status: {nums}%')
	print('------------------\nFirewall 5 cracked\n------------------')
	delay(1)
	for nums in range(0,101):
		delay(0.009)
		print(f'Cracking firewall 6; status: {nums}%')
	print('------------------\nFirewall 6 cracked\n------------------')
	delay(1)

def hacker4():
	for r, d, f in os.walk('/Users/rafael/Documents/Programming/'):
		for files in f:
			delay(0.003)
			print(files)

def hacker5():
	for r, d, f in os.walk('/Users/rafael/Documents/Programming/'):
		for dirs in d:
			delay(0.003)
			if dirs != '__pycache__' and len(str(dirs)) > 2:
				print(dirs)

if __name__ == '__main__':
	while True:
		randNum = random.randint(0,4)
		if randNum == 0:
			hacker1()
		elif randNum == 2:
			hacker3()
		elif randNum == 3:
			hacker4()
		elif randNum == 4:
			hacker5()
		else:
			hacker2()
