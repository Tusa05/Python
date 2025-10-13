from pages.yougile_projects import YougileProjects


# Bearer Token.
# В эту переменную нужно вписать токен:
my_key = "DF-EVTGaQkzC3IIMa9OJUlg1lPG1KSgEIQtK0UtCDFBHIFNN305VJa1qHM6Lhjsd"

bearer_token = {
    "Authorization": f"Bearer {my_key}"
}

yougile = YougileProjects("https://ru.yougile.com/api-v2/")


# Тесты для метода [GET] /api-v2/projects.
def test_pos_get_list(auth_token=bearer_token):
    response = yougile.get_list(auth_token)
    assert response.status_code == 200
    projects_list = response.json()
    assert len(projects_list["content"]) == projects_list["paging"]["count"]


def test_neg_get_list():
    # Получение списка проектов неавторизованным пользователем.
    response = yougile.get_list()
    assert response.status_code == 401


# Тесты для метода [POST] /api-v2/projects.
def test_pos_create_project(auth_token=bearer_token):
    response = yougile.create_project(auth_token, {"title": "Finance Department"})
    assert response.status_code == 201
    result = response.json()
    assert result["id"] != 0


def test_neg_create_project(auth_token=bearer_token):
    # Создание проекта без указания обязательного значения "Название проекта".
    response = yougile.create_project(auth_token)
    assert response.status_code == 400


# Тесты для метода [PUT] /api-v2/projects/{id}.
def test_pos_modify_project(auth_token=bearer_token):
    response = yougile.create_project(auth_token,
                                      {"title": "Finance Department"})
    result = response.json()
    modified_project = yougile.modify_project(auth_token,
                                              result["id"],
                                              {"title": "Department"})
    assert modified_project.status_code == 200


def test_neg_modify_project(auth_token=bearer_token):
    # Изменение проекта с несуществующим id.
    modified_project = yougile.modify_project(auth_token,
                                              "01234567-89ab-cdef-0123-456789a\
                                               bcdef",
                                              {"title": "Марвел"})
    assert modified_project.status_code == 404


# Тесты для метода [GET] /api-v2/projects/{id}.
def test_pos_get_project(auth_token=bearer_token):
    response = yougile.create_project(auth_token,
                                      {"title": "Department"})
    result = response.json()
    getted_project = yougile.get_project(auth_token, result["id"])
    assert getted_project.status_code == 200


def test_neg_get_project(auth_token=bearer_token):
    # Получение проекта с несуществующим id.
    getted_project = yougile.get_project(auth_token,
                                         "01234567-89ab-cdef-0123-456789abcde\
                                          f")
    assert getted_project.status_code == 404
