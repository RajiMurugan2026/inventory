# Name: Sri Rajarajeshwari
# Assignment: Working with Files and JSON in Python

import json

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# ---------------- Task 1 ----------------
# Read inventory file
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total number of books:", len(inventory))


# ---------------- Task 2 ----------------
# Add new book
inventory.append(new_book)

# Save updated inventory
with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)


# ---------------- Task 3 ----------------
# Read updated file again
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

# Display books
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
