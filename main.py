import tkinter
from tkinter import *
from datetime import datetime


new_y = 140
reply_count = 0

def update_time():
    current_time = datetime.now().strftime("%H:%M")
    return current_time

def contact1_chat(window):
    for widget in window.winfo_children():
        widget.destroy()

    current_time = datetime.now().strftime("%H:%M")

    # Display background
    image_contact_chat_bg = PhotoImage(file="images/wallpaper_bg.png")
    contact_chat_bg = Label(window, image=image_contact_chat_bg)
    contact_chat_bg.place(x=0, y=0, relwidth=1, relheight=1)
    contact_chat_bg.image = image_contact_chat_bg

    # display contact PHOTO
    photo = PhotoImage(file="images/contact for upper screen.png ")
    photo_label = Label(window, image=photo, width=395, height=60)
    photo_label.image = photo
    photo_label.place(x=1, y=1)

    # first/unread massage
    c1_first_msg = Label(window, text=f"Hello! ({current_time})", font=("Arial", 12), fg="black", bg="light blue", anchor="e")
    c1_first_msg.place(x=280, y=100)

    # display contact names
    name = Label(window, text="Youssef", fg="light blue", bg="black", font=("Arial", 20), bd=15)
    name.pack(side=TOP)

    # type a massage
    text = Label(window, text="message")
    text.pack(side=LEFT, anchor="sw")

    # msg ENTRY
    E = Entry(window, font="large_font")
    E.pack(side=BOTTOM, anchor="sw", fill=X)



    def bot_reply_function():
        global new_y
        global reply_count
        if reply_count >4:
            pass
        else:

            loading_label = Label(window, text="", font=("Arial", 12), fg="black", bg="light blue", anchor="e")
            loading_label.place(x=350, y=new_y)

            def show_reply():
                global new_y
                global reply_count
                reply_msg = ""

                if reply_count == 0:
                    reply_msg = f"HI, I am Youssef ({update_time()})"
                elif reply_count == 1:
                    reply_msg = f"How are you? ({update_time()})"
                elif reply_count == 2:
                    reply_msg = f"Can I get full mark? ({update_time()})"
                elif reply_count == 3:
                    reply_msg = f" Thank you so much! ({update_time()})"
                elif reply_count == 4:
                    reply_msg = f"I will go study. Bye! ({update_time()})"
                print(reply_msg)

                bot_label = Label(window, text=reply_msg, font=("Arial", 12), fg="black", bg="light blue", anchor="e")
                bot_label.place(x=200, y=new_y)
                new_y += 40
                reply_count += 1

            def show_dot_3():
                loading_label.config(text=". . .")
                window.after(500, show_reply)
                print(". . . ")

            def show_dot_2():
                loading_label.config(text=". .")
                window.after(500, show_dot_3)
                print(". .")

            def show_dot_1():
                loading_label.config(text=".")
                window.after(500, show_dot_2)
                print(".")

            show_dot_1()

    # SEND NEW LABELS
    def send_function():
        global new_y

        d = E.get()

        if len(d) == 0:
            pass
        else:
            label_text = f"{d} ({update_time()})"
            user_label = Label(window, text=label_text, font=("Arial", 12), anchor="w")
            user_label.place(x=30, y=new_y)
            E.delete(0, END)

            # distance between next msg
            new_y += 40

            # reply after 1 min
            window.after(1000, bot_reply_function)

    # SEND BUTTON
    send_button = Button(window, text="send", fg="black", bg="green", command=send_function)
    send_button.place(x=365, y=680)


def contact_screen():
    # Window1 SET UP
    window1 = Tk()
    window1.title("WhatsApp")
    window1.geometry("400x705+800+220")  # Center The window
    window1.resizable(False, False)  # makes window1 not resizable
    window1.config(bg="green")

    # Window1 BackGround
    image_whatsapp = PhotoImage(file="images/Contact_Screen.png")
    window1_bg = Label(window1, image=image_whatsapp)
    window1_bg.place(x=0, y=0, relwidth=1, relheight=1)
    window1_bg.pack()

    # CONTACTS
    # Contact [ ONE ] Button Set up (Important Contact)
    image_contact1 = PhotoImage(file="images/c1.png")
    button_contact1 = tkinter.Button(window1, image=image_contact1, width=400, height=65,
                                     command=lambda: contact1_chat(window1))
    button_contact1.place(x=0, y=210)

    # Contact [ TWO ] Button Set up (Just for show)
    image_contact2 = PhotoImage(file="images/c2.png")
    button_contact2 = tkinter.Button(window1, image=image_contact2, width=400, height=70)
    button_contact2.place(x=0, y=279)

    # Contact [ THREE ] Button Set up (Just for show)
    image_contact3 = PhotoImage(file="images/c3.png")
    button_contact3 = tkinter.Button(window1, image=image_contact3, width=400, height=70)
    button_contact3.place(x=0, y=349)

    # Contact [ FOUR ] Button Set up (Just for show)
    image_contact4 = PhotoImage(file="images/c4.png")
    button_contact4 = tkinter.Button(window1, image=image_contact4, width=400, height=70)
    button_contact4.place(x=0, y=420)

    # Contact [ FIVE ] Button Set up (Just for show)
    image_contact5 = PhotoImage(file="images/c5.png")
    button_contact5 = tkinter.Button(window1, image=image_contact5, width=400, height=70)
    button_contact5.place(x=0, y=490)

    window1.mainloop()


contact_screen()


