import pytest
import allure
from api.posts_api import PostsApi
from models.post_model import Post

@pytest.fixture
def posts_api():
    return PostsApi()

@allure.feature("Posts API")
@allure.story("Create post")
def test_success_create_post(posts_api):
    with allure.step("Create post with title, body and user_id"):
        title, body, user_id = "title new post", "text new post", 8
        response = posts_api.create_post(title, body, user_id)
    with allure.step("Verify response status code"):
        assert response.status_code == 201

@allure.feature("Posts API")
@allure.story("Get post")
def test_succes_get_post(posts_api):
    with allure.step("Request post with id 1"):
        post_id = 1
        response = posts_api.get_post(post_id)
    with allure.step("Verify response status code"):
        assert response.status_code == 200
    with allure.step("Verify post id in response"):
        assert response.json()["id"] == post_id

@allure.feature("Posts API")
@allure.story("Get post")
@pytest.mark.parametrize("post_id", [1, 5, 10, 100])
def test_get_valid_posts(posts_api, post_id):
    with allure.step(f"Request post with id {post_id}"):
        response = posts_api.get_post(post_id)
    with allure.step("Verify response status code"):
        assert response.status_code == 200

@allure.feature("Posts API")
@allure.story("Delete post")
def test_delete_post(posts_api):
    with allure.step("Delete post with id 2"):
        post_id = 2
        response = posts_api.delete_post(post_id)
    with allure.step("Verify response status code"):
        assert response.status_code == 200

@allure.feature("Posts API")
@allure.story("Get post")
def test_post_data_type(posts_api):
    with allure.step("Request post with id 3"):
        response = posts_api.get_post(3)
    data = response.json()

    with allure.step("Verify valid id"):
        assert isinstance(data["id"], int)
    with allure.step("Verify valid title"):
        assert isinstance(data["title"], str)
    with allure.step("Verify valid body"):
        assert isinstance(data["body"], str)
    with allure.step("Verify valid userId"):
        assert isinstance(data["userId"], int)

@allure.feature("Posts API")
@allure.story("Get post")
def test_get_post_validation(posts_api):
    with allure.step("Request post with id 1"):
        response = posts_api.get_post(1)
    with allure.step("Verify valid data"):
        Post(**response.json())

@allure.feature("Posts API")
@allure.story("Get post")
@pytest.mark.xfail
def test_create_get_post(posts_api):
    with allure.step("Create post with title, body and user_id"):
        title, body, user_id = "title new post", "text new post", 8
        response = posts_api.create_post(title, body, user_id)
    with allure.step("Getting the new post id"):
        new_post_id = response.json()["id"]
    with allure.step("Request new post with id"):
        get_response = posts_api.get_post(new_post_id)
    with allure.step("Verify response status code"):
        assert get_response.status_code == 200      # The test fails because the fake API doesn't update resources when a post is created / Тест не проходит, так как фейк апи не обновляет базу при создании поста
    with allure.step("Verify post title in response"):
        assert get_response.json()["title"] == title
