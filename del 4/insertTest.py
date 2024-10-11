import tkinter as tk

root = tk.Tk()
root.title("Message Widget Example")

# Create a Message widget with a long text
msg_text = "This is a long message that will wrap to multiple lines. " * 10
msg = tk.Message(root, text=msg_text, width=300, font=("Helvetica", 16))

# Set the width and height of the Message widget
msg.config(width=3000, padx=50, pady=50)
msg.pack()

root.mainloop()
