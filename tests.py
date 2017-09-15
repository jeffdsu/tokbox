from tokbox import get_purchasing_power_during_sale, get_price_of_book_during_sale


def validate_usable_dollars_lt_initial_price_case():

    usable_dollars = 40

    initial_book_price = 50
    discount = 4
    price_floor = 25

    (num_books, remaining_dollars) = (num_books, remaining_dollars) = get_purchasing_power_during_sale(initial_book_price, discount, price_floor, usable_dollars)


    assert num_books == 0 and remaining_dollars == 40

def validate_given_case():

    usable_dollars = 300

    initial_book_price = 50
    discount = 4
    price_floor = 25

    (num_books, remaining_dollars) = (num_books, remaining_dollars) = get_purchasing_power_during_sale(initial_book_price, discount, price_floor, usable_dollars)


    assert num_books == 8 and remaining_dollars == 9

def validate_initial_book_negative_case():

    usable_dollars = 300

    initial_book_price = -1
    discount = 4
    price_floor = 25

    try:
        (num_books, remaining_dollars) = get_purchasing_power_during_sale(initial_book_price, discount, price_floor, usable_dollars)

    except Exception as e:
        # If I were to build a full app, these would probably go into some exception library, and compares would be done on Exception objs
        assert str(e) == 'Initial price should be greater than 0'
        return

    assert False, "Should have thrown negative value exception"

def validate_discount_negative_case():

    usable_dollars = 300

    initial_book_price = 50
    discount = -4
    price_floor = 25

    try:
        (num_books, remaining_dollars) = get_purchasing_power_during_sale(initial_book_price, discount, price_floor, usable_dollars)

    except Exception as e:
        # If I were to build a full app, these would probably go into some exception library, and compares would be done on Exception objs
        assert str(e) == 'Discount cannot be less than 0'
        return

    assert False, "Should have thrown negative value exception"

def validate_price_floor_negative_case():

    usable_dollars = 300

    initial_book_price = 50
    discount = 4
    price_floor = -25

    try:
        (num_books, remaining_dollars) = get_purchasing_power_during_sale(initial_book_price, discount, price_floor, usable_dollars)

    except Exception as e:
        # If I were to build a full app, these would probably go into some exception library, and compares would be done on Exception objs
        assert str(e) == 'Price floor cannot be less than 0'
        return

        assert False, "Should have thrown negative value exception"

def validate_price_floor_lt_initial_price_negative_case():

    usable_dollars = 300

    initial_book_price = 20
    discount = 4
    price_floor = 25

    try:
        (num_books, remaining_dollars) = get_purchasing_power_during_sale(initial_book_price, discount, price_floor, usable_dollars)

    except Exception as e:
        # If I were to build a full app, these would probably go into some exception library, and compares would be done on Exception objs
        assert str(e) == 'Price floor cannot be greater than Initial book price'
        return

    assert False, "Should have thrown negative value exception"

if __name__ == "__main__":

    validate_given_case()
    validate_usable_dollars_lt_initial_price_case()
    validate_initial_book_negative_case()
    validate_discount_negative_case()
    validate_price_floor_negative_case()
    validate_price_floor_lt_initial_price_negative_case()