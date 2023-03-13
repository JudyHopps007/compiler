import tkinter as tk
global row_num_widget, Editor

keyword = ['if' ,'from']

def on_return_press(event):
    text = event.widget
    # Get the text that was entered after the Return key was pressed
    input_text = text.get("end-1c linestart", "end-1c lineend")
    print("Input text:", input_text)



def update_row_numbers(event=None):
    row_num_widget.config(state="normal") # Enable the Text widget
    row_num_widget.delete("1.0", "end") # Delete old roe detail information
    num_lines = Editor.index("end-1c").split(".")[0] # Get the number of lines in the Editor section
    for line_num in range(1, int(num_lines) + 1):  # Insert row numbers into the row_num_widget
        row_num_widget.insert("end", str(line_num) + "\n")
    row_num_widget.config(state="disabled") # Disable the Text widget


def colorize_text(event):
    # Remove existing tags
    Editor.tag_remove("red", "1.0", "end")
    Editor.tag_remove("green", "1.0", "end")
    Editor.tag_remove("black", "1.0", "end")

    # Get the text from the Text widget and split it into words
    text = Editor.get("1.0", "end")

    key = 0
    while key < len(keyword):
        index = text.find(keyword[key])
        while index != -1:
            tag = "green"
            color = "green"

            start = "1.%d" % index
            end = "1.%d" % (index+4)

            Editor.tag_add(tag, start, end)
            Editor.tag_config(tag, foreground=color)

            index = text.find("from", index + 1)
        key += 1

def main():
    global row_num_widget, Editor
    app = tk.Tk()
    app.state("zoomed")
    app.config(bg='gray')
    app.minsize(1000, 900)

    # ========================================================= Navigation Bar ========================
    nav_bar_bg = "#232B2B"
    nav_bar = tk.Frame(app, bg=nav_bar_bg)
    nav_bar.place(x=0, y=0, relwidth=1, height=35)





    # ======================================================== Editor Section ============================

    Text_Frame =  tk.Frame(app, border=0, bg='green')
    Text_Frame.place(x=0, y=35, relwidth=1, relheight=0.75)

    Editor_color = "#EEDC82"
    row_num_widget = tk.Text(Text_Frame, wrap="none", font=("Courier New", 12), width=4, padx=5, takefocus=0, border=0, background=Editor_color)
    row_num_widget.place(x=0, y=0, width=50, relheight=1)
    row_num_widget.config(state="disabled")

    Editor = tk.Text(Text_Frame, border=0, bg=Editor_color, font=("Courier New", 12), wrap="none")
    Editor.place(x=51, y=0, relwidth=1, relheight=1)

    scrollbar = tk.Scrollbar(Text_Frame, troughcolor=Editor_color, bg=Editor_color)
    scrollbar.pack(side="right", fill="y")

    # Link the scrollbar to the Text widget
    Editor.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Editor.yview, bg="blue")

    #Editor.bind("<Return>", on_return_press)
    Editor.bind("<Key>", update_row_numbers) # Bind the update_row_numbers function to changes in the text widget
    Editor.bind("<KeyRelease>", colorize_text)

    # ======================================================== Terminal  Section ============================

    Terminal = tk.Frame(app, border=0, bg='green')
    Terminal.place(x=0, rely=0.785, relwidth=1, relheight=0.2)





    app.mainloop()

if  __name__ == "__main__":
    main()