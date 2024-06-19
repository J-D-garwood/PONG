import pyglet
from pyglet import shapes
batch = pyglet.graphics.Batch()
batch_menu = pyglet.graphics.Batch()
batch_2 = pyglet.graphics.Batch()
batch_line = pyglet.graphics.Batch()
from pyglet.window import key
from pyglet.window import mouse
from pyglet import font
font.add_file('resources/Pixellettersfull-BnJ5.ttf')
from Player import Player
from pongtitle import letter_patterns, DRAW_TIT

window = pyglet.window.Window(640, 427)
keys = key.KeyStateHandler()
window.push_handlers(keys)

# menu screen
standard_mode_button_txt = pyglet.text.Label('Standard',color=(255, 0, 0, 255),
                          font_name='Times New Roman',
                          font_size=15,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

standard_mode_button_square = shapes.Rectangle(x=window.width//2-50, y=window.height//2-20, width=100, height=35, color=(255, 255, 0), batch=batch_menu)

oneVone_mode_button_txt = pyglet.text.Label('1v1',color=(255, 0, 0, 255),
                          font_name='Times New Roman',
                          font_size=15,
                          x=window.width//2, y=window.height//2-50,
                          anchor_x='center', anchor_y='center')

oneVone_mode_button_square = shapes.Rectangle(x=window.width//2-50, y=window.height//2-70, width=100, height=35, color=(255, 255, 0), batch=batch_menu)

p1_wins_text = pyglet.text.Label('Player 1 wins!!',
                          font_name='Times New Roman',
                          font_size=50,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

p2_wins_text = pyglet.text.Label('Player 2 wins!!',
                          font_name='Times New Roman',
                          font_size=50,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

you_win_text = pyglet.text.Label('You win!!',
                          font_name='Times New Roman',
                          font_size=50,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

you_lost_text = pyglet.text.Label('You lost :(',
                          font_name='Times New Roman',
                          font_size=50,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

def check_scores(player1, player2):
    global GameOn
    global standard
    global oneVone
    if (player1.score==1):
        if(standard):
            you_win_text.draw()
        elif(oneVone):
            p1_wins_text.draw()
        return True
    elif (player2.score==1):
        if(standard):
            you_lost_text.draw()
        elif(oneVone):
            p2_wins_text.draw()
        return True
    else:
        return False


def render_menu_screen():
    standard_mode_button_square.draw()
    standard_mode_button_txt.draw()
    oneVone_mode_button_square.draw()
    oneVone_mode_button_txt.draw()
    return

def render_halfway_line():
    for i in range(100):
        dot = shapes.Rectangle(x=i*10, y=window.height//2, width=3, height=1, color=(255, 255, 255), batch=batch_line)
        batch_line.draw()
    

Game_Over_image = pyglet.image.load("resources/GAME_OVER.jpg")
Game_Over = pyglet.sprite.Sprite(Game_Over_image, x=140, y=30)

You_Win_image = pyglet.image.load("resources/YOU_WIN.jpeg")
You_Win = pyglet.sprite.Sprite(You_Win_image, x=-10, y=-100)

def render_scores(player1, player2):
    p1_score = pyglet.text.Label(str(player2.score),
                          font_name='Times New Roman',
                          font_size=20,
                          x=window.width//2, y=(window.height//2)+50,
                          anchor_x='center', anchor_y='center')
    p2_score = pyglet.text.Label(str(player1.score),
                          font_name='Times New Roman',
                          font_size=20,
                          x=window.width//2, y=(window.height//2)-50,
                          anchor_x='center', anchor_y='center')
    p1_score.draw()
    p2_score.draw()
    return

def render_GAME_OVER():
    Game_Over.draw()

def render_YOU_WIN():
    You_Win.draw()

# Player variables
player_x = 310
player_y = 10

# AI variables
ai_x = 310
ai_y = 407
target_x = 310

# Ball variables
ball_x_speed = 8
ball_y_speed = 8
Ball_init = False
direction_change = False


# general game variables
GameOn = False
standard = False
oneVone = False
GameOnCount = 0
option2Reset = False
player1 = Player()
player2 = Player()


ball_image = pyglet.image.load("resources/updated_ball_image.png")
ball = pyglet.sprite.Sprite(ball_image, x=0, y=0)

player = shapes.Rectangle(player_x, player_y, 70, 10, color=(255, 255, 255), batch=batch)
player1Rect = shapes.Rectangle(player_x, player_y, 70, 10, color=(0, 0, 255), batch=batch_2)
player2Rect = shapes.Rectangle(ai_x, ai_y, 70, 10, color=(255, 0, 0), batch=batch_2)
ai = shapes.Rectangle(ai_x, ai_y, 70, 10, color=(255, 255, 255), batch=batch)
image = pyglet.resource.image('resources/menu_wallpaper.jpg')


def calc_ideal_location():
    global ball_x_speed
    global ball_y_speed
    if (ball_y_speed==-8):
        return 310
    else:
        rolling_x = ball.x
        rolling_y = ball.y
        while (rolling_y<427):
            rolling_x+=ball_x_speed
            rolling_y+=8
        return rolling_x

def wall_rebound_location(old_target):
    global ball_x_speed
    global ball_y_speed
    im_x = old_target
    rolling_y = 427
    while (im_x>640 or im_x<0):
        im_x-=ball_x_speed
        rolling_y-=8
    while(rolling_y<427):
        im_x+=ball_x_speed
        rolling_y+=8
    return im_x

def move_ai():
    global ball_x_speed
    global ball_y_speed
    global target_x
    global change
    global change_count
    target_x = calc_ideal_location()
    if (target_x>640 or target_x<0):
        target_x_2 = wall_rebound_location(target_x)
        if (ai.x<target_x-29 and ai.x>target_x-36):
            return
        if (ai.x<target_x_2-35):
            if (ai.x<550):
                ai.x+=6
        elif (ai.x>target_x_2-35):
            if (ai.x>10):
                ai.x-=6
    else:
        if (ai.x<target_x-29 and ai.x>target_x-36):
            return
        if (ai.x<target_x-35):
            if (ai.x<550):
                ai.x+=6
        elif (ai.x>target_x-35):
            if (ai.x>10):
                ai.x-=6
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
                if(ball.y<0):
                    player2.add_to_score()
                    ball.x = 300
                    ball.y = 300
                    ball_y_speed *= -1
                    return
                else: 
                    player1.add_to_score()
                    ball.x = 300
                    ball.y = 100
                    ball_y_speed *= -1
                    return

        elif (ball.x>p1_x-10 and ball.x<(p1_x+80) and ball.y>(p1_y+8) and ball.y<(p1_y+14)):
            ball_y_speed *= -1
            ball.x += ball_x_speed
            ball.y += ball_y_speed
        elif (ball.x>ai_x-10 and ball.x<(ai_x+80) and ball.y>(ai_y-5) and ball.y<(ai_y+5)):
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
    global option2Reset
    if GameOn and standard:
            check = check_scores(player1, player2)
            if (not check):
                render_halfway_line()
                render_scores(player1, player2)
                move_ball(player.x, player.y, ai.x, ai.y)
                batch.draw()
                move_ai()
            else:
                check_scores(player1, player2)
                option2Reset = True
    elif GameOn and oneVone:
            check = check_scores(player1, player2)
            if (not check):
                render_halfway_line()
                render_scores(player1, player2)
                move_ball(player1Rect.x, player1Rect.y, player2Rect.x, player2Rect.y)
                batch_2.draw()
            else: 
                check_scores(player1, player2)
                option2Reset = True
    else:
        image.blit(0, 0)
        render_menu_screen()
        DRAW_TIT()

@window.event 
def on_key_press(symbol, modifiers):
    global GameOn
    global standard
    global oneVone
    global player1
    global player2
    if (option2Reset):
        if (symbol==key.R):
            GameOn = False
            standard = False
            oneVone = False
            player1.reset2zero()
            player2.reset2zero()
    if GameOn and standard:
        if (symbol==key.LEFT):
            if(player.x>10):
                player.x -= 35
        elif (symbol==key.RIGHT):
            if(player.x<550):
                player.x += 35
        return
    elif GameOn and oneVone:
        if (symbol==key.LEFT):
            if(player.x>10):
                player1Rect.x -= 35
        elif (symbol==key.RIGHT):
            if(player.x<550):
                player1Rect.x += 35
        elif (symbol==key.D):
            if(ai.x<550):
                player2Rect.x += 35
        elif (symbol==key.A):
            if(ai.x>10):
                player2Rect.x -= 35
        return
    
@window.event 
def on_mouse_press(x, y, button, modifiers):
    global GameOn
    global standard
    global oneVone
    if GameOn:
        return
    else:
        if(x>269 and x<371):
            if(y>141 and y<177):
                GameOn = True
                oneVone = True
            elif(y>194 and y<230):
                GameOn = True
                standard = True
pyglet.app.run()
