import tkinter as tk


def on_return_press(event):
    text = event.widget
    # Get the text that was entered after the Return key was pressed
    input_text = text.get("end-1c linestart", "end-1c lineend")
    print("Input text:", input_text)

def main():
    app = tk.Tk()
    app.state("zoomed")
    app.config(bg='gray')

    # ========================================================= Navigation Bar ========================
    nav_bar_bg = "#232B2B"
    nav_bar = tk.Frame(app, bg=nav_bar_bg)
    nav_bar.place(x=0, y=0, relwidth=1, height=35)



    # ======================================================== Editor Section ============================

    Home_Tab = tk.Text(app, border=0)
    Home_Tab.place(y=35, relwidth=1, relheight=0.9)

    #Editor.bind("<Return>", on_return_press)





    app.mainloop()


if  __name__ == "__main__":
    main()