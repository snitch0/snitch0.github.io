import tkinter as tk
import time


def fuzz_bizz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FuzzBizz"
    elif n % 3 == 0:
        return "Fuzz"
    elif n % 5 == 0:
        return "Bizz"
    else:
        return str(n)


def update_counter():
    global counter
    counter += 1
    label_counter.config(text=f"カウントアップ: {counter}")
    label_fuzz_bizz.config(text=f"FuzzBizz: {fuzz_bizz(counter)}")
    root.after(1000, update_counter)


counter = 0

root = tk.Tk()
root.title("FuzzBizz カウンター")

label_counter = tk.Label(root, text=f"カウントアップ: {counter}", font=("Helvetica", 16))
label_counter.pack(pady=10)

label_fuzz_bizz = tk.Label(
    root, text=f"FuzzBizz: {fuzz_bizz(counter)}", font=("Helvetica", 16)
)
label_fuzz_bizz.pack(pady=10)

update_counter()

root.mainloop()
