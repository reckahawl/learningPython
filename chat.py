import tkinter as tk
import requests
from datetime import datetime
import sqlite3

DATABASE_FILE = "chat.db"
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    timestamp TEXT
)
"""

class ChatPanel(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # create labels and entries for username and password
        tk.Label(self, text="Username:").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)
        tk.Label(self, text="Password:").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        # create login button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1)

        # create text box for chat messages
        self.chat_box = tk.Text(self)
        self.chat_box.grid(row=3, column=0, columnspan=2)

        # create entry for sending messages
        self.message_entry = tk.Entry(self)
        self.message_entry.grid(row=4, column=0)
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.grid(row=4, column=1)

        # create database connection and table
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.conn.cursor()
        self.cursor.execute(CREATE_TABLE_QUERY)
        self.conn.commit()

    def login(self):
        # check username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = requests.post("http://localhost:8000/login", data={"username": username, "password": password})
        if response.status_code == 200:
            self.login_button.configure(state="disabled")
            self.username_entry.configure(state="disabled")
            self.password_entry.configure(state="disabled")
            self.chat_box.configure(state="normal")
            self.message_entry.configure(state="normal")
            self.send_button.configure(state="normal")
            self.chat_box.insert(tk.END, "You are logged in.\n")
        else:
            self.chat_box.insert(tk.END, "Invalid username or password.\n")

    def send_message(self):
        message = self.message_entry.get()
        username = self.username_entry.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.chat_box.insert(tk.END, f"{username}: {message}\n")
        self.message_entry.delete(0, tk.END)
        self.cursor.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)", (username, message, timestamp))
        self.conn.commit()
        response = requests.post("http://localhost:8000/message", data={"username": username, "message": message, "timestamp": timestamp})

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chat Panel")

    chat_panel = ChatPanel(root)
    chat_panel.pack()

    root.mainloop()
