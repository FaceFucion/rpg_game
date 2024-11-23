import sqlite3

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
            quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
        )
    """)
    conn.commit()
    conn.close()

# Добавление 15 товаров
def add_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    products = [
        ("Товар 1", 150.0, 10),
        ("Товар 2", 80.0, 5),
        ("Товар 3", 20.0, 50),
        ("Товар 4", 500.0, 2),
        ("Товар 5", 120.0, 15),
        ("Товар 6", 90.0, 7),
        ("Товар 7", 300.0, 8),
        ("Товар 8", 75.0, 20),
        ("Товар 9", 60.0, 6),
        ("Товар 10", 45.0, 12),
        ("Товар 11", 200.0, 3),
        ("Товар 12", 10.0, 100),
        ("Товар 13", 30.0, 25),
        ("Товар 14", 400.0, 1),
        ("Товар 15", 5.0, 150),
    ]
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()

# Изменение количества товара по id
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

# Изменение цены товара по id
def update_price(product_id, new_price):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

# Удаление товара по id
def delete_product(product_id):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

# Вывод всех товаров
def get_all_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

# Поиск товаров дешевле лимита по цене и с количеством больше лимита
def find_products_by_price_and_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    """, (price_limit, quantity_limit))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

# Поиск товаров по названию
def search_products_by_name(search_term):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM products
        WHERE product_title LIKE ?
    """, ('%' + search_term + '%',))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

# Пример использования функций
if __name__ == "__main__":
    create_database()
    add_products()
    print("Все товары:")
    get_all_products()
    print("\nТовары дешевле 100 сом и с количеством больше 5:")
    find_products_by_price_and_quantity(100, 5)
    print("\nТовары с названием, содержащим 'мыло':")
    search_products_by_name("мыло")
    print("\nИзменение количества товара id=1:")
    update_quantity(1, 50)
    get_all_products()
    print("\nУдаление товара id=2:")
    delete_product(2)
    get_all_products()