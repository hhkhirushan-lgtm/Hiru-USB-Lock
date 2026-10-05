import tkinter as tk
import math
import time

# ============================================================
# HIRU USB LOCK
# Cinematic Prototype
# ============================================================

PASSWORD = "1234"

BG = "#02060D"
PANEL = "#07131F"
CYAN = "#00E5FF"
CYAN2 = "#008CFF"
WHITE = "#E8FBFF"
RED = "#FF2448"
GREEN = "#00FF9D"
DIM = "#416A7D"


class HiruLock:

    def __init__(self, root):

        self.root = root

        self.root.title("HIRU USB LOCK")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.animation_running = False

        self.show_login()

    # ========================================================
    # CLEAR SCREEN
    # ========================================================

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ========================================================
    # BACKGROUND
    # ========================================================

    def create_background(self):

        self.canvas = tk.Canvas(
            self.root,
            width=900,
            height=600,
            bg=BG,
            highlightthickness=0
        )

        self.canvas.pack()

        # Border

        self.canvas.create_rectangle(
            18, 18, 882, 582,
            outline="#0A3448",
            width=2
        )

        self.canvas.create_rectangle(
            25, 25, 875, 575,
            outline="#06202F",
            width=1
        )

        # Corner elements

        corners = [
            (30, 30, 90, 30),
            (30, 30, 30, 90),

            (870, 30, 810, 30),
            (870, 30, 870, 90),

            (30, 570, 90, 570),
            (30, 570, 30, 510),

            (870, 570, 810, 570),
            (870, 570, 870, 510)
        ]

        for x1, y1, x2, y2 in corners:

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill=CYAN,
                width=2
            )

        # Small decorative dots

        for x in range(50, 850, 40):

            self.canvas.create_oval(
                x,
                55,
                x + 2,
                57,
                fill="#124052",
                outline=""
            )

        return self.canvas

    # ========================================================
    # LOGIN SCREEN
    # ========================================================

    def show_login(self):

        self.clear()

        self.root.configure(bg=BG)

        canvas = self.create_background()

        # Top system text

        canvas.create_text(
            55,
            85,
            text="HIRU SECURITY SYSTEM",
            fill=DIM,
            font=("Segoe UI", 9, "bold"),
            anchor="w"
        )

        canvas.create_text(
            845,
            85,
            text="SYSTEM ONLINE",
            fill=GREEN,
            font=("Segoe UI", 9, "bold"),
            anchor="e"
        )

        # Main title

        canvas.create_text(
            450,
            145,
            text="HIRU USB LOCK",
            fill=CYAN,
            font=("Segoe UI", 34, "bold")
        )

        canvas.create_text(
            450,
            185,
            text="SECURE PORTABLE ACCESS SYSTEM",
            fill=DIM,
            font=("Segoe UI", 10)
        )

        # Welcome

        canvas.create_text(
            450,
            255,
            text="WELCOME BACK HIRU",
            fill=WHITE,
            font=("Segoe UI", 25, "bold")
        )

        canvas.create_text(
            450,
            288,
            text="ENTER AUTHORIZATION CODE",
            fill="#52869C",
            font=("Segoe UI", 9)
        )

        # Password frame

        self.password_frame = tk.Frame(
            self.root,
            bg="#06131E",
            highlightbackground="#0B526C",
            highlightthickness=1
        )

        self.password_frame.place(
            x=285,
            y=315,
            width=330,
            height=58
        )

        self.password = tk.Entry(
            self.password_frame,
            show="●",
            font=("Segoe UI", 18),
            justify="center",
            bg="#06131E",
            fg=WHITE,
            insertbackground=CYAN,
            relief="flat",
            bd=0
        )

        self.password.pack(
            fill="both",
            expand=True,
            padx=15
        )

        self.password.focus()

        # Unlock button

        self.unlock = tk.Button(
            self.root,
            text="UNLOCK SYSTEM",
            command=self.check_password,
            font=("Segoe UI", 11, "bold"),
            fg=BG,
            bg=CYAN,
            activeforeground=BG,
            activebackground=WHITE,
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        self.unlock.place(
            x=335,
            y=395,
            width=230,
            height=48
        )

        # Status

        self.status = tk.Label(
            self.root,
            text="● SYSTEM LOCKED",
            font=("Segoe UI", 9, "bold"),
            fg="#3C7084",
            bg=BG
        )

        self.status.place(
            x=450,
            y=475,
            anchor="center"
        )

        # Bottom text

        canvas.create_text(
            450,
            535,
            text="AUTHORIZED USER ONLY  •  HIRU SECURITY NETWORK",
            fill="#1D4352",
            font=("Segoe UI", 8)
        )

        self.root.bind(
            "<Return>",
            lambda event: self.check_password()
        )

    # ========================================================
    # PASSWORD
    # ========================================================

    def check_password(self):

        entered = self.password.get()

        if entered == PASSWORD:

            self.access_granted()

        else:

            self.unauthorized()

    # ========================================================
    # ACCESS GRANTED
    # ========================================================

    def access_granted(self):

        self.root.unbind("<Return>")

        self.clear()

        self.root.configure(bg="#00130C")

        canvas = tk.Canvas(
            self.root,
            width=900,
            height=600,
            bg="#00130C",
            highlightthickness=0
        )

        canvas.pack()

        # Outer circles

        center_x = 450
        center_y = 285

        for radius in range(40, 220, 35):

            canvas.create_oval(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                outline="#063D2B",
                width=1
            )

        canvas.create_text(
            450,
            190,
            text="AUTHORIZATION VERIFIED",
            fill="#49D9A3",
            font=("Segoe UI", 10, "bold")
        )

        canvas.create_text(
            450,
            285,
            text="ACCESS GRANTED",
            fill=GREEN,
            font=("Segoe UI", 38, "bold")
        )

        canvas.create_text(
            450,
            335,
            text="WELCOME BACK HIRU",
            fill="#9DFFE0",
            font=("Segoe UI", 13)
        )

        canvas.create_text(
            450,
            430,
            text="USB SECURITY SYSTEM UNLOCKED",
            fill="#438F77",
            font=("Segoe UI", 9)
        )

        self.animate_access(canvas, 0)

        self.root.after(
            3000,
            self.show_vault
        )

    # ========================================================
    # ACCESS ANIMATION
    # ========================================================

    def animate_access(self, canvas, angle):

        if not canvas.winfo_exists():
            return

        rad = math.radians(angle)

        x = 450 + math.cos(rad) * 190
        y = 285 + math.sin(rad) * 190

        dot = canvas.create_oval(
            x - 3,
            y - 3,
            x + 3,
            y + 3,
            fill=GREEN,
            outline=""
        )

        canvas.after(
            20,
            lambda: self.remove_animation_dot(
                canvas,
                dot,
                angle + 8
            )
        )

    def remove_animation_dot(self, canvas, dot, next_angle):

        try:

            canvas.delete(dot)

            self.animate_access(
                canvas,
                next_angle
            )

        except:

            pass

    # ========================================================
    # UNAUTHORIZED
    # ========================================================

    def unauthorized(self):

        self.root.unbind("<Return>")

        self.clear()

        self.root.configure(bg="#120207")

        canvas = tk.Canvas(
            self.root,
            width=900,
            height=600,
            bg="#120207",
            highlightthickness=0
        )

        canvas.pack()

        # Warning border

        canvas.create_rectangle(
            20,
            20,
            880,
            580,
            outline="#5A0C19",
            width=2
        )

        # Warning symbol

        canvas.create_text(
            450,
            120,
            text="⚠",
            fill=RED,
            font=("Segoe UI", 65, "bold")
        )

        canvas.create_text(
            450,
            210,
            text="UNAUTHORIZED ENTRY",
            fill=RED,
            font=("Segoe UI", 30, "bold")
        )

        canvas.create_text(
            450,
            280,
            text="☠",
            fill=WHITE,
            font=("Segoe UI", 90, "bold")
        )

        canvas.create_text(
            450,
            385,
            text="ACCESS DENIED",
            fill="#FF7187",
            font=("Segoe UI", 13, "bold")
        )

        canvas.create_text(
            450,
            425,
            text="SECURITY ALERT ACTIVATED",
            fill="#7E2838",
            font=("Segoe UI", 9)
        )

        canvas.create_text(
            450,
            510,
            text="RETURNING TO AUTHORIZATION...",
            fill="#55202A",
            font=("Segoe UI", 8)
        )

        self.warning_flash(canvas, 0)

        self.root.after(
            3500,
            self.show_login
        )

    # ========================================================
    # WARNING FLASH
    # ========================================================

    def warning_flash(self, canvas, count):

        if count >= 8:
            return

        current = "#FF2448" if count % 2 == 0 else "#120207"

        canvas.configure(
            bg=current
        )

        self.root.after(
            120,
            lambda: self.warning_flash(
                canvas,
                count + 1
            )
        )

    # ========================================================
    # VAULT SCREEN
    # ========================================================

    def show_vault(self):

        self.clear()

        self.root.configure(bg=BG)

        canvas = self.create_background()

        canvas.create_text(
            450,
            150,
            text="USB ACCESS GRANTED",
            fill=CYAN,
            font=("Segoe UI", 28, "bold")
        )

        canvas.create_text(
            450,
            200,
            text="HIRU USB IS CURRENTLY UNLOCKED",
            fill=WHITE,
            font=("Segoe UI", 12)
        )

        canvas.create_text(
            450,
            260,
            text="VAULT STATUS",
            fill=DIM,
            font=("Segoe UI", 9, "bold")
        )

        canvas.create_text(
            450,
            300,
            text="●  ACCESSIBLE",
            fill=GREEN,
            font=("Segoe UI", 18, "bold")
        )

        lock_button = tk.Button(
            self.root,
            text="LOCK USB",
            command=self.show_login,
            font=("Segoe UI", 11, "bold"),
            fg=BG,
            bg=CYAN,
            activebackground=WHITE,
            relief="flat",
            cursor="hand2"
        )

        lock_button.place(
            x=350,
            y=385,
            width=200,
            height=48
        )

        canvas.create_text(
            450,
            500,
            text="HIRU USB LOCK  •  SECURITY SYSTEM",
            fill="#1D4352",
            font=("Segoe UI", 8)
        )


# ============================================================
# START APPLICATION
# ============================================================

root = tk.Tk()

app = HiruLock(root)

root.mainloop()
