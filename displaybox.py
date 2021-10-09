from tkinter import *
from animechan import js
import textwrap
quote = textwrap.wrap(js['quote'])
by = ' ~~  ' + js['character'] + ' from ' + js['anime']
by = textwrap.wrap(by)
qbox = Tk()
text = Text(qbox)
text.insert(INSERT, "\n".join(quote))
text.insert(INSERT, "\n".join(by))
text.pack()
qbox.mainloop()
