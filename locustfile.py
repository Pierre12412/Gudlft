from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = ()
    def on_start(self):
        self.client.post("/showSummary", {
            "email": "admin@irontemple.com",
        })
        self.client.get("/logout")

    @task
    def index(self):
        self.client.get("/book/Fall%20Classic/Iron%20Temple")

    @task
    def about(self):
        self.client.get("/")

