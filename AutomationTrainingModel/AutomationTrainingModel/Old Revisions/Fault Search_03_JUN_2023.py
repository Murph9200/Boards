import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
import os

def search_keywords_in_file(file_path, keywords):
    found_solutions = []
    total_keywords = len(keywords)
    max_percentage_match = 0
    best_solution = ""

    try:
        with open(file_path, 'r', encoding='utf-8') as file: # Fixes the problems with char recognition
            lines = file.readlines()
            total_lines = len(lines)

            # Picks the best answer based on keyword percentage match.
            for i in range(total_lines):
                line = lines[i].strip()
                keyword_matches = sum(keyword in line for keyword in keywords)
                percentage_match = (keyword_matches / total_keywords) * 100

                if percentage_match > max_percentage_match:
                    max_percentage_match = percentage_match
                    if i + 1 < total_lines:
                        best_solution = lines[i + 1].strip()

        if max_percentage_match >= 50:  # 50 starting point may need to adjust later? 50 is working so far
            found_solutions.append(best_solution)

    # Populate error if file name gets changed.
    except IOError:
        messagebox.showerror("File Error", "Error opening the file.")

    return found_solutions

# Main display window
def show_search_screen(file_path):
    search_window = tk.Toplevel(window)
    search_window.title("Search")
    search_window.geometry("400x200")
    search_window.configure(bg=bg_color)

    # Detecting search window button pressed
    def search_button_clicked():
        keywords = entry.get()
        solutions = search_keywords_in_file(file_path, keywords.split(","))

        # Checking for solution based on percentage match
        if solutions:
            messagebox.showinfo("Solutions Found", "\n".join(solutions))
        else:
            messagebox.showinfo("No Solutions", "No solutions found.")

    # Keyword entry field
    entry = tk.Entry(search_window, width=40, font=button_font, bg="#ECF0F1", fg="#2C3E50", borderwidth=2)
    entry.pack(pady=20)

    # Sub window search button
    search_button = tk.Button(search_window, text="Search", command=search_button_clicked, **button_style)
    search_button.pack()

# Create main window
window = tk.Tk()
window.title("Automated Information Center")
window.geometry("600x400")

# Define colors
bg_color = "#2C3E50"  # Dark blue-grey background
fg_color = "#ECF0F1"  # Light grey-white text
button_bg_color = "#3498DB"  # Light blue button background
button_fg_color = "#FFFFFF"  # White button text

# Main window color
window.configure(bg=bg_color)

# Set font
header_font = font.Font(family="Helvetica", size=14, weight="bold")
button_font = font.Font(family="Helvetica", size=12)

# Label above robot and machine buttons
label = tk.Label(
    window,
    text="Please select the robot for robot issues, or the machine for machine issues",
    fg=fg_color,
    bg=bg_color,
    font=header_font,
    wraplength=500,
    justify="center"
)
label.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

# Define relative paths for image files
robot_image_path = os.path.join(os.path.dirname(__file__), "robot.png")
machine_image_path = os.path.join(os.path.dirname(__file__), "machine.png")

if not os.path.exists(robot_image_path):
    messagebox.showerror("File Error", f"Robot image not found at {robot_image_path}")
    window.destroy()  # Close the window if the image is not found

if not os.path.exists(machine_image_path):
    messagebox.showerror("File Error", f"Machine image not found at {machine_image_path}")
    window.destroy()  # Close the window if the image is not found

# Load and resize images
robot_image = Image.open(robot_image_path)
robot_image = robot_image.resize((100, 100), Image.LANCZOS)
robot_photo = ImageTk.PhotoImage(robot_image)

machine_image = Image.open(machine_image_path)
machine_image = machine_image.resize((100, 100), Image.LANCZOS)
machine_photo = ImageTk.PhotoImage(machine_image)

# Button styles
button_style = {
    "bg": button_bg_color,
    "fg": button_fg_color,
    "font": button_font,
    "activebackground": "#2980B9",  # Slightly darker blue on hover
    "activeforeground": fg_color,
    "borderwidth": 0,
    "highlightthickness": 0,
    "cursor": "hand2"
}

# Robot button
robot_button = tk.Button(
    window,
    image=robot_photo,
    command=lambda: show_search_screen(os.path.join(os.path.dirname(__file__), "Fault_Codes.txt")),
    **button_style
)
robot_button.grid(row=1, column=0, padx=50, pady=20)

# Machine button
machine_button = tk.Button(
    window,
    image=machine_photo,
    command=lambda: show_search_screen(os.path.join(os.path.dirname(__file__), "Machine_Code.txt")),
    **button_style
)
machine_button.grid(row=1, column=1, padx=50, pady=20)

# Start the application
window.mainloop()

