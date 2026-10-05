import tkinter as tk
from tkinter import messagebox
import time
import threading

# =========================================================
# HIRU USB LOCK - FIRST PROTOTYPE
# =========================================================

PASSWORD = "1234"

BG = "#020812"
CYAN = "#00eaff"
BLUE = "#087cff"
WHITE = "#e9fbff"
RED = "#ff2448"
DARK = "#061522"


class HiruUSBLock:

    def __init__(self, root):
        self.root = root

        root.title("HIRU USB LOCK")
        root.geometry("700x500")
        root.configure(bg=BG)
        root.resizable(False, False)

        self.build_screen()

    # -----------------------------------------------------
    # MAIN SCREEN
    # -----------------------------------------------------

    def build_screen(self):

        self.clear_screen()

        title = tk.Label(
            self.root,
            text="HIRU USB LOCK",
            font=("Segoe UI", 28, "bold"),
            fg=CYAN,
            bg=BG
        )
        title.pack(pady=(55, 5))

        subtitle = tk.Label(
            self.root,
            text="SECURE USB ACCESS SYSTEM",
            font=("Segoe UI", 10),
            fg="#6ca8c9",
            bg=BG
        )
        subtitle.pack()

        welcome = tk.Label(
            self.root,
            text="WELCOME BACK HIRU",
            font=("Segoe UI", 22, "bold"),
            fg=WHITE,
            bg=BG
        )
        welcome.pack(pady=(65, 25))

        self.password = tk.Entry(
            self.root,
            show="●",
            font=("Segoe UI", 18),
            justify="center",
            bg=DARK,
            fg=WHITE,
            insertbackground=CYAN,
            relief="flat",
            width=22
        )
        self.password.pack(ipady=12)

        self.password.focus()

        unlock = tk.Button(
            self.root,
            text="UNLOCK",
            command=self.check_password,
            font=("Segoe UI", 12, "bold"),
            fg=BG,
            bg=CYAN,
            activeforeground=BG,
            activebackground=WHITE,
            relief="flat",
            width=18,
            height=2,
            cursor="hand2"
        )
        unlock.pack(pady=25)

        self.status = tk.Label(
            self.root,
            text="SYSTEM LOCKED",
            font=("Segoe UI", 9),
            fg="#437b91",
            bg=BG
        )
        self.status.pack(pady=10)

        self.root.bind("<Return>", lambda event: self.check_password())

    # -----------------------------------------------------
    # PASSWORD CHECK
    # -----------------------------------------------------

    def check_password(self):

        entered = self.password.get()

        if entered == PASSWORD:
            self.access_granted()

        else:
            self.unauthorized()

    # -----------------------------------------------------
    # ACCESS GRANTED
    # -----------------------------------------------------

    def access_granted(self):

        self.clear_screen()

        self.root.configure(bg="#00150f")

        label = tk.Label(
            self.root,
            text="ACCESS GRANTED",
            font=("Segoe UI", 36, "bold"),
            fg="#00ff9d",
            bg="#00150f"
        )
        label.pack(expand=True)

        sub = tk.Label(
            self.root,
            text="WELCOME HIRU",
            font=("Segoe UI", 13),
            fg="#8affcc",
            bg="#00150f"
        )
        sub.pack(pady=(0, 150))

        self.root.after(2500, self.open_vault)

    # -----------------------------------------------------
    # UNAUTHORIZED
    # -----------------------------------------------------

    def unauthorized(self):

        self.clear_screen()

        self.root.configure(bg="#140207")

        warning = tk.Label(
            self.root,
            text="⚠",
            font=("Segoe UI", 65, "bold"),
            fg=RED,
            bg="#140207"
        )
        warning.pack(pady=(50, 5))

        title = tk.Label(
            self.root,
            text="UNAUTHORIZED ENTRY",
            font=("Segoe UI", 27, "bold"),
            fg=RED,
            bg="#140207"
        )
        title.pack()

        skull = tk.Label(
            self.root,
            text="☠",
            font=("Segoe UI", 90),
            fg=WHITE,
            bg="#140207"
        )
        skull.pack(pady=15)

        info = tk.Label(
            self.root,
            text="ACCESS DENIED",
            font=("Segoe UI", 12, "bold"),
            fg="#ff7187",
            bg="#140207"
        )
        info.pack()

        self.root.after(3000, self.build_screen)

    # -----------------------------------------------------
    # VAULT
    # -----------------------------------------------------

    def open_vault(self):

        self.clear_screen()

        self.root.configure(bg=BG)

        title = tk.Label(
            self.root,
            text="USB ACCESS GRANTED",
            font=("Segoe UI", 25, "bold"),
            fg=CYAN,
            bg=BG
        )
        title.pack(pady=(80, 20))

        info = tk.Label(
            self.root,
            text="HIRU USB IS UNLOCKED",
            font=("Segoe UI", 15),
            fg=WHITE,
            bg=BG
        )
        info.pack()

        close = tk.Button(
            self.root,
            text="LOCK USB",
            command=self.build_screen,
            font=("Segoe UI", 12, "bold"),
            fg=BG,
            bg=CYAN,
            relief="flat",
            width=18,
            height=2,
            cursor="hand2"
        )
        close.pack(pady=40)

    # -----------------------------------------------------
    # CLEAR
    # -----------------------------------------------------

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


# =========================================================
# START
# =========================================================

root = tk.Tk()

app = HiruUSBLock(root)

root.mainloop()
