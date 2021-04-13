# -*- coding: utf-8 -*-

import pytest

from eve.vignettes.models import Vignette


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


@pytest.mark.django_db()
def test_get_active_vignettes(client, load_expected_body, load_input_body, clear_json, depp_diff):
    input_data = load_input_body(__file__, "get_active_vignettes.json")
    expected_response_body = load_expected_body(__file__, "get_active_vignettes.json")
    vignette_first = Vignette()
    vignette_second = Vignette()
    response = client.get("/vignettes/1")
    return


@pytest.mark.django_db()
def test_get_licence_plate_validate(client, load_expected_body, load_input_body, clear_json, depp_diff):
    return


@pytest.mark.django_db()
def test_get_history(client, load_expected_body, load_input_body, clear_json, deep_diff):
    return
