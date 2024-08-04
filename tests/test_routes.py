from fastapi.testclient import TestClient

from src.main import app
from src.config import load_config

client = TestClient(app)
config = load_config()

token_name = config.api_token.api_key_name
token = config.api_token.api_key


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == 'Novorossiysk 1968'


def test_read_items():
    response = client.get("/get_configs", headers={token_name: token})
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "sport_ru",
            "url": "https://www.sport.ru/rssfeeds/news.rss",
            "destination": "sport_news",
            "resource_id": 1
        },
        {
            "name": "mk_ru",
            "url": "https://www.mk.ru/rss/sport/index.xml",
            "destination": "sport_news",
            "resource_id": 2
        },
        {
            "name": "sport_rambler",
            "url": "https://sport.rambler.ru/rss/sportrelated/",
            "destination": "sport_news",
            "resource_id": 4
        }
    ]


def test_read_items_bad_token():
    response = client.get("/get_configs", headers={token_name: 'some_fake_token'})
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate credentials"}

# def test_create_item():
#     response = client.post(
#         "/add_new_config/",
#         headers={token_name: token},
#         json={
#             'destination': 'The Foo Barters',
#             'name': 'foobar',
#             'url': 'Foo Bar'}
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "foobar",
#         "url": "Foo Bar",
#         "destination": "The Foo Barters",
#         'resource_id': 8
#     }
#
#
# def test_remove_item():
#     response = client.delete(
#         "/rm_config/8",
#         headers={token_name: token})
#     assert response.status_code == 200
#     assert response.json() == {
#         'destination': 'The Foo Barters',
#         'name': 'foobar',
#         'resource_id': 8,
#         'url': 'Foo Bar'
#     }
