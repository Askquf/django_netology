import random
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

@pytest.fixture()
def client():
    return APIClient()

@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db()
def test_get_course(client, course_factory):
    #Arrange
    course = course_factory(_quantity=1)

    #Act
    response = client.get(f'/api/v1/courses/{course[0].id}/')

    #Assert
    assert response.status_code == 200
    assert response.json()['id'] == course[0].id
    assert response.json()['students'] == list(course[0].students.all())
    assert response.json()['name'] == course[0].name

@pytest.mark.django_db()
def test_get_list_courses(client, course_factory):
    #Arrange
    course = course_factory(_quantity=10)

    #Act
    response = client.get(f'/api/v1/courses/')
    data = response.json()

    #Assert
    assert response.status_code == 200
    for i, item in enumerate(data):
        assert item['id'] == course[i].id
        assert item['students'] == list(course[i].students.all())
        assert item['name'] == course[i].name

@pytest.mark.django_db()
def test_get_id_filtered_courses(client, course_factory):
    #Arrange
    course = course_factory(_quantity=10)
    id = random.randint(0, 9)

    #Act
    response = client.get(f'/api/v1/courses/?id={course[id].id}')
    data = response.json()

    #Assert
    assert response.status_code == 200
    assert data[0]['id'] == course[id].id
    assert data[0]['students'] == list(course[id].students.all())
    assert data[0]['name'] == course[id].name

@pytest.mark.django_db()
def test_get_name_filtered_courses(client, course_factory):
    #Arrange
    course = course_factory(_quantity=10)
    id = random.randint(0, 9)
    name = course[id].name

    #Act
    response = client.get(f'/api/v1/courses/?name={name}')
    data = response.json()

    #Assert
    assert response.status_code == 200
    assert data[0]['id'] == course[id].id
    assert data[0]['students'] == list(course[id].students.all())
    assert data[0]['name'] == course[id].name

@pytest.mark.django_db()
def test_post_course(client):
    #Arrange
    count = Course.objects.count()
    data = {'name': 'name', 'students': []}

    #Act
    response = client.post(f'/api/v1/courses/', data=data)

    #Assert
    assert response.status_code == 201
    assert count + 1 == Course.objects.count()
    assert response.json()['students'] == data['students']
    assert response.json()['name'] == data['name']

@pytest.mark.django_db()
def test_patch_course(client, course_factory):
    #Arrange
    course = course_factory(_quantity=1)
    data = {'name': 'name', 'students': []}
    #Act
    response = client.patch(f'/api/v1/courses/{course[0].id}/', data=data)

    #Assert
    assert response.status_code == 200
    assert response.json()['students'] == data['students']
    assert response.json()['name'] == data['name']

@pytest.mark.django_db()
def test_del_course(client, course_factory):
    #Arrange
    course = course_factory(_quantity=1)
    count = Course.objects.count()

    #Act
    response = client.delete(f'/api/v1/courses/{course[0].id}/')

    #Assert
    assert response.status_code == 204
    assert count - 1 == Course.objects.count()