import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Bank, Branch

# Create engine with proper SQLite settings
engine = create_engine('sqlite:///bank.db', connect_args={'timeout': 30})
Base.metadata.create_all(engine)

# Create session with proper settings
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

try:
    # Load the CSV file
    print("Loading CSV file...")
    df = pd.read_csv('bank_branches.csv')
    
    # Clean the data - replace NaN with None
    df = df.where(pd.notnull(df), None)
    
    # Create unique banks dataframe
    print("Processing bank data...")
    banks_df = df[['bank_id', 'bank_name']].drop_duplicates()
    banks_df = banks_df.rename(columns={'bank_name': 'name'})
    
    # Create branches dataframe
    print("Processing branch data...")
    branches_df = df[['ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank_id']]
    
    # Create a new session
    session = Session()
    
    # Insert banks
    print("Inserting banks...")
    for _, row in banks_df.iterrows():
        bank = Bank(
            id=row['bank_id'],
            name=row['name']
        )
        session.merge(bank)
    
    # Commit banks first
    session.commit()
    
    # Insert branches
    print("Inserting branches...")
    for _, row in branches_df.iterrows():
        branch = Branch(
            ifsc=row['ifsc'],
            branch=row['branch'],
            address=row['address'],
            city=row['city'],
            district=row['district'],
            state=row['state'],
            bank_id=row['bank_id']
        )
        session.merge(branch)
    
    # Final commit
    session.commit()
    print("Database seeded successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    if 'session' in locals():
        session.rollback()
    raise

finally:
    if 'session' in locals():
        session.close()
