from .form import OrderForm
from .state import State
from .order import Order
from .event import Event

class Controller:
    def __init__(self):
        pass
    
    def run(self):
        """注文受け付けを実行
        """
        # 初期化
        state = State()
        order = Order()
        
        while True:
            # フォームの処理
            form = OrderForm()
            message = form.get_input_message(display=state.display)
            input_menu = form.input(message = message)

            # 状態をアップデート
            if input_menu == 'スキップ':
                state.skip_order()
            else:
                # 注文（イベント)をインスタンス化
                event = Event(
                    menu_type=state.menu_type,
                    menu_name=input_menu)
                
                # 注文リストを更新
                order.add_order(event=event)
                
                # 注文リストを元に状態を更新
                state.update(order=order)
            
            # 状態を出力
            output_dict = {
                "選択済み商品": order.order_menu_list,
                "直前のイベントコード：": order.last_event_code,
                "状態番号": state.state_num,
                "注文金額": order.order_price,
                "値引金額": state.discount_price,
                "発券可否": state.ticketing_available,
            }
            form.output(out_dict=output_dict)
    