import tkinter as tk
from tkinter import ttk


class FriendlyFaceApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Весёлое окно")
        self.root.geometry("380x320")
        self.root.resizable(False, False)

        self._build_widgets()

    def _build_widgets(self) -> None:
        self.button = ttk.Button(self.root, text="Привет", command=self.show_message)
        self.button.pack(pady=20)

        self.message_frame = ttk.Frame(self.root)
        self.message_frame.pack(fill=tk.BOTH, expand=True)

        self.message_label = ttk.Label(self.message_frame, text="", font=("Arial", 16))
        self.message_label.pack(pady=10)

        self.canvas = tk.Canvas(self.message_frame, width=260, height=180, bg="#fdf6e3", highlightthickness=0)
        self.canvas.pack()

    def show_message(self) -> None:
        self.message_label.config(text="Сам дурак")
        self._draw_face()

    def _draw_face(self) -> None:
        self.canvas.delete("all")

        self.canvas.create_oval(40, 20, 220, 200, fill="#ffe28a", outline="#e0b44c", width=3)

        self.canvas.create_oval(90, 70, 120, 100, fill="white", outline="#3b3b3b", width=2)
        self.canvas.create_oval(140, 70, 170, 100, fill="white", outline="#3b3b3b", width=2)
        self.canvas.create_oval(102, 82, 112, 92, fill="#1c3f95", outline="")
        self.canvas.create_oval(152, 82, 162, 92, fill="#1c3f95", outline="")

        self.canvas.create_polygon(130, 105, 120, 130, 140, 130, fill="#e06f6f", outline="#9c2c2c", width=2)

        self.canvas.create_arc(85, 120, 195, 200, start=200, extent=140, style=tk.ARC, outline="#b72c55", width=5)
        self.canvas.create_arc(95, 130, 185, 190, start=200, extent=140, style=tk.ARC, outline="#ea507e", width=3)

        self.canvas.create_line(60, 40, 100, 30, width=4, fill="#e0b44c")
        self.canvas.create_line(200, 40, 160, 30, width=4, fill="#e0b44c")
        self.canvas.create_line(50, 60, 90, 50, width=4, fill="#e0b44c")
        self.canvas.create_line(210, 60, 170, 50, width=4, fill="#e0b44c")


def main() -> None:
    root = tk.Tk()
    FriendlyFaceApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
