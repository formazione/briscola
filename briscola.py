# briscola 3

from random import shuffle, choice

# these are the cards colors
COLOR = ['♥', '♦', '♣', '♠']

# CARS contains tuples with numbers and color
CARDS = [(c, s) for c in range(1, 11) for s in COLOR]
cards = [str(c) + s for c in range(1, 11) for s in COLOR]
# pcval is the dictionary with the value of each card
pcval = {1: 11,
         2: 0,
         3: 10,
         4: 0,
         5: 0,
         6: 0,
         7: 0,
         8: 2,
         9: 3,
         10: 4}


def getcards():
    "takes three cards from the deck"
    _cards = []
    for n in range(3):
        c = choice(cards)
        cards.pop(cards.index(c))
        _cards.append(c)
    _cards = ' '.join(_cards)
    return _cards


# player and pc gets 3 cards
mycards = getcards()
pccards = getcards()

briscola = choice(cards)
print(f"me {mycards} \npc {pccards} \nbriscola={briscola}")

import tkinter

root = tkinter.Tk()
root.geometry("400x400")
root.title("Card game")
frame = tkinter.Frame(root)
frame.pack(side='top')
player = tkinter.Label(frame, text="Briscola", font="30")
player.pack(side='left')
player_cards = tkinter.Label(frame, text="", fg="red", bg='yellow', font="Arial 24")
player_cards.pack(side='left')
player_cards['text'] = briscola

# ===================== second frame =======

frame2 = tkinter.Frame(root)
frame2.pack()

lab_over_listbox = tkinter.Label(frame2, text="Player cards", font="18")
lab_over_listbox.pack()

listbox = tkinter.Listbox(frame2, font="Arial 24", height=3, width=4)
for item in mycards.split(" "):
    listbox.insert(0, item)
listbox.pack()

lab_under_listbox = tkinter.Label(frame2, text="Choose a card")
lab_under_listbox.pack(side='bottom')

root.mainloop()
