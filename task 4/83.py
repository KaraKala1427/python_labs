


def sending_cost(amount_items, cost_item=2.95, cost_first=10.95):    
    
    total_cost = cost_first + cost_item*(amount_items-1)
    
    return total_cost

cost = float(input("Input number of items: "))

print("Total shipping charge: %f" %sending_cost(cost))