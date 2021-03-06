# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2018-2018 by Exopy Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Test the api module and get_icon helper function.

"""
from exopy.app.icons.api import get_icon


def test_get_icon(app, icon_workbench):
    """Test getting an icon using the helper function.

    """
    assert get_icon(icon_workbench, 'folder-open')
