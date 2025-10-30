# ## 4. 반복문(loops)
# # For 반복문
# # for 변수 in 반복대상:
# #       실행할코드

# #예제1.
# for i in range(5):
#     print("Moving forward!", i)

# #예제2.
# sensors = [0.4, 0.6, 0.5]
# for distance in sensors:
#     print(f"Sensor reads {distance} m")

# #예제3.
# robot = {
#     "name": "TurtleeBot",
#     "speed": 0.4,
#     "battery": 80
#     }

# for key, value in robot.items():  ## .items()는 키하고 값 쌍으로 꺼내옴
#     print(f"{key}: {value}")

# # While 반목문
# # while 조건:
# #    실행할 코드

# #예제4.
# battery = 100

# while battery > 0 :
#     print(f"Battery: {battery}%")
#     battery -= 20 # 20씩 감소
# print("Battery empty!")

# #예제5.

# while True:
#     command = input("enter command (go/stop): ").lower()

#     if command == "go":
#         print("Robot Moving")
#     elif command == "stop":
#         print("Robot Stopped")
#         break     # 반복 종료
#     else:
#         print("unknown command")

## 연습 문제
#1. 
for i in range(5):                  ##range(1,6)을 사용하여도 됨
    print(i+1)

#2.
sensors = [0.4, 0.5, 0.6]
for distance in sensors:
    print("Sensor reading:", distance)   # print(f"Sensor reading: {distance}")

#3.
battery = 100
while battery > 0:
    print("Battery:", battery, "%")
    battery -= 20

print("Battery empty!")

#4.
while True:
    command = input("Please put stop/go:").lower()

    if command == "go":
        print("Robot moving!")
    elif command  == "stop":
        print("Robot Stopped")
        break
    else:
        print("Wrong Input")

