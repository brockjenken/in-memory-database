from transaction_database import TransactionDatabase

'''This driver contains the sample code. Feel free to add and remove code to test'''


def main():
    my_db = TransactionDatabase()

    my_db.put("example", "foo")
    print(my_db.get("example"))  # returns "foo"
    my_db.delete("example")
    print(my_db.get("example"))  # returns null
    my_db.delete("example")

    my_db.create_transaction("abc")
    my_db.put("a", "foo", "abc")
    print(my_db.get("a", "abc"))  # returns "foo"
    print(my_db.get("a"))  # returns null

    my_db.create_transaction("xyz")
    my_db.put("a", "bar", "xyz")
    print(my_db.get("a", "xyz"))  # returns "bar"
    my_db.commit_transaction("xyz")
    print(my_db.get("a"))  # returns "bar"

    try:
        my_db.commit_transaction("abc")  # failure
    except Exception:
        print("FIRST FAILURE")

    print(my_db.get("a"))  # returns "bar"
    my_db.create_transaction("abc")
    my_db.put("a", "foo", "abc")
    print(my_db.get("a"))  # returns "bar"
    my_db.rollback_transaction("abc")
    try:
        my_db.put("a", "foo", "abc")  # failure
    except Exception:
        print("SECOND FAILURE")
    print(my_db.get("a"))  # returns "bar"

    my_db.create_transaction("def")
    my_db.put("b", "foo", "def")
    print(my_db.get("a", "def"))  # returns bar
    print(my_db.get("b", "def"))  # returns foo
    my_db.rollback_transaction("def")
    print(my_db.get("b"))  # returns None


if __name__ == "__main__":
    main()



