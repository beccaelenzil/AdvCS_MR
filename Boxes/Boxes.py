from visual import *

myBox = box(color = (1.0, 0.0, 0.0))
while True:
    # Slow down the animation to 60 frames per second.
    # Change the value to see the effect!
    rate(60)
    myBox.rotate(angle=pi/100)

# complete the exercise that includes multiple boxes