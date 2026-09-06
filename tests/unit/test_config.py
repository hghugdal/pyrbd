"""Test setting global configs."""

from pyrbd import config

# pylint: disable=missing-function-docstring

arrow_style_before = config.ARROW_STYLE
serif_font_before = config.SERIF_FONT
output_dir_before = config.OUTPUT_DIR
source_dir_before = config.SOURCE_DIR


def test_arrow_style_config() -> None:
    config.ARROW_STYLE = "->"
    assert config.ARROW_STYLE == "->"


def test_serif_font_contif() -> None:
    config.SERIF_FONT = True
    assert config.SERIF_FONT


def test_output_dir_config() -> None:
    config.OUTPUT_DIR = "rbd_output"
    assert config.OUTPUT_DIR == "rbd_output"


def test_source_dir_config() -> None:
    config.SOURCE_DIR = ""
    assert config.SOURCE_DIR == ""


def test_reset_defaults_fixture() -> None:
    assert arrow_style_before == config.ARROW_STYLE
    assert serif_font_before == config.SERIF_FONT
    assert output_dir_before == config.OUTPUT_DIR
    assert source_dir_before == config.SOURCE_DIR
