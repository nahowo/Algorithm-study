import sys
input=sys.stdin.readline

def func():
    name={"NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy"}
    school=input().rstrip()
    return name[school]

print(func())