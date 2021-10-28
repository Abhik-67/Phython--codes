class PlacementPreparation:
    def __init__(self):
        self.course = "TCS Campus preparation"
        self.duration = "2 months"
   
    def show(self):
        print("Course:", self.course)   #Course: TCS Campus preparation
        print("Duration:", self.duration) #Duration: 2 months
outer = PlacementPreparation()
outer.show()



class Color:

  def __init__(self):
    self.name = 'Green'
    self.lg = self.Lightgreen()
    
  def show(self):
    print("Name:", self.name)   #Name: Green
    
  class Lightgreen:
     def __init__(self):
        self.name = 'Light Green'
        self.code = '024avc'
    
     def display(self):
        print("Name:", self.name) #Name: Light Green
        print("Code:", self.code) #Code: 024avc
  
outer = Color()
outer.show()
g = outer.lg
g.display()
