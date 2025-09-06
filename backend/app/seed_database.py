# backend/seed_db.py
from app.db.database import SessionLocal, engine, Base
from app.models.category import Category
from app.models.product import Product
from app.models.user import User # Import user to ensure all tables are known

def seed_database():
    # This makes sure all tables are created
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Check if categories already exist
        if db.query(Category).count() == 0:
            print("Seeding categories...")
            cat1 = Category(name="Sustainable Kitchen")
            cat2 = Category(name="Eco-Friendly Office")
            cat3 = Category(name="Outdoor & Adventure")
            db.add_all([cat1, cat2, cat3])
            db.commit()
            print("Categories seeded.")
        else:
            print("Categories already exist.")

        # Check if products already exist
        if db.query(Product).count() == 0:
            print("Seeding products...")
            # Re-fetch categories to get their IDs
            cat1 = db.query(Category).filter_by(name="Sustainable Kitchen").one()
            cat2 = db.query(Category).filter_by(name="Eco-Friendly Office").one()
            cat3 = db.query(Category).filter_by(name="Outdoor & Adventure").one()

            prod1 = Product(name="Bamboo Cutting Board", description="A durable and eco-friendly cutting board.", price=25.50, category_id=cat1.id)
            prod2 = Product(name="Reusable Silicone Food Bags", description="Set of 4, perfect for snacks and sandwiches.", price=19.99, category_id=cat1.id)
            prod3 = Product(name="Recycled Paper Notebook", description="100-page notebook made from 100% recycled paper.", price=9.75, category_id=cat2.id)
            prod4 = Product(name="Solar-Powered Charger", description="Portable charger for your devices, powered by the sun.", price=45.00, category_id=cat3.id)
            prod5 = Product(name="Stainless Steel Water Bottle", description="Keeps drinks cold for 24 hours.", price=22.00, category_id=cat3.id)

            db.add_all([prod1, prod2, prod3, prod4, prod5])
            db.commit()
            print("Products seeded.")
        else:
            print("Products already exist.")

    finally:
        db.close()

if __name__ == "__main__":
    print("Starting database seeding process...")
    seed_database()
    print("Seeding process finished.")