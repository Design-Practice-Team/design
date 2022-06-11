import classes


def main():
    """
    本システムのメイン関数

    Args:
        なし
    Return:
        なし
    """

    mm = classes.MarchandideMaster()
    sc = classes.ShoppingCart()
    tm = classes.TicketingMachine(sc, mm)

    tm.get_order(category="1")


if __name__ == "__main__":
    main()
