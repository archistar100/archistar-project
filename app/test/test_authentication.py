#!/usr/bin/env python
"""Unit tests for the src.authentication module."""

from unittest import TestCase
from mock import patch
import src.authentication as auth

class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""

    @patch('__builtin__.open')
    def test_login_success(self, mock_open):
        """Test the login function when things go right."""
        mock_open.return_value.read.return_value = \
            "dan|pfeiffer"
        self.assertTrue(auth.login('dan', 'pfeiffer'))

    @patch('__builtin__.open')
    def test_login_bad_creds(self, mock_open):
        """Test the login function when bad creds are passed."""
        mock_open.return_value.read.return_value = \
            "scott|steele"
        self.assertFalse(auth.login('dan', 'pfeiffer'))

    @patch('__builtin__.open')
    def test_login_error(self, mock_open):
        """Test the login function when an error happens."""
        mock_open.side_effect = IOError()
        self.assertFalse(auth.login('scott', 'steele'))
