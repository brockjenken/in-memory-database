"""
Python does not support overloading, so overloading has been implemented by using *args. If a transaction_id is
provided as a third arg, it will call the transaction-relevant method, denoted by being preceded by an underscore.

The database is split into three main collections:
    data: stores the committed data
    transaction: stores the transactions
    invalid_ids: stores all invalidated ids

All of the time complexities of the get/put/delete methods are on the scale of O(c) / O(1). Many built-in
functions are used, and all report O(1) on average. Lists have been avoided to improve performance. The amoritzed
worst-case values are arguably too pessimistic, and as such average values were used. These reported values can be
found here:

https://wiki.python.org/moin/TimeComplexity

To simplify the creation of transactions the Transaction Model is used. The time complexities of creating the models
and parsing them to dicts are on the scale of O(1), as it is directly proportional to the number of fields in the model 
(2 in this case).
"""

from .transaction_model import TransactionModel as Transaction

'''Constants'''
KEY = "key"
INITIAL_VALUE = "initial_value"
NEW_VALUE = "new_value"


class TransactionDatabase:
    def __init__(self):
        self.data = {}
        self.transactions = {}
        self.invalid_ids = set()

    '''General functions'''
    def get(self, key: str, *args) -> str:
        if len(args) > 0:
            return self._get(key, args[0])

        return self.data.get(key)

    def _get(self, key: str, transaction_id: str) -> str:
        self.check_valid_transaction(transaction_id)

        transaction = Transaction(**self.transactions[transaction_id])
        return transaction.get_value(key)

    def put(self, key: str, value: str, *args):
        if len(args) > 0:
            return self._put(key, value, args[0])

        self.data[key] = value

    def _put(self, key: str, value: str, transaction_id: str):
        self.check_valid_transaction(transaction_id)

        transaction = Transaction(**self.transactions[transaction_id])
        transaction.set_value(key, value)

        self.transactions[transaction_id] = transaction.dict()

    def delete(self, key: str, *args):
        if len(args) > 0:
            return self._delete(key, args[0])

        self.data.pop(key, None)

    def _delete(self, key: str, transaction_id: str):
        self.check_valid_transaction(transaction_id)

        transaction = Transaction(**self.transactions[transaction_id])
        transaction.delete_value(key)

        self.transactions[transaction_id] = transaction

    '''Transaction functions'''
    def create_transaction(self, transaction_id: str):
        self.check_valid_transaction(transaction_id, detect_absent=False)

        transaction = Transaction(id=transaction_id)
        transaction.initialize_data(self.data)
        self.transactions[transaction_id] = transaction.dict()

    def rollback_transaction(self, transaction_id: str):
        self.check_valid_transaction(transaction_id)
        self.transactions.pop(transaction_id)

    def commit_transaction(self, transaction_id: str):
        self.check_valid_transaction(transaction_id)

        transaction = Transaction(**self.transactions[transaction_id])

        for k, values in transaction.get_data().items():
            if self.data.get(k) != values[INITIAL_VALUE]:
                self.rollback_transaction(transaction_id)
                raise ValueError("The data has been modified since the beginning of the transaction")

        for k, values in transaction.get_data().items():
            self.data[k] = values[NEW_VALUE]

        self.invalid_ids.add(transaction_id)

    '''Helper methods'''
    def check_valid_transaction(self, transaction_id: str, detect_absent: bool = True):
        if detect_absent and transaction_id not in self.transactions:
            raise KeyError("Transaction does not exist.")
        elif not detect_absent and transaction_id in self.transactions:
            raise KeyError("Transaction already exists.")

        if transaction_id in self.invalid_ids:
            raise KeyError("This transaction ID has already been committed.")
