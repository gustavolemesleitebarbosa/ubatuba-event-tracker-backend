from app.database import engine, Base
from app.models import Event
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_db():
    # Verify environment variables are loaded
    required_vars = [
        'SUPABASE_DB_USER',
        'SUPABASE_DB_PASSWORD',
        'SUPABASE_DB_HOST',
        'SUPABASE_DB_NAME'
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db() 