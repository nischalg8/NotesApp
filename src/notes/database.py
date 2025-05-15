from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from notes.config import get_settings
from notes.logger import logger  


settings = get_settings()


engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def test_connection():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(lambda conn: None)
        logger.info("Database connected successfully!")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")

# Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session