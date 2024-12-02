class CountInstances: 
    counter = 0
    def __init__(self): 
        CountInstances.counter += 1
    def __del__(self): 
        CountInstances.counter -= 1
    @staticmethod
    def getNumInstances():
        return CountInstances.counter


c1 = CountInstances()
print(CountInstances.getNumInstances())
c2 = CountInstances()
print(CountInstances.getNumInstances())
print(c1.getNumInstances())