Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> def drawSnake(rad, angle, len, neckrad):
	for I in range(len):
		turtle.circle(rad, angle)
		turtle.circle(-rad, angle)
	turtle.circle(rad, angle/2)
	turtle.fd(rad)
	turtle.ciecle(neckrad+1, 180)
	turtle.fd(rad*2/3)

	
>>> def main():
	turtle.setup(1300, 800, 0, 0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor("blue")
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)

	
>>> main()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    main()
  File "<pyshell#18>", line 7, in main
    drawSnake(40,80,5,pythonsize/2)
  File "<pyshell#9>", line 7, in drawSnake
    turtle.ciecle(neckrad+1, 180)
AttributeError: module 'turtle' has no attribute 'ciecle'
>>> 
>>> main()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    main()
  File "<pyshell#18>", line 2, in main
    turtle.setup(1300, 800, 0, 0)
  File "<string>", line 5, in setup
turtle.Terminator
>>> main()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    main()
  File "<pyshell#18>", line 7, in main
    drawSnake(40,80,5,pythonsize/2)
  File "<pyshell#9>", line 7, in drawSnake
    turtle.ciecle(neckrad+1, 180)
AttributeError: module 'turtle' has no attribute 'ciecle'
>>> 
