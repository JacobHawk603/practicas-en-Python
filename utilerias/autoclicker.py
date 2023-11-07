import mouse
import time

# left click
# mouse.click('left')

# # right click
# mouse.click('right')

# # middle click
# mouse.click('middle')

def switch_bandera():
    global bandera

    # print("right click")
    bandera = False

if __name__ == "__main__":

    bandera = True
    events = mouse.record()
    
    while bandera:

    #     mouse.click('left')
    #     mouse.wheel(1)
    #     # print("click")
    #     x,y = mouse.get_position()

    #     print(x,y)
        
    #     mouse.on_click(callback=print("left click"))

    #     time.sleep(3)

        mouse.on_click(callback=switch_bandera)

        mouse.play(events[:-1])