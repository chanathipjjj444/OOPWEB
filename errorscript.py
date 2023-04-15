

# room_cat = RoomList()
# room1 = Room(101, 'Standard', 3, 1000, 'TV, AC', 'Queen', True)
# room2 = Room(102, 'Deluxe', 3, 2000, 'TV, AC, Jacuzzi', 'King', True)
# room3 = Room(103, 'Deluxe', 4, 3000, 'TV, AC, Jacuzzi', 'Queen', True)

# room_cat.add_room(room1)
# room_cat.add_room(room2)
# room_cat.add_room(room3)


# add_on_cat = Addons()
# breakfast1 = BreakfastService("breakfast","corn soup","soup", 100)
# breakfast2 = BreakfastService("breakfast","sisler salad","salad",120)
# spa1 = SpaService("spa","Open 9am","picture",100)
# add_on_cat.add_breakfast_service(breakfast1)
# add_on_cat.add_spa_service(spa1)
# add_on_cat.add_breakfast_service(breakfast2)

# add_on_cat2 = Addons()
# breakfast3 = BreakfastService("breakfast","sisler-salad","salad", 100)
# breakfast4 = BreakfastService("breakfast","oishi buffe","buffe",350)
# add_on_cat2.add_breakfast_service(breakfast3)
# add_on_cat2.add_breakfast_service(breakfast4)

# hotel1 = Hotel('Hotel A', 5, 2, "A", "Lardprao", "Bangkok", [room1, room2],[add_on_cat])
# hotel2 = Hotel('Hotel B', 5, 2, "A", "Lardprao", "Bangkok", [room1, room2],[add_on_cat2])

# # create a hotel catalog and add the hotel
# catalog = HotelCatalog()
# catalog.add_hotel(hotel1)
# catalog.add_hotel(hotel2)
# print("before booking")

# hotel1.show_room()


# book1=Booking(room_cat,"28-2-2021","1-3-2021",3,1)

# book1.book_room_check("Hotel A", 101)

# hotel1.show_room()

# credit_cat = Catalog_creditcard()
# credit_cat.manage_card()

# credit1 = Creditcard(101,"Prayut","475-123-568")
# credit1.receive_data_card(credit_cat.card_number_list,credit_cat.card_name_list)


# credit1.check_credit_card()
# credit1.balance_in_card(credit_cat.balance_list)
# print("Balance in credit card is "+str(credit1.get_balance_in_card())+" bath")

# coupon = TypeCoupon("coupon A","discount 100 bath",100)
# promotion = Promotion()
# promotion.add_coupon(coupon)

# pay1 = Payment( 457123450, credit1)
# pay1.set_money(credit1.get_balance_in_card())
# pay1.set_price_room(room1.price_room)
# print("Price room "+str(room1.room_number)+" is "+str(pay1.get_price_room())+" bath")
# print("##Before Process Payment")
# print("Payment status is ",pay1.get_payment_status())

# pay1.set_total_day(book1.total_day)
# pay1.set_add_on_price(book1.service_price)
# pay1.set_total_price()
# pay1.use_coupon()
# pay1.process_payment()

# #book second time 
# book2=Booking(room_cat,"20-3-2021","25-3-2021",3,1)
# book2.book_room_check("Hotel B", 101)

