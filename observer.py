# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------

class Subject:
    
    observers = []

    def add(self, obj):
        self.observers.append(obj)

    def remove(self, obj):
        pass

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(args)

class Observer:
    def update(self):
        raise NotImplementedError("Update Delegation")


class ConcreteObserverA(Observer):
    def __init__(self, obj):
        self.observer_a = obj
        self.observer_a.add(self)

    def update(self, *args, **kwargs):
        print("\nUpdate within ConcreteObserverA")
        print("\nA new registration was made:", args)
