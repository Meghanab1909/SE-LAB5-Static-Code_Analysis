"""Inventory Management System

A simple Python module for managing an inventory of items.
Demonstrates secure coding, clean style, and static analysis compliance.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s"
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(
            "Invalid item or quantity type: item=%s (%s), qty=%s (%s)",
            item,
            type(item),
            qty,
            type(qty),
        )
        return logs

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %s of %s", qty, item)
    return logs


def remove_item(item, qty):
    """Remove a specific quantity of an item from the inventory."""
    try:
        if item not in stock_data:
            raise KeyError(f"{item} not found in stock data.")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %s of %s", qty, item)
    except KeyError as error:
        logging.error("Error removing item: %s", error)


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        logging.info("Inventory data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.warning("Inventory file not found. Starting with empty data.")
        return {}



def save_data(file="inventory.json"):
    """Persist the current inventory state to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Inventory data saved successfully.")


def print_data():
    """Display all items and their quantities in the inventory."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below a specified quantity threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program to demonstrate inventory functions."""
    logs = []
    logs = add_item("apple", 10, logs)
    logs = add_item("banana", 2, logs)
    logs = add_item(123, "ten", logs)  # Invalid input - safely handled
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    # Assign loaded data without using `global`
    loaded_data = load_data()
    stock_data.clear()
    stock_data.update(loaded_data)
    print_data()
    logging.info("Program execution completed successfully.")

if __name__ == "__main__":
    main()
