# -*- coding: utf-8 -*-

import os

import pytest


@pytest.fixture(scope="module")
def load_input_body(load_json):
    def _load_input_body(test_location, input_file):
        directory = os.path.dirname(test_location)
        filename = os.path.join(directory, "input", input_file)
        return load_json(filename)

    return _load_input_body


@pytest.fixture(scope="module")
def load_expected_body(load_json):
    def _load_expected_body(test_location, expected_file):
        directory = os.path.dirname(test_location)
        filename = os.path.join(directory, "expected", expected_file)
        return load_json(filename)

    return _load_expected_body


@pytest.fixture()
def clear_json():
    def __remove_attrs(rjson, clr_attrs):
        for ca in clr_attrs:
            rjson.pop(ca, None)

    def _clear_json(response_json, clear_attributes=["id"]):
        if isinstance(response_json, list):
            for rjson in response_json:
                __remove_attrs(rjson, clear_attributes)
        else:
            __remove_attrs(response_json, clear_attributes)

    return _clear_json
