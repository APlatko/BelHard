# Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс

# Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на таблицу Brand)).
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для бренда и машины.
# Создать пользовательский интерфейс


from sqlalchemy import create_engine, MetaData, Table, Integer, Column, String, Float
from sqlalchemy import delete, update, select, insert

meta = MetaData()

engine = create_engine('sqlite:///goods.sqlite', echo=True)
conn = engine.connect()

products = Table('products', meta,
                 Column('id', Integer, primary_key=True),
                 Column('title', String),
                 Column('price', Float),
                 Column('amount', Integer),
                 Column('comment', String)
                 )

meta.create_all(engine)


def Insert():
    ins = products.insert().values(
        title=input("Write product title: "),
        price=float(input("insert price: ")),
        amount=int(input("insert amount: ")),
        comment=input("Write a comment: "),
    )
    result = conn.execute(ins)


def View():
    conn = engine.connect()
    selectt = select([products])
    result = conn.execute(selectt)
    print(result.fetchall())


def Delete():
    id = int(input("Enter id to delete: "))
    delet = delete(products).where(
        products.c.id.like(id)
    )
    result = conn.execute(delet)


def Update():
    id = int(input("Enter product id to update: "))
    # title = input("Write product title"),
    # new_price = input("insert price"),
    # amount = int(input("insert amount")),
    # comment = input("Write a comment"),
    change = products.update().where(products.c.id.like(id)).values(title=input("Write product title: "),
                                                                    price=float(input("Insert price: ")),
                                                                    amount=int(input("Insert amount: ")),
                                                                    comment=input("Write a comment: "))
    result = conn.execute(change)


while True:
    print(
        " enter 1 for Insert\n",
        "enter 2 for Delete\n",
        "enter 3 for View\n",
        "enter 4 for Update\n",
        "enter 0 for Quit\n",
    )

    choice = int(input("Enter the choice: "))
    if choice == 0:
        break
    else:
        {1: Insert, 2: Delete, 3: View, 4: Update}.get(choice)()
