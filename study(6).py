# ##복습
# #1
# def greet(name):
#     print(f"Hello, {name}!")

# name = input("Enter your name: ")
# greet(name)



# #2
# def calc_distance(speed, time):
#     distance = speed * time
#     print(f"The distance is {distance} m")
#     return distance

# calc_distance(3, 4)

# #3
# def battery_check(level):
#     if level >= 50:
#         print("OK")
#     elif 20 <= level <50:
#         print("Low Battery")
#     else:
#         print("Critically Low!")

# battery_check (10)

# #4
# while True:
#     cmd = input("Please write down go/stop: ").lower()
#     if cmd == "go":
#         print("Moving!")
#     elif cmd == "stop":
#         print("Stop!")
#         break
#     else:
#         print("Please write only stop/go")

# #5-1
# def report(name, battery, speed):
#     print(f"Robot: {name}")
#     print(f"Battery: {battery}%")
#     print(f"Speed: {speed} m/s")
#     if battery < 20:
#         print("Need Charging!")
#     else:
#         print("Need Charging!")

# report("TurtleBot", 80, 0.5)

# #5-2
# def report(name, battery, speed):
#     info = f"""
# Robot: {name}
# Battery: {battery}%
# Speed: {Speed} m/s
# """
#     print(info.strip())
#     if battery < 20:
#         print("Need charge")
#     else:
#         print("Status Normal")

# #5-3
# def report(name, battery, speed):
#     info = {
#         "Robot": name,
#         "Battery": f"{battery}%"
#         "Speed": f"{speed} m/s"
#     }
#     for key, value in info.items():
#         print(f"{key}: {value}")

#     print(" Need Charging!" if battery < 20 else "Status Normal")


# ## Lesson 6
# # 파일 입출력
# #1.열기(open)
# #2.읽기/쓰기(read/write)
# #3.닫기(close)


# #1  파일 쓰기
# file = open("robot_log.txt", "w") # "w" = write (새로쓰기)

# file.write("Robot initialized.\n")
# file.write("Speed: 0.5 m/s \n")
# file.write("Battery: 80% \n")

# file.close()

# #2 파일 읽기
# file = open("robot_log.txt", "r")
# content = file.read()
# print(content)
# file.close()

# # 자동 닫기
# with open("robot_log.txt", "a") as file: # "a" append (추가)
#     file.write("Task completed.\n")

# # with 는 file.close()가 자동

# def log_status(name, speed, battery):
#     with open("robot_log.txt", "a") as file:
#         file.write(f"Robot: {name}, Speed: {speed}, Battery: {battery}% \n")

# log_status("TurtleBot", 0.5, 80)


# # 입력 오류 방지

# try:
#     value = int(input("Enter a number: "))
#     print("You entered:", value)

# except:
#     print("Invalid input! Please enter a numer")



# try:
#     file = open("robot_log.txt", "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print(" File not found")
#     with open("robot_log.txt", "w") as file:
#         file.write("New log created.\n")

# try:
#     f = open("robot_log.txt", "r")
#     print("File opened.")
# except:
#     print("⚠️ Error while opening.")
# finally:
#     print("Process finished.")

file = open("log.txt", "w")

file.write("Robot Started!")

file.close()

file = open("log.txt","r")

content = file.read()

print(content)

file.close()

with open("log.txt", "a") as file:
     file.write("Speed updated: 0.4m/s")


try:
     file = open("log.txt", "r")
     print(file.read())
     file.close
