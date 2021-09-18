from common.path_url import WikiPathURL

from locust import HttpUser, task, between


class MyUser(HttpUser):

    wait_time = between(1, 2)

    def on_start(self):
        self.client.get(WikiPathURL.MAIN_PAGE)

    @task(2)
    def tab_cofiguration(self):
        self.client.get(WikiPathURL.TAB_CONFIGURATION)
        self.client.get(WikiPathURL.TAB_CONFIGURATION_FILE)

    @task(1)
    def tab_api(self):
        self.client.get(WikiPathURL.TAB_API)
