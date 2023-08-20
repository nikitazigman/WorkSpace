import pytest
from unittest.mock import patch


@pytest.fixture
def mock_logger_debug():
    with patch("loguru.logger.debug") as mock_logger_debug:
        yield mock_logger_debug
