
from data_baze.requests_test import create_all_tables

def start_db():
    try:
        create_all_tables()
        print("Database and tables created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")
if __name__ == "__main__":
    start_db()
    print("Database initialization complete.")