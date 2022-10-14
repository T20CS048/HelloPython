'''
Created on 2022/10/14

@author: t20cs048
'''
import random

def janken (a,b):
    if a == b:
        print('引き分け',end="")
    elif a == b-1 or a == b+2:
        print('Aの勝ち',end="")
    else:
        print('Bの勝ち',end="")

        
def hand(n):
    if n == 0:
        print('グー',end="")
    elif n == 1:
        print('チョキ',end="")
    elif n == 2:
        print('パー',end="")
        
a = 0
b = 0

a=random.randint(0,2)
b=random.randint(0,2)

print('Aの手:',end="")
hand(a)
print(' v.s. Bの手:',end="")
hand(b)
print(' -> ',end="")
janken(a,b)