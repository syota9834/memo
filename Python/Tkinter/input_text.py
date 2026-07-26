import tkinter as tk


def show_text():
    value = entry.get()

    label.config(
        text=value
    )


root = tk.Tk()

root.title("入力テスト")
root.geometry("300x200")


entry = tk.Entry(root)
entry.pack()


button = tk.Button(
    root,
    text="表示",
    command=show_text
)

button.pack()


label = tk.Label(root)
label.pack()


root.mainloop()
