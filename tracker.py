import uuid
from datetime import date
from db import get_connect
import psycopg2.extras

def add_item():
    name = input("Enter the item name: ")
    price = float(input("Enter price: "))
    category = input("Enter category of the item: ")

    # accept empty input if user dont know brand and type
    item_type = input("Enter type of the item [optional]: ").strip()
    brand = input("Enter brand [optional]: ").strip()
    
    item_id = uuid.uuid4()

    conn = get_connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO items (id, name, price, category, item_type, brand, date)
        VALUES(%s, %s, %s, %s, %s, %s, %s)
""", (str(item_id), name, price, category, item_type, brand, date.today()))
    
    conn.commit()
    cur.close()
    conn.close()

    print(f"✅ Item added with ID: {item_id}")


def add_note():
    item_id = input("Enter the id: ")
    note = input("Enter note: ")

    conn = get_connect()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM items WHERE id = %s", (item_id,))
    if cur.fetchone(): # to check whether item was found on the DB
        cur.execute("INSERT INTO notes (item_id, content) VALUES(%s, %s)", (item_id, note))

        conn.commit()
        print("Note added successfully.")
    else:
        print("Item not found.")

    cur.close()
    conn.close()


def view_report():
    name = input("Search by name: ").strip()
    category = input("Filter by category(optional): ")

    conn = get_connect()
    # makes every row a dictionary-like object
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    
    query = "SELECT * FROM items WHERE TRUE"
    store = []

    if category:
        query += " AND category = %s"
        store.append(category)

    if name:
        query += " AND LOWER(name) LIKE %s"
        store.append(f"%{name.lower()}%")

    cur.execute(query, store)
    rows = cur.fetchall()

    # calculate total money spent on the item
    total = sum(float(row['price']) for row in rows)
     
    print("\nPrice Tracker Report:")
    category_total = {}
    for row in rows:
        print(f"Item: {row['name']}, Price: ${row['price']:}, "
              f"Category: {row['category']}, Date: {row['date']}, Brand: {row['brand']}")
    cat = row['category']
    category_total[cat] = category_total.get(cat, 0) + float(row['price'])

    print(f"\nTotal Items: {len(rows)}")
    print(f"Total Spent: {total}")

    print("Category Breakdown:")
    for cat, val in category_total.items():
        print(f"{cat}: ${val:.2f}")

    cur.close()
    conn.close()

def view_notes():
    item_id = input("Enter item ID: ")

    conn = get_connect()
    cur = conn.cursor()
    cur.execute("SELECT content FROM notes WHERE item_id = %s", (item_id,))
    notes = cur.fetchall()

    if notes:
        print("Notes:")
        for note in notes:
            print(f"- {note[0]}")
    else:
        print("No notes found or item does not exist.")
    cur.close()
    conn.close()


    