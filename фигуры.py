import tkinter as tk
from tkinter import messagebox

class ShapesDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Построение фигур")

        self.radius_label = tk.Label(self.root, text="Радиус круга:")
        self.radius_entry = tk.Entry(self.root)
        self.radius_label.pack()
        self.radius_entry.pack()

        self.draw_circle_button = tk.Button(self.root, text="Построить круг", command=self.draw__circle)
        self.draw_circle_button.pack()

        self.base_label = tk.Label(self.root, text="Основание треугольника:")
        self.base_entry = tk.Entry(self.root)
        self.base_label.pack()
        self.base_entry.pack()

        self.height_label = tk.Label(self.root, text="Высота треугольника:")
        self.height_entry = tk.Entry(self.root)
        self.height_label.pack()
        self.height_entry.pack()

        self.draw_triangle_button = tk.Button(self.root, text="Построить треугольник", command=self.draw__triangle)
        self.draw_triangle_button.pack()

        self.A_label = tk.Label(self.root, text="Сторона прямоугольника (A):")
        self.A_entry = tk.Entry(self.root)
        self.A_label.pack()
        self.A_entry.pack()

        self.B_label = tk.Label(self.root, text="Сторона прямоугольника (B):")
        self.B_entry = tk.Entry(self.root)
        self.B_label.pack()
        self.B_entry.pack()

        self.draw_rectangle_button = tk.Button(self.root, text="Построить прямоугольник", command=self.draw__rectangle)
        self.draw_rectangle_button.pack()

        self.canvas = tk.Canvas(self.root, bg="white", width=400, height=400)
        self.canvas.pack()

    def draw_circle(self, radius):
        x, y = 200, 200
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, outline='blue', width=2, fill='blue', tags='circle')

    def draw_triangle(self, base, height):
        x, y = 200, 200
        x1, y1 = x - base/2, y + height/2
        x2, y2 = x + base/2, y + height/2
        x3, y3 = x, y - height/2
        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline='green', width=2, fill='green', tags='triangle')

    def draw_rectangle(self, width, height):
        x, y = 200, 200
        x1, y1 = x - width/2, y - height/2
        x2, y2 = x + width/2, y + height/2
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='red', width=2, fill='red', tags='rectangle')

    def draw_shapes(self):
        self.canvas.delete('all')  # Очистить Canvas перед построением новых фигур

        try:
            radius = float(self.radius_entry.get())
            base = float(self.base_entry.get())
            height = float(self.height_entry.get())

            # Проверка на отрицательные значения
            if radius <= 0 or base <= 0 or height <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return

            self.draw_circle(radius)
            self.draw_triangle(base, height)
            self.draw_rectangle(base, height)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

    def draw__circle(self):
        self.canvas.delete('all')  # Очистить Canvas перед построением новых фигур

        try:
            radius = float(self.radius_entry.get()) * 10

            # Проверка на отрицательные значения
            if radius <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return

            self.draw_circle(radius)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

    def draw__triangle(self):
        self.canvas.delete('all')  # Очистить Canvas перед построением новых фигур

        try:
            base = float(self.base_entry.get()) * 10
            height = float(self.height_entry.get()) * 10

            # Проверка на отрицательные значения
            if base <= 0 or height <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return

            self.draw_triangle(base, height)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

    def draw__rectangle(self):
        self.canvas.delete('all')  # Очистить Canvas перед построением новых фигур

        try:
            A = float(self.A_entry.get()) * 10
            B = float(self.B_entry.get()) * 10

            # Проверка на отрицательные значения
            if A <= 0 or B <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return

            self.draw_rectangle(A, B)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

def main():
    root = tk.Tk()
    drawer = ShapesDrawer(root)
    root.mainloop()

if __name__ == "__main__":
    main()