import pprint

def main():
    main_menu = input("メインを入力: ")
    pprint.pprint({
        "選択済み商品：": [main_menu],
        "イベントコード：": "***",
        "状態番号": "***",
        "発券可否": "***",
        "合計金額": "***",
        "値引き有無": "***",
        })
    
    side_menu_1 = input("サイド1を入力:")
    pprint.pprint({
        "選択済み商品：": [main_menu, side_menu_1],
        "イベントコード：": "***",
        "状態番号": "***",
        "発券可否": "***",
        "合計金額": "***",
        "値引き有無": "***",
        })

    side_menu_2 = input("サイド2を入力: ")
    pprint.pprint({
        "選択済み商品：": [main_menu, side_menu_1, side_menu_2],
        "イベントコード：": "***",
        "状態番号": "***",
        "発券可否": "***",
        "合計金額": "***",
        "値引き有無": "***",
        })
    

if __name__ == "__main__":
    main()