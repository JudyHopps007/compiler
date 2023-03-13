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

    Nav_Bar = tk.Frame(app)
    Nav_Bar.place()
    Editor = tk.Text(app)
    #Editor.place(relheight=1, relwidth=1, relx=0, rely=0)

    Editor.bind("<Return>", on_return_press)





    app.mainloop()


if  __name__ == "__main__":
    main()