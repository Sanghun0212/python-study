# ## 복습
# #1. 
# name = input("이름을 입력하시오: ")
# print(f"Hello, {name}! Welcome to robot world.")

# #2.
# speeds = [0.3, 0.5, 0.8]

# print(f"Speed: {speeds[0]} m/s")
# print(f"Speed: {speeds[1]} m/s")
# print(f"Speed: {speeds[2]} m/s")

# #3.
# battery = 40
# if battery < 20:
#     print("Critical battery")
# elif 20 < battery < 50:
#     print("Battery Low")
# elif battery >= 50:
#     print("Battery OK")
# else:
#     print("Need charge immediately")

# #4.   ### 집중 요망

# while True:
#     cmd = input("Enter command (go/stop): ").lower()
#     if cmd == "go":
#         print("Moving!")
#     elif cmd == "stop":
#         print("Stopped.")
#         break
#     else:
#         print("Invalid Command")


# ## for --> 정해진 횟수 만큼 반복할 때 사용
# # for 변수 in 반복대상:
# #     실행할 코드
# for i in range(5):
#     print(i)

# sensors = [0.4, 0.5, 0.6]
# for distance in sensors:
#     print(f"Sensor: {distance} m")

# robot = {
#     "name" : "TurtleBot",
#     "Speed" : 0.4,
#     "Battery" : 90
#     }
# for key, value in robot.items():
#     print(f"{key}: {value}")

# for i in range(2):
#     for j in range(3):
#         print(i, j)

# ## while --> 조건이 참일 동안 반복항때
# # while 조건:
# #     실행할 코드

# count = 5
# while count > 0:
#     print(count)
#     count -=1
# print("Go!")

# battery = 100
# while battery >0:
#     print(f"battery: {battery}%")
#     battery -= 25
# print("Battery empty!")

# while True:
#     cmd = input("Enter command(go/stop): ").lower()
#     if cmd == "stop":
#         print("Robot Stopped")
#         break
#     print("Robot Moving!")


# ## 5. 함수(Def)
# # def 함수이름(매개변수):
# #     실행할 코드
# #     return 결과값

# def greet():
#     print("Hello, Robot!")

# greet()

# def move(distance):
#     print(f"Robot moved {distance} meters.")

# move(5)

# def drive(direction, speed):
#     print(f"moving {direction} at {speed} m/s")

# drive("backward", 0.3)

# def calc_distance(time, speed):
#     distance = time * speed
#     return distance

# result = calc_distance(5, 0.4)
# print(f"Distance: {result} m")

# def check_battery(battery):
#     if battery < 20:
#         print("Critical Battery")
#     elif battery <50:
#         print("battery low!")
#     else:
#         print("battery ok")

# check_battery(70)


# # 연습문제
# #1. 
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Sanghun")

# #2. 
# def calc_distance(speed, time):
#     distance = speed * time
#     return distance

# result = calc_distance(50, 4)
# print(f"The distance is: {result}")

# def battery_check(level):
#     if level < 20:
#         print("Critical battery")
#     elif level < 50:
#         print("Battery low")
#     else:
#         print("Battery OK")


# battery_check(50)

# def execute_command(command):
#     while True:
#         if command == "go":
#             print("Robot Moving")
#         elif command == "stop":
#             print("Robot Stopped")
#             break
#         else:
#             print("Unknown Command")
#     return command


# execute_command("stop")

##추가 문제
#1
def adjust_speed(current, target):
    if current < target:
        print(f"Increasing speed until {target}")
    elif current > target:
        print(f"Decreaing speed until {target}")
    else:
        print("Speed OK")
    

adjust_speed(0.4, 0.6)
# 출력: Increasing speed...

adjust_speed(0.7, 0.5)
# 출력: Decreasing speed...

adjust_speed(0.5, 0.5)
# 출력: Speed OK


#2
def report_status(name, battery, speed):
    print(f"Robot: {name}")
    if battery < 20:
        print(f"Battery: {battery}")
    else:
        print(f"Current Battery is: {battery}")
    
    print(f"speed: {speed} m/s")

    return report_status
    

report_status("TurtleBot", 15, 0.5)



## Return의 기본 역활 --> 함수의 결과를 밖으로 돌려주ㅠ는것