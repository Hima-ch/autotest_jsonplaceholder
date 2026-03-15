import pytest
import allure
from api.posts_api import PostsApi
from models.post_model import Post

@pytest.fixture
def posts_api():
    return PostsApi()

@allure.feature("Performance")
@allure.story("Response time stability")
def test_stability(posts_api):
    with allure.step("Repeat request post with id 1 10 times"):
        times = []
        for i in range(10):
            response = posts_api.get_post(1)
            times.append(response.seconds)
        avg_time = sum(times) / len(times)
    with allure.step(f"Verify average response time (Actual: {avg_time:.2f}s)"):
        assert avg_time < 1.5
