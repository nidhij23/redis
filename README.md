# Redis Store
Redis store is a redis like key-value store in Python
To run the redis store run the following command from the root directoy:
```
python server.py
```
## Commands:
1. GET <key> - retrieves a value for a given key
2. SET <key> <value> - associates a key with a value and stores it in memory
3. UNSET <key>
4. NUMEQUALTO <value> - Returns the number of keys that are associated with the given value
5. END - exits the program
6. BEGIN - begins a transaction (no parameters)
7. COMMIT - commits the transaction
8. ROLLBACK - rolls back the transaction

## Run Unit Tests:
This uses python's unittest framework

To run unit tests from the root directory run the below command:
```
python3 -m unittest -v test_commandController.py
```

