# -*- coding: utf-8 -*-

import pytest

from eve.users.models import Users


@pytest.mark.django_db()
def test_patch_one_user(client, load_expected_body, load_input_body, clear_json, deep_diff, django_db_blocker):
    input_data = load_input_body(__file__, "patch_one_user.json")
    user = Users(email=input_data["email"], first_name=input_data["first_name"], last_name=input_data["last_name"], phone=input_data["phone"])
    user.save()
    user_id = user.id
    expected_response_body = load_expected_body(__file__, "patch_one_user.json")
    patch_res = client.patch("/users/" + str(user_id), input_data, content_type="application/json")
    response = client.get("/users/" + str(user_id))
    response_body = response.json()
    clear_json(response_body)
    assert patch_res.status_code == 200
    assert response.status_code == 200
    assert deep_diff(response_body, expected_response_body)


@pytest.mark.django_db()
def test_get_one_user(client, load_expected_body, load_input_body, clear_json, deep_diff):
    input_data = load_input_body(__file__, "get_one_user.json")
    user = Users(email=input_data["email"], first_name=input_data["first_name"], last_name=input_data["last_name"], phone=input_data["phone"])
    user.save()
    user_id = user.id
    expected_response_body = load_expected_body(__file__, "get_one_user.json")
    client.patch("/users/" + str(user_id), input_data, content_type="application/json")
    response = client.get("/users/" + str(user_id))
    response_body = response.json()
    clear_json(response_body)
    assert response.status_code == 200
    assert deep_diff(response_body, expected_response_body)

