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

    """
    メインメニューの注文
    """
    tm.get_order(category=mm.MAIN_NUM)
    if tm.ask_yes_or_no(tm.MESSAGE_ASK_TICKETING):
        tm.issue_ticket()

    """
    サイドメニュー1の注文
    """
    while tm.ask_yes_or_no(tm.MESSAGE_ASK_ORDER_SIDE1) == True:
        tm.get_order(category=mm.SIDE1_NUM)

    if tm.ask_yes_or_no(tm.MESSAGE_ASK_TICKETING):
        tm.issue_ticket()

    """
    サイドメニュー2の注文
    """
    while tm.ask_yes_or_no(tm.MESSAGE_ASK_ORDER_SIDE2) == True:
        tm.get_order(category=mm.SIDE2_NUM)

    tm.issue_ticket()


if __name__ == "__main__":
    main()
