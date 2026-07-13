class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new connection...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

# Test Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
