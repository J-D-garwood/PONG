import pyglet
from pyglet import shapes
batch = pyglet.graphics.Batch()
batch_menu = pyglet.graphics.Batch()
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window(640, 427)
keys = key.KeyStateHandler()
window.push_handlers(keys)


# menu screen
standard_mode_button_txt = pyglet.text.Label('Standard',color=(255, 0, 0, 255),
                          font_name='Times New Roman',
                          font_size=20,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

standard_mode_button_square = shapes.Rectangle(x=window.width//2-50, y=window.height//2-20, width=100, height=35, color=(255, 255, 0), batch=batch_menu)

oneVone_mode_button_txt = pyglet.text.Label('1v1',color=(255, 0, 0, 255),
                          font_name='Times New Roman',
                          font_size=20,
                          x=window.width//2, y=window.height//2-50,
                          anchor_x='center', anchor_y='center')

oneVone_mode_button_square = shapes.Rectangle(x=window.width//2-50, y=window.height//2-70, width=100, height=35, color=(255, 255, 0), batch=batch_menu)

def render_menu_screen():
    standard_mode_button_square.draw()
    standard_mode_button_txt.draw()
    oneVone_mode_button_square.draw()
    oneVone_mode_button_txt.draw()
    return

# Player variables
player_x = 310
player_y = 10

# AI variables
ai_x = 310
ai_y = 407
target_x = 310

# Ball variables
ball_x_speed = 3
ball_y_speed = 3
Ball_init = False
direction_change = False


# general game variables
GameOn = False


ball_image = pyglet.image.load("resources/updated_ball_image.png")
ball = pyglet.sprite.Sprite(ball_image, x=0, y=0)
player = shapes.Rectangle(player_x, player_y, 70, 10, color=(255, 255, 255), batch=batch)
ai = shapes.Rectangle(ai_x, ai_y, 70, 10, color=(255, 255, 255), batch=batch)
image = pyglet.resource.image('resources/menu_wallpaper.jpg')

def calc_ideal_location():
    global ball_x_speed
    global ball_y_speed
    if ball_y_speed<0:
        return 310
    else:
        rolling_x = ball.x
        rolling_y = ball.y
        while (rolling_x<640 and rolling_x>0 and rolling_y<427 and rolling_y>0):
            rolling_x+=ball_x_speed
            rolling_y+=ball_x_speed
        return rolling_x

def move_ai():
    global ball_x_speed
    global ball_y_speed
    global target_x
    target_x = calc_ideal_location()
    if (ai.x<target_x-35):
        ai.x+=3
    else:
        ai.x-=3
    return

def move_ball(p1_x, p1_y, ai_x, ai_y):
    global Ball_init
    global ball_x_speed
    global ball_y_speed
    global direction_change
    if Ball_init:
        if (ball.x>625 or ball.x<0 or ball.y>412 or ball.y<0) and direction_change == False:
            if (ball.x>625 or ball.x<0):
                ball_x_speed *= -1
                ball.x += ball_x_speed
                ball.y += ball_y_speed
            else:
                ball_y_speed *= -1
                ball.x += ball_x_speed
                ball.y += ball_y_speed
        elif (ball.x>p1_x and ball.x<(p1_x+70) and ball.y>(p1_y+10) and ball.y<(p1_y+15)):
            ball_y_speed *= -1
            ball.x += ball_x_speed
            ball.y += ball_y_speed
        elif (ball.x>ai_x and ball.x<(ai_x+70) and ball.y>(ai_y-5) and ball.y<(ai_y)):
            ball_y_speed *= -1
            ball.x += ball_x_speed
            ball.y += ball_y_speed
        else:
            direction_change = False
            ball.x += ball_x_speed
            ball.y += ball_y_speed
    else:
        Ball_init = True
        ball.x = 20
        ball.y = 20
    ball.draw()
    return True

@window.event
def on_draw():
    window.clear()
    if GameOn:
        move_ball(player.x, player.y, ai.x, ai.y)
        batch.draw()
        move_ai()
    else:
        image.blit(0, 0)
        render_menu_screen()

@window.event 
def on_key_press(symbol, modifiers):
    if GameOn:
        if (symbol==key.LEFT):
            player.x -= 35
        elif (symbol==key.RIGHT):
            player.x += 35
        return
    else:
        return
    
@window.event 
def on_mouse_press(x, y, button, modifiers):
    global GameOn
    if GameOn:
        return
    else:
        if (x>window.width//2-50 and x<window.width//2+50 and y<window.height//2-70 and y>window.height//2-35):
            GameOn = True 
        return

pyglet.app.run()
