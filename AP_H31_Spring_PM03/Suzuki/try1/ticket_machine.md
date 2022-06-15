## 応用情報技術者過去問題 平成31年春期 午後問3

### 目次
1. [メモ](#memo)
2. [アクティビティ図](#activity)
3. [クラス図](#class)
4. [シーケンス図（全体）](#sequence-whole)
5. [シーケンス図（メインメニュー）](#sequence-menu)
6. [シーケンス図（発券処理）](#sequence-ticketing)

<a id="memo"></a>

### メモ
- イベントコードと状態番号のコンソール出力は行わない（ユーザーにとって不要な情報であるため）
- エラークラスの設計と実装はTBD
- 発券可能条件
    - メイン商品が一つ選択されていること
    - オプション商品が選択されていること

<a id="activity"></a>

### アクティビティ図
#### システム全体のフロー
```plantuml
@startuml
start
:メインメニューの選択;

if (発券) then (しない)

    while (サイド1を購入する)
        :サイドメニュー1を選択;
    endwhile

    if (発券) then (しない)
        while (サイド2を購入する)
            :サイドメニュー2を選択;
        endwhile
        :発券処理;
        stop
    else (する)
        :発券処理;
        stop
    endif

else (する)
    :発券処理;
    stop
endif
@enduml
```

#### 発券処理のフロー
```plantuml
@startuml
start
    repeat
        :お金を投入;
    repeat while (投入金額=合計金額)
    :発券メッセージ;
stop
@enduml
```

<a id="class"></a>

### クラス図
```plantuml
@startuml
TicketingMachine o-- ShoppingCart
TicketingMachine o-- MarchandiseMaster
MarchandiseMaster <.. ShoppingCart

class TicketingMachine {
    shopping_cart : ShoppingCart
    marchandise_master : MarchandiseMaster
    ask_yes_or_no()
    get_order()
    _get_menu()
    _show_menu()
    _show_option()
    _show_current_status()
    issue_ticket()
    get_input_amount()
}

note left of TicketingMachine::marchandise_master
    商品マスタのデータフレーム。csvで作成する。
    ・商品カテゴリ
    ・商品名
    ・セットメニュー適用可否フラグ
    ・オプション番号
    ・価格
end note

note left of TicketingMachine::ask_yes_or_no()
    ユーザーにyesかnoかを問い合わせる。
    その結果をboolで返す
end note 

note left of TicketingMachine::_show_current_status()
    現在の注文一覧、
    合計金額、割引金額
    を表示する。
end note

note left of TicketingMachine::ask_yes_or_no()
    ユーザーに発券要否を問い合わせる。
    その結果をboolで返す
end note

note left of TicketingMachine::issue_ticket
    発券処理をする。
    1.ユーザーに発券の要否を確認
    2.発券する場合は、お金の投入を促す
    3.発券し、システム終了
end note

class ShoppingCart {
    order_list : list
    total_amount : int
    input_amount : int
    discount_amount : int
    calculate_total_amount()
    calculate_set_discount()
}

note left of ShoppingCart::order_list
    商品名とその金額の二次元配列
end note

note left of ShoppingCart::ask_yes_or_no()
    発券可能な状態か判定する。発券可能となる条件は下記。
    ・order_listを参照し、メインメニューが1つ選択されている
    ・投入金額 > 合計商品 となる場合
end note

class MarchandiseMaster {
    menu : Dataframe
}

@enduml
```
<a id="sequence-whole"></a>

### シーケンス図（全体）

```plantuml
@startuml
actor User
control Main
participant TicketingMachine
participant ShoppingCart
participant MarchandiseMaster

User -> Main : Execute source
activate Main

Main -> MarchandiseMaster
activate MarchandiseMaster
MarchandiseMaster --> Main : marchandise_master(MarchandiseMaster)
deactivate MarchandiseMaster

Main -> ShoppingCart
activate ShoppingCart
ShoppingCart --> Main : shopping_cart(ShoppingCart)
deactivate ShoppingCart

Main -> TicketingMachine : marchandise_master(MarchandiseMaster)\nshopping_cart(ShoppingCart)
activate TicketingMachine
TicketingMachine --> Main : ticketing_machine(TicketingMachine)
deactivate TicketingMachine


' メインメニューの選択
ref over User, Main, TicketingMachine, ShoppingCart
    各メニュー受付（メインメニュー）
end ref

Main -> TicketingMachine : ask_yes_or_no()
activate TicketingMachine
TicketingMachine -> User : 発券要否の確認
User --> TicketingMachine : 発券指示（yes/no）（str）
deactivate TicketingMachine

opt ask_yes_or_no() = True
    ref over User, Main, TicketingMachine, ShoppingCart
        発券処理
    end ref
end 

' サイドメニュー1の選択
loop ask_yes_or_no() = True
    Main -> TicketingMachine : ask_yes_or_no()
    activate TicketingMachine
    TicketingMachine -> User : 注文の要否を確認
    User --> TicketingMachine : 注文指示（yes/no）（str）
    deactivate TicketingMachine
    ref over User, Main, TicketingMachine, ShoppingCart
        各メニュー受付（サイドメニュー1）
    end ref
end 


Main -> TicketingMachine : ask_yes_or_no()
activate TicketingMachine
TicketingMachine -> User : 発券要否の確認
User --> TicketingMachine : 発券指示（yes/no）（str）
deactivate TicketingMachine

opt ask_yes_or_no() = True
    ref over User, Main, TicketingMachine, ShoppingCart
        発券処理
    end ref
end

' サイドメニュー2の選択
loop ask_yes_or_no() = True
    Main -> TicketingMachine : ask_yes_or_no()
    activate TicketingMachine
    TicketingMachine -> User : 注文の要否を確認
    User --> TicketingMachine : 注文指示（yes/no）（str）
    deactivate TicketingMachine
    ref over User, Main, TicketingMachine, ShoppingCart
        各メニュー受付（サイドメニュー2）
    end ref
end 

ref over User, Main, TicketingMachine, ShoppingCart
    発券処理
end ref

@enduml
```
<a id="sequence-menu"></a>

### シーケンス図（各メニュー受付）
```plantuml
@startuml
actor User
control Main
participant TicketingMachine
participant ShoppingCart

activate Main

Main -> TicketingMachine : get_order(category(1~3))
activate TicketingMachine
    TicketingMachine -> TicketingMachine : _show_menu(category(1~3))
    activate TicketingMachine
    TicketingMachine -> User : メインメニュー一覧を表示
    deactivate TicketingMachine

    TicketingMachine -> TicketingMachine : _get_menu(category(1~3))
    activate TicketingMachine
    TicketingMachine -> User : メニュー選択指示
    User --> TicketingMachine : menu_id（str）

    opt オプション有り
        TicketingMachine -> TicketingMachine : _show_option(option番号)
        activate TicketingMachine
        TicketingMachine -> User : オプションメニュー一覧を表示
        deactivate TicketingMachine

        TicketingMachine -> TicketingMachine : _get_menu("4")
        activate TicketingMachine
        TicketingMachine -> User : メニュー選択指示
        User --> TicketingMachine : option_id (str)
        deactivate TicketingMachine
    end
    deactivate TicketingMachine

    TicketingMachine -> ShoppingCart : calculate_total_amount()
    TicketingMachine -> ShoppingCart : calculate_set_discount()

    TicketingMachine -> TicketingMachine : _show_current_status()
    activate TicketingMachine
    TicketingMachine -> User : 現在の注文と金額情報を表示
    deactivate TicketingMachine

    deactivate TicketingMachine

deactivate Main

@enduml
```

<a id="sequence-ticketing"></a>

### シーケンス図（発券処理）
```plantuml
@startuml
actor User
control Main
participant TicketingMachine

Main -> TicketingMachine : issue_ticket()
activate TicketingMachine
loop 投入金額合計 >= 合計金額
    TicketingMachine -> TicketingMachine : _show_current_status()
    activate TicketingMachine
    TicketingMachine -> User : 現在の注文と金額情報を表示
    deactivate TicketingMachine
    
    TicketingMachine -> TicketingMachine : get_input_amount()
    activate TicketingMachine
    TicketingMachine -> User : 金額の投入指示
    User --> TicketingMachine : 投入金額（int）
    deactivate TicketingMachine
end
TicketingMachine -> User : 発券メッセージ（システム終了）
deactivate TicketingMachine


@enduml
```