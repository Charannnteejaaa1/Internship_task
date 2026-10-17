# Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input().strip())
set_a = set(map(int, input().split()))
n = int(input().strip())
set_b = set(map(int, input().split()))
for value in sorted(set_a ^ set_b):
    print(value)
