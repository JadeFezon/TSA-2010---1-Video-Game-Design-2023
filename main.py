import pygame
import subprocess
pygame.init()
white = (255, 255, 255)
display_width = 1000
display_height = 790
gameDisplay = pygame.display.set_mode((display_width, display_height))
titleScreen = pygame.image.load("Screen Shot 2023-03-14 at 9.22.02 PM.png")
titlescreen = pygame.transform.scale(titleScreen, (display_width, display_height))
pygame.mixer.music.load("Lets Bash.wav")
pygame.mixer.music.play(loops = -1)
title = True
while title == True:
    gameDisplay.fill(white)
    gameDisplay.blit(titlescreen, (0, 0))
    pygame.display.set_caption("Block Bash")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                title = False

import pygame
import time
import random
import sys

def cutscene1():
    import pygame
    import subprocess
    import subprocess
    pygame.init()
    white = (255, 255, 255)
    display_width = 1000
    display_height = 790
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    titleScreen = pygame.image.load("image001 (1).png")
    titlescreen = pygame.transform.scale(titleScreen, (display_width, display_height))
    arrow = pygame.image.load("Untitled.jpeg")
    Arrow = pygame.transform.scale(arrow, (50, 50))
    choice = 0
    pygame.font.init()
    message = 1
    Blockle = pygame.image.load("blockle.png")
    blockle = pygame.transform.scale(Blockle, (300, 300))
    speechBubble = pygame.image.load("blockleSpeech.png")
    bubble = pygame.transform.scale(speechBubble, (700, 500))
    font = pygame.font.Font(None, 36)
    dialogue = ""
    while True:
        gameDisplay.fill(white)
        pygame.display.set_caption("Block Bash")
        gameDisplay.blit(bubble, (200, 000))
        gameDisplay.blit(blockle, (50, 500))
        if message == 1:
            dialogue = "Hi! My name's blockle. You seem to have stumbled\nin around here. Say, could you help me out?\n(Press the space bar to advance dialogue)"
            lines = dialogue.splitlines()
        if message == 2:
            dialogue = "You will?! Oh, thank you!"
            lines = dialogue.splitlines()
        if message == 3:
            dialogue = "So there's been a bunch of these blocks lately,\n and they just fall everywhere. It's quite\nannoying, not to mention dangerous!"
            lines = dialogue.splitlines()
        if message == 4:
            dialogue = "I noticed recently that if three are stacked \n together, in a line or in an l shape. they dissapear. \nWe need to clear as many as we can, \nand stop them from falling."
            lines = dialogue.splitlines()
        if message == 5:
            dialogue = "How do you do that? Well when they fall, ancient \n legends talk of the person behind the \n screen who can control these blocks, by rotating\n and moving them."
            lines = dialogue.splitlines()
        if message == 6:
            dialogue = "How does the proverb go? \nI think it goes something like this..."
            lines = dialogue.splitlines()
        if message == 7:
            dialogue = """The keys of the arrows shall shift the very course\nof nature, while the q and w buttons shall\n twist it to the controller's will."""
            lines = dialogue.splitlines()
        if message == 8:
            dialogue = "Be careful, though, matrices are delicate. That's \n where you stack the blocks. If too many fall\n and they stack over the red line, in 5 seconds,\n you're toast!"
            lines = dialogue.splitlines()
        if message == 8:
            dialogue = "Let's go clear some blocks!"
            lines = dialogue.splitlines()
        y = 170  # Starting y position for the first line

        for line in lines:
            text = font.render(line, True, (0, 0, 0))
            rect = text.get_rect(center=(550, y))
            gameDisplay.blit(text, rect)
            y += text.get_height() + 10  # Add some vertical spacing between lines

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    message = message + 1
        if message > 8:
            pygame.quit()
            quit()
import pygame
import subprocess
pygame.init()
white = (255, 255, 255)
display_width = 1000
display_height = 790
gameDisplay = pygame.display.set_mode((display_width, display_height))
titleScreen = pygame.image.load("image001 (1).png")
titlescreen = pygame.transform.scale(titleScreen, (display_width, display_height))
arrow = pygame.image.load("Untitled.jpeg")
Arrow = pygame.transform.scale(arrow, (50, 50))
choice = 0
play = False
while play == False:
    gameDisplay.fill(white)
    gameDisplay.blit(titlescreen, (0, 0))
    pygame.display.set_caption("Block Bash")
    if choice == 0:
        pygame.draw.rect(gameDisplay,(255, 0, 0), (150, 200, 50, 50) )
        pygame.display.update()
    elif choice == 1:
        pygame.draw.rect(gameDisplay,(0, 255, 0), (150, 400, 50, 50) )
        pygame.display.update()
    if choice == 2:
        pygame.draw.rect(gameDisplay,(0, 0, 255), (150, 600, 50, 50) )
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if choice > 0:
                    choice -= 1
                elif choice == 0:
                    choice = 2
            if event.key == pygame.K_DOWN:
                if choice < 2:
                    choice += 1
                elif choice == 2:
                    choice = 0
            if event.key == pygame.K_SPACE:
                if choice == 0:
                    cutscene1()
                if choice == 1:
                    play = True

display_width = 1000
clock = pygame.time.Clock()
clock.tick(60)
white = (255, 255, 255)
display_height = 800
redBlock = pygame.image.load('Screen Shot 2023-03-09 at 5.18.54 PM.png')
redBlockSmall = pygame.transform.scale(redBlock, (50, 50))
yellowBlock = pygame.image.load('Screen Shot 2023-03-09 at 5.18.39 PM.png')
YBlock = pygame.transform.scale(yellowBlock, (50, 50))
blueBlock = pygame.image.load('Screen Shot 2023-03-09 at 5.19.21 PM.png')
BBlock = pygame.transform.scale(blueBlock, (50, 50))
greenBlock = pygame.image.load('Screen Shot 2023-03-09 at 5.19.33 PM.png')
GBlock = pygame.transform.scale(greenBlock, (50, 50))
gameDisplay = pygame.display.set_mode((display_width, display_height))
originblock = 0
upBlock = 0
cBlock = 0
dBlock = 0
block1 = 0
block2 = 0
block3 = 0
block4 = 0
gaming = True  # You will need to relocate this at some point
gBlock1 = 0
gBlock2 = 0
gBlock3 = 0
gBlock4 = 0
x = (display_width - 900)
y = (display_height - 800)
blockX = 500
blockY = (display_height - 580)
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
string = ""
List = []
strikes = 0
blockXList = []
blockYList = []
clumpID = 0
colorID1List = []
colorID2List = []
colorID3List = []
colorID4List = []
clumpIDList = []
colorID1 = ""
colorID2 = ""
colorID3 = ""
colorID4 = ""
yCollision = False
fallTime = 1
rFallTime = 1
ultColorList = []
twoInARow = False
threeInARow = False
points = 0
twoInRowList1 = []
twoInRowList2 = []
twoInRowList3 = []
twoInRowList4 = []
def createString():
    one = random.choice(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    two = random.choice(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    three = random.choice(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    four = random.choice(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    five = random.choice(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    six = random.choice(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    string = (one + two + three + four + five + six)


def createMatrix():
    strikes = 0
    while strikes < 300:
        createString()
        if string in List:
            strikes += 1
        else:
            List.append(string)
            strikes = 0


def generateBlock():
    blockX = 500
    blockY = 220
    xCollision = False
    yCollision = False
    if originblock == 1:
        block1 = gameDisplay.blit(redBlockSmall, (blockX, blockY))
        colorID1 = "red"
        pygame.display.update()
    if originblock == 2:
        block1 = gameDisplay.blit(YBlock, (blockX, blockY))
        colorID1 = "yellow"
        pygame.display.update()
    if originblock == 3:
        block1 = gameDisplay.blit(BBlock, (blockX, blockY))
        colorID1 = "blue"
        pygame.display.update()
    if originblock == 4:
        block1 = gameDisplay.blit(GBlock, (blockX, blockY))
        colorID1 = "green"
        pygame.display.update()

    if upBlock == 1:
        block2 = gameDisplay.blit(redBlockSmall, (blockX, blockY - 50))
        colorID2 = "red"
        pygame.display.update()
    if upBlock == 2:
        block2 = gameDisplay.blit(YBlock, (blockX, blockY - 50))
        colorID2 = "yellow"
        pygame.display.update()
    if upBlock == 3:
        block2 = gameDisplay.blit(BBlock, (blockX, blockY - 50))
        colorID2 = "blue"
        pygame.display.update()
    if upBlock == 4:
        block2 = gameDisplay.blit(GBlock, (blockX, blockY - 50))
        colorID2 = "green"
        pygame.display.update()
    if cBlock == 1:
        block3 = gameDisplay.blit(redBlockSmall, (blockX - 50, blockY - 50))
        colorID3 = "red"
        pygame.display.update()
    if cBlock == 2:
        block3 = gameDisplay.blit(YBlock, (blockX - 50, blockY - 50))
        colorID3 = "yellow"
        pygame.display.update()
    if cBlock == 3:
        block3 = gameDisplay.blit(BBlock, (blockX - 50, blockY - 50))
        colorID3 = "blue"
        pygame.display.update()
    if cBlock == 4:
        block3 = gameDisplay.blit(GBlock, (blockX - 50, blockY - 50))
        colorID3 = "green"
        pygame.display.update()
    if dBlock == 1:
        block4 = gameDisplay.blit(redBlockSmall, (blockX - 50, blockY))
        colorID4 = "red"
        pygame.display.update()
    if dBlock == 2:
        block4 = gameDisplay.blit(YBlock, (blockX - 50, blockY))
        colorID4 = "yellow"
        pygame.display.update()
    if dBlock == 3:
        block4 = gameDisplay.blit(BBlock, (blockX - 50, blockY))
        colorID4 = "blue"
        pygame.display.update()
    if dBlock == 4:
        block4 = gameDisplay.blit(GBlock, (blockX - 50, blockY))
        colorID4 = "green"
        pygame.display.update()
    colorID1List.append(originblock)
    colorID2List.append(upBlock)
    colorID3List.append(cBlock)
    colorID4List.append(dBlock)
    ultColorList.append((originblock, upBlock, cBlock, dBlock))

def function1():
    global blockY
    while gaming == True:
        grounded = False
        originblock = random.randint(1, 4)
        upBlock = random.randint(1, 4)
        dBlock = random.randint(1, 4)
        cBlock = random.randint(1, 4)
        generateBlock()
        while grounded == False:
            for i in range(0, 10):
                time.sleep(1)
                if (blockY + 50) <= 720:
                    blockY += 50
                moveDown()
                pygame.display.update()
                # Collision Code.
            blockY = (display_height - 580)
            gBlock1 = block1
            gBlock2 = block2
            gBlock3 = block3
            gBlock4 = block4
            pygame.display.update()
            grounded = True


def function2():
    while gaming == True:
        gameDisplay.fill(white)
        matrix(x, y)
        gameDisplay.blit(gBlock1, (blockX, blockY))
        gameDisplay.blit(gBlock2, (blockX, blockY - 50))
        gameDisplay.blit(gBlock3, (blockX - 50, blockY - 50))
        gameDisplay.blit(gBlock4, (blockX - 50, blockY))

def moveDown():
        if originblock == 1:
            gameDisplay.fill(white)
            matrix(x, y)
            gameDisplay.blit(redBlockSmall, (blockX, blockY))
            update()
            text_rect.center = (785, 365)
            pygame.display.update()
            colorID1 = "red"
        if originblock == 2:
            gameDisplay.fill(white)
            matrix(x, y)
            gameDisplay.blit(YBlock, (blockX, blockY))
            update()
            text_rect.center = (785, 365)
            pygame.display.update()
            colorID1 = "yellow"
        if originblock == 3:
            gameDisplay.fill(white)
            matrix(x, y)
            gameDisplay.blit(BBlock, (blockX, blockY))
            update()
            text_rect.center = (785, 365)
            pygame.display.update()
            colorID1 = "blue"
        if originblock == 4:
            gameDisplay.fill(white)
            matrix(x, y)
            gameDisplay.blit(GBlock, (blockX, blockY))
            update()
            text_rect.center = (785, 365)
            pygame.display.update()
            colorID1 = "green"
        if upBlock == 1:
            gameDisplay.blit(redBlockSmall, (blockX, blockY - 50))
            pygame.display.update()
            colorID2 = "red"
        if upBlock == 2:
            gameDisplay.blit(YBlock, (blockX, blockY - 50))
            pygame.display.update()
            colorID2 = "yellow"
        if upBlock == 3:
            gameDisplay.blit(BBlock, (blockX, blockY - 50))
            pygame.display.update()
            colorID2 = "blue"
        if upBlock == 4:
            gameDisplay.blit(GBlock, (blockX, blockY - 50))
            pygame.display.update()
            colorID2 = "green"
        if cBlock == 1:
            gameDisplay.blit(redBlockSmall, (blockX - 50, blockY - 50))
            pygame.display.update()
            colorID3 = "red"
        if cBlock == 2:
            gameDisplay.blit(YBlock, (blockX - 50, blockY - 50))
            pygame.display.update()
            colorID3 = "yellow"
        if cBlock == 3:
            gameDisplay.blit(BBlock, (blockX - 50, blockY - 50))
            pygame.display.update()
            colorID3 = "blue"
        if cBlock == 4:
            gameDisplay.blit(GBlock, (blockX - 50, blockY - 50))
            pygame.display.update()
            colorID3 = "green"
        if dBlock == 1:
            gameDisplay.blit(redBlockSmall, (blockX - 50, blockY))
            pygame.display.update()
            colorID4 = "red"
        if dBlock == 2:
            gameDisplay.blit(YBlock, (blockX - 50, blockY))
            pygame.display.update()
            colorID4 = "yellow"
        if dBlock == 3:
            gameDisplay.blit(BBlock, (blockX - 50, blockY))
            pygame.display.update()
            colorID4 = "blue"
        if dBlock == 4:
            gameDisplay.blit(GBlock, (blockX - 50, blockY))
            pygame.display.update()
            colorID4 = "green"

def update():
   if 720 in blockYList:
        for z in range(0, clumpID):
            if ultColorList[z] == (-1, -1, -1, -1):
                continue
            if ultColorList[z][0] == 1:
                gameDisplay.blit(redBlockSmall, ((blockXList[z]), (blockYList[z])))
                text_rect.center = (785, 365)
            elif ultColorList[z][0] == 2:
                gameDisplay.blit(YBlock, ((blockXList[z]), (blockYList[z])))
                text_rect.center = (785, 365)
            elif ultColorList[z][0] == 3:
                gameDisplay.blit(BBlock, ((blockXList[z]), (blockYList[z])))
                text_rect.center = (785, 365)
            elif ultColorList[z][0] == 4:
                gameDisplay.blit(GBlock, ((blockXList[z]), (blockYList[z])))
                text_rect.center = (785, 365)

            if ultColorList[z][1] == 1:
                gameDisplay.blit(redBlockSmall, ((blockXList[z]), (blockYList[z]) - 50))
                text_rect.center = (785, 365)
            elif ultColorList[z][1] == 2:
                gameDisplay.blit(YBlock, ((blockXList[z]), (blockYList[z]) - 50))
                text_rect.center = (785, 365)
            elif ultColorList[z][1] == 3:
                gameDisplay.blit(BBlock, ((blockXList[z]), (blockYList[z]) - 50))
                text_rect.center = (785, 365)
            elif ultColorList[z][1] == 4:
                gameDisplay.blit(GBlock, ((blockXList[z]), (blockYList[z]) - 50))
                text_rect.center = (785, 365)

            if ultColorList[z][2] == 1:
                gameDisplay.blit(redBlockSmall, ((blockXList[z]) - 50, (blockYList[z]) - 50))
                text_rect.center = (785, 365)
            elif ultColorList[z][2] == 2:
                gameDisplay.blit(YBlock, ((blockXList[z]) - 50, (blockYList[z]) - 50))
                text_rect.center = (785, 365)
            elif ultColorList[z][2] == 3:
                gameDisplay.blit(BBlock, ((blockXList[z]) - 50, (blockYList[z]) - 50))
                text_rect.center = (785, 365)
            elif ultColorList[z][2] == 4:
                gameDisplay.blit(GBlock, ((blockXList[z]) - 50, (blockYList[z]) - 50))
                text_rect.center = (785, 365)

            if ultColorList[z][3] == 1:
                gameDisplay.blit(redBlockSmall, ((blockXList[z]) - 50, (blockYList[z])))
                text_rect.center = (785, 365)
            elif ultColorList[z][3] == 2:
                gameDisplay.blit(YBlock, ((blockXList[z]) - 50, (blockYList[z])))
                text_rect.center = (785, 365)
            elif ultColorList[z][3] == 3:
                gameDisplay.blit(BBlock, ((blockXList[z]) - 50, (blockYList[z])))
                text_rect.center = (785, 365)
            elif ultColorList[z][3] == 4:
                gameDisplay.blit(GBlock, ((blockXList[z]) - 50, (blockYList[z])))
                text_rect.center = (785, 365)
def twoInRow():
    twoInARow = False
    if originblock == dBlock:
        twoInARow = True
        twoInRowList1.append(twoInARow)
        twoInRowList4.append(twoInARow)
        twoInARow = False
    else:
        twoInRowList1.append(twoInARow)
        twoInRowList4.append(twoInARow)
    if upBlock == cBlock:
      if twoInARow:
        threeInARow = True
      else:
        twoInARow = True
        twoInRowList3.append(twoInARow)
        twoInRowList2.append(twoInARow)
        twoInARow = False
    else:
        twoInRowList3.append(twoInARow)
        twoInRowList2.append(twoInARow)
    if cBlock == dBlock:
      if twoInARow:
        threeInARow = True
      else:
        twoInARow = True
        twoInRowList3.append(twoInARow)
        twoInRowList4.append(twoInARow)
        twoInARow = False
    else:
        twoInRowList3.append(twoInARow)
        twoInRowList4.append(twoInARow)
    if originblock == upBlock:
      if twoInARow:
            threeInARow = True
      else:
            twoInARow = True
            twoInRowList1.append(twoInARow)
            twoInRowList2.append(twoInARow)
            twoInARow = False
    else:
        twoInRowList1.append(twoInARow)
        twoInRowList2.append(twoInARow)
    if 720 in blockYList and xCollision and yCollision:
        if cBlock == colorID2List[collidingClump]:
            if twoInRowList3[clumpID] == True or twoInRowList2[collidingClump] == True:
                threeInARow = True
            else:
              twoInARow = True
        if dBlock == colorID1List[collidingClump]:
            if twoInRowList4[clumpID] == True or twoInRowList1[collidingClump] == True:
                threeInARow = True
            else:
                twoInARow = True
        if originblock == colorID4List[collidingClump]:
            if twoInRowList1[clumpID] == True or twoInRowList4[collidingClump] == True:
                threeInARow = True
            else:
                twoInARow = True
        if upBlock == colorID3List[collidingClump]:
            if twoInRowList2[clumpID] == True or twoInRowList3[collidingClump] == True:
                threeInARow = True
            else:
                twoInARow = True
    if xCollision and yCollision and threeInARow:
       blockXList[collidingClump - 1] = 0
       blockYList[collidingClump - 1] = 0




def Destruction():
    if xCollision and yCollision and threeInARow:
       blockXList[collidingClump - 1] = 0
       blockYList[collidingClump - 1] = 0




while True:
    pygame.event.get()


    def main():

        pygame.init()

        pygame.display.set_caption("Game")


    main()
    gameDisplay.fill(white)
    matrixImg = pygame.image.load('Screen Shot 2023-03-09 at 5.21.07 PM.png')
    createMatrix()


    def matrix(x, y):
        gameDisplay.blit(matrixImg, (x, y))

    x = (display_width - 900)
    y = (display_height - 800)
    blockX = 500
    blockY = (display_height - 580)
    matrix(x, y)
    pygame.display.update()
    pygame.event.get()
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    # Render the text
    text = font.render("Points: {}".format(points), True, (255, 255, 255))

    # Get the rectangle containing the text
    text_rect = text.get_rect()

    # Center the text on the screen
    text_rect.center = (785, 365)

    # Blit the text to the screen
    gameDisplay.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.get()





    grounded = False  # Relocate Soon

    while gaming == True:
        grounded = False
        yCollision = False
        xCollision = False
        originblock = random.randint(1, 4)
        upBlock = random.randint(1, 4)
        dBlock = random.randint(1, 4)
        cBlock = random.randint(1, 4)
        generateBlock()
        clumpID + 1
        clumpIDList.append(clumpID)
        print(colorID1List)
        print(colorID2List)
        print(colorID3List)
        print(colorID4List)
        print(clumpID)
        print(colorID1)
        print(colorID2)
        print(colorID3)
        print(colorID4)

        while grounded == False:
            for i in range(0, 10):
                time.sleep(fallTime / 10)
                print(colorID1List)
                print(colorID2List)
                print(colorID3List)
                print(colorID4List)
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                                blockX = blockX - 50
                                moveDown()
                                if xCollision and yCollision:
                                    blockX = blockX + 50
                            elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                                blockX = blockX + 50
                                moveDown()
                                if xCollision and yCollision:
                                    blockX = blockX - 50
                            elif event.key == pygame.K_q:
                                print("Q pressed")
                                originblock = originblock
                                rOriginBlock = originblock
                                originblock = upBlock
                                upBlock = cBlock
                                cBlock = dBlock
                                dBlock = rOriginBlock
                                colorID1List.pop(clumpID)
                                colorID2List.pop(clumpID)
                                colorID3List.pop(clumpID)
                                colorID4List.pop(clumpID)
                                rcolorID = colorID1
                                colorID1 = colorID2
                                colorID2 = colorID3
                                colorID3 = colorID4
                                colorID4 = rcolorID
                                colorID1List.append(originblock)
                                colorID2List.append(upBlock)
                                colorID3List.append(cBlock)
                                colorID4List.append(dBlock)
                                ultColorList.pop(clumpID)
                                ultColorList.append((originblock, upBlock, cBlock, dBlock))
                                moveDown()
                            elif event.key == pygame.K_w:
                                rOriginBlock = originblock
                                originblock = dBlock
                                dBlock = cBlock
                                cBlock = upBlock
                                upBlock = rOriginBlock
                                colorID1List.pop(clumpID)
                                colorID2List.pop(clumpID)
                                colorID3List.pop(clumpID)
                                colorID4List.pop(clumpID)
                                rcolorID = colorID1
                                colorID1 = colorID4
                                colorID4 = colorID3
                                colorID3 = colorID2
                                colorID2 = rcolorID
                                colorID1List.append(originblock)
                                colorID2List.append(upBlock)
                                colorID3List.append(cBlock)
                                colorID4List.append(dBlock)
                                ultColorList.pop(clumpID)
                                ultColorList.append((originblock, upBlock, cBlock, dBlock))
                                moveDown()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:

                                fallTime = 0.1
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN:
                                fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT  and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                        elif event.key == pygame.K_RIGHT  and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                print(twoInARow)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()

                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                time.sleep(fallTime / 10)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and blockX - 50 >= 310:
                            blockX = blockX - 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX + 50
                                moveDown()
                        elif event.key == pygame.K_RIGHT and blockX + 50 <= 610:
                            blockX = blockX + 50
                            moveDown()
                            if xCollision and yCollision:
                                blockX = blockX - 50
                                moveDown()
                        elif event.key == pygame.K_q:
                            print("Q pressed")
                            originblock = originblock
                            rOriginBlock = originblock
                            originblock = upBlock
                            upBlock = cBlock
                            cBlock = dBlock
                            dBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID2
                            colorID2 = colorID3
                            colorID3 = colorID4
                            colorID4 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            moveDown()
                        elif event.key == pygame.K_w:
                            rOriginBlock = originblock
                            originblock = dBlock
                            dBlock = cBlock
                            cBlock = upBlock
                            upBlock = rOriginBlock
                            colorID1List.pop(clumpID)
                            colorID2List.pop(clumpID)
                            colorID3List.pop(clumpID)
                            colorID4List.pop(clumpID)
                            rcolorID = colorID1
                            colorID1 = colorID4
                            colorID4 = colorID3
                            colorID3 = colorID2
                            colorID2 = rcolorID
                            colorID1List.append(originblock)
                            colorID2List.append(upBlock)
                            colorID3List.append(cBlock)
                            colorID4List.append(dBlock)
                            ultColorList.pop(clumpID)
                            ultColorList.append((originblock, upBlock, cBlock, dBlock))
                            text_rect.center = (785, 365)
                            moveDown()
                            text_rect.center = (785, 365)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            fallTime = 0.1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            fallTime = rFallTime
                print(originblock)
                print(upBlock)
                print(cBlock)
                print(dBlock)
                print(blockXList)
                print(blockYList)
                print("xColl:", xCollision)
                print("yColl:", yCollision)
                print("2 in row:",twoInARow)
                print(blockX)
                print(blockY)
                print(twoInRowList1)
                print(twoInRowList2)
                print(twoInRowList3)
                print(twoInRowList4)
                print(threeInARow)
                print(clumpID)
                print("---------")
                update()

                if 720 in blockYList:
                  for l in range(0 , len(blockYList)):
                      if blockY >= blockYList[l] - 100 and colorID1List[l] != -1:
                          yCollision = True
                      else:
                          yCollision = False
                      if blockX <= blockXList[l] + 50 and blockX >= blockXList[l] - 50 :
                          xCollision = True
                          if xCollision and yCollision:
                            collidingClump = clumpIDList[l]
                            print(collidingClump)
                            twoInARow = False
                            threeInARow = False
                            if originblock == dBlock:
                                twoInARow = True
                                twoInRowList1.append(twoInARow)
                                twoInRowList4.append(twoInARow)
                                twoInARow = False
                            else:
                                twoInRowList1.append(twoInARow)
                                twoInRowList4.append(twoInARow)
                            if upBlock == cBlock:
                                if twoInARow:
                                    threeInARow = True
                                else:
                                    twoInARow = True
                                    twoInRowList3.append(twoInARow)
                                    twoInRowList2.append(twoInARow)
                                    twoInARow = False
                            else:
                                twoInRowList3.append(twoInARow)
                                twoInRowList2.append(twoInARow)
                            if cBlock == dBlock:
                                if twoInARow:
                                    threeInARow = True
                                else:
                                    twoInARow = True
                                    twoInRowList3.append(twoInARow)
                                    twoInRowList4.append(twoInARow)
                                    twoInARow = False
                            else:
                                twoInRowList3.append(twoInARow)
                                twoInRowList4.append(twoInARow)
                            if originblock == upBlock:
                                if twoInARow:
                                    threeInARow = True
                                else:
                                    twoInARow = True
                                    twoInRowList1.append(twoInARow)
                                    twoInRowList2.append(twoInARow)
                                    twoInARow = False
                            else:
                                twoInRowList1.append(twoInARow)
                                twoInRowList2.append(twoInARow)
                            if 720 in blockYList and xCollision and yCollision:
                                if cBlock == colorID2List[collidingClump]:
                                    if twoInRowList3[clumpID] == True or twoInRowList2[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if dBlock == colorID1List[collidingClump]:
                                    if twoInRowList4[clumpID] == True or twoInRowList1[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if originblock == colorID4List[collidingClump]:
                                    if twoInRowList1[clumpID] == True or twoInRowList4[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if upBlock == colorID3List[collidingClump]:
                                    if twoInRowList2[clumpID] == True or twoInRowList3[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if dBlock == colorID3List[collidingClump]:
                                    if twoInRowList4[clumpID] == True or twoInRowList3[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if dBlock == colorID2List[collidingClump]:
                                    if twoInRowList4[clumpID] == True or twoInRowList2[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if originblock == colorID3List[collidingClump]:
                                    if twoInRowList1[clumpID] == True or twoInRowList3[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                                if originblock == colorID2List[collidingClump]:
                                    if twoInRowList1[clumpID] == True or twoInRowList2[collidingClump] == True:
                                        threeInARow = True
                                    else:
                                        twoInARow = True
                            if threeInARow:
                                blockXList.append(blockX)
                                blockYList.append(blockY)
                                blockXList.pop(len(blockXList) - 1)
                                blockYList.pop(len(blockXList) - 1)
                                blockXList.pop(collidingClump)
                                blockYList.pop(collidingClump)
                                colorID1List.pop(collidingClump)
                                colorID2List.pop(collidingClump)
                                colorID3List.pop(collidingClump)
                                colorID4List.pop(collidingClump)
                                colorID1List.pop(clumpID - 1)
                                colorID2List.pop(clumpID - 1)
                                colorID3List.pop(clumpID - 1)
                                colorID4List.pop(clumpID -1)
                                ultColorList[clumpID] = (-1, -1, -1, -1)
                                clumpID = clumpID - 2
                                update()
                                threeInARow = False
                                twoInARow = False
                                points = points + 5
                      else:
                          xCollision = False

                if yCollision == True and xCollision == True:
                    grounded = True
                    print("Y:", blockYList)
                    print(blockXList)
                    break
                if (blockY + 50) <= 720:
                  blockY += 50
                moveDown()
                pygame.display.update()
            blockXList.append(blockX)
            blockYList.append(blockY)

            print(blockXList)
            print(blockYList)
            print(clumpIDList)
            update()

            blockY = 220
            clumpID = clumpID + 1
            grounded = True