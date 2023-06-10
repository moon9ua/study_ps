import sys
input = sys.stdin.readline

n = int(input())
l = [0] * n
r = [0] * n

for _ in range(n):
    a,b,c = input().rstrip().split()
    if b != '.':
        l[ord(a)-ord('A')] = ord(b)-ord('A')
    if c != '.':
        r[ord(a)-ord('A')] = ord(c)-ord('A')

def preorder(x):
    print(chr(x+ord('A')), end='')
    if l[x]: preorder(l[x])
    if r[x]: preorder(r[x])

def inorder(x):
    if l[x]: inorder(l[x])
    print(chr(x+ord('A')), end='')
    if r[x]: inorder(r[x])

def postorder(x):
    if l[x]: postorder(l[x])
    if r[x]: postorder(r[x])
    print(chr(x+ord('A')), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)