"""
Setup and configuration for pytest
"""

import time
from unittest.mock import Mock

import pytest


@pytest.fixture(autouse=True)
def add_time_mock(doctest_namespace: dict[str, object]) -> None:
	"""
	Add a doctest mock for `time.sleep()`
	"""
	time.sleep = Mock(return_value=None)
