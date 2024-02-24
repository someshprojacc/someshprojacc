import tkinter as tk
from tkinter import messagebox


# I wanted to upload file.py format because i made gui program
# So you can test it.
# Its made on VS Code

def convert_number_to_words(number):
    # Define lists for digits, tens, and special cases
    units = ['', 'One', 'Two', 'Three', 'Four',
             'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
             'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty',
            'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million', 'Billion',
                 'Trillion', 'Quadrillion', 'Quintillion']

    # Function to convert numbers less than 1000 to words
    def convert_less_than_thousand(num):
        if num == 0:
            return ''
        elif num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ' ' + convert_less_than_thousand(num % 10)
        else:
            return units[num // 100] + ' Hundred ' + convert_less_than_thousand(num % 100)

    # Function to convert numbers greater than 1000 to words
    def convert(num):
        if num == 0:
            return 'Zero'

        words = ''
        for i in range(len(thousands)):
            if num % 1000 != 0:
                words = convert_less_than_thousand(
                    num % 1000) + ' ' + thousands[i] + ' ' + words
            num //= 1000
        return words.strip()

    return convert(number)


def convert_number():
    try:
        number = int(entry.get())
        if abs(number) > 999999999999999999:
            messagebox.showerror(
                "Error", "Number is too large. Please enter a number with at most 18 digits.")
        else:
            words = convert_number_to_words(number)
            # Format the result to wrap every 3 words
            formatted_words = '\n'.join(
                [' '.join(words.split()[i:i+3]) for i in range(0, len(words.split()), 3)])
            # Display
            result_label.config(text=f"Equivalent words:\n{formatted_words}")
    except ValueError:
        messagebox.showerror(
            "Error", "Invalid input. Please enter a valid integer number.")


def change_button_color(event):
    if event == 'enter':
        convert_button.config(bg='lightgreen')
    elif event == 'leave':
        convert_button.config(bg='lightblue')


def about_message():
    messagebox.showinfo(
        "About", "Made by Somesh H. Kumar \n OR \n Somesh Roy \n For EXTERN CLUB PROJECT")


def copy_text():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))


def change_copy_button_color(event):
    if event == 'enter':
        copy_button.config(bg='lightgreen')
    elif event == 'leave':
        copy_button.config(bg='lightblue')


# Create the main GUI application window
root = tk.Tk()
root.title("Number to Words Converter")
root.geometry("1200x700")  # Set initial size of the window
# Minimum size of Window so window not look ugly when size changed
root.minsize(1200, 600)
root.config(bg='lightblue')

# Create and configure Widgets To Display in Window
entry_label = tk.Label(
    root, text="Enter an integer number (up to 18 digits):", fg="green", font=("Helvetica", 20))
entry = tk.Entry(root, width=30, font=("Helvetica", 20))
convert_button = tk.Button(
    root, text="Convert", command=convert_number, font=("Helvetica", 20))
convert_button.bind('<Enter>', lambda event: change_button_color('enter'))
convert_button.bind('<Leave>', lambda event: change_button_color('leave'))
result_label = tk.Label(root, text="Equivalent words:",
                        # Changed text color to blue
                        fg="blue", font=("Helvetica", 18))
# Background color
result_label.config(bg="lightyellow")

# Widgets in the window configuring display objects
entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
entry.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
convert_button.grid(row=1, column=0, columnspan=2,
                    padx=10, pady=5, sticky="nsew")
result_label.grid(row=2, column=0, columnspan=2,
                  padx=10, pady=5, sticky="nsew")

# Menu button
menubar = tk.Menu(root)
menubar.config(bg="lightgreen", fg="red", activebackground="lightgreen")
menubar.add_command(label="About", command=about_message)
root.config(menu=menubar)

# Add a button to copy text
copy_button = tk.Button(
    root, text="Copy", command=copy_text, font=("Helvetica", 20))
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
copy_button.bind('<Enter>', lambda event: change_copy_button_color('enter'))
copy_button.bind('<Leave>', lambda event: change_copy_button_color('leave'))

root.mainloop()
