import tkinter as tk
global row_num_widget, Editor

def on_return_press(event):
    text = event.widget
    # Get the text that was entered after the Return key was pressed
    input_text = text.get("end-1c linestart", "end-1c lineend")
    print("Input text:", input_text)

def update_row_numbers(event=None):
    row_num_widget.delete("1.0", "end") # Delete old roe detail information
    num_lines = Editor.index("end-1c").split(".")[0] # Get the number of lines in the Editor section
    for line_num in range(1, int(num_lines) + 1):  # Insert row numbers into the row_num_widget
        row_num_widget.insert("end", str(line_num) + "\n")

def main():
    global row_num_widget, Editor
    app = tk.Tk()
    app.state("zoomed")
    app.config(bg='gray')

    # ========================================================= Navigation Bar ========================
    nav_bar_bg = "#232B2B"
    nav_bar = tk.Frame(app, bg=nav_bar_bg)
    nav_bar.place(x=0, y=0, relwidth=1, height=35)





    # ======================================================== Editor Section ============================

    Text_Frame =  tk.Frame(app, border=0, bg='green')
    Text_Frame.place(x=45, y=35, relwidth=0.6, relheight=0.9)


    row_num_widget = tk.Text(Text_Frame, width=4, padx=5, takefocus=0, border=0, background="#f7f7f7")
    row_num_widget.place(x=0, y=0, width=45, relheight=1)

    Editor = tk.Text(Text_Frame, border=0, bg='#EEDC82')
    Editor.place(x=45, y=0, relwidth=1, relheight=1)

    scrollbar = tk.Scrollbar(Text_Frame, troughcolor="red")
    scrollbar.pack(side="right", fill="y")

    # Link the scrollbar to the Text widget
    Editor.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Editor.yview)

    #Editor.bind("<Return>", on_return_press)
    Editor.bind("<Key>", update_row_numbers) # Bind the update_row_numbers function to changes in the text widget




    app.mainloop()


if  __name__ == "__main__":
    main()