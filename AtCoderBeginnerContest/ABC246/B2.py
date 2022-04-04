"""複素数でやってみる
"""

A, B = map(int, input().split())
z = A + B * 1j

ans = z / abs(z)
print(ans.real, ans.imag)
