from distutils.command.install import install
from xml.sax.xmlreader import InputSource
import PySimpleGUI as sg
sg.theme("Topanga")
Hammer  = 5.2
Great_Sword = 4.8
Hunting_Horn = 4.2
Charge_Blade = 3.6
Switch_Axe = 3.5
Long_Sword = 3.3
Insect_Glaive = 3.1
Lance = 2.3
Gunlance = 2.3
Heavy_Bowgun = 1.5
Sword_and_Shield = 1.4
Dual_Blades = 1.4
Light_Bowgun = 1.3
Bow = 1.2

Red = 0.5
Orange = 0.75
Yellow = 1
Green = 1.05
Blue = 1.20
White = 1.32
Purple = 1.39

ERed = 0.25
EOrange = 0.5
EYellow = 0.75
EGreen = 1
EBlue = 1.0625
EWhite = 1.15
EPurple = 1.25
layout = [ 
    [sg.Text("Select Weapon:")],
    [sg.Button("Hammer"), sg.Button("Great Sword"), sg.Button("Hunting Horn"), sg.Button("Charge Blade"), sg.Button("Switch Axe"), sg.Button("Long Sword"), sg.Button("Insect Glaive")],

    [sg.Button("Lance"), sg.Button("Gunlance"), sg.Button("Heavy Bowgun"), sg.Button("Sword and Shield"), sg.Button("Dual Blades"), sg.Button("Light Bowgun"), sg.Button("Bow")]
]
window = sg.Window("MHW Weapon Damage", layout)
while True:
    event, values = window.read()
    if event  == "Hammer":
     X = Hammer
     Z = 0.37
     break
    elif event  == "Great Sword":
     X = Great_Sword
     Z = 0.48
     break
    elif event  == "Hunting Horn":
     X = Hunting_Horn
     Z = 0.24
     break
    elif event  == "Charge Blade":
     X = Charge_Blade
     Z = 0.38
     break
    elif event  == "Switch Axe":
     X = Switch_Axe
     Z = 0.23
     break
    elif event  == "Long Sword":
     X = Long_Sword
     Z = 0.24
     break
    elif event  == "Insect Glaive":
     X = Insect_Glaive
     Z = 0.16
     break
    elif event  == "Lance":
     X = Lance
     Z = 0.2
     break
    elif event  == "Gunlance":
     X = Gunlance
     Z = 0.24
     break
    elif event  == "Heavy Bowgun":
     X = Heavy_Bowgun
     Z = 0.1
     break
    elif event  == "Sword and Shield":
     X = Sword_and_Shield
     Z = 0.16
     break
    elif event  == "Dual Blades":
     X = Dual_Blades
     Z = 0.11
     break
    elif event  == "Light Bowgun":
     X = Light_Bowgun
     Z = 0.1
     break
    elif event  == "Bow":
     X = Bow
     Z = 0.07
     break
    elif event == sg.WIN_CLOSED:
        X = 0
        Z = 0
        break
window.close()
layout1 = [
    [sg.Text("Select Weapon Sharpness")],
    [sg.Button("Red"), sg.Button("Orange")],
    [sg.Button("Yellow"), sg.Button("Green")],
    [sg.Button("Blue"), sg.Button("White")],
    [sg.Button("Purple"), sg.Button("Ranged Weapon")]
]
window1 = sg.Window("MHW Weapon Damage", layout1)

while True:
    event, values =window1.read()
    if event == ("Red"):
     Y = Red
     YE = ERed
    elif event == ("Orange"):
     Y = Orange
     YE = EOrange
    elif event == ("Yellow"):
     Y = Yellow
     YE = EYellow
    elif event == ("Green"):
     Y = Green
     YE = EGreen
    elif event == ("Blue"):
     Y = Blue
     YE = EBlue
    elif event == ("White"):
     Y = White
     YE = EWhite
     break
    elif event == ("Purple"):
     Y = Purple
     YE = EPurple
     break
    elif event == ("Ranged Weapon"):
     Y = 1
     YE = 1
     break
    else: sg.WIN_CLOSED 
    Y = 0
    YE = 0
    break
window1.close()
layout2 = [
    [sg.Text("Input Weapon Damage:")],
    [sg.InputText(key='-DAMAGE-')],
    [sg.Submit()]
]
window2 = sg.Window("MHW Weapon Damage", layout2)
while True:
    event, values = window2.read()
    if event: sg.WIN_CLOSED
    break
window2.close()
WD = int(values['-DAMAGE-'])
Raw_Damamge = int(WD / X * Y * Z *0.8)
layout3 = [
    [sg.Text("Input Elemental Damage")],
    [sg.InputText(key='-ED-')],
    [sg.Button("Submit")],
    [sg.Button("No Element")]
]
window3 = sg.Window("MHW Weapon Damage", layout3)
while True:
    event, values = window3.read()
    if event == ("No Element"):
     window3.close()
     sg.popup("Your Average Damage per Hit is: " + str(Raw_Damamge))
     break     
    elif event == ("Submit"):
     ED = int(values['-ED-'])
     Elemental_Damage = int(ED/10 * YE * 0.3)
     Total_Damage = int((Raw_Damamge + Elemental_Damage))
     window3.close()
     sg.popup("Your Average Raw Damage per Hit is: " + str(Raw_Damamge),"\nYour Average Elemental Damage per Hit is: " + str(Elemental_Damage), "\nYour Average Total Damage per Hit is: "+ str(Total_Damage))
     break
    elif sg.WIN_CLOSED:
        break