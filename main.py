import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.dialogs import Messagebox
import socket
import tkinter as tk

sk = socket.socket()
class Client:
    def __init__(self,serverip,port):
        sk.connect((serverip,port))


root = ttk.Window(title='PyChat聊天室 By WIN-HORROR',
                  themename='superhero',
                  size=[1500, 1000],
                  iconphoto=None)
ChatName = ttk.StringVar()
IsAnonymous = ttk.BooleanVar()
root.iconbitmap(default=r'./favicon.ico')
ttk.Label(root,
          width=10).grid()
ttk.Label(root,
          text='聊天名：').grid(row=1,
                               column=1,
                               pady=25,
                               sticky=ttk.W)
ChatNameEntry = ttk.Entry(root,
                          bootstyle="info",
                          textvariable=ChatName)
ToolTip(ChatNameEntry,text='你的聊天名',bootstyle=(INFO,INVERSE))
ChatNameEntry.grid(row=1,
                   column=2,
                   sticky=ttk.W)
ttk.Label(root,
          text='是否匿名：').grid(row=2,
                                 column=1,
                                 sticky=ttk.W)
def AnonymousButtonUpdated():
    if IsAnonymous.get():
        ChatNameEntry.configure(state=DISABLED)
        print('Disabled!')
    else:
        ChatNameEntry.configure(state=NORMAL)
        print('Enabled!')

IsAnonymousButton = ttk.Checkbutton(bootstyle="warning-square-toggle",
                                    command=AnonymousButtonUpdated,
                                    variable=IsAnonymous,
                                    onvalue=True,
                                    offvalue=False)
ToolTip(IsAnonymousButton,text='是否要匿名',bootstyle=(INFO,INVERSE))
IsAnonymousButton.grid(row=2,
                       column=2,
                       sticky=ttk.W)

def SubmitName():
    name = ChatName.get()
    if name == '':
        print('None!')
        Messagebox.show_error(message='聊天名不可为空！',
                              title='错误！',
                              parent=root,
                              alert=True)
    else:


SubmitNameButton = ttk.Button(bootstyle=(INFO,OUTLINE),
                              text='提交',
                              command=SubmitName)
ToolTip(SubmitNameButton,text='提交你的聊天名',bootstyle=(WARNING,INVERSE))
SubmitNameButton.grid(row=3,
                      column=1,
                      sticky=ttk.W,
                      pady=25)
root.mainloop()