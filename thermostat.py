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


rot = Tk()

#define the windows and frames
#topframe = Frame(rot)
#topframe.pack()
#bottomframe = Frame(rot)
#bottomframe.pack(side=BOTTOM)

# define the buttons and labels
title = Label(rot, text='TIME')
invisable = Label(rot, text='  ')  #  space the buttons out

main = 'MAIN\n' + str(mainTemp)[:4]

# Define a list of buttons for the UI
button1 = Button(rot, text = main, fg = 'red', bg = 'black')
button2 = Button(rot, text = 'upstairs\n' + str(upstair)[:4], fg = 'blue')
button3 = Button(rot, text = 'BASEMENT\n', fg = 'red')
button4 = Button(rot, text = ' GARAGE \n', fg = 'red')
# place the buttons
title.grid(columnspan=5)
invisable.grid(row = 1, column = 2)
button1.grid(row=1, column= 1)
button2.grid(row=1, column= 3)
button3.grid(row=2, column= 1)
button4.grid(row=2, column= 3)


rot.mainloop()



