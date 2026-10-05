import customtkinter as ctk
from DataManager import DataManager

class ConfigWindow:

    def __init__(self):

        ctk.set_appearance_mode("dark")

        self.root = ctk.CTk()

        self.data_manager = DataManager()

        self.root.title("Snake Game")
        self.root.geometry("450x450")
        self.root.resizable(False, False)

        self.root.iconbitmap("imgs/icon.ico")

        self.font = ctk.CTkFont(
            family="Super Mario Bros. NES",
            size=16
        )

        self.root.MusicToggle = ctk.CTkSwitch(
            self.root,
            text="Music",
            font=self.font,
            command=self.music_changed
        )

        self.root.SoundToggle = ctk.CTkSwitch(
            self.root,
            text="Sound",
            font=self.font,
            command=self.sound_changed
        )

        self.root.volumeLabel = ctk.CTkLabel(
            self.root,
            font=self.font,
            text="Volume"
        )

        self.root.volumeSlider = ctk.CTkSlider(
            self.root,
            command=self.get_volume
        )

        self.root.MusicToggle.pack(pady=20)
        self.root.SoundToggle.pack(pady=20)
        self.root.volumeLabel.pack(pady=10)
        self.root.volumeSlider.pack(pady=5)

        if self.data_manager.get_data("music"):
            self.root.MusicToggle.select()
        else:
            self.root.MusicToggle.deselect()

        if self.data_manager.get_data("sound"):
            self.root.SoundToggle.select()
        else:
            self.root.SoundToggle.deselect()

        self.root.volumeSlider.set(
            self.data_manager.get_data("volume") / 100
        )

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

    def close(self):

        self.root.quit()

    def run(self):

        self.root.mainloop()

        self.root.destroy()

    def music_changed(self):
        value = self.root.MusicToggle.get()
        self.data_manager.change_data("music", value)

    def sound_changed(self):
        value = self.root.SoundToggle.get()
        self.data_manager.change_data("sound", value)

    def get_volume(self, value):
        result = int(value * 100)
        self.data_manager.change_data("volume", result)