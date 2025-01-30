import tkinter as tk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha(): #check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a') 
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process_message():
    text = entry_message.get()
    shift = int(entry_shift.get())
    if var.get() == 1:  # Encrypt
        result = encrypt(text, shift)
    else:  # Decrypt
        result = decrypt(text, shift)
    label_result.config(text=result)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")

# Create and place labels and entry fields
label_message = tk.Label(window, text="Enter Message:")
label_message.grid(row=0, column=0)

entry_message = tk.Entry(window)
entry_message.grid(row=0, column=1)

label_shift = tk.Label(window, text="Enter Shift:")
label_shift.grid(row=1, column=0)

entry_shift = tk.Entry(window)
entry_shift.grid(row=1, column=1)

var = tk.IntVar()
radio_encrypt = tk.Radiobutton(window, text="Encrypt", variable=var, value=1)
radio_encrypt.grid(row=2, column=0)

radio_decrypt = tk.Radiobutton(window, text="Decrypt", variable=var, value=2)
radio_decrypt.grid(row=2, column=1)

button_process = tk.Button(window, text="Process", command=process_message)
button_process.grid(row=3, columnspan=2)

label_result = tk.Label(window, text="")
label_result.grid(row=4, columnspan=2)

# Start the GUI loop
window.mainloop()
