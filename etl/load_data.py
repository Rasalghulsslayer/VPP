"""
Data Loading Module for VPP-1

Loads survey data from CSV into a PostgreSQL database table.
"""

import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection configuration (edit or use environment variables)
DATABASE_CONFIG = {
	'username': 'postgres',
	'password': 'voyage_presque_parfait',
	'host': 'localhost',
	'port': '5432',
	'database': 'vpp_db'
}

def get_connection_string():
	"""Build PostgreSQL connection string"""
	return f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"


def load_to_database(csv_path, table_name='survey_responses'):
	"""
	Load survey data into PostgreSQL database
	Args:
		csv_path (str): Path to CSV file
		table_name (str): Target table name in database
	"""
	print(f"💾 Loading data from {csv_path} to PostgreSQL table '{table_name}'...")
	connection_string = get_connection_string()
	try:
		engine = create_engine(connection_string)
		df = pd.read_csv(csv_path)
		if df.empty:
			print("⚠️  No data to load!")
			return
		# Load data to database (replace table)
		df.to_sql(table_name, engine, if_exists='replace', index=False)
		print(f"✅ Loaded {len(df)} rows to table '{table_name}'")
	except Exception as e:
		print(f"❌ Error loading data: {e}")
		print("💡 Check your PostgreSQL server, credentials, and that the database exists.")

def test_database_connection():
	"""
	Test database connection without loading data
	"""
	print("🔌 Testing database connection...")
	connection_string = get_connection_string()
	try:
		engine = create_engine(connection_string)
		result = pd.read_sql("SELECT 1 as test", engine)
		if result.iloc[0]['test'] == 1:
			print("✅ Database connection successful!")
			return True
		else:
			print("❌ Database connection test failed")
			return False
	except Exception as e:
		print(f"❌ Database connection failed: {e}")
		return False

if __name__ == "__main__":
	# Print the connection string for verification
	conn_str = get_connection_string()
	print("Connection string:", conn_str)
	# Test direct SQLAlchemy connection
	try:
		engine = create_engine(conn_str)
		with engine.connect() as conn:
			print("✅ Direct SQLAlchemy connection successful!")
	except Exception as e:
		print("❌ Direct SQLAlchemy connection failed:", e)

	if test_database_connection():
		# Load user profiles
		load_to_database("data/users_profiles.csv", table_name="users_profiles")
		# Load user travels
		load_to_database("data/users_travels.csv", table_name="users_travels")
	else:
		print("Fix database connection before loading data.")

