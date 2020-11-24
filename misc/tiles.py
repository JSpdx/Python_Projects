
# rectangles squares triangles
#dimensions | color | area | description


class Rectangle(object):

    def __init__(self, width=4, height=4, color='white'):
        self.width = width
        self.height = height
        self.color = color
        
        

    def area(self):
        return self.width * self.height

    @property
    def description(self):
        return f"Rec: w:{self.width} h:{self.height} color:{self.color} area: {self.area}"

    def __str__(self):
        return self.description

    def __repr__(self):
        return self.description

class Square(Rectangle):
    def __init__(self, width=3, color='pink'):
        super().__init__(width=width, height=width, color=color)
        #self.description = f"square w:{self.width} h:{self.height} color:{self.color}"

    
    

shapes= [
    Rectangle(width=10, height=10),
    Rectangle(),
    Rectangle(width=5, height=8),
    Rectangle(width=3, height=7),
]

for s in shapes:
    print(s)
    print(s.description, 'has area', s.area())
