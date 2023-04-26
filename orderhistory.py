class OrderHistory:
    def __init__(self):
        self.history = []
        
    def show_history(self):
        for history in self.history:
            print("Date check in :",history.check_in, 
                  "Date check out:",history.check_out, 
                  "Number people:",history.num_people, 
                  "Total room:",history.num_room, 
                  "Hotel name:",history.hotel_name, 
                  "Room number:",history.room_number)
order_history = OrderHistory()