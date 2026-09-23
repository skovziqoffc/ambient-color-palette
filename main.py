import tkinter as tk
import threading
import keyboard
from color_engine import ext_dom_colors

class PaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        keyboard.add_hotkey("ctrl+shift+q", lambda: self.root.after(0, self.draw_cv))
        keyboard.add_hotkey("ctrl+shift+m", self.root.quit)
        
    def draw_cv(self):
        self.ov = tk.Toplevel(self.root)
        self.ov.attributes("-fullscreen", True, "-alpha", 0.3)
        self.cv = tk.Canvas(self.ov, cursor="cross", bg="#000", highlightthickness=0)
        self.cv.pack(fill="both", expand=True)
        self.x1 = self.y1 = self.rect = None
        self.cv.bind("<ButtonPress-1>", self.on_dn)
        self.cv.bind("<B1-Motion>", self.on_drg)
        self.cv.bind("<ButtonRelease-1>", self.on_up)
        
    def on_dn(self, e):
        self.x1, self.y1 = e.x, e.y
        self.rect = self.cv.create_rectangle(self.x1, self.y1, self.x1, self.y1, outline="#fff", width=2)
        
    def on_drg(self, e):
        self.cv.coords(self.rect, self.x1, self.y1, e.x, e.y)
        
    def on_up(self, e):
        x2, y2 = e.x, e.y
        self.ov.destroy()
        cols = ext_dom_colors(self.x1, self.y1, x2, y2)
        self.show_win(cols) if cols else None

    def show_win(self, cols):
        self.win = tk.Toplevel(self.root)
        self.win.title("Ambient Palette")
        self.win.geometry("520x130")
        self.win.resizable(False, False)
        self.win.config(bg="#121212")
        self.win.attributes("-topmost", True)
        
        tk.Label(self.win, text="COLOR PALETTE EXTRACTED", fg="#3b82f6", bg="#121212", font=("Segoe UI", 8, "bold")).pack(pady=(10, 0))
        tk.Label(self.win, text="Click a block to copy code", fg="#a3a3a3", bg="#121212", font=("Segoe UI", 9)).pack(pady=(2, 8))
        
        box = tk.Frame(self.win, bg="#121212")
        box.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        
        for c in cols:
            b = tk.Frame(box, bg=c, cursor="hand2", highlightbackground="#1e1e1e", highlightthickness=1)
            b.pack(side="left", fill="both", expand=True, padx=3)
            lbl = tk.Label(b, text=c, bg=c, fg=self.get_fg(c), font=("Consolas", 10, "bold"))
            lbl.pack(expand=True)
            b.bind("<Button-1>", lambda e, col=c: self.cp(col))
            lbl.bind("<Button-1>", lambda e, col=c: self.cp(col))

    def get_fg(self, hex_c):
        hex_c = hex_c.lstrip('#')
        r, g, b = tuple(int(hex_c[i:i+2], 16) for i in (0, 2, 4))
        return "#121212" if ((r * 299 + g * 587 + b * 114) / 1000) > 135 else "#fff"

    def cp(self, txt):
        self.root.clipboard_clear()
        self.root.clipboard_append(txt)
        self.root.update()
        self.win.title(f"Copied {txt}!")
        self.win.after(1000, lambda: self.win.title("Ambient Palette"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PaletteApp(root)
    root.mainloop()
