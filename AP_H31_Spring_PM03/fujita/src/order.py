from .event import Event

class Order:
    """注文リストを管理するクラス
        Attributes:
            order_list: 注文リスト。具体的にはEventクラスのリスト
    """
    def __init__(self):
        self.order_list = []

    def add_order(
        self,
        event: Event,
        ) -> None:
        """注文リストに注文(イベント)を追加する

        Args:
            even (int): イベント
            menu_name (str): 商品名称
        """
        pass

    def delete_order(self) -> None:
        """注文を削除する（仕様外）
        """
        pass
    
    @property
    def order_menu_list(self) -> list[dict]:
        """

        Returns:
            list[str]: 商品名のリスト
            list[dict]: 商品名のリスト
        """
        pass


    @property
    def order_price(self) -> int:
        """合計注文金額を計算

        Returns:
            int: order_price
        """
        pass
    
    @property
    def last_event_code(self) -> int:
        """最後に入力されたイベントコードを返却

        Returns:
            int: 最後のイベントコード
        """
        pass
    