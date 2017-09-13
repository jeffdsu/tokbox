import logging
import argparse


def get_args():
    """
        Get input args
     """
    parser = argparse.ArgumentParser(description='Tokbox programming test')
    parser.add_argument('--initial_book_price', required=True, type=float,
                        help='initial book price')
    parser.add_argument('--discount', type=float, required=True,
                        help='discount per book')

    parser.add_argument('--price_floor', type=float, required=True,
                        help='price floor of sale')

    parser.add_argument('--usuable_dollars', type=float, required=True,
                        help='dollar amount purchaser has')


    args = parser.parse_args()

    return args


def get_price_of_book_during_sale(book_num):
    """
    Figures out how much the nth book will cost

    Accepts a book count

    Return dollar amount of the nth book
    """

    price_without_floor = CONST_initial_book_price - CONST_discount * (book_num - 1)

    return CONST_price_floor if price_without_floor <= CONST_price_floor else price_without_floor

def can_purchase(price_of_book, total_usuable_dollars, current_cost):
    """
    Checks with the remaining dollars, if the current book can be bought

    Accepts a the price of nth_book, total usuable dollars, and current cost of in cart

    Return True/False
    """

    if price_of_book <= (total_usuable_dollars - current_cost):
        return True
    return False

def check_purchasing_power(usable_dollar_amount, func_price_of_nth_book):
    """
    Figures out with a given amount of dollars, how many books, and the remaining dollars

    Accepts dollar amount, a function that calculates the nth book

    Return a (purchasable_book_count, remaing_dollars)

    Note: If this were a full on application, this should be moved a utils folder
    """
    temp_cost = 0
    book_count = 1

    while(temp_cost < usable_dollar_amount):  #TODO <- check > or >=


        price_of_nth_book = get_price_of_book_during_sale(book_count)

        logger.debug("[{}] price_of_nth_book = {}".format(book_count, price_of_nth_book))

        if can_purchase(price_of_nth_book, usable_dollar_amount, temp_cost):

            temp_cost += func_price_of_nth_book(book_count)
            logger.debug("[{}] temp_cost = {}".format(book_count, temp_cost))
            book_count += 1

        else:
            break

    # jeff - book - 1 because book_count will have incremented 1 extra time for last purchase
    return (book_count - 1, usable_dollar_amount - temp_cost)


def validate_and_return_initial_book_price(initial_book_price):
    if initial_book_price <= 0:
        raise Exception("Initial should be greater than 0")

    return  initial_book_price

def validate_and_return_discount(discount):

    if discount < 0:
        raise Exception("Discount cannot be less than 0")

    return discount


def validate_and_return_price_floor(price_floor, initial_book_price):

    if price_floor < 0:
        raise Exception("Price floor cannot be less than 0")

    if initial_book_price < price_floor:
        raise Exception("Price floor cannot be greater than Initial book price")

    return price_floor

def validate_usuable_dollars(usuable_dollars):
    if usuable_dollars < 0:
        raise Exception("usuable_dollars cannot be less than 0")

    return usable_dollars

if __name__ == "__main__":

    args = get_args()

    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG)

    # Once these are set, they should never be changed anywhere inside code
    CONST_initial_book_price = validate_and_return_initial_book_price(args.initial_book_price)
    CONST_discount = validate_and_return_discount(args.discount)
    CONST_price_floor = validate_and_return_price_floor(args.price_floor, CONST_initial_book_price)

    usable_dollars = args.usuable_dollars

    (num_books, remaining_dollars) = check_purchasing_power(usable_dollars, get_price_of_book_during_sale)

    logger.info("Number of purchasable books: {}".format(num_books))
    logger.info("Remaining dollars: {}".format(remaining_dollars))