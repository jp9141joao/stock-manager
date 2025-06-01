# 🛒 **Stock Manager** 📦

An interactive system for managing a product inventory. With this, you can add, remove, view, and modify products in the inventory through a simple and intuitive terminal menu.

---

## 🚀 **Project Overview**

The program is a **Stock Manager**, built in Python, which allows the user to manage a list of products with their quantities and attributes (price, quantity, name, etc.) in a simple and interactive way.

This project provides full functionality to:

* **Add products to the inventory**
* **Remove products from the inventory**
* **Modify specific attributes of a product**
* **View active inventory**
* **Manage inventory entries in an intuitive way**

---

## 🛠️ **Key Features**

### Implemented Functionalities:

1. **Add Product to Inventory**: Inserts products into the inventory with quantity and price.
2. **Remove Products from Inventory**: Removes a specific product from the inventory by code.
3. **Modify Attributes of a Product**: Changes attributes such as name, quantity, or price.
4. **View Active Inventory**: Lists all products in the inventory with their information.
5. **Management with Automatically Generated Codes**: Prevents duplicates when adding products.
6. **Input Validation**: The system automatically checks for invalid entries.
7. **Intuitive Menu with Clear Options** for program navigation.

---

## 💾 **Setup**

### Prerequisites

* Python 3.x must be installed on your system.
* The environment must allow execution of Python scripts.

---

## ▶️ **How to Run**

1. Clone this repository to your local environment:

   ```bash
   git clone https://github.com/your-username/gerenciador-estoque.git
   ```

2. Navigate to the project folder:

   ```bash
   cd gerenciador-estoque
   ```

3. Run the code in the terminal with:

   ```bash
   python your_file.py
   ```

---

## 📚 **Menu Functionalities**

After starting the program, you will see the following menu in the terminal:

```
* Stock Manager *
-------------------------------------------
1- Add Product to Inventory
2- Remove Products from Inventory
3- Change Item Attributes
4- Exit
```

### Options:

1. **Add Product to Inventory**

   * Inserts a product into the inventory with its name, quantity, and an optional price.

2. **Remove Products from Inventory**

   * Removes a product from the inventory using its automatically generated unique code.

3. **Change Item Attributes**

   * Modifies specific attributes of a product:

     * Name
     * Price
     * Quantity

4. **Exit**

   * Closes the program.

---

## ⚙️ **Technologies Used**

* **Python 3.x**: Main programming language.
* **`os` Library**: To clear the console screen.
* **List Management with Dictionaries**: Central data structure.

---

## 🎮 **Sample Workflow**

1. The program displays the main menu.
2. The user chooses **Add Product to Inventory**.
3. The system prompts for information such as:

   * Product name
   * Available quantity
   * Price (optional)
4. The product is added to the inventory with an automatically generated code.
5. The user can view the list of products in the inventory.

---

Now you have a functional Stock Manager ready to use! 🚀 Good luck with your management! 🛒✨
