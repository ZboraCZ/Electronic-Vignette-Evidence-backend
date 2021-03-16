# -*- coding: utf-8 -*-

import json

import pytest
from deepdiff import DeepDiff


@pytest.fixture(scope="session")
def load_json():
    def _load_json(filepath):
        with open(filepath, "r", encoding="UTF-8") as f:
            return json.load(f)

    return _load_json


@pytest.fixture(scope="session")
def deep_diff():
    def _deep_diff(d1, d2):
        return not DeepDiff(d1, d2, ignore_order=True)

    return _deep_diff
