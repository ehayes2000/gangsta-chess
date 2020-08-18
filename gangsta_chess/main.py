import gangsta_chess.ui.ui as ui
import tkinter as tk

ui.initialize()
ui.get_board().create_image(ui.get_square_cord(1, 0), image=ui.get_board().b_knight, anchor=tk.NW)
ui.display()
