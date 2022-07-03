class AbstractPizzaFactory:
    amount_dict = {"high": 12, "medium": 10, "low": 8}

    def __init__(self, pizza_factory):
        self.factory = pizza_factory
        self.pizza_materials = []

    def make_pizza(self, amount_str="mudium"):
        """
        各種類のピザの素材クラスを生成し、リストに格納するメソッド

        Args:
            amount_str(str): 分量を示す文字列（amount_dictのKeyに相当)
        Return:
            なし
        """
        amount = self.amount_dict[amount_str]
        self.pizza_materials.append(self.factory.add_dough(amount))
        self.pizza_materials.append(self.factory.add_source(amount))
        self.pizza_materials.append(self.factory.add_topping(amount))

    def check_pizza(self):
        """
        各種類のピザの素材オブジェクトの素材名と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        for material in self.pizza_materials:
            material.check()

    def add_dough(self, amount=10):
        """
        doughオブジェクト生成のための抽象メソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        pass

    def add_source(self, amount=10):
        """
        sourceオブジェクト生成のための抽象メソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        pass

    def add_topping(self, amount=10):
        """
        toppingオブジェクト生成のための抽象メソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        pass


class FactoryA(AbstractPizzaFactory):
    def __init__(self):
        pass

    def add_dough(self, amount=10):
        """
        doughオブジェクト生成するメソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        return WheatDough(amount)

    def add_source(self, amount=10):
        """
        sourceオブジェクト生成するメソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        return TomatoSauce(amount)

    def add_topping(self, amount=10):
        """
        toppingオブジェクト生成のための抽象メソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        return CornTopping(amount)


class Dough:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        """
        素材と分量を標準出力する抽象メソッド

        Args:
            なし
        Return:
            なし
        """
        pass


class WheatDough(Dough):
    def check(self):
        """
        素材と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        print(f"素材：小麦粉、分量：{self.amount}")


class Sauce:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        """
        素材と分量を標準出力する抽象メソッド

        Args:
            なし
        Return:
            なし
        """
        pass


class TomatoSauce(Sauce):
    def check(self):
        """
        素材と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        print(f"素材：トマトソース、分量：{self.amount}")


class Topping:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        """
        素材と分量を標準出力する抽象メソッド

        Args:
            なし
        Return:
            なし
        """
        pass


class CornTopping(Topping):
    def check(self):
        """
        素材と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        print(f"素材：コーン、分量：{self.amount}")


# 新しいピザ追加
class FactoryB(AbstractPizzaFactory):
    def __init__(self):
        pass

    def add_dough(self, amount=10):
        """
        doughオブジェクト生成するメソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        return RiceDough(amount)

    def add_source(self, amount=10):
        """
        sourceオブジェクト生成するメソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        return BasilSauce(amount)

    def add_topping(self, amount=10):
        """
        toppingオブジェクト生成のための抽象メソッド

        Args:
            amount(int): 分量
        Return:
            なし
        """
        return CheeseTopping(amount)


class RiceDough(Dough):
    def check(self):
        """
        素材と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        print(f"素材：米粉、分量：{self.amount}")


class BasilSauce(Sauce):
    def check(self):
        """
        素材と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        print(f"素材：バジルソース、分量：{self.amount}")


class CheeseTopping(Topping):
    def check(self):
        """
        素材と分量を標準出力するメソッド

        Args:
            なし
        Return:
            なし
        """
        print(f"素材：チーズ、分量：{self.amount}")
