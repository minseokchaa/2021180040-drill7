from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습 설정
        self.image = load_image('grass.png')
    def update(self):
        pass        #변하는게 없기 때문
    def draw(self):
        self.image.draw(400,30)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1 ) % 8
        self.x +=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



def reset_world():
    global running
    global grass
    global boy
    global  team

    running = True
    grass = Grass()         # 잔디를 생성한다. 객체 생성
    team = [Boy() for i in range(11)]

running = True

def update_world():
    grass.update()  #객체의 상태를 업데이트
    for boy in team:
        boy.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()
# game main loop code


while running:
    #game logic
    handle_events()
    update_world()  #상호작용 시뮬레이션
    render_world()  #그 결과를 보여준다.
    delay(0.05)




# finalization code

close_canvas()
