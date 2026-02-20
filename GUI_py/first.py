from tkinter import *
import customtkinter as ct
root=ct.CTk()
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")
root.title("Harshit Ranjan")
root.geometry("800x600")
label=ct.CTkLabel(#Label
    root,
    text="ka ji babu dbawa jor se",
    font=("Arial",20),
    text_color=("green")
)
label.pack(pady=20)
def button_clicked():#button function
    print("WOW")
button=ct.CTkButton(#button
    root,
    text="Dbao na",
    command=button_clicked,
    width=200,
    height=40,
    hover_color="black"
)
def get_input():#Entry function
    text= Entry.get()
    print(f"you Entered: {text}")
entry_val=ct.CTkEntry(#entry
    root,
    placeholder_text="Enter your name",
    width=200,
)
button2=ct.CTkButton(#button2 do nothing
    root,
    text="submit",
    width=200
)
def checkbox_event():#checkbox function
    print(f"Checkbox is:{checkbox_var.get()}")
checkbox_var=ct.StringVar(value="off")#defualt should be off
checkbox=ct.CTkCheckBox(#checkbox
    root,
    text="I am agree to",
    variable=checkbox_var, 
    checkbox_height=20,
    checkbox_width=20,
    onvalue="on",
    offvalue="off",
    command=checkbox_event
)
radio_var=ct.IntVar(value=1)
radio1=ct.CTkRadioButton(
    root,
    text="Option1",
    variable=radio_var,
    value=1
)
radio2=ct.CTkRadioButton(
    root,
    text="option2",
    variable=radio_var,
    value=2
)
def slider_event(value):
    print(f"sloder value:{value}")
slider=ct.CTkSlider(
    root,
    from_=0,
    to=100,
    number_of_steps=20,
    command=slider_event
)
progress=ct.CTkProgressBar(
    root,
    width=300
)
progress.pack(pady=20)
progress.set(0.5)
slider.pack(pady=20)
#packs
radio1.pack(pady=20)
radio2.pack(pady=20)
checkbox.pack(pady=20)
entry_val.pack(pady=20)
button2.pack(pady=10)
button.pack(pady=20)
root.mainloop()