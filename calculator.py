import tkinter

# ---------------- SETTINGS ---------------- #

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

A = "0"
operator = None
B = None

# --------------- FUNCTIONS ---------------- #

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        return str(int(num))
    return str(num)

def button_clicked(value):
    global A, B, operator

    # ------------- RIGHT SIDE OPERATORS ------------- #
    if value in right_symbols:
        if value == "=":
            if operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    result = numA + numB
                elif operator == "-":
                    result = numA - numB
                elif operator == "×":
                    result = numA * numB
                elif operator == "÷":
                    result = numA / numB

                label["text"] = remove_zero_decimal(result)
                clear_all()
            return

        # Store operator
        if operator is None:
            A = label["text"]
            label["text"] = "0"
        operator = value
        return

    # ---------------- TOP SPECIAL BUTTONS ---------------- #
    if value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

        elif value == "√":
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)

        return

    # ---------------- NUMBERS AND DECIMAL ---------------- #
    if value == ".":
        if "." not in label["text"]:
            label["text"] += "."
        return

    if value.isdigit():
        if label["text"] == "0":
            label["text"] = value
        else:
            label["text"] += value
        return


# --------------------- UI SETUP ----------------------- #

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=color_black,
    foreground=color_white,
    anchor="e",
    width=4
)
label.grid(row=0, column=0, columnspan=4, sticky="we")

# create buttons
for r, row in enumerate(button_values):
    for c, val in enumerate(row):
        btn = tkinter.Button(
            frame, text=val, font=("Arial", 30),
            width=4, height=1,
            command=lambda v=val: button_clicked(v)
        )

        if val in top_symbols:
            btn.config(background=color_light_gray, foreground=color_black)
        elif val in right_symbols:
            btn.config(background=color_orange, foreground=color_white)
        else:
            btn.config(background=color_dark_gray, foreground=color_white)

        btn.grid(row=r+1, column=c)

frame.pack()

# ------------- CENTER WINDOW ------------- #
window.update()
W = window.winfo_width()
H = window.winfo_height()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

x = (sw // 2) - (W // 2)
y = (sh // 2) - (H // 2)

window.geometry(f"{W}x{H}+{x}+{y}")
window.mainloop()
