from graphics import *

win = GraphWin('Shapes')

### Draw a red circle centered at point (100, 100)
### with radius 30
center = Point(300, 300)
circ = Circle(center, 90)
circ.setFill('red')
circ.draw(win)

### Put a textual label in center of circle
label = Text(center, "Red Circle")
label.draw(win)

### Draw a square using Rectangle object
rect = Rectangle(Point(90, 90), Point(210, 210))
rect.draw(win)

### Draw a line segment using a Line object
line = Line(Point(60, 90), Point(540, 495))
line.draw(win)

### Draw an oval using the Oval object
oval = Oval(Point(60, 450), Point(540, 597))
oval.draw(win)
win.getMouse()
