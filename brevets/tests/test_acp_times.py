"""
Nose tests for acp_times.py
"""
from acp_times.py import open_time, close_time

import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

"""
Testing Opening Times
"""

def test_short_control():
    """
    Test a control set to exactly 15km
    Should return exactly one hour later
    """
    assert open_time(15, 200, 2017-10-18T06:00:00+00:00) == 2017-10-18T07:00:00+00:00

def test_example1():
    """
    From example 1 on the rules page
    Test that on a 200km brevet with a 175 control
    opening time is 5H09 after start
    """
    assert open_time(175, 200, 2017-10-18T06:00:00+00:00) == 2017-10-18T11:09:00+00:00

def test_example2():
    """
    From example 2 on the rules page
    Test that on a 600 km brevet with a 350 control
    opening time is 10H34 after start
    """
    assert open_time(350, 600, 2017-10-18T06:00:00+00:00) == 2017-10-18T16:34:00+00:00

"""
Testing Closing Times
"""

def test_correct_closing_time():
    """
    Test that closing time at start point is calculated correctly
    """
    assert close_time(0, 600, 2017-10-18T06:00:00+00:00) == 2017-10-18T07:00:00+00:00

def test_example1():
    """
    From example 1 on rules page
    Test that on a 200km brever with a 175 control
    closing time is 11H40 after start
    """
    assert close_time(175, 200, 2017-10-18T06:00:00+00:00) == 2017-10-18T17:40:00+00:00

def test_example2():
    """
    From example 2 on rules page
    Test that on a 600 brevet with any control
    closing time should be as shown
    """
    assert close_time(200, 600, 2017-10-18T06:00:00+00:00) == 2017-10-18T19:20:00+00:00
    assert close_time(500, 600, 2017-10-18T06:00:00+00:00) == 2017-10-19T15:20:00+00:00
    assert close_time(600, 600, 2017-10-18T06:00:00+00:00) == 2017-10-19T22:00:00+00:00

def test_example3():
    """
    From example 3 on rules page
    Test that on a 1000km brevet with 890km control
    closing time is 65H23
    """
    assert close_time(890, 1000, 2017-10-18T06:00:00+00:00) == 2017-10-20T23:23:00+00:00
