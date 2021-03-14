# -*- coding: utf-8 -*-

import pytest


@pytest.mark.django_db()
def test_get_vignette_types(client, load_expected_body, clear_json, deep_diff):
    response = client.get("/vignettes/types")
    response_body = response.json()
    clear_json(response_body)
    expected_response_body = load_expected_body(__file__, "get_vignette_types.json")
    assert response.status_code == 200
    assert deep_diff(response_body, expected_response_body)
