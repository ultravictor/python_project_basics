import customtkinter as ct
from btns import *
#main window setting
win=ct.CTk()
win.title("Calculator")
win.geometry("350x480+1250+100")
win.resizable(False,False)
win.attributes("-topmost", True)
win.overrideredirect(True)
#Components
border=ct.CTkFrame(                                                                    #FRAME
    win,
    border_color="#4A90E2",
    fg_color="#1E1E1E",
    border_width=5,
    corner_radius=15
)

button_config = {
    "width": 60,
    "height": 60,
    "corner_radius": 40
}

#NUMBER BUTTONS
btn1=ct.CTkButton(
    border,
    text="C",
    command=num_button1,
    **button_config
)
btn2=ct.CTkButton(
    border,
    text="%",
    command=num_button2,
    **button_config
)
btn3=ct.CTkButton(
    border,
    text=".",
    command=num_button3,
    **button_config
)
btn4=ct.CTkButton(
    border,
    text="/",
    command=num_button4,
    **button_config
)

btn5=ct.CTkButton(
    border,
    text="7",
    command=num_button5,
    **button_config
)
btn6=ct.CTkButton(
    border,
    text="8",
    command=num_button6,
    **button_config
)
btn7=ct.CTkButton(
    border,
    text="9",
    command=num_button7,
    **button_config
)
btn8=ct.CTkButton(
    border,
    text="x",
    command=num_button8,
    **button_config
)
btn9=ct.CTkButton(
    border,
    text="4",
    command=num_button9,
    **button_config
)
btn10=ct.CTkButton(
    border,
    text="5",
    command=num_button10,
    **button_config
)
btn11=ct.CTkButton(
    border,
    text="6",
    command=num_button11,
    **button_config
)
btn12=ct.CTkButton(
    border,
    text="-",
    command=num_button12,
    **button_config
)
btn13=ct.CTkButton( 
    border,
    text="1",
    command=num_button13,
    **button_config
)
btn14=ct.CTkButton( 
    border,
    text="0",
    command=num_button14,
    **button_config
)
btn15=ct.CTkButton(
    border,
    text="+",
    command=num_button15,
    **button_config
)
btn16=ct.CTkButton(
    border,
    text="=",
    command=num_button16,
    **button_config
)
btn17=ct.CTkButton(
    border,
    text="CLOSE",
    width=300,
    height=40,
    command=win.destroy,
    fg_color="red", 
    text_color="white",
    corner_radius=40
)
# ROW 1 (y=120)
btn1.place(x=20, y=100)
btn2.place(x=100, y=100)
btn3.place(x=180, y=100)
btn4.place(x=260, y=100)

# ROW 2 (y=195)
btn5.place(x=20, y=175)
btn6.place(x=100, y=175)
btn7.place(x=180, y=175)
btn8.place(x=260, y=175)

# ROW 3 (y=270)
btn9.place(x=20, y=250)
btn10.place(x=100, y=250)
btn11.place(x=180, y=250)
btn12.place(x=260, y=250)

# ROW 4 (y=345)
btn13.place(x=20, y=325)
btn14.place(x=100, y=325)
btn15.place(x=180, y=325)
btn16.place(x=260, y=325)
# ROW 5 (y=420)
btn17.place(x=20, y=400)

#close_btn.pack(anchor="ne", padx=10, pady=10)



border.pack(fill="both",expand=True)
win.mainloop()