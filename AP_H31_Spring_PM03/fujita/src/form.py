import pprint
from .state import State


class OrderForm:
    """注文を取得するフォームを管理する
    """
    def __init__(self, state : State) -> None:
        self.state = state
    
    def input(self, message: str) -> str:
        """フォームの入力をvalidatして返す

        Args:
            message (str): 画面に表示するメッセージ
                ex: 'メインメニューを選んでください'

        Returns:
            str: 入力値
        """
        while True:
            text = input(message)
            is_valid = self.validate_input(text, menu_type = self.state.menu_type)
            if is_valid:
                break
        return text
    
    def output(self, out_dict: dict) -> None:
        """画面に標準出力

        Args:
            out_dict (dict): _description_
        """
        pprint.pprint(out_dict)

    def validate_input(self, text: str) -> bool:
        """入力した値が問題ないかチェック

        Args:
            message (str): 入力内容
        """
        if len(text) > 2:
            return True
        else:
            return False
    
    def get_input_message(self, display: str) -> str:
        """画面状態を元に、入力時のメッセージを取得する

        Args:
            display (str): 画面状態（main, side1, side2, option）

        Returns:
            str: メッセージ
        """
        # 画面マスタを参照してメッセージを取得する
        
        pass
