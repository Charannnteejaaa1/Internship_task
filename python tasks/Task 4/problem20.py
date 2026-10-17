# No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = sum(1 if value in a else -1 if value in b else 0 for value in arr)
print(happiness)
