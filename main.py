import tkinter as tk

global row_num_widget, Editor, Terminal, Terminal_display
import platform
import os
import ctypes
import re

# Disable DPI awareness on Windows
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ctypes.windll.shcore.SetProcessDpiAwareness(True)




def on_return_press():
    user_input = Editor.get("1.0", "end")
    # Get the text that was entered after the Return key was pressed
    # input_text = text.get("end-1c linestart", "end-1c lineend")
    print("Input text:", user_input)
    Terminal_display.delete("1.0", "end")
    Terminal_display.insert("1.0", user_input)


def update_row_numbers(event=None):
    row_num_widget.config(state="normal")  # Enable the Text widget
    row_num_widget.delete("1.0", "end")  # Delete old roe detail information
    num_lines = Editor.index("end-1c").split(".")[0]  # Get the number of lines in the Editor section
    for line_num in range(1, int(num_lines) + 1):  # Insert row numbers into the row_num_widget
        row_num_widget.insert("end", str(line_num) + "\n")
    row_num_widget.config(state="disabled")  # Disable the Text widget

def colorize_text(event):
    add_space()
    keyword = ['if', 'from']
    # Remove existing tags
    Editor.tag_remove("red", "1.0", "end")
    Editor.tag_remove("green", "1.0", "end")
    Editor.tag_remove("black", "1.0", "end")


    for key in keyword:
        start = "1.0"
        key_length = len(key)
        while True:
            #start = Editor.search(key, start, stopindex="end", nocase=True)
            start = Editor.search(r"\y" + re.escape(key) + r"\y", start, stopindex="end", regexp=True)
            if not start:
                break
            dif = int(start[2:])
            dif = dif + key_length
            end = start[0: 2] + f"{dif}"
            #end = f"{start}+{len(key)}c"
            Editor.tag_add("green", start, end)
            Editor.tag_config("green", foreground="green")
            start = end


def add_space(): # to Insert a space at the beginning of each line
    current_line = Editor.index(tk.INSERT).split(".")[0]
    current_char = Editor.index(tk.INSERT).split(".")[1]
    if current_char == '0':
        Editor.insert(f"{current_line}.0", " ")






def main():
    global row_num_widget, Editor, Terminal, Terminal_display
    app = tk.Tk()
    # app.state("zoomed")
    app.config(bg='gray')
    app.minsize(1000, 900)

    container = tk.Frame(app, bg="#232B2B")
    container.place(x=0, y=0, relwidth=1, relheight=1)

    # ========================================================= Navigation Bar ========================
    nav_bar_bg = "#232B2B"
    nav_bar = tk.Frame(container, bg=nav_bar_bg)
    nav_bar.place(x=0, y=0, relwidth=1, height=35)

    nav_bar = tk.Button(nav_bar, bg=nav_bar_bg, text="Run", fg='white', borderwidth=0, border=0, activebackground=nav_bar_bg, activeforeground="green", command=on_return_press)
    nav_bar.place(x=0, y=0, relwidth=0.05, relheight=1)

    # ======================================================== Editor Section ============================

    Text_Frame = tk.Frame(container, border=0, bg=nav_bar_bg)
    Text_Frame.place(x=0, y=35, relwidth=1, relheight=0.75)

    Editor_color = "#3A3A38"
    row_num_widget = tk.Text(Text_Frame, wrap="none", font=("Courier New", 12), width=4, padx=5, takefocus=0, border=0, background=Editor_color)
    row_num_widget.place(x=0, y=0, width=50, relheight=1)
    row_num_widget.config(state="disabled")

    Editor = tk.Text(Text_Frame, border=0, bg=Editor_color, font=("Courier New", 12), wrap="none", fg='white')
    Editor.place(x=51, y=0, relwidth=1, relheight=1)
    Editor.insert("insert", " ")

    Editor.bind("<Key>", update_row_numbers)  # Bind the update_row_numbers function to changes in the text widget
    Editor.bind("<KeyRelease>", colorize_text)

    # Define a function to synchronize the scrolling of the two widgets
    def sync_scrollbar(*args):
        Editor.yview_moveto(args[0])
        row_num_widget.yview_moveto(args[0])

    # Bind the <Configure> and <MouseWheel> events of both widgets to the synchronization function
    for widget in (Editor, row_num_widget):
        widget.bind("<Configure>", lambda event: sync_scrollbar(event.widget.yview()[0]))
        widget.bind("<MouseWheel>", lambda event: sync_scrollbar(event.widget.yview()[0]))

    # ======================================================== Terminal  Section ============================
    Text_Frame_2 = tk.Frame(container, border=0, bg=nav_bar_bg)
    Text_Frame_2.place(x=0, rely=0.79, relwidth=1, relheight=0.2)

    Terminal_display = tk.Text(Text_Frame_2, border=0, bg=Editor_color, font=("Courier New", 12), wrap="none")
    Terminal_display.place(x=51, y=0, relwidth=1, relheight=1)

    scrollbar2 = tk.Scrollbar(Text_Frame_2, troughcolor=Editor_color, bg=Editor_color)
    scrollbar2.pack(side="right", fill="y")

    # Link the scrollbar to the Text widget
    Terminal_display.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=Terminal_display.yview, bg="blue")

    app.mainloop()


if __name__ == "__main__":
    main()
