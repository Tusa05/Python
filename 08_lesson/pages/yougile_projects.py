import requests


class YougileProjects:

    def __init__(self, url):
        self.url = url

    def get_list(self, auth_token=None):
        response = requests.get(self.url + "projects", headers=auth_token)
        return response

    def create_project(self, auth_token=None, title={}):
        response = requests.post(self.url + "projects", headers=auth_token,
                                 data=title)
        return response

    def modify_project(self, auth_token=None, id="", title={}):
        response = requests.put(self.url + "projects/" + id,
                                headers=auth_token, data=title)
        return response

    def get_project(self, auth_token=None, id=""):
        response = requests.get(self.url + "projects/" + id,
                                headers=auth_token)
        return response
