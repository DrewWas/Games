from pygame import *

"""
FIX THIS LATER... COULD BE HELPFUL!!!
"""



init()
display.init()
window = display.set_mode((1000,1000))
display.set_caption("fonts")

fonts = list(font.get_fonts())

def main():
    run = True
    x = 0
    xpos = 1
    while run:
        window.fill((255,255,255))
        for events in event.get():
             if events.type == QUIT:
                 run = False

        for i in range(len(fonts) - 1):
            for j in range(4):
	        try:
	            myFont = font.SysFont(fonts[x], 20)
	            text = myFont.render(fonts[x], False, (0,138,255))
	            window.blit(text, (25 * i , 25 * j))
	            x += 1
		except:
		    myFont = font.SysFont(fonts[x+1], 20)
		    text = myFont.render(fonts[x+1], False, (0,138,255))
		    window.blit(text, (20 * (x + 1), 20))
		    x += 1
		else:
	            break

        display.update()


    print(fonts) 

main()
