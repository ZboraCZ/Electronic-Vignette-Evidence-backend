# -*- coding: utf-8 -*-

import pytest

@pytest.mark.django_db()
def test_delete_remove(client, load_expected_body, load_input_body, clear_json, deep_diff):
    return