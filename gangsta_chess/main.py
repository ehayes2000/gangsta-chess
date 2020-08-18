import gangsta_chess.ui.ui as ui
import tkinter as tk


def main_loop():
    ui.get_board().delete("1,0")
    ui.get_root().after(2000, main_loop)


ui.initialize()
ui.get_board().create_image(ui.get_square_cord(1, 0), image=ui.get_board().b_knight, anchor=tk.NW, tags="1,0")
ui.get_root().after(2000, main_loop)
ui.display()
