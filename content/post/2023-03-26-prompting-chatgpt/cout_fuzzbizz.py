import time
from tkinter import *
from tkinter import ttk


def fizz_buzz(number):
    """FuzzBizz問題を解決する関数です。

    引数:
        number (int): FuzzBizz問題に適用する整数

    戻り値:
        str: FuzzBizz問題の結果
    """
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def update_count():
    """カウントアップする数字とFuzzBizzの結果を更新し、ラベルに表示します。"""
    global count
    count += 1
    count_label.config(text=str(count))
    fizz_buzz_result = fizz_buzz(count)
    fizz_buzz_label.config(text=fizz_buzz_result)
    root.after(1000, update_count)


count = 0

# GUIの作成
root = Tk()
root.title("FizzBuzzカウンター")

frame = ttk.Frame(root, padding="30 15")
frame.grid(row=0, column=0, sticky=(W, E, N, S))

count_label = ttk.Label(frame, text=str(count), font=("Helvetica", 24))
count_label.grid(row=0, column=0, pady=10)

fizz_buzz_label = ttk.Label(frame, text="", font=("Helvetica", 24))
fizz_buzz_label.grid(row=1, column=0, pady=10)

# カウントアップとFuzzBizzの結果を更新
root.after(1000, update_count)

root.mainloop()