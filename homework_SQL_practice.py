from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }
    """
    cur = con.cursor()
    cur.execute("INSERT INTO customers (customerid, customername, contactname, address, city, postalcode, country)"
                " VALUES ('92', 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore')")
    con.commit()



def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM Customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    query = "SELECT * FROM Customers WHERE country = 'Germany';"
    cur.execute(query)
    return cur.fetchall()



def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    cur = con.cursor()
    query = "UPDATE Customers SET CustomerName = 'Johnny Depp' WHERE CustomerID = 1;"
    cur.execute(query)
    return con.commit()



def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    cur = con.cursor()
    query = "DELETE FROM Customers WHERE CustomerID = (SELECT COUNT(CustomerID) FROM Customers);"
    cur.execute(query)
    return con.commit()

def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    query = "SELECT Country FROM Suppliers;"
    cur.execute(query)
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    query = "SELECT Country FROM Suppliers ORDER BY Country DESC;"
    cur.execute(query)
    return cur.fetchall()

def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """

    query = ("SELECT City, Count(CustomerName)"
            "FROM Customers GROUP BY City;")
    cur.execute(query)
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    query = "SELECT City, Count(CustomerName) FROM Customers GROUP BY City HAVING Count(CustomerName)>10;"
    cur.execute(query)
    return cur.fetchall()

def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    query = "SELECT * FROM Customers WHERE CustomerID < 11;"
    cur.execute(query)
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    query = "SELECT * FROM Customers WHERE CustomerID > 11;"
    cur.execute(query)
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    query = "SELECT SupplierID, SupplierName, ContactName, City, Country" \
            " FROM Suppliers WHERE Country = 'USA' OR Country = 'UK' OR Country = 'Japan';"
    cur.execute(query)
    return cur.fetchall()

def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    query = "SELECT Products.ProductName FROM Products, Suppliers WHERE Suppliers.Country = 'Sweden' AND Suppliers.SupplierID=Products.SupplierID;"
    cur.execute(query)
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    query = "SELECT Products.ProductID, Products.ProductName, Products.Unit, Products.Price, Suppliers.Country, Suppliers.City, Suppliers.SupplierName FROM Suppliers, Products WHERE Products.SupplierID=Suppliers.SupplierID;"
    cur.execute(query)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    query = "SELECT Customers.CustomerName, Customers.ContactName, Customers.Country, Orders.OrderID FROM Customers, Orders WHERE Customers.CustomerID=Orders.CustomerID ORDER BY Orders.OrderID ASC;"
    cur.execute(query)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    query = "SELECT Customers.CustomerName AS customername, Customers.address , Customers.Country AS customercountry, Suppliers.Country AS suppliercountry,Suppliers.SupplierName AS suppliername FROM Customers LEFT JOIN Suppliers ON Customers.Country = Suppliers.Country ORDER BY Customers.Country ASC, Customers.CustomerName ASC;"
    cur.execute(query)
    return cur.fetchall()
