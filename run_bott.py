from processor import processMessage 
from Tkinter import *
import time

global count
count = 0
class myApp:
    def __init__(self, parent):

        self.myParent = parent
        self.myParent.resizable(False, False)

        self.text = Text(parent, width=60, height=30)
        self.text.grid(row=0,column=0,columnspan=3)
        self.text.insert(INSERT, "Hello Guest!")
        self.text.configure(state="disabled", font="monaco", relief="solid")
        
        self.scrollbar = Scrollbar(parent, orient='vertical')
        self.scrollbar.config(command = self.text.yview)
        self.scrollbar.grid(row=0, column=3, sticky=N+S)

        self.entry = Entry(parent)
        self.entry.configure(width=53, font='monaco', relief="sunken")
        self.entry.grid(row=1, column=0, columnspan=2)
        self.entry.bind('<Return>', self.onEnter_a)
        self.entry.focus_set()

        self.button = Button(parent, text="Send", command=self.onEnter)
        self.button.grid(row=1, column=2)

        self.text.configure(yscrollcommand = self.scrollbar.set)
        self.myParent.update()
        self.myParent.geometry(self.myParent.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, END)
        
    def color_text(self, word, fg_color='black', bg_color='white'): 
        global count
        word = word + " "
        tag = 'tag'+str(count)
        count += 1
        self.text.insert('end', word)
        end_index = self.text.index('end')
        begin_index = "%s-%sc" % (end_index, len(word)+1)
        self.text.tag_add(tag, begin_index, end_index)
        self.text.tag_config(tag, foreground=fg_color, background=bg_color)
        self.text.see('end')
        

    def replyText(self, msg):
        botName = '\n[Bot]'
        returnMessage = processMessage(msg)
        #print returnMessage
        self.color_text(botName, 'red', 'white')
        self.color_text(returnMessage)
        self.text.see('end')
        
        
    def onEnter(self):
        msg = self.entry.get()
        self.text.configure(state="normal")
        uName = '\n[You]'
        self.color_text(uName, 'blue', 'white')
        #self.text.insert(END, uName)
        self.color_text(msg, 'black', 'white')
        self.replyText(msg)
        #self.text.insert(END, msg)
        self.text.configure(state="disabled")
        self.entry.focus_set()
        self.entry.selection_range(0, END)
    
    def onEnter_a(self, event):
        self.onEnter()

root = Tk()
myapp = myApp(root)
root.wm_title("bott, bot on turing test... ")
root.mainloop()
