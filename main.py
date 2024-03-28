import pygame
import pygame_widgets
from pygame_textinput import pygame_textinput
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import math
from tkinter import messagebox


class MathPendulum:
    def __init__(self, width=800, height=600, length=200, radian=90, angular_velocity=0.1, gravity=9.81, mass=5, damping_factor=0.99):
        self.width = width
        self.height = height
        self.pivot = (width // 2, 100)
        self.length = length  # Длина маятника
        self.radian = radian # Угол
        self.angle = math.radians(radian)  # Начальный угол в радианах
        self.angular_velocity = angular_velocity  # Угловая скорость
        self.gravity = gravity  # Ускорение свободного падения
        self.mass = mass  # Масса объекта
        self.damping_factor = damping_factor  # Коэффициент затухания
        self.start = False

        self.s_length = length  # Длина маятника
        self.s_radian = radian  # Угол
        self.s_angle = math.radians(radian) # Начальный угол в радианах
        self.s_angular_velocity = angular_velocity  # Угловая скорость
        self.s_gravity = gravity  # Ускорение свободного падения
        self.s_mass = mass  # Масса объекта
        self.s_damping_factor = damping_factor  # Коэффициент затухания

    def update(self):
        if(self.start):
            # Вычисляем координаты конца маятника
            end_x = int(self.pivot[0] + self.length * math.sin(self.angle))
            end_y = int(self.pivot[1] + self.length * math.cos(self.angle))

            # Рисуем маятник и точку крепления
            pygame.draw.line(root, black, self.pivot, (end_x, end_y), 5)
            pygame.draw.circle(root, red, self.pivot, 10)

            # Обновляем угловую скорость и угол
            angular_acceleration = -self.gravity / self.length * math.sin(self.angle)
            angular_acceleration += (self.mass * self.gravity * math.cos(self.angle)) / (self.length ** 2)
            self.angular_velocity += angular_acceleration
            self.angular_velocity *= self.damping_factor
            self.angle += self.angular_velocity

            # Ограничиваем угол в пределах от -π до π
            self.angle = self.angle % (2 * math.pi)
        pass

    def updateoptions(self):
        try:
            length = float(textbox1.getText() if textbox1.getText() else self.s_length)
            print(length)
            # Проверка на отрицательные значения
            if length <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return
            self.s_length = length
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

        pass

        try:
            angle = math.radians(float(textbox2.getText() if textbox2.getText() else self.s_radian))
            print(angle)
            # Проверка на отрицательные значения
            if angle <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return
            self.s_angle = angle

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

        pass

        try:
            angular_velocity = float(textbox3.getText() if textbox3.getText() else self.s_angular_velocity)
            print(angular_velocity)
            # Проверка на отрицательные значения
            if angular_velocity <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return
            self.s_angular_velocity = angular_velocity

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

        pass

        try:
            gravity = float(textbox4.getText() if textbox4.getText() else self.s_gravity)
            print(gravity)
            # Проверка на отрицательные значения
            if gravity <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return
            self.s_gravity = gravity

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

        pass

        try:
            mass = float(textbox5.getText() if textbox5.getText() else self.s_mass)
            print(mass)
            # Проверка на отрицательные значения
            if mass <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return
            self.s_mass = mass

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

        pass

        try:
            damping_factor = float(textbox6.getText() if textbox6.getText() else self.s_damping_factor)
            print(damping_factor)
            # Проверка на отрицательные значения
            if damping_factor <= 0:
                messagebox.showerror("Ошибка", "Значения должны быть положительными")
                return
            self.s_damping_factor = damping_factor

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения")

        pass

    def flipflop_start(self):
        self.length = self.s_length  # Длина маятника
        self.radian = self.s_radian  # Угол
        self.angle = self.s_angle  # Начальный угол в радианах
        self.angular_velocity = self.s_angular_velocity  # Угловая скорость
        self.gravity = self.s_gravity  # Ускорение свободного падения
        self.mass = self.s_mass  # Масса объекта
        self.damping_factor = self.s_damping_factor  # Коэффициент затухания
        self.start = not(self.start)
        pass

# Цвета и характеристики окна
white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
gray = (125, 125, 125)
width, height = 1200, 500

pygame.init()
textinput = pygame_textinput.TextInputVisualizer()

font = pygame.font.SysFont("Consolas", 18)

root = pygame.display.set_mode((width, height))
pygame.display.set_caption("Математический маятник")
mp = MathPendulum()

clock = pygame.time.Clock()

button1 = Button(
    # Mandatory Parameters
    root,  # Surface to place button on
    850,  # X-coordinate of top left corner
    400,  # Y-coordinate of top left corner
    175,  # Width
    75,  # Height

    # Optional Parameters
    text='Старт',  # Text to display
    fontSize=24,  # Size of font
    textColour=(255,255,255),
    borderColour= (186, 186, 186),
    borderThickness=(2),
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=gray,  # Colour of button when not being interacted with
    hoverColour=(143, 143, 143),  # Colour of button when being hovered over
    pressedColour=(49, 212, 65),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: mp.flipflop_start() # Function to call when clicked on
)

button2 = Button(
    # Mandatory Parameters
    root,  # Surface to place button on
    1025,  # X-coordinate of top left corner
    400,  # Y-coordinate of top left corner
    175,  # Width
    75,  # Height

    # Optional Parameters
    text='Обновить значения',  # Text to display
    fontSize=24,  # Size of font
    textColour=(255,255,255),
    borderColour= (186, 186, 186),
    borderThickness=(2),
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=gray,  # Colour of button when not being interacted with
    hoverColour=(143, 143, 143),  # Colour of button when being hovered over
    pressedColour=(0, 255, 196),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: mp.updateoptions() # Function to call when clicked on
)

textbox1 = TextBox(root, 900, 30, 300, 40,
                   fontSize=28,
                   borderColour=gray,
                   textColour=black,
                   radius=6,
                   borderThickness=2)
textbox1.setText(mp.s_length)

textbox2 = TextBox(root, 900, 90, 300, 40,
                   fontSize=28,
                   borderColour=gray,
                   textColour=black,
                   radius=6,
                   borderThickness=2)
textbox2.setText(mp.s_radian)

textbox3 = TextBox(root, 900, 150, 300, 40,
                   fontSize=28,
                   borderColour=gray,
                   textColour=black,
                   radius=6,
                   borderThickness=2)
textbox3.setText(mp.s_angular_velocity)

textbox4 = TextBox(root, 900, 210, 300, 40,
                   fontSize=28,
                   borderColour=gray,
                   textColour=black,
                   radius=6,
                   borderThickness=2)
textbox4.setText(mp.s_gravity)

textbox5 = TextBox(root, 900, 270, 300, 40,
                   fontSize=28,
                   borderColour=gray,
                   textColour=black,
                   radius=6,
                   borderThickness=2)
textbox5.setText(mp.s_mass)

textbox6 = TextBox(root, 900, 330, 300, 40,
                   fontSize=28,
                   borderColour=gray,
                   textColour=black,
                   radius=6,
                   borderThickness=2)
textbox6.setText(mp.s_damping_factor)


running = True
while running:
    root.fill(white)
    mp.update()
    label1 = font.render("Длина маятника:", True, black)
    root.blit(label1, (900, 10))

    label2 = font.render("Начальный угол в радианах:", True, black)
    root.blit(label2, (900, 70))

    label3 = font.render("Угловая скорость:", True, black)
    root.blit(label3, (900, 130))

    label4 = font.render("Ускорение свободного падения:", True, black)
    root.blit(label4, (900, 190))

    label5 = font.render("Масса объекта:", True, black)
    root.blit(label5, (900, 250))

    label6 = font.render("Коэффициент затухания:", True, black)
    root.blit(label6, (900, 310))


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    pygame_widgets.update(events)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
