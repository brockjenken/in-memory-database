# Simple Transaction Database
A simple in-memory transactional database. 

## Description
Operations can either be  performed immediately by operating 
get/put/delete commands or by creating transactions, staging 
operations and then committing.

### Transaction
A Transaction model is used to simplify the process of creating, 
accessing, and deleting transactions and their relevant data. Each
transaction object is comprised of an `id` and a `data` field. Each 
entry of the `data` field is comprised of a `key` and a dict containing
the `initial_value` of when the change was staged and the `new_value` the
transaction plans to commit.

If a value is changed in the global data after a change is staged in the 
transaction, the commit will fail and the ID will become available again.

If a commit succeeds, the transaction will remain in the database 
and its id will be registered so it can not be used in the future. 

Errors are also thrown if one attempts to access a Transaction that does not
exist.

## Usage
Run the provided driver file by executing:
```bash
python driver.py
```

The provided driver file can be modified for further testing.
