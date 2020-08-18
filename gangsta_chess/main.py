import gangsta_chess.ui.ui as ui
import tkinter as tk

ui.initialize()
ui.get_board().asd = ui.get_piece("./resources/pieces/b_rook.png")
ui.get_board().create_image(0, 0, image=ui.get_board().asd, anchor=tk.NW)
ui.display()
