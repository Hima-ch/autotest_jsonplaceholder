import pytest
import allure
from api.posts_api import PostsApi
from models.post_model import Post

@pytest.fixture
def posts_api():
    return PostsApi()

@allure.feature("Posts API")
@allure.story("Negative scenarios")
def test_error_get_post(posts_api):
    with allure.step("Step 1: Request post with invalid id"):
        post_id = 999
        response = posts_api.get_post(post_id)
    with allure.step("Step 2: Verify response status code"):
        assert response.status_code == 404

@allure.feature("Posts API")
@allure.story("Negative scenarios")
@pytest.mark.parametrize("invalid_id", ["abc", "-34", "h*&"])
def test_get_post_with_invalid_id(posts_api, invalid_id):
    with allure.step(f"Step 1: Request post with invalid id {invalid_id}"):
        response = posts_api.get_post(invalid_id)
    with allure.step("Step 2: Verify response status code"):
        assert response.status_code == 404

@allure.feature("Posts API")
@allure.story("Negative scenarios")
@pytest.mark.xfail(reason="The test fails, the fake API allows you to create a post with an empty title and returns a 201 / Тест не проходит, фейк апи позволяет создать пост с пустым заголовком и возвращает 201")
def test_create_post_with_no_title(posts_api):
    with allure.step("Step 1: Create post with invalid title"):
        title, body, user_id = "", "abcd", 6
        response = posts_api.create_post(title, body, user_id)
    with allure.step("Step 2: Verify response status code"):
        assert response.status_code == 400
