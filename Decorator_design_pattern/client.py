from components.cones.normal_cone import Normal_Cone
from components.cones.orange_cone import Orange_Cone
from components.cones.vanila_cone import Vanila_Cone
from components.scoops.buttermilk_scoop import Buttermilk_Scoop
from components.scoops.chocolate_scoop import Chocolate_Scoop
from components.scoops.vanila_scoop import Vanila_Scoop
from components.toppings.chocolate_toppings import Chocolate_toppings
from components.toppings.vanila_toppings import Vanila_toppings

class client():
    icecream = Vanila_toppings(Vanila_Cone(Chocolate_Scoop(Orange_Cone())))
    print('cost:', icecream.get_cost())
    print('Icecream:', icecream.get_discription())