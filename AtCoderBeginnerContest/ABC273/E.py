"""
E - Notebook
https://atcoder.jp/contests/abc273/tasks/abc273_e
"""
import sys

input = sys.stdin.readline


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


Q = int(input())
root = Node(-1, None)
now = root

notebook = {}
for _ in range(Q):
    q = list(input().split())

    if q[0] == "ADD":
        x = int(q[1])
        now = Node(x, now)

    elif q[0] == "DELETE":
        if now != root:
            now = now.parent

    elif q[0] == "SAVE":
        y = int(q[1])
        notebook[y] = now

    elif q[0] == "LOAD":
        z = int(q[1])
        if z in notebook:
            now = notebook[z]
        else:
            now = root

    print(now.value)
