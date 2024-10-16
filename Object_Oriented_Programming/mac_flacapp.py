import os
import json
import tkinter as tk
import sox  
import numpy as np

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FLACTOOL")
        self.geometry("600x500")  
        self.maindirectory = self.makedirectory("FLACTOOL")
        mainlabel = tk.Label(self, text="Mini FLAC processor", font=("Times New Roman", 18))
        mainlabel.pack(pady=10, padx=10)  
        self.button1 = self.button_1("FLAC Dumb Down", "Reduce to 16bit / 44.1Khz; Appropriate for fancy foobar playback on portable devices")
        self.button2 = self.button_2("Appropriate for phones", "Manipulate FLAC for better listening experience for poor DAC capabilities")
        self.updatemonitor = tk.Text(self, wrap='word', height=10)
        self.updatemonitor.pack(pady=10, padx=10, fill='both', expand=False)
        self.updatemonitor.insert('end', "Updates: \n")
        self.sequence_display = tk.Text(self, wrap='word', height=10)
        self.sequence_display.pack(pady=10, padx=10, expand=True)
        self.sequence_display.insert('end', "FLAC Files Loaded:\n")
        self.loadqueries()
        self.tfm = sox.Transformer()

    def button_1(self, buttontext, labeltext):
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)
        button = tk.Button(frame, text=buttontext, bg="#03d3fc", command=self.dumb_down)  # Removed ()
        button.pack()
        label = tk.Label(frame, text=labeltext)
        label.pack()
        return button
        
    def button_2(self, buttontext, labeltext):
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)
        button = tk.Button(frame, text=buttontext, bg="#e3fc03", command=self.apply_earwax)  # Removed ()
        button.pack()
        label = tk.Label(frame, text=labeltext)
        label.pack()
        return button
        
    def makedirectory(self, foldername):
        desktopdirectory = os.path.expanduser("~/Desktop")
        pathforworkingfolder = os.path.join(desktopdirectory, foldername)
        if not os.path.exists(pathforworkingfolder):
            os.mkdir(pathforworkingfolder)
        subfolders = ["User_FLAC_repository", "Conversion_results", "AppFiles"]
        pathdictionary = {"FLACTOOL": pathforworkingfolder}
        for folder in subfolders:
            subfolderpath = os.path.join(pathforworkingfolder, folder)
            if not os.path.exists(subfolderpath):
                os.makedirs(subfolderpath)
            pathdictionary[folder] = subfolderpath
        return pathdictionary

    def get_files(self):
        pathdictionary = self.maindirectory  # Use the existing directory
        queryfolder = pathdictionary["User_FLAC_repository"]
        querysequencepaths = {}
        for file in os.listdir(queryfolder):
            if file.endswith('.flac'):  
                path = os.path.join(queryfolder, file)
                name = os.path.splitext(file)[0]
                querysequencepaths[name] = path
        pathforappdata = pathdictionary["AppFiles"]
        querydatafile = "flac_list.json"
        pathforquerydata = os.path.join(pathforappdata, querydatafile)
        with open(pathforquerydata, 'w') as file:
            json.dump(querysequencepaths, file)
        return querysequencepaths if querysequencepaths else None  

    def __iter__(self):
        song_paths = self.get_files()
        if song_paths is not None:
            return iter(song_paths.values())  
        return iter([])  

    def dumb_down(self):
        pathdictionary = self.maindirectory
        folder = pathdictionary["Conversion_results"]
        for path in self: 
            name, ext = os.path.splitext(os.path.basename(path))
            if '.' in name:  # Check if the name has a period
                name = '.'.join(name.split('.')[:-1])  # Join all but the last part
                output_filepath = os.path.join(folder, f"{name}.flac")
                sample_rate = 44100
                y = np.sin(2 * np.pi * 440.0 * np.arange(sample_rate * 1.0) / sample_rate)
                self.tfm.build(
                    input_array=y,
                    sample_rate_in= sample_rate,
                    output_filepath= output_filepath
                )
                self.updatemonitor.insert('end', f"Converted: {path} to {output_filepath}\n")  # Update the monitor

    def loadqueries(self):
        querypaths = self.get_files()
        if querypaths is None:
            self.sequence_display.insert('end', "No FLAC files have been added to the user repository")
        else:
            for name in querypaths.keys():
                self.sequence_display.insert('end', f"{name}.flac\n")
        return querypaths

    def apply_earwax(self):
        pass  # Implement this method as needed

if __name__ == "__main__":
    app = Application()
    app.mainloop()
