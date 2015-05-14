import tkinter
from tkinter.ttk import Combobox
from random import randint

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

GRASS_BOTTOM = WINDOW_HEIGHT
GRASS_TOP = WINDOW_HEIGHT - 200
GRASS_COLOR = '#5e5' #green

TREE_INITIAL_BASE_X = 400
TREE_INITIAL_BASE_Y = 1
TREE_INITIAL_SIZE = 5


trunk_points = [
    (40, 45), (47.5, 52), (52.5, 50), (52.5, 50), (52.5, 90),
    (54, 93), (60, 100), (64, 103), (68, 106), (73, 110),
    (66, 107), (62, 103), (55, 100), (53, 103), (54, 108),
    (50, 115), (55, 109), (48, 103), (50, 100), (40, 105), (27, 107),
    (17, 116), (18, 105), (30, 102), (35, 100), (43, 90), (42.5, 45)
]

leafs_points = [
    (42.5, 50), (47.5, 52), (52.5, 50), (60, 55),
    (80, 60), (90, 55), (95, 45), (102, 35), (95, 25),
    (97, 25), (80, 10), (70, 5), (62, 10), (50, 5),
    (35, 10), (20, 15), (15, 25), (10, 35), (15, 45),
    (10, 55), (20, 65), (35, 60), (42.5, 50)
]

leaf_points = [
    (5, 3), (5.5, 1), (7, 0), (7, 2), (5, 3)
]





class Tree:
    def __init__(self, base_x, base_y, max_size):
        self.base_x = base_x
        self.base_y = base_y
        self.size = 1
        self.max_size = max_size


        scaled_trunk_coords = []
        for point in trunk_points:
            scaled_trunk_coords.append(self.size * point[0] + base_x)
            scaled_trunk_coords.append(self.size * point[1] + base_y)
        self.trunk = canvas.create_polygon(scaled_trunk_coords, fill='brown', smooth=True)

        scaled_leafs_coords = []
        for point in leafs_points:
            scaled_leafs_coords.append(self.size * point[0] + base_x)
            scaled_leafs_coords.append(self.size * point[1] + base_y)
        self.leafs = canvas.create_polygon(scaled_leafs_coords, fill='green', smooth=True)

    def growing(self):
        pass

    def generate_leaf(self):
        leaf_base_x = self.base_x + randint(10 * self.size, 100 * self.size)
        leaf_base_y = self.base_y + 45 * self.size

        scaled_leaf_coords = []
        for point in leaf_points:
            scaled_leaf_coords.append(self.size * point[0] + leaf_base_x)
            scaled_leaf_coords.append(self.size * point[1] + leaf_base_y)
        leaf = canvas.create_polygon(scaled_leaf_coords, fill='green', smooth=True)

        falling_place = randint(600, 700)

        self.falling_leaf(leaf, leaf_base_x, leaf_base_y, falling_place)

    def falling_leaf(self, leaf, leaf_base_x, leaf_base_y, falling_place):
        leaf_base_y += 5
        if leaf_base_y < falling_place:
            scaled_leaf_coords = []
            for point in leaf_points:
                scaled_leaf_coords.append(self.size * point[0] + leaf_base_x)
                scaled_leaf_coords.append(self.size * point[1] + leaf_base_y)
            canvas.coords(leaf, tkinter._flatten(scaled_leaf_coords))
            canvas.after(30, self.falling_leaf, leaf, leaf_base_x, leaf_base_y, falling_place)

    def generate_apple(self):
        if self.size > self.max_size:
            return
        chance_to_grow = randint(1, 10)
        if chance_to_grow == 5:
            base_x = randint(self.base_x + 20*self.size, self.base_x + 80*self.size)
            base_y = randint(self.base_y + 15*self.size, self.base_y + 50*self.size)
            apple = Apple(base_x, base_y, self.size)
            apple.growing(0)
            canvas.tag_bind(apple.apple, '<ButtonPress-1>', lambda event, apple=apple:
                                     onAppleClick(event, apple))
        canvas.after(2000, self.generate_apple)


class Apple:
    def __init__(self, base_x, base_y, max_size):
        self.isDisrupted = False
        self.base_x = base_x
        self.base_y = base_y

        size = 0
        self.max_size = max_size
        self.leaf = canvas.create_polygon(base_x + 5 * size, base_y + 3 * size, base_x + 5.5 * size, base_y + 1 * size, base_x + 7 * size, base_y + 0 * size, base_x + 7 * size, base_y + 2 * size, base_x + 5 * size, base_y + 3 * size,  smooth=True, fill='green')
        self.apple = canvas.create_polygon(base_x + 5 * size, base_y + 3 * size, base_x + 6.5 * size, base_y + 2.5 * size, base_x + 8 * size, base_y + 3 * size, base_x + 8.5 * size, base_y + 5.5 * size, base_x + 7 * size, base_y + 8 * size, base_x + 5 * size, base_y + 7.8 * size, base_x + 3 * size, base_y + 8 * size, base_x + 1.5 * size, base_y + 5.5 * size, base_x + 2 * size, base_y + 3 * size, base_x + 3.5 * size, base_y + 2.5 * size, base_x + 5 * size, base_y + 3 * size, fill='red', smooth=True, outline='black')
        self.line = canvas.create_line(base_x + 5 * size, base_y + 1 * size, base_x + 5 * size, base_y + 3 * size, width=5, fill='brown', smooth=True)

    def change_size(self, size):
        self.size = size
        canvas.coords(self.leaf, self.base_x + 5 * size, self.base_y + 3 * size, self.base_x + 5.5 * size, self.base_y + 1 * size, self.base_x + 7 * size, self.base_y + 0 * size, self.base_x + 7 * size, self.base_y + 2 * size, self.base_x + 5 * size, self.base_y + 3 * size)
        canvas.coords(self.apple, self.base_x + 5 * size, self.base_y + 3 * size, self.base_x + 6.5 * size, self.base_y + 2.5 * size, self.base_x + 8 * size, self.base_y + 3 * size, self.base_x + 8.5 * size, self.base_y + 5.5 * size, self.base_x + 7 * size, self.base_y + 8 * size, self.base_x + 5 * size, self.base_y + 7.8 * size, self.base_x + 3 * size, self.base_y + 8 * size, self.base_x + 1.5 * size, self.base_y + 5.5 * self.size, self.base_x + 2 * self.size, self.base_y + 3 * self.size, self.base_x + 3.5 * self.size, self.base_y + 2.5 * self.size, self.base_x + 5 * self.size, self.base_y + 3 * self.size)
        canvas.coords(self.line, self.base_x + 5 * size, self.base_y + 1 * size, self.base_x + 5 * size, self.base_y + 3 * size)

    def change_position(self, base_x, base_y):
        self.base_x = base_x
        self.base_y = base_y
        canvas.coords(self.leaf, self.base_x + 5 * self.size, self.base_y + 3 * self.size, self.base_x + 5.5 * self.size, self.base_y + 1 * self.size, self.base_x + 7 * self.size, self.base_y + 0 * self.size, self.base_x + 7 * self.size, self.base_y + 2 * self.size, self.base_x + 5 * self.size, self.base_y + 3 * self.size)
        canvas.coords(self.apple, self.base_x + 5 * self.size, self.base_y + 3 * self.size, self.base_x + 6.5 * self.size, self.base_y + 2.5 * self.size, self.base_x + 8 * self.size, self.base_y + 3 * self.size, self.base_x + 8.5 * self.size, self.base_y + 5.5 * self.size, self.base_x + 7 * self.size, self.base_y + 8 * self.size, self.base_x + 5 * self.size, self.base_y + 7.8 * self.size, self.base_x + 3 * self.size, self.base_y + 8 * self.size, self.base_x + 1.5 * self.size, self.base_y + 5.5 * self.size, self.base_x + 2 * self.size, self.base_y + 3 * self.size, self.base_x + 3.5 * self.size, self.base_y + 2.5 * self.size, self.base_x + 5 * self.size, self.base_y + 3 * self.size)
        canvas.coords(self.line, self.base_x + 5 * self.size, self.base_y + 1 * self.size, self.base_x + 5 * self.size, self.base_y + 3 * self.size)

    def growing(self, i):
        if i < self.max_size and not self.isDisrupted:
            self.change_size(i)
            canvas.after(10, self.growing, (i + 0.01))

    def falling(self, i):
        self.base_y += 5
        falling_place = randint(600, 700)
        if self.base_y < falling_place:

            self.change_position(self.base_x, self.base_y)
            window.after(30, self.falling, (i+1))

def windowdrag(event):
    chance_to_fall = randint(1, 100)
    if chance_to_fall == 5:
        pass# tree.generate_leaf()

def onAppleClick(event, apple):
    apple.isDisrupted = True
    apple.falling(1)

def make_tree(event):
    tree = Tree(event.x, event.y, 4)
    tree.generate_apple()

window = tkinter.Tk()
window.bind('<Configure>', windowdrag)
canvas = tkinter.Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bg='#bbe')


# tree = Tree(TREE_INITIAL_BASE_X, TREE_INITIAL_BASE_Y, TREE_INITIAL_SIZE)
tool_panel = tkinter.Frame(window, height=50, width=300)
tool_panel.pack()
tree_size_label = tkinter.Label(tool_panel, text='tree size: ')
tree_size_label.pack(side=tkinter.LEFT)
tree_size_combobox = Combobox(tool_panel, state='readonly', values=['1', '2', '3', '4'], width=10)
tree_size_combobox.pack()
grass = canvas.create_rectangle(0, GRASS_BOTTOM, WINDOW_WIDTH, GRASS_TOP, fill='#5e5')
canvas.tag_bind(grass, '<ButtonPress-1>', make_tree)
# tree.generate_apple()
# threading.Thread(target=tree.generate_apple).start()

canvas.pack()

window.mainloop()


