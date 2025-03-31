class Item:

    
    def __init__(self,profit,weight,name):
        self.weight = weight
        self.profit = profit
        self.name = name
    def __str__(self):
        return f"name:{self.name},weight:{self.weight},profit:{self.profit}"

def fractionalKnapsack(W,arr:list):
    arr.sort(key=lambda x:(x.profit/x.weight),reverse = True)

    finalValue = 0.0
    addedItems = []

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalValue += item.profit
            addedItems.append(item)
        else:
            finalValue += item.profit * W/item.weight
            addedItems.append(Item(item.profit * W/item.weight,W/item.weight,item.name))
            break
    print(item.weight)

    return finalValue,addedItems

if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10,'mug'), Item(100, 20,'bag'), Item(120, 30,'car')]
    max_val,items2 = fractionalKnapsack(W,arr=arr)
    print(max_val)
    for k in items2:
        print(k)