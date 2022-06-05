import pandas as pd
import pprint


class MarchandideMaster:
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
        self.order_list = []
        self.total_amount = 0
        self.input_amount = 0
        self.discount_amount = 0
        self.change_amount = 0


class TicketingMachine:
    def __init__(self, shopping_cart, marchandise_master):
        self.shopping_cart = shopping_cart
        self.marchandise_master = marchandise_master

    def show_menu(self, category):
        """
        メインメニューの一覧を標準出力する。

        Args:
            category(str) : 商品の分類番号
        Return:
            なし
        """
        # print出力の体裁を整える
        pd.set_option("display.unicode.east_asian_width", True)

        print(
            self.marchandise_master.query(f'Category == "{category}"')[
                ["ID", "Name", "Price"]
            ]
        )

    def show_current_status(self):
        """
        現在の注文一覧、投入金額、合計金額、割引金額を標準出力する。

        Args:
            なし
        Return:
            なし
        """
        print("現在の注文一覧")
        pprint.pprint(self.shopping_cart.order_list)

        print("投入金額")
        print(self.shopping_cart.input_amount)

        print("合計金額")
        print(self.shopping_cart.total_amount)

        print("割引金額")
        print(self.shopping_cart.discount_amount)

    def get_menu(self, category):
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
        menu_id = input("メニュー番号を入力してください: ")

        # TODO menu_idの検証

        # メニュー名と価格の取得（必ず1レコード返ってくる想定。1レコード目のみを取得）
        menu = self.marchandise_master.MARCHANDISE_MASTER.query(f'ID == "{menu_id}"')[
            ["Name", "Price", "Option"]
        ].to_dict(orient="index")[0]

        self.shopping_cart.order_list.append([menu["Name"], menu["Price"]])

        # オプション品の受付と追加
        if menu["Option"] != 0:
            self.show_menu("4")
            option_id = input("オプション品のメニュー番号を入力してください: ")

            # TODO menu_idの検証をここで行う
            option = self.marchandise_master.MARCHANDISE_MASTER.query(
                f'ID == "{menu_id}"'
            )[["Name", "Price"]].to_dict(orient="index")[0]
            self.shopping_cart.order_list.append([option["Name"], option["Price"]])

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
