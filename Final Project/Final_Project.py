#recipeapplication
class recipe1():

    def __init__(self,recipename,products):
     self.recipename=recipename
     self.products=products
    def cook(self):
        print("Cook it anymore!")
    def mix(self):
        print("Mix it!")
    def add(self):
        print("Add!")
    def showRecipeName(self):
        print("Pastry",self.recipename)
    def showProducts(self):
        print("a glass of warm water".self.products)
        print("one teacup of oil".self.products)
        print("a glass of warm milk".self.products)
        print("blind eye flour".self.products)
        print("two eggs".self.products)
        print("one fresh yeast".self.products)
        print("one teaspoon of sugar".self.products)
        print("salt".self.products)
    def Making(self):
        print("mix the yeast with milk,water and sugar in a bowl to dissolve:")
        recipe1=mix("yeast")
        recipe1.mix()
        print("add egg,salt and oil on it:")
        recipe1=add("egg,salt,oil")
        recipe1.add()
        print("add the flour slowly and knead until you have a soft dough:")
        print("then, cover it and let it rest for about 1 hour to ferment:")
        print("take shape from the rested dough and place it on a tray:")
        print("leave it on the tray for 10-15 minutes to ferment:")
        recipe1=cook("pastery")
        recipe1.cook()
class recipe2():        
    def __init__(self,recipename,products):
            self.recipename=recipename
            self.products=products
    def showRecipeName(self):
            print("Lemon IceCream",self.recipename) 
def showProducts(self):
        print("three glasses of milk",self.products)
        print("four lemons",self.products)
        print("one tea glass of sugar",self.products)
        print("one teaspoon of sahlep",self.products)
        print("one tablespoon of sugar",self.products)
        print("half a teaspoon of turmeric",self.products)
def Making(self):
    print("in a saucepan, whisk the salep, milk and sugar and boil over medium heat:")
    print("turn off the heat 2-3 minutes after it starts to boil:")
    print("cool by stirring occasionally:")
    print("grate the zest of lemons in a different bowl and squeeze the juice:")
    print("add sugar and turmeric on it and mix:")
    recipe2=add("sugar")
    recipe2.add()
    print("add the lemon mixture to the cooled salve and whisk it well:")
    recipe2=mix("lemon")
    recipe2.mix()
    print("when your ice cream is smooth, put it in the freezer and let it sit for 4-5 hours:")
    print("during the waiting period, take it out of the freezer every hour, whisk it with a whisk and let it get consistency:")


class recipe3():
   def __init__(self,recipename,products):
       self.recipename=recipename
       self.products=products
   def showRecipeName(self):
           print("Omelette",self.recipename)
def showProducts(self):
    print("four eggs",self.products)
    print("half teaspoon of salt",self.products)
    print("half teaspoon of black pepper",self.products)
    print("one tablespoon of butter",self.products)
    print("one tablespoon of olive oil",self.products)
def Making(self):
    print("in a deep mixing bowl, take 4 eggs into a bowl:")
    print("combine half a teaspoon of salt and pepper,with a whisk, whisk it from bottom to top until air bubbles form:")
    print("heat your pan and heat 1 tablespoon of butter and olive oil each:")
    print("then pour the egg mixture into the pan,reduce the heat and cook until the bottom is golden:")
    recipe3=mix("egg")
    recipe3.mix()
    recipe3=cook("egg")
    recipe3.cook()
