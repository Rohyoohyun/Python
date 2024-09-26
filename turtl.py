import turtle as t

def draw_polygon(length, n):
    t.shape('turtle')
    t.color('red', 'yellow')
    t.begin_fill()
    for i in range(n):
        t.forward(length)
        t.left(360/n)
    t.end_fill()
    t.exitonclick()  # 프로그램이 마우스 클릭 후 종료

draw_polygon(100, 5)
