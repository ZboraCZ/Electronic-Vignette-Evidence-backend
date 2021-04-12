# -*- coding: utf-8 -*-

import pytest

from eve.users.models import Users


@pytest.mark.django_db()
def test_post_registration(client, load_input_body, clear_json):
    input_data = load_input_body(__file__, "post_registration.json")
    post_res = client.post("/auth/registration", input_data, content_type="application/json")
    response_body = post_res.json()
    clear_json(response_body)
    fist_key = list(response_body.keys())[0]
    assert post_res.status_code == 200
    assert fist_key == "accessToken"

