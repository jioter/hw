from typing import List
import psycopg2

from relational_database.config import DATABASE

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

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    # con = psycopg2.connect(**DATABASE)
    with con.cursor() as cursor:
        # insert_query = "INSERT INTO customers VALUES (92 , 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');"
        #insert_query = "INSERT INTO customers VALUES {}".format(
            # "(92 , 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore')")
        customer_name = "Thomas"
        contactname = "David"
        address = "Some Address"
        city = "London"
        postalcode = "774"
        country = "Singapore"
        insert_query = f"""
        INSERT INTO Customers(CustomerName,ContactName,Address,City,PostalCode,Country)
            VALUES (
            '{customer_name}', 
            '{contactname}',
            '{address}',
            '{city}',
            '{postalcode}',
            '{country}'
            )"""
        cursor.execute(insert_query)
    con.commit()



def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """

    insert_query = "SELECT * FROM Customers;"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    insert_query = "SELECT  * FROM Customers WHERE Country = 'Germany';"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    with con.cursor() as cursor:
        insert_query = "UPDATE Customers SET customername = 'Johnny Depp' WHERE CustomerID = 1;"
        cursor.execute(insert_query)
    con.commit()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cursor:
        insert_query = "DELETE FROM Customers WHERE CustomerID = (select max(CustomerID) from Customers);"
        cursor.execute(insert_query)
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    insert_query = "SELECT Country FROM suppliers;"
    cur.execute(insert_query)
    return cur.fetchmany()

def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    insert_query = "SELECT Country FROM Suppliers ORDER BY Country DESC;"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """

    insert_query = "SELECT  *  FROM Customers;"
    cur.execute(insert_query)
    return cur.fetchmany()

def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    insert_query = "SELECT City, COUNT(CustomerID) FROM Customers GROUP BY City HAVING COUNT(CustomerID) > 10;"
    cur.execute(insert_query)
    return cur.fetchmany()




def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    insert_query = "SELECT * FROM Customers ORDER BY CustomerID LIMIT 10;"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    insert_query = "SELECT * FROM Customers ORDER BY CustomerID LIMIT 0 OFFSET 10;"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    insert_query = "SELECT Supplierid,Suppliername,Contactname,City,Country FROM Suppliers WHERE Country = 'USA' OR Country = 'UK' OR Country = 'Japan';"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    insert_query = "SELECT Products.Productname FROM Products, Suppliers " \
                   "WHERE Country = 'Sweden' AND Products.SupplierID = Suppliers.SupplierID;"
    cur.execute(insert_query)
    return cur.fetchmany()

def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    insert_query = "SELECT Products.ProductID, Products.Productname, Products.Unit, Products.Price, Suppliers.Country, Suppliers.City, Suppliers.Suppliername  FROM Products, Suppliers WHERE Products.SupplierID = Suppliers.SupplierID;"
    cur.execute(insert_query)
    return cur.fetchmany()

def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    insert_query = "SELECT Customers.CustomerName, Customers.ContactName, Customers.Country, Orders.OrderID FROM Customers, Orders WHERE Customers.CustomerID = Orders.CustomerID ORDER BY OrderID ASC;"
    cur.execute(insert_query)
    return cur.fetchmany()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    insert_query = "SELECT Customers.CustomerName, Customers.Address, Customers.Country, Suppliers.Country,Suppliers.SupplierName FROM Customers, Suppliers WHERE Customers.Country = Suppliers.Country ORDER BY Suppliers.Country ASC;"
    cur.execute(insert_query)
    return cur.fetchmany()
