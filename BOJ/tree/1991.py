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

def preorder(node):
    print(chr(node+ord('A')), end='')
    if l[node]: preorder(l[node])
    if r[node]: preorder(r[node])

def inorder(node):
    if l[node]: inorder(l[node])
    print(chr(node+ord('A')), end='')
    if r[node]: inorder(r[node])

def postorder(node):
    if l[node]: postorder(l[node])
    if r[node]: postorder(r[node])
    print(chr(node+ord('A')), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)