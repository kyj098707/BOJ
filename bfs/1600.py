import sys
input = sys.stdin.readline
from collections import deque

m_x = [1,0,-1,0]
m_y = [0,1,0,-1]

h_x = [2,1,-1,-2,-2,-1,1,2]
h_y = [1,2,2,1,-1,-2,-2,-1]
### 3차원 배열을 만들어서 접근 하면 좋을 듯
k = int(input())
m, n = 