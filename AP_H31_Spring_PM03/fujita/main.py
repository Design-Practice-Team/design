import pprint

def main():
    main_menu = input("メインを入力: ")
    pprint.pprint({
        "選択済み商品：": [main_menu],
        "直前のイベントコード：": "***",
        "状態番号": "***",
        "注文金額": "***",
        "値引金額": "***",
        "発券可否": "***",
        })
    
    side_menu_1 = input("サイド1を入力:")
    pprint.pprint({
        "選択済み商品：": [main_menu, side_menu_1],
        "直前のイベントコード：": "***",
        "状態番号": "***",
        "注文金額": "***",
        "値引金額": "***",
        "発券可否": "***",
        })

    side_menu_2 = input("サイド2を入力: ")
    pprint.pprint({
        "選択済み商品：": [main_menu, side_menu_1, side_menu_2],
        "直前のイベントコード：": "***",
        "状態番号": "***",
        "注文金額": "***",
        "値引金額": "***",
        "発券可否": "***",
        })
    

if __name__ == "__main__":
    main()