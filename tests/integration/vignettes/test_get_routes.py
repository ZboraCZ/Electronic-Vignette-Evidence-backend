# -*- coding: utf-8 -*-

import pytest


@pytest.mark.django_db()
def test_get_vignette_types(client, load_expected_body, clear_json, deep_diff):
    response = client.get("/vignettes/types")
    response_body = response.json()
    clear_json(response_body)
    expected_response_body = load_expected_body(
        __file__, "get_vignette_types.json"
    )
    assert response.status_code == 200
    assert deep_diff(response_body, expected_response_body)


@pytest.mark.django_db()
def test_get_one_vignette_type(client, load_expected_body, load_input_body, clear_json, deep_diff):
    input_data = load_input_body(__file__, "patch_one_vignette_type.json")
    expected_response_body = load_expected_body(__file__, "patch_one_vignette_type.json")
    patch = client.patch("/vignettes/types/1/edit", input_data, content_type="application/json")
    response = client.get("/vignettes/types")
    response_body = response.json()
    clear_json(response_body)
    assert patch.status_code == 200
    assert deep_diff(response_body, expected_response_body)