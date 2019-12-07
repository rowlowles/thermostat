print(' STARTING...\n')
import wirelesstagpy
from tkinter import *

# read the sensors
api = wirelesstagpy.WirelessTags(username='rob.lowles@gmail.com', password='3scope14')
tags = api.load_tags()
alltags = {}
for (uuid, tag) in tags.items():
    #alltags.append({tag.name: tag.temperature})
    alltags[tag.name] = tag.temperature
    print(' {}, temp: {:.1f}, humidity: {:.3f} '.format(
                tag.name, tag.temperature,
                tag.humidity))
#   if (tag.name == 'Main room') :
 #       mainTemp = tag.temperature
mainTemp= alltags['Main room']
upstair = alltags['upstairs']

print('\n take action')

roomLimits = {
    'Main room': [16, 21],
    'basement': [8, 15],
    'Garage': [5, 10],
    'upstairs': [10, 21],
    'heater': [0,0],
    'inside': [0,0]
}
currentTagData = api.load_tags()
for (uuid, tag) in currentTagData.items():
    if (tag.temperature < roomLimits[tag.name][0]):
        print('Turn on heater for {}'.format(tag.name))
    if (tag.temperature > roomLimits[tag.name][1]):
        print('Turn off heater for {}'.format(tag.name))


print ('  grab a temp ', mainTemp)
print(' \n\ngenerating GUI..\n')

def button1action(event) :
    print ('button 1 pressed')







rot = Tk()
rot.geometry("240x320+1000+500")
rot.configure(bg = 'grey')
#define the windows and frames
#topframe = Frame(rot)
#topframe.pack()
#bottomframe = Frame(rot)
#bottomframe.pack(side=BOTTOM)

# Define a frame for each button and place the frames on a grid
button1frame = Frame(rot, bg = 'black', height = "100", width = '100', relief= 'groove')

button1frame.grid(row=1, column= 1)
button1frame.focus_force()
button1frame.bind("<Button-1>", button1action)
label1a = Label(button1frame, text = "main", fg = 'white', bg = 'black', font=("Helvetica", 15) )
label1a.pack()


# bind does not work on the frame if there is a label on it. 





button2frame = Frame(rot,bg = 'black')
button3frame = Frame(rot,bg = 'black')
button4frame = Frame(rot,bg = 'black')
invisable = Label(rot, text='  ')  #  space the buttons out

invisable.grid(row = 1, column = 2)
button2frame.grid(row=1, column= 3)
button3frame.grid(row=2, column= 1)
button4frame.grid(row=2, column= 3)



print(' \n\nframes generated, now place the buttons in each frame..\n')

# Each frame has several label, with different fount sizes plus 1 button

label1a = Label(button1frame, text = "main", fg = 'white', bg = 'black', font=("Helvetica", 15) )
#label1b = Label(button1frame, text = str(mainTemp)[:4],  fg = 'white', bg = 'black',  font=("Helvetica", 20))
#label1c = Label(button1frame, text = 'set = ' +  str(roomLimits['Main room'][0]) , fg = 'white', bg = 'black',  font=("Helvetica",10))
label1a.pack()
#label1b.pack()
#label1c.pack()



button2 = Button(button2frame, text = 'upstairs\n' + str(upstair)[:4], fg = 'white', bg = 'orange')
button3 = Button(button3frame, text = 'BASEMENT\n', fg = 'red')
button4 = Button(button4frame, text = ' GARAGE \n', fg = 'red')

button2.pack()
button3.pack()
button4.pack()





rot.mainloop()



