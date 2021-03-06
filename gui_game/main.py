import pygame
import numpy as np
import pos # pos.py module import
import cli_board

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("ul omok")

oo = 50
spot_pos = 50/2
block = 50
turn = 1
np_omok_board = np.zeros([15, 15])
# sound
sound_put_stone = pygame.mixer.Sound("src/sound/put_stone.ogg")
sound_put_stone.set_volume(0.3)
sound_end = pygame.mixer.Sound("src/sound/end.ogg")
sound_end.set_volume(0.5)

running = True
pos_count = -1

while running: # 좌표 리스트로 구하기
    apb = pos.pos_apb(pos_count)

    for i in range(15):
        globals()[f"{apb}{i}"] = [oo + (i * 50), (oo + block*(pos_count+1))] # 각 칸의 좌표를 변수로 지정 ex) a0 = [53, 53]
    pos_count += 1

    if pos_count > 13:
        running = False

running = True
pos_count = -1

while running: # 포지션 구하기 
    apb = pos.pos_apb(pos_count) # 알파벳 값 구하기
    
    for i in range(15):
        globals()[f"white_{apb}{i}_pos"] = [(oo + (i * 50)) * -1, ((oo + block*(pos_count+1)) * -1 )] # 보이지 않는 곳에 생성 ex) a0 = [-53, -53]
    # print(globals()[f"{apb}{i}_pos"])
    pos_count += 1
    
    if pos_count > 13:
        running = False

run = True

running = True
pos_count = -1
while running:
    apb = pos.pos_apb(pos_count)
    
    for i in range(15):
        globals()[f"black_{apb}{i}_pos"] = [(oo + (i * 50)) * -1, ((oo + block*(pos_count+1)) * -10 )] # 보이지 않는 곳에 생성 ex) a0 = [-53, -53]
    # print(globals()[f"{apb}{i}_pos"])
    pos_count += 1
    
    if pos_count > 13:
        running = False

run = True

# img
background = pygame.image.load("src/img/ed_omok_board.png") # omok_board
background = pygame.transform.scale(background, (800, 800)) # board_scale
#load
omok_black = pygame.image.load("src/img/omok_black.png")
omok_white = pygame.image.load("src/img/omok_white.png")
#scale
omok_black = pygame.transform.scale(omok_black, (50, 50))
omok_white = pygame.transform.scale(omok_white, (50, 50))

end = False

while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = list(pygame.mouse.get_pos())
            print(mouse_pos)
            
            if end != True:
                running = True
            pos_count = -1
            run_count = 1
            while running:
                apb = pos.pos_apb(pos_count)
                for i in range(15):
                    globals()[f"{apb}{i}"] = [oo + (i * 50), (oo + block*(pos_count+1))] # 각 칸의 좌표를 변수로 지정 ex) a0 = [53, 53]
                    if mouse_pos[0] >= globals()[f"{apb}{i}"][0]-15: # 테스트용
                        if mouse_pos[0] <= globals()[f"{apb}{i}"][0]+15:
                            if mouse_pos[1] >= globals()[f"{apb}{i}"][1]-15:
                                if mouse_pos[1] <= globals()[f"{apb}{i}"][1]+15:
                                    win = False
                                    np_omok_board, turn, overlap, np_x, np_y, win, turn_type = cli_board.create_board(turn, i, apb, np_omok_board) # size, first_color, board_run, y, x
                                    print(np_omok_board)
                                    
                                    if overlap != True:
                                        if np_omok_board[np_y, np_x] == 1:
                                            globals()[f"black_{apb}{i}_pos"] = [globals()[f"{apb}{i}"][0]-spot_pos, globals()[f"{apb}{i}"][1]-spot_pos]
                                            sound_put_stone.play()
                                            
                                        if np_omok_board[np_y, np_x] == 2:
                                            globals()[f"white_{apb}{i}_pos"] = [globals()[f"{apb}{i}"][0]-spot_pos, globals()[f"{apb}{i}"][1]-spot_pos]
                                            sound_put_stone.play()

                                        if win == True:
                                            running = False
                                            end = True
                                            sound_put_stone.play()
                                            break
                                            

                                        turn += 1
                                        overlap = False

                                    # globals()[f"{apb}{i}_pos"] = [globals()[f"{apb}{i}"][0]-spot_pos, globals()[f"{apb}{i}"][1]-spot_pos]
                if end != True:
                    pos_count += 1

                    if pos_count > 13:
                        running = False

                    

            # pos.put_omok_stone(mouse_pos, spot_pos)
            
            """
            if mouse_pos[0] >= a0[0]-5: # 테스트용
                if mouse_pos[0] <= a0[0]+10:
                    if mouse_pos[1] >= a0[1]-10:
                        if mouse_pos[1] <= a0[1]+10:
                            a0_pos = [a0[0]-spot_pos, a0[1]-spot_pos]

            if mouse_pos[0] >= b0[0]-5: # 테스트용
                if mouse_pos[0] <= b0[0]+10:
                    if mouse_pos[1] >= b0[1]-10:
                        if mouse_pos[1] <= b0[1]+10:
                            b0_pos = [b0[0]-spot_pos, b0[1]-spot_pos]
            """
    screen.blit(background, (0, 0))

    # screen.blit(omok_white, a0_pos)
    # screen.blit(omok_black, b0_pos)

    running = True
    pos_count = -1

    while running:
        apb = pos.pos_apb(pos_count)

        for i in range(15):
            globals()[f"{apb}{i}"] = [oo + (i * 50), (oo + block*(pos_count+1))] # 각 칸의 좌표를 변수로 지정 ex) a0 = [53, 53]
            screen.blit(omok_white, globals()[f"white_{apb}{i}_pos"])
            screen.blit(omok_black, globals()[f"black_{apb}{i}_pos"])
        pos_count += 1

        if pos_count > 13:
            running = False



    # stone blit
    # screen.blit(omok_white, (a0[0]-spot_pos, a0[1]-spot_pos))
    

    pygame.display.update()
    clock.tick(30) # fps

pygame.quit()
    
