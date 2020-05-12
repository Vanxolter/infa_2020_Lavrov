from graph import *

#лицо
penColor(0, 0, 0)
brushColor("yellow")
circle(250, 250, 200)

#левый глаз
penColor(0, 0, 0)
brushColor("red")
circle(150, 200, 50)

#правый глаз
penColor(0, 0, 0)
brushColor("red")
circle(350, 200, 30)

#левый зрачек
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(150, 200, 15)

#правый зрачек
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(350, 200, 15)

#mouth ( РОТ )
penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(150, 350, 350, 370)

#левая бровь
penSize(20)
penColor(0, 0, 0)
line(100, 100, 220, 173)

#правая бровь
penSize(20)
penColor(0, 0, 0)
line(400, 130, 300, 180)

run()