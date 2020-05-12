from graph import *

#стена
penColor(85, 68, 0)
brushColor(85, 68, 0)
rectangle(0, 0, 500, 280)

#окно
penColor(213, 255, 230)
brushColor(213, 255, 230)
rectangle(290, 10, 490, 260)

#стекло1
penColor(135, 205, 222)
brushColor(135, 205, 222)
rectangle(295, 15, 390, 80)

#стекло2
penColor(135, 205, 222)
brushColor(135, 205, 222)
rectangle(400, 15, 480, 80)

#стекло3
penColor(135, 205, 222)
brushColor(135, 205, 222)
rectangle(295, 90, 390, 250)

#стекло4
penColor(135, 205, 222)
brushColor(135, 205, 222)
rectangle(400, 90, 480, 250)

#пол
penColor(128, 102, 0)
brushColor(128, 102, 0)
rectangle(0, 280, 500, 1000)

#клубок (круг)
penColor(0, 0, 0)
brushColor(153, 153, 153)
circle(290, 530, 50)

#Кот хвост
penColor(0, 0, 0)
brushColor(200, 113, 55)
oval(380, 340, 420, 490)

#Кот тело
penColor(0, 0, 0)
brushColor(200, 113, 55)
oval(100, 290, 400, 430)

#Кот правая лапа
penColor(0, 0, 0)
brushColor(200, 113, 55)
oval(70, 350, 110, 430)

#Кот правая лапа
penColor(0, 0, 0)
brushColor(200, 113, 55)
oval(115, 400, 195, 440)

#кот зад лапа 1
penColor(0, 0, 0)
brushColor(200, 113, 55)
circle(320, 400, 45)

#Кот зад лапа 2
penColor(0, 0, 0)
brushColor(200, 113, 55)
oval(330, 410, 365, 490)

#кот голова
penColor(0, 0, 0)
brushColor(200, 113, 55)
circle(140, 350, 60)

#кот л глаз
penColor(0, 0, 0)
brushColor(136, 170, 0)
circle(115, 350, 15)

#кот л зрачек 
penColor(0, 0, 0)
brushColor(0, 0, 0)
oval(113, 335, 118, 365)

#кот п глаз
penColor(0, 0, 0)
brushColor(136, 170, 0)
circle(165, 350, 15)

#кот 5 зрачек 
penColor(0, 0, 0)
brushColor(0, 0, 0)
oval(165, 335, 170, 365)

#носяра
penColor(0, 0, 0)
brushColor(255, 204, 170)
polygon([(135, 365), (145, 365), (140, 370)])

#носяра 2
penColor(0, 0, 0)
line(140, 370, 140, 383)

#рот л
arc(140, 370, 137, 371, start = 0, end = 20, )

run()