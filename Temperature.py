import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result_c.set(f"{temp:.2f} °C")
            result_f.set(f"{f:.2f} °F")
            result_k.set(f"{k:.2f} K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result_c.set(f"{c:.2f} °C")
            result_f.set(f"{temp:.2f} °F")
            result_k.set(f"{k:.2f} K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result_c.set(f"{c:.2f} °C")
            result_f.set(f"{f:.2f} °F")
            result_k.set(f"{temp:.2f} K")

        else:
            messagebox.showerror("Error", "Please select a unit")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Main Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.resizable(False, False)

# Variables
result_c = tk.StringVar()
result_f = tk.StringVar()
result_k = tk.StringVar()

# Title
tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Temperature:").grid(row=0, column=0, padx=5, pady=5)
entry_temp = tk.Entry(frame)
entry_temp.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Unit:").grid(row=1, column=0, padx=5, pady=5)
combo_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.grid(row=1, column=1)
combo_unit.current(0)

# Convert Button
tk.Button(root, text="Convert", width=15, command=convert_temperature).pack(pady=10)

# Output Frame
output = tk.Frame(root)
output.pack(pady=10)

tk.Label(output, text="Celsius:").grid(row=0, column=0, padx=5)
tk.Entry(output, textvariable=result_c, state="readonly").grid(row=0, column=1)

tk.Label(output, text="Fahrenheit:").grid(row=1, column=0, padx=5)
tk.Entry(output, textvariable=result_f, state="readonly").grid(row=1, column=1)

tk.Label(output, text="Kelvin:").grid(row=2, column=0, padx=5)
tk.Entry(output, textvariable=result_k, state="readonly").grid(row=2, column=1)

root.mainloop()
