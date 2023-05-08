from tkinter import *
import tkinter.filedialog, tkinter as tk, time
from tkinter import messagebox as mb

def app_exit():
    answer = tkinter.messagebox.askokcancel(u'\u0412\u044b\u0445\u043e\u0434', u'\u0412\u044b \u0442\u043e\u0447\u043d\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0432\u044b\u0438\u0306\u0442\u0438?')
    if answer:
        app.destroy()


def change_theme(theme):
    textbox['bg'] = view_colors[theme]['text_bg']
    textbox['fg'] = view_colors[theme]['text_fg']


def change_fonts(fontsg):
    textbox['font'] = fonts[fontsg]['font']


def NewFile():
    answer = tkinter.messagebox.askokcancel(u'\u041d\u043e\u0432\u044b\u0438\u0306 \u0444\u0430\u0438\u0306\u043b', u'\u0412\u044b \u0442\u043e\u0447\u043d\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0438\u0306 \u0444\u0430\u0438\u0306\u043b? \u0412\u0441\u0435 \u043d\u0435\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u0308\u043d\u043d\u044b\u0435 \u0444\u0430\u0438\u0306\u043b\u044b \u0443\u0434\u0430\u043b\u044f\u0442\u0441\u044f')
    if answer:
        textbox.delete('1.0', 'end')
        textbox.pack()

def prg():
    tkinter.messagebox.showinfo('О программе', 'Вы используете PrintWord версии 1.3.1.\nСпасибо за выбор нашей программы!\n Евгений Чертин. 2023. ')

def LoadFile():
    global cur_path
    ftypes = [
     (u'\u0412\u0441\u0435 \u0444\u0430\u0439\u043b\u044b', '*'), (u'txt \u0444\u0430\u0439\u043b\u044b', '*.txt'), (u'\u0424\u0430\u0439\u043b\u044b Python', '*.py'), (u'\u0424\u0430\u0439\u043b\u044b html', '*.html'), (u'\u0424\u0430\u0439\u043b\u044b Microsoft Word', '*.docx'), (u'\u0444\u0430\u0439\u043b\u044b PrintWord 1.0', '*.sp78'), (u'\u0444\u0430\u0439\u043b\u044b PrintWord 1.1', '*.pw11')]
    fn = tkinter.filedialog.Open(app, filetypes=ftypes).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn).read())
    cur_path = fn


def SaveFile():
    file_path = filedialog.asksaveasfilename(defaultextension='.*', filetypes=(('Текстовые документы', '*.txt'), ('Все файлы', '*.'),  ('Файлы PrintWord', '*.prtw')))
    f = open(file_path, 'w', encoding='utf-8')
    text = textbox.get('1.0', END)
    f.write(text)
    f.close()

class App(tk.Tk):

    def __init__(self):
        super().__init__()


app = App()
app.geometry('1366x768')
app.title('PrintWord 1.3.1')
panelFrame = Frame(app, height=25, bg='steelblue')
textFrame = Frame(app, height=340, width=600)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font='Colibri 11', wrap=WORD)
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
menu = tk.Menu()
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label=u'\u041d\u043e\u0432\u044b\u0438\u0306 \u0444\u0430\u0438\u0306\u043b', command=NewFile)
file_menu.add_command(label=u'\u041e\u0442\u043a\u0440\u044b\u0442\u044c', command=LoadFile)
file_menu.add_separator()
file_menu.add_command(label=u'\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a', command=SaveFile)
menu.add_cascade(label=u'\u0424\u0430\u0438\u0306\u043b', menu=file_menu)
view_menu = Menu(menu, tearoff=0)
menu.add_cascade(label=u'\u0412\u0438\u0434', menu=view_menu)
view_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label=u'\u0421\u0432\u0435\u0442\u043b\u0430\u044f', command=(lambda : change_theme('light')))
view_menu_sub.add_command(label=u'\u0422\u0435\u0308\u043c\u043d\u0430\u044f', command=(lambda : change_theme('dark')))
view_menu.add_cascade(label=u'\u0422\u0435\u043c\u0430', menu=view_menu_sub)
font_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub.add_command(label='Times New Roman', command=(lambda : change_fonts('Times New Roman')))
font_menu_sub.add_command(label='Comic Sans MS', command=(lambda : change_fonts('CSMS')))
font_menu_sub.add_command(label='Colibri', command=(lambda : change_fonts('Colibri')))
font_menu_sub.add_command(label='Arial', command=(lambda : change_fonts('Arial')))
view_menu.add_cascade(label=u'\u0428\u0440\u0438\u0444\u0442', menu=font_menu_sub)
view_colors = {'dark':{'text_bg':'gray4', 
  'text_fg':'white'}, 
 'light':{'text_bg':'white', 
  'text_fg':'black'}}
fonts = {'Times New Roman':{'font': ('Times New Roman', 11)}, 
 'CSMS':{'font': ('Comic Sans MS', 11)}, 
 'Colibri':{'font': ('Colibri', 11)}, 
 'Arial':{'font': ('Arial', 11)}}
menu.add_command(label=u'\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435', command=prg)
menu.add_command(label=u'\u0412\u044b\u0438\u0306\u0442\u0438', command=app_exit)
app.config(menu=menu)
app.mainloop()
