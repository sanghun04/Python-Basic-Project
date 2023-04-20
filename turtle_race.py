import turtle
import random

# 거북이 생성
t1 = turtle.Turtle() 
t2 = turtle.Turtle()  

# 거북이 색상 설정
t1.color("blue")  
t2.color("red") 

# 거북이 모양 설정
t1.shape("turtle")  
t2.shape("turtle") 

# 거북이 시작 위치 설정
t1.penup() 
t1.goto(0, 200) 
t1.pendown() 

t2.penup()  
t2.goto(0, -200) 
t2.pendown()  

# 승부 예측 입력
prediction = "" 
while prediction not in ["파랑", "빨강"]: 
    prediction = turtle.textinput("경주 게임", "파랑 or 빨강")  

# 경주 시작
while t1.xcor() < 300 or t2.xcor() < 300:  
    t1.forward(random.randint(1, 10)) 
    t2.forward(random.randint(1, 10))  
    print(f"t1: {int(t1.xcor())} vs t2: {int(t2.xcor())}") 

# 승자 확인
if t1.xcor() > t2.xcor(): 
    winner = "파랑" 
else: 
    winner = "빨강" 

# 결과 출력
if prediction == winner: 
    print("끝")
else: 
    print("끝") 

# 결과 표시
if winner == "파랑":  
    t1.write("승리", font=("맑은 고딕", 30)) 
else:  
    t2.write("승리", font=("맑은 고딕", 30))

turtle.penup() 
turtle.goto(0, 0)  
if prediction == winner:  
    turtle.write("예측 성공")  
else:  
    turtle.write("예측 실패")  

turtle.exitonclick() 