import pandas as pd
import pprint


class MarchandideMaster:
    OPTION_NUM = "4"
    MARCHANDISE_MASTER = pd.DataFrame(
        columns=["ID", "Category", "Name", "Set", "Option", "Price"],
        data=[
            ["001", "1", "牛丼", True, 1, 380],
            ["002", "1", "豚丼", True, 1, 350],
            ["003", "1", "鮭定食", True, 0, 450],
            ["101", "2", "野菜サラダ", True, 2, 100],
            ["102", "2", "ポテトサラダ", True, 2, 130],
            ["103", "2", "漬物", True, 0, 100],
            ["104", "2", "生卵", False, 0, 60],
            ["105", "2", "温泉卵", False, 0, 70],
            ["201", "3", "味噌汁", True, 0, 60],
            ["202", "3", "豚汁", False, 0, 190],
            ["203", "3", "スープ", True, 0, 200],
            ["401", "4", "並", False, 1, 0],
            ["402", "4", "大盛り", False, 1, 100],
            ["403", "4", "特盛り", False, 1, 200],
            ["404", "4", "ゴマドレッシング", False, 2, 0],
            ["405", "4", "和風ドレッシング", False, 2, 0],
        ],
    )


class ShoppingCart:
    def __init__(self):
        self.order_df = pd.DataFrame(columns=[], data=[])
        self.total_amount = 0
        self.input_amount = 0
        self.discount_amount = 0
        self.change_amount = 0

    def calculate_total_amount(self):
        """
        現在の合計金額を算出するメソッド

        Args:
            なし
        Return:
            なし
        """
        self.total_amount = self.order_df["Price"].sum()

    # def calculate_set_discount(self):
    #     """
    #     現在の割引金額を算出するメソッド

    #     Args:
    #         なし
    #     Return:
    #         なし
    #     """


class TicketingMachine:
    INDEX_0 = 0

    def __init__(self, shopping_cart, marchandise_master):
        self.sc = shopping_cart
        self.mm = marchandise_master

    def get_order(self, category):
        """
        ユーザーからの注文を取得するメソッド

        Args:
            category(str) : 商品の分類番号
        Return:
            なし
        """

        self._show_menu(category)
        self._get_menu(category)

        self.sc.calculate_total_amount()
        # self.shopping_cart.calculate_set_discount()

        self._show_current_status()

    def _show_menu(self, category):
        """
        商品の分類番号に応じた、メニューの一覧を標準出力する。

        Args:
            category(str) : 商品の分類番号
        Return:
            なし
        """
        # print出力の体裁を整える
        pd.set_option("display.unicode.east_asian_width", True)

        print(
            self.mm.MARCHANDISE_MASTER.query(f'Category == "{category}"')[
                ["ID", "Name", "Price"]
            ]
        )

    def _show_current_status(self):
        """
        現在の注文一覧、投入金額、合計金額、割引金額を標準出力する。

        Args:
            なし
        Return:
            なし
        """
        print("現在の注文一覧")
        pprint.pprint(self.shopping_cart.order_df)

        print("投入金額")
        print(self.shopping_cart.input_amount)

        print("合計金額")
        print(self.shopping_cart.total_amount)

        print("割引金額")
        print(self.shopping_cart.discount_amount)

    def _get_menu(self, category):
        """
        ユーザーからのメニューID値の入力を受け付ける.

        Args:
            category(str):メニューID値
        Return:
            なし
        TODO:
            category変数を用いて、ユーザー入力のvalidationをする.
            ※本物の券売機では、UIでユーザーの行動を制限する思うので、入力値の検証は不要
            余力があったら実装する。
        """
        menu_id = input("メニューIDを入力してください: ")

        # TODO menu_idの検証をここで行う
        # メニュー名と価格の取得
        menu = self.mm.MARCHANDISE_MASTER.query(f'ID == "{menu_id}"')
        self.sc.order_df.append(menu)

        # オプション品の受付と追加
        if menu.at[self.INDEX_0, "Option"] != 0:
            # TODO 上記で選択したメニューに関連するおオプション品だけ表示するようにする.
            self._show_menu(self.mm.OPTION_NUM)
            option_id = input("オプション品のメニューIDを入力してください: ")

            # TODO menu_idの検証をここで行う
            option = self.mm.MARCHANDISE_MASTER.query(f'ID == "{option_id}"')
            self.sc.order_df.append(option)

    def get_input_amount(self):
        """
        投入金額のユーザー入力を受け付ける

        Args:
            なし
        Return:
            なし
        """
        amount = input("投入金額をを入力してください: ")

        if amount.isdigit() == False:
            print("[Error]金額が不正です")
            exit()

        self.shopping_cart.input_amount = int(amount)

    def get_ticketing(self):
        """
        発券のユーザー入力を受け付ける

        Args:
            なし
        Return:
            なし
        """
        user_input = input("発券しますか？(yes/no): ")

        if user_input not in ["yes", "no"]:
            print("[Error]入力値が不正です（yesもしくはno）")
            exit()
