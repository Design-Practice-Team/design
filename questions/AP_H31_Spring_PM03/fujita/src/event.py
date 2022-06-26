
class Event:
    """イベント（≒注文）を定義するクラス
        Attributes:
            menu_type: メニュー種別
            menu_name: メニュー名
            event_code: イベントコード
    """
    def __init__(
        self,
        menu_type,
        menu_name,
    ):
        self.menu_type = menu_type
        self.menu_name = menu_name
        self.event_code = self.get_event_code(
                menu_type=self.menu_type,
                menu_name=self.menu_name,
        )


    @staticmethod
    def get_event_code(menu_type: str, menu_name: str) -> str:
        """メニュー種別とメニュー名から、商品マスタを元にイベントコードを取得する

        Args:
            menu_type (str): メニュー種別
            menu_name (str): メニュー名

        Returns:
            str: イベントコード
        """
        # 商品マスタ.csvを利用
        pass

    
    @property
    def type_name(self) -> str:
        """分類名を商品マスタから取得

        Returns:
            str: 分類名
        """
        # 商品マスタ.csvを利用
        pass
    
    @property
    def price(self) -> int:
        """商品の金額を商品マスタから取得

        Returns:
            int: 金額
        """
        # 商品マスタ.csvを利用
        pass
    

