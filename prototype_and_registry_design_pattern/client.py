from prototype_class import Train
from train_prototype_registry import Train_Prototype_Registry

if __name__ == '__main__':
    
    morning = Train()
    morning.setfare(10)
    morning.setengine_type('IC engine')
    morning.setseats(500)
    morning.settimings('morning')

    afternoon = Train()
    afternoon.setfare(10)
    afternoon.setengine_type('IC engine')
    afternoon.setseats(200)
    afternoon.settimings('afternoon')

    evening = Train()
    evening.setfare(10)
    evening.setengine_type('IC engine')
    evening.setseats(700)
    evening.settimings('evening')

    registry = Train_Prototype_Registry()
    registry.save(morning)
    registry.save(afternoon)
    registry.save(evening)

    Mumbai_express = registry.get('morning')
    Delhi_express = registry.get('afternoon')
    Chennai_express = registry.get('evening')

    Mumbai_express.setstations('Mumbai')
    Delhi_express.setstations('Delhi')
    Chennai_express.setstations('Chennai')

    print(Mumbai_express)
    print(Delhi_express)
    print(Chennai_express)




