import push2_python
import random
import numpy
from PIL import Image
import time

# Init Push2
push = push2_python.Push2(run_simulator=True)
print(dir(push))


# Define util function to generate a frame with some colors to be shown in the display
# Frames are created as matrices of shape 960x160 and with colors defined in bgr565 format
# This function is defined in a rather silly way, could probably be optimized a lot ;)
def generate_3_color_frame():
    colors = ['{b:05b}{g:06b}{r:05b}'.format(
        r=int(31*random.random()), g=int(63*random.random()), b=int(31*random.random())),
        '{b:05b}{g:06b}{r:05b}'.format(
        r=int(31*random.random()), g=int(63*random.random()), b=int(31*random.random())),
        '{b:05b}{g:06b}{r:05b}'.format(
        r=int(31*random.random()), g=int(63*random.random()), b=int(31*random.random()))]
    colors = [int(c, 2) for c in colors]
    line_bytes = []
    for i in range(0, 960):  # 960 pixels per line
        if i <= 960 // 3:
            line_bytes.append(colors[0])
        elif 960 // 3 < i <= 2 * 960 // 3:
            line_bytes.append(colors[1])
        else:
            line_bytes.append(colors[2])
    frame = []
    for i in range(0, 160):  # 160 lines
        frame.append(line_bytes)
    return numpy.array(frame, dtype=numpy.uint16).transpose()

# Pre-generate different color frames
color_frames = list()
for i in range(0, 20):
    color_frames.append(generate_3_color_frame())

# Now crate an extra frame which loads an image from a file. Image must be 960x160 pixels.
img = Image.open('test.png')#_img_960x160.png')
frame = numpy.array(img)
frame = frame/255  # Convert rgb values to [0.0, 1.0] floats

# Now lets configure some action handlers which will display frames in Push2's display in 
# reaction to pad and button presses
@push2_python.on_pad_pressed()
def on_pad_pressed(push, pad_n, pad_ij, velocity):
    print("pad PRESSED")
    # Display one of the three color frames on the display
    random_frame = random.choice(color_frames)
    push.display.display_frame(random_frame)

@push2_python.on_button_pressed()
def on_button_pressed(push, button_name):
    print("button PRESSED")
    # Display the frame with the loaded image
    push.display.display_frame(frame, input_format=push2_python.constants.FRAME_FORMAT_RGB)

@push2_python.on_button_pressed(push2_python.constants.BUTTON_PLAY)
def on_play_pressed(push):
    print('Play!')

@push2_python.on_button_pressed('play')
def on_play_pressed(push):
    print('Play!')

@push2_python.on_button_pressed('85')
def on_play_pressed(push):
    print('Play!')
# Start infinite loop so the app keeps running
print('App runnnig...')
colors = ['black','orange','yellow','turquoise','dark_gray','purple','pink','light_gray','white','light_gray','dark_gray','blue', 'green','red', 'white']

colors2 = ["white","green"]
import numpy
#push.display.display_frame(numpy.array(img,dtype=numpy.uint16), input_format=push2_python.constants.FRAME_FORMAT_RGB)

@push2_python.on_touchstrip()
def on_touchstrip(push, value):
    print("ASD")
    print('Touchstrip touched with value', value)


color = "green"
print(   dir(push.buttons))
while True:
    push.buttons.set_all_buttons_color("white")
    for i in range(0,8):
        for j in range(0,8):
            pad_ij = (i, j)  # Fourth pad of the top row
            color = random.choice(colors)
            #print(pad_ij)
            #print(color)
            #print("\n")
            push.pads.set_pad_color(pad_ij,color=color)
            time.sleep(.1)
    
