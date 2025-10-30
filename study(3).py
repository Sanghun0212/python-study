# ## Review
# #1
# name = "Turtlebot"
# v = "0.4"  # 숫자를 쓸때에는 " " 생략하기
# battery = "90"
# print(f"Robot {name} is moving at {v}m/s with battery {90}%") # print(f "  {넣을 문자 및 숫자} ")

# #2
# r = 0.05 
# pi = 3.14159
# circumference = r * pi 
# print(f" Wheel circumference: {circumference}")

# #3
# distance = [0.3, 0.5, 0.4]
# distance.append(0.6)  ##추가는 .append()
# distance[1] = 0.45
# print(distance)

# #4
# robot = {
#     "name": "MiniBot",
#     "speed": 1.0
# }
# robot["Battery"] = 80  ## 닥셔너리 조작에서 뒤에 추가 할때 robot[" "] = $$ 하면 자동으로 추가가 됨
# robot["speed"] = 1.2
# print(robot)

# #5
# robots = [
#     {"name": "A", "speed": "0.4"},
#     {"name": "B", "speed": "0.6"}
# ]
# robots[1]["speed"] = 0.8
# robots[0]["name"] = "Alpha"
# print(robots)

# #6
# user_name = input("이름을 입력하시오")
# print(f"Hello, {user_name}! Welcome to the robot world!")

##조건문 (if, elif, else)
#“배터리가 부족하면 충전하러 가고, 충분하면 움직인다.”
#if 조건:
#   실행할 코드
#elif 다른 조건:
#   다른 코드
#else: 
#   나머지 경우 코드

#  if

# battery = int(input("put your battery left"))  #이경우에는 input 만 쓸 경우 파이썬이 인식하지 못한다 
#                                                #따라서 int() 나 float()를 써서 사용해야함

# if battery < 50:
#     print("\u26A0 Battery low! Going to charge.")

# else:
#     print("Battery OK! Keep moving.")

## if + elif + else
# speed = float(input("속도를 입력하시오")) ##int() --> 정수 (개수 or 카운트 등)
#                                         ##float() --> 실수 (속도, 거리, 시간 등)

# if speed == 0:
#     print("Robot stopped")

# elif speed < 0.5:
#     print(":Robot moving slowly.")

# else:
#     print("Robot moving fast!")

# # 예제 4.

# battery = 80
# obstacle = False

# if battery >50 and not obstacle:
#     print(" move forward ")

# # 중첩 조건문 

# battery = 70
# obstacle = True

# if battery > 50:
#     if obstacle:
#         print("Stop - obstavle ahead")
#     else:
#         print("Move Forwards")
# else:
#     print("Low battery")

## 연습문제
#1.
battery = 30

if battery < 50:
    print("Battery Low!")

else: 
    print("Battery OK")

#2. 
speed = 0.7
if speed == 0:
    print("Robot Stopped")
elif 0 < speed <= 0.5:
    print("Moving Slowly")
else:
    print("Moving fast!")

#3.
battery = 70
obstacle = True

if battery > 50 and not obstacle:
    print("Move Forward")
elif obstacle:
    print("Robot Stopped")
elif battery < 50:
    print("Charge Battery!")

#4.
command = input("Enter command (Go/Stop): ") # 여기에 .lower()만 추가 하면 대소문자 구분 필요없음
if command == "Go":             ## 그냥 "Go" 만 쓰는 것이 아니라 command == "Go" 라고 해야함 
    print("Robot Moving")
elif command == "Stop":
    print("Robot stopped")
else:
    print("Unknown command")
