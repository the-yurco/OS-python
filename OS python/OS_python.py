from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter
import webbrowser
import pygame
from tkinter import filedialog
from tkinter import messagebox
from pygame.mixer import stop


def music():
    global plocha2
    plocha2 = Toplevel(plocha)
    plocha2.title("MUSIC")
    plocha2.geometry("500x500")
    plocha2.config(background="orangered2")

    pygame.mixer.init()

    def add_song():
        song = filedialog.askopenfilename(
            initialdir="hudba/", title="Vyber si pesnicku", filetypes=(("mp3 files", "*.mp3"),))
        song = song.replace("C:/hudba/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)

    def add_many_songs():
        songs = filedialog.askopenfilenames(
            initialdir="hudba/", title="Vyber si pesnicku", filetypes=(("mp3 files", "*.mp3"),))

        for song in songs:
            song = song.replace("C:/hudba/", "")
            song = song.replace(".mp3", "")

            song_box.insert(END, song)

    def play():
        song = song_box.get(ACTIVE)

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    def stop():
        pygame.mixer.music.stop()
        song_box.selection_clear(ACTIVE)

    def next_button():
        next_one = song_box.curselection()

        next_one = next_one[0]+1

        song = song_box.get(next_one)

        song = f"C:/hudba/{song}.mp3"

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        song_box.selection_clear(0, END)

        song_box.activate(next_one)

        song_box.selection_set(next_one, last=None)

    def delete_song():
        song_box.delete(ANCHOR)
        pygame.mixer.music.stop()

    def delete_all_songs():
        song_box.delete(0, END)

        pygame.mixer.music.stop()

    global paused
    paused = False

    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    song_box = Listbox(plocha2, bg="black", fg="orangered2",
                       width=60, selectbackground="gray", selectforeground="black")
    song_box.pack(pady=20)

    # buttony
    back_btn_img = PhotoImage(
        file="C:\SKUSANIE KODOV\graphical user\+OS 1.1\previous.png")
    forward_btn_img = PhotoImage(
        file="C:\SKUSANIE KODOV\graphical user\+OS 1.1\ext.png")
    play_btn_img = PhotoImage(
        file="C:\SKUSANIE KODOV\graphical user\+OS 1.1\play.png")
    pause_btn_img = PhotoImage(
        file="C:\SKUSANIE KODOV\graphical user\+OS 1.1\pause.png")
    stop_btn_img = PhotoImage(
        file="C:\SKUSANIE KODOV\graphical user\+OS 1.1\stop.png")

    controls_frame = Frame(plocha2)
    controls_frame.pack()

    forward_button = Button(
        controls_frame, image=forward_btn_img, borderwidth=0, command=next_button)
    play_button = Button(controls_frame, image=play_btn_img,
                         borderwidth=0, command=play)
    pause_button = Button(controls_frame, image=pause_btn_img,
                          borderwidth=0, command=lambda: pause(paused))
    stop_button = Button(controls_frame, image=stop_btn_img,
                         borderwidth=0, command=stop)

    forward_button.grid(row=0, column=1, padx=10)
    play_button.grid(row=0, column=2, padx=10)
    pause_button.grid(row=0, column=3, padx=10)
    stop_button.grid(row=0, column=4, padx=10)

    my_menu = Menu(plocha2)
    plocha2.config(menu=my_menu)

    add_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Pridat pesnicku:", menu=add_song_menu)
    add_song_menu.add_command(
        label="Pridat jednu pesnicku do plylistu", command=add_song)

    add_song_menu.add_command(
        label="Pridat viac pesniciek do plylistu", command=add_many_songs)

    remove_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Vymazat pesnicky", menu=remove_song_menu)
    remove_song_menu.add_command(
        label="Vymazat jednu pesnicku do plylistu", command=delete_song)
    remove_song_menu.add_command(
        label="V ymazat viac pesniciek do plylistu", command=delete_all_songs)

    plocha2.mainloop()


def notepad():
    global plocha3
    plocha3 = Toplevel(plocha)
    plocha3.title("NOTEPAD")
    plocha3.geometry("500x500")
    plocha3.config(background="cyan2")

    my_frame = Frame(plocha3)
    my_frame.pack(pady=5)

    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    my_text = Text(my_frame, width=40, height=25, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()

    text_scroll.config(command=my_text.yview)

    plocha3.mainloop()


def game():
    root = Tk()
    root.title('Piskorky')
    root.geometry('320x360')

# X ide prve
    kliknutie = True
    kroky = 0

# vypnutie tlacitok
    def vypnutie_tlacitok():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

# funkcia na checknutie kto vyhral

    def checknutiektovyhral():
        global vyherca
        vyherca = False

        if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
            b1.config(bg='deeppink2')
            b2.config(bg='deeppink2')
            b3.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
            b4.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b6.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
            b7.config(bg='deeppink2')
            b8.config(bg='deeppink2')
            b9.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()

        elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
            b1.config(bg='deeppink2')
            b4.config(bg='deeppink2')
            b7.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()

        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
            b2.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b8.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()

        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
            b3.config(bg='deeppink2')
            b6.config(bg='deeppink2')
            b9.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()

        elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
            b1.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b9.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()
        elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
            b3.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b7.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()

        # ked vyhra O

        elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
            b1.config(bg='deeppink2')
            b2.config(bg='deeppink2')
            b3.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()
        elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
            b4.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b6.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()
        elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
            b7.config(bg='deeppink2')
            b8.config(bg='deeppink2')
            b9.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'X vyhrava!!')
            vypnutie_tlacitok()

        elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
            b1.config(bg='deeppink2')
            b4.config(bg='deeppink2')
            b7.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()

        elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
            b2.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b8.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()

        elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
            b3.config(bg='deeppink2')
            b6.config(bg='deeppink2')
            b9.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()

        elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
            b1.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b9.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()
        elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
            b3.config(bg='deeppink2')
            b5.config(bg='deeppink2')
            b7.config(bg='deeppink2')
            vyherca = True
            messagebox.showinfo('Piskorky', 'O vyhrava!!')
            vypnutie_tlacitok()

        # remiza
        if kroky == 9 and vyherca == False:
            messagebox.showinfo('Piskorky', 'Je to remiza\n nikto nevyhrava!!')
    # kliknutie tlacitka funkcia

    def b_click(b):
        global kliknutie, kroky

        if b['text'] == ' ' and kliknutie == True:
            b['text'] = 'X'
            kliknutie = False
            kroky += 1
            checknutiektovyhral()
        elif b['text'] == ' ' and kliknutie == False:
            b['text'] = 'O'
            kliknutie = True
            kroky += 1
            checknutiektovyhral()
        else:
            messagebox.showerror(
                'Piskorky', 'Toto policko uz bolo vybrate\nvyber si ine...')

    # restart funkcia

    def restart():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global kliknutie, kroky
        kliknutie = True
        kroky = 0

        # tlacitka
        b1 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b1))
        b2 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b2))
        b3 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b3))

        b4 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b4))
        b5 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b5))
        b6 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b6))

        b7 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b7))
        b8 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b8))
        b9 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6,
                    bg='SystemButtonFace', background="pink", command=lambda: b_click(b9))

    # mriezka tlacitiek

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    # menu

    moje_menu = Menu(root)
    root.config(menu=moje_menu)

    # nastavenia menu

    nastavenia_menu = Menu(moje_menu, tearoff=False)
    moje_menu.add_cascade(label='Nastavenia', menu=nastavenia_menu)
    nastavenia_menu.add_command(label='Restartovat hru', command=restart)

    restart()

    root.mainloop()


def chrome():
    global plocha5
    plocha5 = Toplevel(plocha)
    plocha5.title("CHROME")
    plocha5.geometry("500x500")
    plocha5.config(background="yellow")

    def open_browser(e):
        webbrowser.open_new("https://www.google.com/")

    my_button = Button(plocha5, text="Google Chrome", font=(
        "Helvetica", 24), command=lambda: open_browser(1))
    my_button.pack(pady=50)
    my_button.config(background="cyan2")

    plocha5.mainloop()


def main_screen():
    global plocha

    plocha = Tk()
    plocha.title("+OS.1.1")
    plocha.iconbitmap("")
    plocha.geometry("500x500")
    plocha.config(background="gray12")

    Button(plocha, text="MUSIC", bg="orangered2",
           width="10", height="1", command=music).pack()
    Button(plocha, text="NOTEPAD", bg="cyan2",
           width="10", height="1", command=notepad).pack()
    Button(plocha, text="GAME", bg="deeppink2",
           width="10", height="1", command=game).pack()
    Button(plocha, text="CHROME", bg="yellow",
           width="10", height="1", command=chrome).pack()

    plocha.mainloop()


main_screen()
