import classes


def main():
    """
    本プログラムのメイン関数

    Args:
        なし
    Return:
        なし
    """

    factory_a = classes.AbstractPizzaFactory(classes.FactoryA())
    factory_a.make_pizza("high")
    factory_a.check_pizza()

    """
    新種類のピザが追加された際の機能追加
    """
    print("------------------")
    factory_b = classes.AbstractPizzaFactory(classes.FactoryB())
    factory_b.make_pizza("low")
    factory_b.check_pizza()


if __name__ == "__main__":
    main()
