import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
import os

def search_keywords_in_file(file_paths, keywords):
    found_solutions = []
    total_keywords = len(keywords)

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:  # Fixes the problems with char recognition
                lines = file.readlines()
                total_lines = len(lines)

                # Picks the best answer based on keyword percentage match.
                for i in range(total_lines):
                    line = lines[i].strip()
                    keyword_matches = sum(keyword in line for keyword in keywords)
                    percentage_match = (keyword_matches / total_keywords) * 100

                    if percentage_match >= 50:
                        if i + 1 < total_lines:
                            solution = lines[i + 1].strip()
                            found_solutions.append(solution)

        # Populate error if file name gets changed.
        except IOError:
            messagebox.showerror("File Error", f"Error opening the file: {file_path}")

    return found_solutions

# Main display window
def show_search_screen(file_paths):
    search_window = tk.Toplevel(window)
    search_window.title("Search")
    search_window.geometry("400x300")
    search_window.configure(bg=bg_color)

    # Detecting search window button pressed
    def search_button_clicked():
        keywords = entry.get()
        solutions = search_keywords_in_file(file_paths, keywords.split(","))

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

# Function to save user notes
def save_user_notes():
    fault_code = fault_code_text.get("1.0", tk.END).strip()
    solution = solution_text.get("1.0", tk.END).strip()
    if fault_code or solution:
        try:
            with open("usernotes.txt", "a", encoding="utf-8") as file:
                if fault_code:
                    file.write(fault_code + "\n")
                if solution:
                    file.write(solution + "\n")
                file.write("\n")  # Add a newline for separation
            messagebox.showinfo("Notes Saved", "Your notes have been saved.")
            fault_code_text.delete("1.0", tk.END)  # Clear the text area after saving
            solution_text.delete("1.0", tk.END)  # Clear the text area after saving
        except IOError:
            messagebox.showerror("File Error", "Error saving the notes.")
    else:
        messagebox.showwarning("No Input", "Please enter some notes before saving.")

# Create main window
window = tk.Tk()
window.title("Automated Information Center")
window.geometry("600x600")  # Adjusted to accommodate notes section

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
    command=lambda: show_search_screen([os.path.join(os.path.dirname(__file__), "Fault_Codes.txt"), "usernotes.txt"]),
    **button_style
)
robot_button.grid(row=1, column=0, padx=50, pady=20)

# Machine button
machine_button = tk.Button(
    window,
    image=machine_photo,
    command=lambda: show_search_screen([os.path.join(os.path.dirname(__file__), "Machine_Code.txt"), "usernotes.txt"]),
    **button_style
)
machine_button.grid(row=1, column=1, padx=50, pady=20)

# Label for Fanuc Fault Code section
fault_code_label = tk.Label(
    window,
    text="Fanuc Fault Code",
    fg=fg_color,
    bg=bg_color,
    font=header_font,
)
fault_code_label.grid(row=2, column=0, columnspan=2, pady=5)

# Text area for Fanuc Fault Code
fault_code_text = tk.Text(
    window,
    width=50,  # Adjusted width
    height=5,  # Adjusted height
    font=button_font,
    bg="#ECF0F1",
    fg="#2C3E50",
    borderwidth=2,
    wrap="word"
)
fault_code_text.grid(row=3, column=0, columnspan=2, padx=20, pady=5)

# Label for Solution section
solution_label = tk.Label(
    window,
    text="Solution",
    fg=fg_color,
    bg=bg_color,
    font=header_font,
)
solution_label.grid(row=4, column=0, columnspan=2, pady=5)

# Text area for Solution
solution_text = tk.Text(
    window,
    width=50,  # Adjusted width
    height=5,  # Adjusted height
    font=button_font,
    bg="#ECF0F1",
    fg="#2C3E50",
    borderwidth=2,
    wrap="word"
)
solution_text.grid(row=5, column=0, columnspan=2, padx=20, pady=5)

# Save notes button
save_button = tk.Button(
    window,
    text="Save Notes",
    command=save_user_notes,
    **button_style
)
save_button.grid(row=6, column=0, columnspan=2, pady=20)

# Start the application
window.mainloop()

