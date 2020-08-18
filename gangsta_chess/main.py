import gangsta_chess.ui.ui as ui
import tkinter as tk


def tk_loop():
    ui.get_root().after(2000, tk_loop)


ui.initialize()
ui.get_board().create_image(ui.get_square_cord(1, 0), image=ui.get_board().b_knight, anchor=tk.NW, tags="1,0")
ui.get_board().create_image(ui.get_square_cord(2, 0), image=ui.get_board().w_knight, anchor=tk.NW, tags="2,0")
ui.get_root().after(2000, tk_loop)
ui.display()
