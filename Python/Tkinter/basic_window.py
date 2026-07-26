import tkinter as tk

# メインウィンドウを作成
root = tk.Tk()

# ウィンドウタイトル
root.title("My App")

# ウィンドウサイズ
root.geometry("400x300")

# ラベルを作成
label = tk.Label(
    root,
    text="Hello World"
)

# ラベルを配置
label.pack()

# イベントループを開始
root.mainloop()
