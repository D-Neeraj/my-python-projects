Dishes = """
Dishes Available:\n
(Example: 2-2, 4-1 i.e: Dosa * 2qty, Pongal * 1qty)\n
1.Idly      - $20   6.Chicken Briyani   - $140  11.Veg Fried Rice       - $60
2.Dosa      - $40   7.Mutton Briyani    - $180  12.Chicken Fried Rice   - $90
3.Poori     - $50   8.Veg Meals         - $100  13.Tandoori             - $210
4.Pongal    - $30   9.Chicken 65        - $80   14.Parotta              - $20
5.Idiyappam - $20   10.Chicken lollypop - $105  15.Shawarma             - $100
"""



# if __name__ == '__main__':
print("")
print("\t\t\t\t\t\t****** WELCOME_TO_HOTEL_MAZHAI_THULI ******")
option = int(input("Press 1 to Order\nPress 2 to Exit\n"))
if option==1:
    print(Dishes)
    orders=input("Please select your dishes:").split(",")
    print(orders)