import pprint

def main():
    main_menu = input("メインを入力: ")
    pprint.pprint({
        "選択済み商品：": [{"type": "main", "name": main_menu, "option": "***"}],
        "直前のイベントコード：": "***",
        "状態番号": "***",
        "注文金額": "***",
        "値引金額": "***",
        "発券可否": "***",
        })
    
    side_menu_1 = input("サイド1を入力:")
    pprint.pprint({
        "選択済み商品：": [
            {"type": "main", "name": main_menu, "option": "***"},
            {"type": "side_1", "name": side_menu_1, "option": "***"},
            ],
        "直前のイベントコード：": "***",
        "状態番号": "***",
        "注文金額": "***",
        "値引金額": "***",
        "発券可否": "***",
        })

    side_menu_2 = input("サイド2を入力: ")
    pprint.pprint({
        "選択済み商品：": [
            {"type": "main", "name": main_menu, "option": "***"},
            {"type": "side_1", "name": side_menu_1, "option": "***"},
            {"type": "side_2", "name": side_menu_2, "option": "***"},
            ],
        "直前のイベントコード：": "***",
        "状態番号": "***",
        "注文金額": "***",
        "値引金額": "***",
        "発券可否": "***",
        })
    

if __name__ == "__main__":
    main()