n = int(input())
logs = []

for _ in range(n):
    name, action = input().split()
    logs.append((name, action))

# 현재 회사에 있는 사람들을 추적하기 위한 집합(set) 생성
current_employees = set()

for log in logs:
    name, action = log
    if action == "enter":
        current_employees.add(name)
    else:
        current_employees.remove(name)

# 결과 출력
sorted_employees = sorted(current_employees, reverse=True)
for employee in sorted_employees:
    print(employee)