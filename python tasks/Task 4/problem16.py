# Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest = sorted(set(score for name, score in students))[1]

    for name in sorted(name for name, score in students if score == second_lowest):
        print(name)