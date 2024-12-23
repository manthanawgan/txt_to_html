import tkinter as tk
from tkinter import filedialog

def gamess_to_html(gamess_text):
    """
    Converts GAMESS input text into HTML formatted code.
    """
    html_output = ["<html>", "<head><title>GAMESS Input File</title></head>", "<body>", "<pre>"]
    
    lines = gamess_text.strip().split("\n")
    for line in lines:
        # will highlight different sections with HTML
        if line.startswith("$"):
            section_name = line.split()[0].strip()   # will check if the text starts with $ and make it bold using strong
            html_output.append(f"<strong>{line}</strong>")
        elif line.strip().startswith("!"):
            html_output.append(f"<em>{line}</em>")    # Comments are made italicized to differnetiate with others
        else:
            html_output.append(line)  # all the other lines will be left as it is

    html_output.extend(["</pre>", "</body>", "</html>"])
    return "\n".join(html_output)


#will be used for handling the file selection,conversion and saving process

def convert_file():
    # will open a dialogbox to let user select a inp file
    file_path = filedialog.askopenfilename(filetypes=[("GAMESS Input files", "*.inp")])
    if not file_path:
        print("No file selected.") #when no file is selected
        return

    with open(file_path, "r") as file:    #will Read the content of the selected file
        gamess_text = file.read()

    html_code = gamess_to_html(gamess_text)    #will Convert GAMESS input to HTML


    # Save the HTML to a file
    output_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if output_path:  #when a location is specified
        with open(output_path, "w") as file:
            file.write(html_code)
        print(f"HTML file created successfully at {output_path}!")
    else:
        print("Save operation cancelled.")

#will Create a GUI for uploading the file
root = tk.Tk()
root.title("GAMESS to HTML Converter")
root.geometry("300x150")

label = tk.Label(root, text="Convert input to html file", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Upload the input file", command=convert_file)
button.pack(pady=10)

root.mainloop()
