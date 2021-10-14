from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1,5)
    def on_start(self):
        self.client.post("/showSummary", {
            "email": "admin@irontemple.com",
        })

    @task
    def index(self):
        self.client.get("/book/Fall%20Classic/Iron%20Temple")

    @task
    def about(self):
        self.client.get("/")

    @task
    def logout(self):
        self.client.get('/logout')

    @task
    def purchase(self):
        self.client.post('/purchasePlaces', {
            'places': '3',
            'competition': 'Fall Classic',
            'club': 'Iron Temple',
        })

    @task
    def display(self):
        self.client.get('/display')