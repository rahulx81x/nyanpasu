from tkinter import *
from animechan import quote, by
from openBrowser import search_anime

qbox = Tk()
text1 = Text(qbox, height=8, width=70)
text1.tag_configure("tag_name", justify='center')
text1.insert("1.0", "\n".join(quote))
text1.tag_add("tag_name", "1.0", "end")
text1.config(wrap="word", font=("Franklin Gothic Medium", 12, "italic"))
text1.grid(row=1,column=0)


text2 = Label(qbox, text=by)
text2.grid(row=2,column=0)

anime_button = Button(qbox, text="Search Anime", command=search_anime)
anime_button.grid(row=3, column=0)

qbox.mainloop()
