from api.base_api import BaseApi

class PostsApi(BaseApi):

    def create_post(self, title, body, user_id):
        return self.post("/posts", payload={"title": title, "body": body, "userId": user_id})

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")