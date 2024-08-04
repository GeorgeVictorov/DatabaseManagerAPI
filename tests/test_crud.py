import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, ParserConfig
from src.crud import create_resource, get_resources, delete_resource

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class TestCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)
        if os.path.exists('test.db'):
            os.remove('test.db')

    def setUp(self):
        self.db = TestingSessionLocal()

    def tearDown(self):
        self.db.close()

    def test_create_resource(self):
        new_resource = ParserConfig(name="Test Resource", url="https://example.com", destination="test")
        created_resource = create_resource(self.db, new_resource)
        self.assertEqual(created_resource.name, new_resource.name)

    def test_get_resources(self):
        new_resource = ParserConfig(name="Test Resource1", url="https://example1.com", destination="test")
        created_resource = create_resource(self.db, new_resource)
        resources = get_resources(self.db)
        self.assertEqual(len(resources), 2)

    def test_delete_resource(self):
        resource = ParserConfig(name="Test Resource2", url="https://example2.com", destination="test")
        self.db.add(resource)
        self.db.commit()
        self.db.refresh(resource)
        deleted_resource = delete_resource(self.db, resource.resource_id)
        self.assertEqual(deleted_resource.name, resource.name)
