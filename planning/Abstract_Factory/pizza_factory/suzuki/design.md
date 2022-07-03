## メモ
新規種類のピザを作成したくなった場合、容易に設計変更をすることができる

## このプログラムについて
本プログラムは、全種類のピザのオブジェクトを作成し、
それぞれのピザの素材と分量を標準出力するものである。

## クラス図
```plantuml
@startuml

AbstractPizzaFactory <|-- FactoryA
AbstractPizzaFactory <|-- FactoryB

Dough <|-up- WheatDough
Dough <|-up- RiceDough

Sauce <|-up- TomatoSauce
Sauce <|-up- BasilSauce

Topping <|-up- CornTopping
Topping <|-up- CheeseTopping

WheatDough <.up. FactoryA
TomatoSauce <.up. FactoryA
CornTopping <.up. FactoryA

RiceDough <.up. FactoryB
BasilSauce <.up. FactoryB
CheeseTopping <.up. FactoryB


class AbstractPizzaFactory {
    + factory: factory
    + pizza_materials: list
    + make_pizza(amount_str : str) : void
    + check_pizza(void) : void
    + add_dough(void) : void
    + add_source(void) : void
    + add_add_topping(void) : void
}


class FactoryA {
    + add_dough(amount : int) : WheatDough
    + add_source(amount : int) : TomatoSauce
    + add_add_topping(amount int) : CornTopping
}

class FactoryB {
    + add_dough(amount : int) : RiceDough
    + add_source(amount : int) : BasilSauce
    + add_add_topping(amount int) : CheeseTopping
}

class Dough {
    + amount: int
}

class WheatDough {
    + check(amount: int) : void
}

class RiceDough {
    + check(amount: int) : void
}

class Sauce {
    + amount: int
}

class TomatoSauce {
    + check(amount: int) : void
}

class BasilSauce {
    + check(amount: int) : void
}

class Topping {
    + amount: int
}

class CornTopping {
    + check(amount: int) : void
}

class CheeseTopping {
    + check(amount: int) : void
}

note "各素材クラスのcheckメソッド：\nそれぞれの素材名と分量を示した文字列を標準出力する" as n1

@enduml
```

## シーケンス図
個別Dough：WheatDough、RiceDough
個別Sauce：TomatoSauce、BasilSauce
個別Topping：CornTopping、CheeseTopping
Factory：FactoryA, FactoryB
を示す。
```plantuml
@startuml
actor User
control Main

User -> Main : プログラム起動
activate Main

    create Factory
    Main -> Factory : Factory()

    create AbstractPizzaFactory
    Main -> AbstractPizzaFactory : AbstractPizzaFactory(Factory)

    Main -> AbstractPizzaFactory : make_pizza("high")
    activate AbstractPizzaFactory
        AbstractPizzaFactory -> AbstractPizzaFactory : amount(int)

        AbstractPizzaFactory -> Factory : add_dough(amount : int)
        activate Factory
        create 個別Dough
        activate 個別Dough
        Factory -> 個別Dough : 個別Dough()
        deactivate 個別Dough
        Factory --> AbstractPizzaFactory : 個別Dough
        deactivate Factory

        AbstractPizzaFactory -> Factory : add_source(amount : int)
        activate Factory
        create 個別Sauce
        Factory -> 個別Sauce : 個別Sauce()
        Factory --> AbstractPizzaFactory : 個別Sauce
        deactivate Factory

        AbstractPizzaFactory -> Factory : add_topping(amount : int)
        activate Factory
        create 個別Topping
        Factory -> 個別Topping : 個別Topping()
        Factory --> AbstractPizzaFactory : 個別Topping
        deactivate Factory

    AbstractPizzaFactory --> Main : None
    deactivate AbstractPizzaFactory

    Main -> AbstractPizzaFactory : check_pizza()
    activate AbstractPizzaFactory
        AbstractPizzaFactory -> 個別Dough  : check()
        activate 個別Dough
        個別Dough --> User : 素材名と分量の標準出力
        deactivate 個別Dough

        AbstractPizzaFactory -> 個別Sauce  : check()
        activate 個別Sauce
        個別Sauce --> User : 素材名と分量の標準出力
        deactivate 個別Sauce

        AbstractPizzaFactory -> 個別Topping  : check()
        activate 個別Topping
        個別Topping --> User : 素材名と分量の標準出力
        deactivate 個別Topping

    AbstractPizzaFactory --> Main : None
    deactivate AbstractPizzaFactory

Main --> User : プログラム終了
deactivate Main


@enduml
```