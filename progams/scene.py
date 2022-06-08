# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
   
    # draw_grid(canvas, scene_width, scene_height, 20)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width = 0, fill = 'deepSkyBlue')
    
    x1, y1, x_end, y_end = 60, 300, 300, 420
    draw_cloud(canvas, x1, y1, x_end, y_end)

    x1, y1, x_end, y_end = 120, 340, 340, 480
    draw_cloud(canvas, x1, y1, x_end, y_end)


    x1, y1, x_end, y_end = 520, 400, 680, 480
    draw_cloud(canvas, x1, y1, x_end, y_end)
     


def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill='burlywood')

    x0, y0, x1, y1, x2, y2 = 260, 0, 560, 0, 420, 165
    draw_road(canvas, x0, y0, x1, y1, x2, y2)

    x0, y0, x1, y1 = 420, 0, 420, 60
    paint_road(canvas, x0, y0, x1, y1) 

    x0, y0, x1, y1 = 420, 80, 420, 120
    paint_road(canvas, x0, y0, x1, y1)

    x0, y0, x1, y1 = 420, 140, 420, 155
    paint_road(canvas, x0, y0, x1, y1)

    x0, y0, x1, y1 = 620, 20, 760, 140 
    draw_house(canvas, x0, y0, x1, y1)

    x0, y0, x1, y1, x2, y2 = 620, 140, 760, 140, 690, 200
    draw_roof(canvas, x0, y0, x1, y1, x2, y2)

    x0, y0, x1, y1 = 680, 20, 720, 80
    draw_door(canvas, x0, y0, x1, y1)


# def draw_grid(canvas, scene_width, scene_height, interval, color='white'):
#     x_label = 20
#     for x in range(interval, scene_width, interval):
#         draw_line(canvas, x, 0, x, scene_height, fill=color)
#         draw_text(canvas, x, x_label, f'{x}', fill=color)

#     y_label = 20
#     for y in range(interval, scene_width, interval):
#         draw_line(canvas, 0, y, scene_width, y, fill=color)
#         draw_text(canvas, y_label, y, f'{y}', fill=color)


def draw_cloud(canvas, x1, y1, x_end, y_end):
    draw_oval(canvas, x1, y1, x_end, y_end, outline='seashell', width=1, fill='snow1')

def draw_road(canvas, x0, y0, x1, y1, x2, y2):
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, outline='black', width=1, fill='gray5')
    
def paint_road(canvas, x0, y0, x1, y1):
    draw_line(canvas, x0, y0, x1, y1, width=5, fill='yellow1')

def draw_house(canvas, x0, y0, x1, y1):
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="black", fill="steelBlue4")

def draw_roof(canvas, x0, y0, x1, y1, x2, y2):
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, outline='gray52', width=1, fill='gray52')

def draw_door(canvas, x0, y0, x1, y1):
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="cornsilk4", fill="cornsilk4")

# Call the main function so that
# this program will start executing.
main()