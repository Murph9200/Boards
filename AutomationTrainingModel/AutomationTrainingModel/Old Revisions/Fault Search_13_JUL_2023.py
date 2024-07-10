import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def search_keywords_in_file(file_path, keywords):
    found_solutions = []
    total_keywords = len(keywords)
    max_percentage_match = 0
    best_solution = ""

    try:
        with open(file_path, 'r', encoding='utf-8') as file: #Fixes the problems with char recogniction 
            lines = file.readlines()
            total_lines = len(lines)

            
            # pickes the best answer based on keyword percentage match.
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

            
    #populate error is file name gets changed.
    except IOError:
        messagebox.showerror("File Error", "Error opening the file.")

    return found_solutions


# Main display window
def show_search_screen(file_path):
    search_window = tk.Toplevel(window)
    search_window.title("Search")
    search_window.geometry("400x200")
    search_window.configure(bg="dark blue")

    #detecting search window button pressed
    def search_button_clicked():
        keywords = entry.get()
        solutions = search_keywords_in_file(file_path, keywords.split(","))


        #checking for solution based on percentage match
        if solutions:
            messagebox.showinfo("Solutions Found", "\n".join(solutions))
        else:
            messagebox.showinfo("No Solutions", "No solutions found.")

    #keyword entry field
    entry = tk.Entry(search_window, width=40)
    entry.pack(pady=20)

    #Sub window search button
    search_button = tk.Button(search_window, text="Search", command=search_button_clicked)
    search_button.pack()

#the display main window/title/size
window = tk.Tk()
window.title("Automated Information Center")
window.geometry("600x400")

# Main window color
window.configure(bg="dark blue")

# label above robot and machine buttons.
label = tk.Label(window, text="Please select the robot for robot issues, or the machine for machine issues", fg="white", bg="dark blue")
label.grid(row=0, column=0, columnspan=3, pady=100, padx=75)

#button images and resize - starting 150,150 (too large)
robot_image = Image.open(r"C:\Users\tycmu\Desktop\FaultSearchProject\robot.png")
robot_image = robot_image.resize((100, 100), Image.LANCZOS)
robot_photo = ImageTk.PhotoImage(robot_image)

machine_image = Image.open(r"C:\Users\tycmu\Desktop\FaultSearchProject\machine.png")
machine_image = machine_image.resize((100, 100), Image.LANCZOS)
machine_photo = ImageTk.PhotoImage(machine_image)

#robot button
robot_button = tk.Button(window, image=robot_photo, command=lambda: show_search_screen(r"C:\Users\tycmu\Desktop\FaultSearchProject\Fault_Codes.txt"))
robot_button.grid(row=1, column=0, padx=100)

#machine button
machine_button = tk.Button(window, image=machine_photo, command=lambda: show_search_screen(r"C:\Users\tycmu\Desktop\FaultSearchProject\Machine_Code.txt"))
machine_button.grid(row=1, column=1, padx=100)

# start
window.mainloop()
