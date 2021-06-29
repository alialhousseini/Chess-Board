import turtle

# Settings
turtle.setup(600, 600)
screen = turtle.Screen()
screen.title('Turtle Chess')
turtle.register_shape('WK.gif')
turtle.register_shape('WQ.gif')
turtle.register_shape('BK.gif')
turtle.register_shape('BQ.gif')
turtle.register_shape('WB.gif')
turtle.register_shape('BB.gif')
turtle.register_shape('WKn.gif')
turtle.register_shape('BKn.gif')
turtle.register_shape('WR.gif')
turtle.register_shape('BR.gif')
turtle.register_shape('WP.gif')
turtle.register_shape('BP.gif')

pen = turtle.Turtle()
def draw():
  for _ in range(4):
    pen.forward(50)
    pen.left(90) 
  pen.forward(50)

pen.setpos(0,200)
pen.speed(80)
for i in range(8):
  pen.up()
  pen.setpos(0, 50 * i)
  pen.down()
  for j in range(8):
    if (i + j)% 2 == 0:
      color ='green'
    else:
      color='white'
    pen.fillcolor(color)
    pen.begin_fill()
    draw()
    pen.end_fill()
pen.hideturtle()

# White King
wk = turtle.Turtle()
wk.shape('WK.gif')
wk.penup()
wk.setpos(225,25)
wk.ondrag(wk.goto)

# White Queen
wq = turtle.Turtle()
wq.shape('WQ.gif')
wq.penup()
wq.setpos(175,25)
wq.ondrag(wq.goto)

# White Bishop 1
wb1 = turtle.Turtle()
wb1.shape('WB.gif')
wb1.penup()
wb1.setpos(275,25)
wb1.ondrag(wb1.goto)

# White Bishop 2
wb2 = turtle.Turtle()
wb2.shape('WB.gif')
wb2.penup()
wb2.setpos(125,25)
wb2.ondrag(wb2.goto)

# White Knight 1
wk1 = turtle.Turtle()
wk1.shape('WKn.gif')
wk1.penup()
wk1.setpos(325,25)
wk1.ondrag(wk1.goto)

# White Knight 2
wk2 = turtle.Turtle()
wk2.shape('WKn.gif')
wk2.penup()
wk2.setpos(75,25)
wk2.ondrag(wk2.goto)

# White Rook 1
wr1 = turtle.Turtle()
wr1.shape('WR.gif')
wr1.penup()
wr1.setpos(375,25)
wr1.ondrag(wr1.goto)

# White Rook 2
wr2 = turtle.Turtle()
wr2.shape('WR.gif')
wr2.penup()
wr2.setpos(25,25)
wr2.ondrag(wr2.goto)

# White Pawn 1
wp1 = turtle.Turtle()
wp1.shape('WP.gif')
wp1.penup()
wp1.setpos(225,75)
wp1.ondrag(wp1.goto)

# White Pawn 2
wp2 = turtle.Turtle()
wp2.shape('WP.gif')
wp2.penup()
wp2.setpos(175,75)
wp2.ondrag(wp2.goto)

# White Pawn 3
wp3 = turtle.Turtle()
wp3.shape('WP.gif')
wp3.penup()
wp3.setpos(275,75)
wp3.ondrag(wp3.goto)

# White Pawn 4
wp4 = turtle.Turtle()
wp4.shape('WP.gif')
wp4.penup()
wp4.setpos(125,75)
wp4.ondrag(wp4.goto)

# White Pawn 5
wp5 = turtle.Turtle()
wp5.shape('WP.gif')
wp5.penup()
wp5.setpos(325,75)
wp5.ondrag(wp5.goto)

# White Pawn 6
wp6 = turtle.Turtle()
wp6.shape('WP.gif')
wp6.penup()
wp6.setpos(75,75)
wp6.ondrag(wp6.goto)

# White Pawn 7
wp7 = turtle.Turtle()
wp7.shape('WP.gif')
wp7.penup()
wp7.setpos(375,75)
wp7.ondrag(wp7.goto)

# White Pawn 8
wp8 = turtle.Turtle()
wp8.shape('WP.gif')
wp8.penup()
wp8.setpos(25,75)
wp8.ondrag(wp8.goto)

# Black King
bk = turtle.Turtle()
bk.shape('BK.gif')
bk.penup()
bk.setpos(225,375)
bk.ondrag(bk.goto)

# Black Queen
bq = turtle.Turtle()
bq.shape('BQ.gif')
bq.penup()
bq.setpos(175,375)
bq.ondrag(bq.goto)

# Black Bishop 1
bb1 = turtle.Turtle()
bb1.shape('BB.gif')
bb1.penup()
bb1.setpos(275,375)
bb1.ondrag(bb1.goto)

# Black Bishop 2
bb2 = turtle.Turtle()
bb2.shape('BB.gif')
bb2.penup()
bb2.setpos(125,375)
bb2.ondrag(bb2.goto)

# Black Knight 1
bk1 = turtle.Turtle()
bk1.shape('BKn.gif')
bk1.penup()
bk1.setpos(325,375)
bk1.ondrag(bk1.goto)

# Black Knight 2
bk2 = turtle.Turtle()
bk2.shape('BKn.gif')
bk2.penup()
bk2.setpos(75,375)
bk2.ondrag(bk2.goto)

# Black Rook 1
br1 = turtle.Turtle()
br1.shape('BR.gif')
br1.penup()
br1.setpos(375,375)
bk1.ondrag(bk1.goto)

# Black Rook 2
br2 = turtle.Turtle()
br2.shape('BR.gif')
br2.penup()
br2.setpos(25,375)
br2.ondrag(br2.goto)

# Black Pawn 1
bp1 = turtle.Turtle()
bp1.shape('BP.gif')
bp1.penup()
bp1.setpos(225,325)
bp1.ondrag(bp1.goto)

# Black Pawn 2
bp2 = turtle.Turtle()
bp2.shape('BP.gif')
bp2.penup()
bp2.setpos(175,325)
bp2.ondrag(bp2.goto)

# Black Pawn 3
bp3 = turtle.Turtle()
bp3.shape('BP.gif')
bp3.penup()
bp3.setpos(275,325)
bp3.ondrag(bp3.goto)

# Black Pawn 4
bp4 = turtle.Turtle()
bp4.shape('BP.gif')
bp4.penup()
bp4.setpos(125,325)
bp4.ondrag(bp4.goto)

# Black Pawn 5
bp5 = turtle.Turtle()
bp5.shape('BP.gif')
bp5.penup()
bp5.setpos(325,325)
bp5.ondrag(bp5.goto)

# Black Pawn 6
bp6 = turtle.Turtle()
bp6.shape('BP.gif')
bp6.penup()
bp6.setpos(75,325)
bp6.ondrag(bp6.goto)

# Black Pawn 7
bp7 = turtle.Turtle()
bp7.shape('BP.gif')
bp7.penup()
bp7.setpos(375,325)
bp7.ondrag(bp7.goto)

# Black Pawn 8
bp8 = turtle.Turtle()
bp8.shape('BP.gif')
bp8.penup()
bp8.setpos(25,325)
bp8.ondrag(bp8.goto)

turtle.done()