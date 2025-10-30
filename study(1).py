# 10/11/2025

print("Hello, robot!")
# print()는 출력명령

#variable
speed = 3.5
direction = "left"
is_moving = "True"

print(speed, direction, is_moving)
# variable은 알파벳, 숫자, _ 로 가능 (숫자로 시작은 불가능)

# 기본 연산자
a = 7
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 몫
print(a % b)  # 나머지
print(a ** b) # 거듭제곱

#문자열
name = "TurtleBot"
print("Hello" + name)
print(f"Hello {name}") # f-spring 추천
print(name.upper()) # 대문자 
print(len(name))  # 문자열 길이

user_name = input("이름을 입력하세요: ")
print(f"안녕, {user_name}!")   # 숫자로 쓰려면 int() or float() 사용

## 연습문제
# 1. 로봇 인사기
robot_name = "TurtleBot"
print(f"Hello, {robot_name}")

#2. 원 둘레 계산기
r = 0.05 # 바퀴 반지름
pi = 3.14159 # 원주율
둘레 = 2 * pi * r
# circumference  로 바꾸기 (한글은 복잡한 프로젝트에 도움 x)


#3. 속도 변환기
v_mps = 0.4
v_kmph = v_mps * 3.6
print(f" speed: {v_kmph} km/h")
# 마지막에 출력문 한번씩 써보기


#4. 문자열 조작
cmd = "go_forward"
cmd_clean = cmd.strip().upper() # .strip() 은 공백 없애기 .upper() 은 대문자로 변환
print(cmd_clean)

