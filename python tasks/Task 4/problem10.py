# Find a String
# HackerRank: https://www.hackerrank.com/challenges/find-a-string/problem

string = input().strip()
sub_string = input().strip()
count = 0
for i in range(len(string) - len(sub_string) + 1):
    if string[i:i + len(sub_string)] == sub_string:
        count += 1
print(count)
