from tkinter import *
from tkinter import scrolledtext

from platform import platform
from urllib.request import Request, urlopen
import json
def webhook_send():
    WEBHOOK_URL = hook.get()
    message = text_area.get("1.0",END)

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass
window = Tk()
window.title("HookSend")
window.geometry('450x240')
window.minsize(450, 240) 
#window.resizable(width=False, height=False)
#frame_main = Frame(window, bg='pink')
frame_text = Frame(window, bg="blue")
topframe = Frame(window)
lbl = Label(topframe, text="Webhook Here: ")
hook = Entry(topframe)
lbl.pack(side=LEFT, anchor='w')
hook.pack(side=LEFT, fill=X, expand=True)
text_area = scrolledtext.ScrolledText(frame_text, height=13, wrap=WORD)
send = Button(topframe, text="send", command=webhook_send)
text_area.pack(fill=BOTH, expand=True)
frame_text.pack(fill=BOTH, expand=True)
send.pack(fill=Y, anchor='e')
topframe.pack(fill=X)
#frame_main.pack(fill = BOTH, expand = True)



window.mainloop()