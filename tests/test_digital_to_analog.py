#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `digital_to_analog` package."""

import pytest

from click.testing import CliRunner

from digital_to_analog import digital_to_analog
from digital_to_analog import cli
from digital_to_analog import client


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

    socket = initialize_client_socket()
    g = Game(socket)
    b = Bird(g, socket)
    assert b.acc == vec(0, 0)


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""

    socket = initialize_client_socket()
    g = Game(socket)
    b = Bird(g, socket)
    assert g.score == 0


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'digital_to_analog.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
