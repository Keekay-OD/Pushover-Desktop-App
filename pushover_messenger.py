import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os

class PushoverMessengerApp:
    def __init__(self, master):
        self.master = master
        master.title("Pushover Messenger")
        master.geometry("600x500")

        # Configuration file
        self.config_file = 'pushover_config.json'
        
        # Tabs
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Create tabs
        self.create_send_message_tab()
        self.create_settings_tab()

        self.create_history_tab()

        # Load existing configuration
        self.load_config()

    def create_settings_tab(self):
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="Settings")

        # Token input
        tk.Label(settings_frame, text="Pushover API Token:").pack(pady=(10, 0))
        self.token_entry = tk.Entry(settings_frame, width=50)
        self.token_entry.pack(pady=5)

        # User Key input
        tk.Label(settings_frame, text="Pushover User Key:").pack(pady=(10, 0))
        self.user_key_entry = tk.Entry(settings_frame, width=50)
        self.user_key_entry.pack(pady=5)

        # Save Settings Button
        save_button = tk.Button(settings_frame, text="Save Settings", command=self.save_settings)
        save_button.pack(pady=20)

    def create_send_message_tab(self):
        send_frame = ttk.Frame(self.notebook)
        self.notebook.add(send_frame, text="Send Message")

        # Message input
        tk.Label(send_frame, text="Message:").pack(pady=(10, 0))
        self.message_entry = tk.Text(send_frame, height=5, width=50)
        self.message_entry.pack(pady=5)

        # Title input (optional)
        tk.Label(send_frame, text="Title (Optional):").pack(pady=(10, 0))
        self.title_entry = tk.Entry(send_frame, width=50)
        self.title_entry.pack(pady=5)

        # Send Button
        send_button = tk.Button(send_frame, text="Send Message", command=self.send_message)
        send_button.pack(pady=20)

    def create_history_tab(self):
        history_frame = ttk.Frame(self.notebook)
        self.notebook.add(history_frame, text="Message History")

        # Treeview for history
        self.history_tree = ttk.Treeview(history_frame, 
            columns=("Date", "Title", "Message"), 
            show='headings'
        )
        self.history_tree.heading("Date", text="Date")
        self.history_tree.heading("Title", text="Title")
        self.history_tree.heading("Message", text="Message")
        self.history_tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Clear History Button
        clear_button = tk.Button(history_frame, text="Clear History", command=self.clear_history)
        clear_button.pack(pady=10)

    def save_settings(self):
        token = self.token_entry.get()
        user_key = self.user_key_entry.get()

        if not token or not user_key:
            messagebox.showerror("Error", "Please enter both Token and User Key")
            return

        config = {
            'token': token,
            'user_key': user_key
        }

        with open(self.config_file, 'w') as f:
            json.dump(config, f)

        messagebox.showinfo("Success", "Settings saved successfully!")

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.token_entry.insert(0, config.get('token', ''))
                self.user_key_entry.insert(0, config.get('user_key', ''))
        except FileNotFoundError:
            pass

    def send_message(self):
        # Load configuration
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "Please configure settings first!")
            return

        message = self.message_entry.get("1.0", tk.END).strip()
        title = self.title_entry.get()

        if not message:
            messagebox.showerror("Error", "Message cannot be empty")
            return

        # Pushover API endpoint
        url = "https://api.pushover.net/1/messages.json"
        
        # Payload
        payload = {
            "token": config['token'],
            "user": config['user_key'],
            "message": message
        }
        
        # Optional title
        if title:
            payload["title"] = title

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Save to history
            self.save_to_history(title, message)

            # Clear message fields
            self.message_entry.delete("1.0", tk.END)
            self.title_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Message sent successfully!")

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to send message: {str(e)}")

    def save_to_history(self, title, message):
        from datetime import datetime
        
        # Ensure history file exists
        history_file = 'message_history.json'
        if not os.path.exists(history_file):
            with open(history_file, 'w') as f:
                json.dump([], f)

        # Load existing history
        with open(history_file, 'r') as f:
            history = json.load(f)

        # Add new message
        history.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'title': title,
            'message': message
        })

        # Save updated history
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=4)

        # Update treeview
        self.load_history()

    def load_history(self):
        history_file = 'message_history.json'
        
        # Clear existing treeview
        for i in self.history_tree.get_children():
            self.history_tree.delete(i)

        try:
            with open(history_file, 'r') as f:
                history = json.load(f)
                
            # Reverse to show most recent first
            for item in reversed(history):
                self.history_tree.insert('', 'end', values=(
                    item['date'], 
                    item.get('title', ''), 
                    item['message']
                ))
        except FileNotFoundError:
            pass

    def clear_history(self):
        history_file = 'message_history.json'
        
        # Confirm before clearing
        if messagebox.askyesno("Clear History", "Are you sure you want to clear message history?"):
            # Remove history file
            if os.path.exists(history_file):
                os.remove(history_file)
            
            # Clear treeview
            for i in self.history_tree.get_children():
                self.history_tree.delete(i)
            
            messagebox.showinfo("Success", "Message history cleared!")

def main():
    root = tk.Tk()
    app = PushoverMessengerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



