# -*- coding: utf-8 -*-
"""模块注释

Author: Lei Wang
Date: April 24, 2024
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"



import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog, Scale, Label
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ImageThresholdingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Thresholding")

        self.img = None
        self.threshold_value = 127

        self.create_widgets()

    def create_widgets(self):
        # Frame to hold widgets
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Button to open image file
        btn_open = tk.Button(frame, text="Open Image", command=self.open_image)
        btn_open.pack(side=tk.LEFT, padx=5)

        # Label for threshold value
        lbl_threshold = tk.Label(frame, text="Threshold Value:")
        lbl_threshold.pack(side=tk.LEFT, padx=5)

        # Scale for threshold value
        self.scale_threshold = Scale(frame, from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_threshold)
        self.scale_threshold.set(self.threshold_value)
        self.scale_threshold.pack(side=tk.LEFT, padx=5)

        # Canvas to display image
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(padx=10, pady=10)

    def open_image(self):
        if file_path := filedialog.askopenfilename():
            # self.img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self.display_image()

    def display_image(self):
        if self.img is not None:
            _, thresh_img = cv2.threshold(self.img, self.threshold_value, 255, cv2.THRESH_BINARY)
            plt.figure(figsize=(5, 5))
            plt.imshow(thresh_img, cmap='gray')
            plt.axis('off')
            plt.title('Thresholded Image')
            plt.tight_layout()

            # Display image in tkinter canvas
            self.plot_to_tk_canvas(plt)

    def plot_to_tk_canvas(self, plt):
        self.canvas.delete("all")  # Clear previous image
        self.fig_agg = FigureCanvasTkAgg(plt.gcf(), master=self.canvas)
        self.fig_agg.draw()
        self.fig_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_threshold(self, val):
        self.threshold_value = int(val)
        self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageThresholdingApp(root)
    root.mainloop()
