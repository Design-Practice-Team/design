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
    ui = classes.UserInterface(sc, mm)

    """
    メインメニューの注文
    """
    ui.get_order(category=mm.MAIN_NUM)
    if ui.ask_yes_or_no(ui.MESSAGE_ASK_TICKETING):
        ui.issue_ticket()

    """
    サイドメニュー1の注文
    """
    while ui.ask_yes_or_no(ui.MESSAGE_ASK_ORDER_SIDE1) == True:
        ui.get_order(category=mm.SIDE1_NUM)

    if ui.ask_yes_or_no(ui.MESSAGE_ASK_TICKETING):
        ui.issue_ticket()

    """
    サイドメニュー2の注文
    """
    while ui.ask_yes_or_no(ui.MESSAGE_ASK_ORDER_SIDE2) == True:
        ui.get_order(category=mm.SIDE2_NUM)

    ui.issue_ticket()


if __name__ == "__main__":
    main()
