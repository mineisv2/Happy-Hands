import pyautogui
def click(x,y):
    pyautogui.moveTo(x, y)

click(950, 10)

import tkinter as tk
import simpleaudio as sa

filename = 'final.wav'

def hello(event):
    print("Working")
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

widget = tk.Tk()



widget.overrideredirect(True)
widget.overrideredirect(False)
widget.attributes('-fullscreen',True)


widget = tk.Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-2>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()

