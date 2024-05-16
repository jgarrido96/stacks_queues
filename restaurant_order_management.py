
# Task 1: Design a queue-based data structure to represent the kitchen's order queue, where orders are processed in the order they are received.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Cannot dequeue from an empty queue!')
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Cannot peek from an empty queue.')
        
    def size(self):
        return len(self.items)
    
# Task 2: Implement functions to add new orders to the kitchen's order queue and remove orders when they are completed.

class Menu:
    def __init__(self):
        self.item = Queue()
    
    def add_to_menu(self, menu_item):
        self.item.enqueue(menu_item)
        print(f'Menu item {menu_item} has been added!')

    def show_menu(self):
        if not self.item.is_empty():
            menu_item = self.item.dequeue()
            print(f'Your menu item search: {menu_item}')
        else:
            print("There are no menu items.")

# Task 3: Design a queue-based data structure to represent the customer order queue, where orders are prioritized based on factors such as customer waiting time and order complexity.

class Order:
    def __init__(self):
        self.order = Queue()

# Task 4: Implement functions to add new orders to the customer order queue, process orders, and notify customers when their orders are ready for pickup or delivery.

    def add_to_orders(self, custy_order):
        self.order.enqueue(custy_order)
        print(f'Customer Order: {custy_order}')

    def show_custy_order(self):
        if not self.order.is_empty():
            custy_order = self.order.dequeue()
            print(f'This customers order: {custy_order}')
        else:
            print("No orders have been placed")


# Task 5: Test the order management system with sample orders to ensure its correctness and efficiency.

jdoggs_menu = Menu()
customers = Order()

jdoggs_menu.add_to_menu("JDoggs BLT")
jdoggs_menu.add_to_menu("JDoggs Sliders")
jdoggs_menu.add_to_menu("JDoggs Un-Curly Fries")
jdoggs_menu.show_menu()
jdoggs_menu.show_menu()
jdoggs_menu.show_menu()


customers.add_to_orders("JDoggs BLT")
customers.add_to_orders("JDoggs Sliders")
customers.show_custy_order()
customers.show_custy_order()
