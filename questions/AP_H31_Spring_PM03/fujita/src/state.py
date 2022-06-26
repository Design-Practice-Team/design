from .order import Order

class State:
    """状態を管理するクラス
        Attributes:
            state_num: 状態番号
            menu_type: メニュー種別
                ≒入力待ちの画面種別
                main→(option)→side1→(option)→side2→(option)の順で推移

    """
    def __init__(self):
        self.state_num = 0
        self.menu_type = 'main'
    
    def update(self, order: Order) -> None:
        """状態をアップデートする

        Args:
            order (Order): 注文クラスのインスタンス
        """
        self._update_state(order_list=order.order_list)
        self._update_menu_type(order_list=order.order_list)
    
    def skip_order(self) -> None:
        """オーダーをスキップしてメニュー種別を変更する
        """
        self.menu_type = 'side1'
    
    def _update_state(self, order_list) -> None:
        """オーダーリストを元に、状態をアップデートする
        """
        # order_listと状態遷移表.csvを利用
        self.state_num = 1
        
    def _update_menu_type(self, order_list) -> None:
        """メニュー種別をアップデートする
        """
        # order_listを元に判定
        self.menu_type = 'side1'
    
    @property
    def ticketing_available(self) -> bool:
        """発券可否を判定

        Returns:
            bool: 発券可=True, 発券不可=False
        """
        pass
    
    @property
    def discount_price(self):
        pass
    
    @property
    def transitionable_event(self):
        pass
    