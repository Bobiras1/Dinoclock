from tkinter import *
import tkinter as tk
import math
import time

# Labels around the clock in clockwise order, starting at top (12 o'clock)
labels = [
    "Stegosaurus",
    "Triceratops",
    "Allosaurus",
    "Ankylosaurus",
    "Brachiosaurus",
    "Diplodocus",
    "Spinosaurus",
    "Velociraptor",
    "Anchiornis Huxleyi",
    "Tyranosaurus",
    "Archeopteryx",
    "Iguanodon"
]

# Clock size
WIDTH = 550
HEIGHT = 550
RADIUS = 200

# Create main window
root = tk.Tk()
root.title("Architectural Clock")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

center_x = WIDTH // 2
center_y = HEIGHT // 2

def draw_clock_face():
    """Draw the circle and labels."""
    # Outer circle
    canvas.create_oval(center_x - RADIUS, center_y - RADIUS,
                       center_x + RADIUS, center_y + RADIUS,
                       width=4)

    # Place the 12 labels
    for i, label in enumerate(labels):
        angle_deg = (i / len(labels)) * 360 - 90  # start from top
        angle_rad = math.radians(angle_deg)
        x = center_x + math.cos(angle_rad) * (RADIUS - 20)
        y = center_y + math.sin(angle_rad) * (RADIUS - 20)
        canvas.create_text(x, y, text=label, font=("Helvetica", 10))

def draw_hand(angle_deg, length, width, color):
    """Draw a single clock hand."""
    angle_rad = math.radians(angle_deg - 90)  # -90 so 0Β° is at top
    x = center_x + math.cos(angle_rad) * length
    y = center_y + math.sin(angle_rad) * length
    canvas.create_line(center_x, center_y, x, y,
                       width=width, fill=color)

def update_clock():
    """Update the clock hands in real time."""
    canvas.delete("hands")  # Remove previous hands (tagged as "hands")

    t = time.localtime()
    second = t.tm_sec
    minute = t.tm_min + second / 60
    hour = (t.tm_hour % 12) + minute / 60

    # Calculate angles
    second_angle = (second / 60) * 360
    minute_angle = (minute / 60) * 360
    hour_angle = (hour / 12) * 360

    # Draw hour, minute, second hands
    canvas.create_line(center_x, center_y,
                       center_x + math.cos(math.radians(hour_angle - 90)) * (RADIUS * 0.5),
                       center_y + math.sin(math.radians(hour_angle - 90)) * (RADIUS * 0.5),
                       width=6, fill="black", tags="hands")

    canvas.create_line(center_x, center_y,
                       center_x + math.cos(math.radians(minute_angle - 90)) * (RADIUS * 0.7),
                       center_y + math.sin(math.radians(minute_angle - 90)) * (RADIUS * 0.7),
                       width=4, fill="black", tags="hands")

    canvas.create_line(center_x, center_y,
                       center_x + math.cos(math.radians(second_angle - 90)) * (RADIUS * 0.85),
                       center_y + math.sin(math.radians(second_angle - 90)) * (RADIUS * 0.85),
                       width=2, fill="red", tags="hands")

    root.after(1000, update_clock)  # Update every second

# Draw the static clock face
draw_clock_face()
# Start updating the clock
update_clock()

root.mainloop()
