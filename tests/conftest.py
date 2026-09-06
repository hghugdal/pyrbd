"""Pytest fixture definitions."""

from collections.abc import Generator

import pytest

from pyrbd import config


@pytest.fixture(name="reset_defaults", autouse=True, scope="function")
def reset_defaults_fixture() -> Generator[None, None, None]:
    """Fixture resetting pysil.config defaults after each test."""

    arrow_style_before = config.ARROW_STYLE
    serif_font_before = config.SERIF_FONT
    output_dir_before = config.OUTPUT_DIR
    source_dir_before = config.SOURCE_DIR

    yield

    config.ARROW_STYLE = arrow_style_before
    config.SERIF_FONT = serif_font_before
    config.OUTPUT_DIR = output_dir_before
    config.SOURCE_DIR = source_dir_before
