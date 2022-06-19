import pandas as pd


class MarchandideMaster:
    MAIN_NUM = "1"
    SIDE1_NUM = "2"
    SIDE2_NUM = "3"
    OPTION_NUM = "4"
    DISCOUNT_PRICE = 50

    MARCHANDISE_MASTER = pd.DataFrame(
        columns=["ID", "Category", "Name", "Set", "Option", "Price"],
        data=[
            ["101", "1", "牛丼", True, 1, 380],
            ["102", "1", "豚丼", True, 1, 350],
            ["103", "1", "鮭定食", True, 0, 450],
            ["201", "2", "野菜サラダ", True, 2, 100],
            ["202", "2", "ポテトサラダ", True, 2, 130],
            ["203", "2", "漬物", True, 0, 100],
            ["204", "2", "生卵", False, 0, 60],
            ["205", "2", "温泉卵", False, 0, 70],
            ["301", "3", "味噌汁", True, 0, 60],
            ["302", "3", "豚汁", False, 0, 190],
            ["303", "3", "スープ", True, 0, 200],
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

    def calculate_total_amount(self):
        """
        現在の合計金額を算出するメソッド

        Args:
            なし
        Return:
            なし
        """
        self.total_amount = self.order_df["Price"].sum()

    def calculate_set_discount(self):
        """
        割引金額を計算するメソッド

        Args:
            なし
        Return:
            なし
        """
        discount_set = {
            MarchandideMaster.MAIN_NUM,
            MarchandideMaster.SIDE1_NUM,
            MarchandideMaster.SIDE2_NUM,
        }
        if discount_set.issubset(self.order_df["Category"].tolist()):
            self.discount_amount = MarchandideMaster.DISCOUNT_PRICE


class TicketingMachine:
    INDEX_0 = 0
    OPTION_COL_NUM = 4
    MESSAGE_ASK_TICKETING = "発券しますか？(yes/no): "
    MESSAGE_ASK_ORDER_SIDE1 = "サイドメニュー1を注文しますか？(yes/no): "
    MESSAGE_ASK_ORDER_SIDE2 = "サイドメニュー2を注文しますか？(yes/no): "

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
        # メニューの取得
        self._show_menu(category)
        self._get_menu(category)

        # 金額の計算
        self.sc.calculate_total_amount()
        self.sc.calculate_set_discount()

        # 買い物状況の出力
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

        print("---------------------------------")
        print(
            self.mm.MARCHANDISE_MASTER.query(f'Category == "{category}"')[
                ["ID", "Name", "Price"]
            ]
        )

    def _show_option(self, option_no):
        """
        オプション番号に応じたオプションメニューの一覧を表示する

        Args:
            option_no(int) : オプション番号
        Return:
            なし
        """
        # print出力の体裁を整える
        pd.set_option("display.unicode.east_asian_width", True)

        print("---------------------------------")
        print(
            self.mm.MARCHANDISE_MASTER.query(
                f'Category == "{self.mm.OPTION_NUM}" and Option == {option_no}'
            )[["ID", "Name", "Price"]]
        )

    def _show_current_status(self):
        """
        現在の注文一覧、投入金額、合計金額、割引金額を標準出力する。

        Args:
            なし
        Return:
            なし
        """
        print("---------------------------------")
        print(f"現在の注文一覧：")
        print(self.sc.order_df)
        print(f"合計金額：{self.sc.total_amount}")
        print(f"割引金額：{self.sc.discount_amount}")
        print(f"支払金額：{self.sc.total_amount - self.sc.discount_amount}")
        print(f"投入金額：{self.sc.input_amount}")

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
        print("---------------------------------")
        menu_id = input("メニューIDを入力してください: ")

        # TODO menu_idの検証をここで行う
        # メニュー名と価格の取得
        menu = self.mm.MARCHANDISE_MASTER.query(f'ID == "{menu_id}"')
        self.sc.order_df = self.sc.order_df.append(menu)

        # オプション品の受付と追加
        if menu.iat[self.INDEX_0, self.OPTION_COL_NUM] != 0:
            self._show_option(menu.iat[self.INDEX_0, self.OPTION_COL_NUM])
            print("---------------------------------")
            option_id = input("オプション品のメニューIDを入力してください: ")

            # TODO menu_idの検証をここで行う
            option = self.mm.MARCHANDISE_MASTER.query(f'ID == "{option_id}"')
            self.sc.order_df = self.sc.order_df.append(option)

    def ask_yes_or_no(self, message):
        """
        ユーザーにyes/noの2択を問い合わせる。

        Args:
            message(str):ユーザー入力の際に表示する文字列
        Return:
            発券の場合=True, 発券しない場合=False
        """
        print("---------------------------------")
        is_ticketing = input(message)

        if is_ticketing == "yes":
            return True
        elif is_ticketing == "no":
            return False
        else:
            print("[Error]yes/noで入力してください")
            exit()

    def issue_ticket(self):
        """
        発券処理を行う

        Args:
            なし
        Return:
            なし
        """
        while self.sc.input_amount < (self.sc.total_amount - self.sc.discount_amount):
            self._show_current_status()
            self.get_input_amount()

        print("---------------------------------")
        print("発券します。ありがとうございました。")
        exit()

    def get_input_amount(self):
        """
        投入金額のユーザー入力を受け付ける

        Args:
            なし
        Return:
            なし
        """
        print("---------------------------------")
        amount = input("投入金額を入力してください: ")

        if amount.isdigit() == False:
            print("[Error]金額が不正です")
            exit()

        self.sc.input_amount += int(amount)
