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


# m = MarchandideMaster()
# pd.set_option("display.unicode.east_asian_width", True)
# code = "001"
# # val1 = m.MARCHANDISE_MASTER.query(f'ID == "001"')[["Name", "Price"]].to_dict(
# #     orient="index"
# # )[0]

# # print(val1["Name"])
# # l = []
# # l.append([val1["Name"], val1["Price"]])
# # print(l)

# val1 = m.MARCHANDISE_MASTER.query(f'ID == "001"')[["Name", "Category", "Price"]]

# print(type(val1))
# print(val1)

# user_input = "apple"
# if user_input not in ["yes", "no"]:
#     print("[Error]金額が不正です")
test_df1 = pd.DataFrame(columns=[], data=[])
test_df2 = pd.DataFrame(
    columns=["ID", "Category", "Name", "Set", "Option", "Price"],
    data=[["001", "1", "牛丼", True, 1, 380]],
)
print("-test_df1-")
print(test_df1)
print("-test_df2-")
print(test_df2)
print("-union-")
pdf = test_df2.append(test_df1)
print(pdf["Category"])
print("---")
val = pdf.at[0, "Category"]
print(val)
print(type(val))
