"""
Nose tests for acp_times.py
"""
from acp_times import open_time, close_time

import nose
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

"""
Helper Function to Allow for 1 minute difference
to account for rounding errors
"""
def nearly(x, y):
    if (x < y):
        time_one = y
        time_two = x
    else:
        time_one = x
        time_two = y
    diff = arrow.get(time_one) - arrow.get(time_two)
    minutes = diff.seconds/60
    return not ( int(minutes) > 1)

"""
Testing Opening Times
"""

def test_short_control():
    """
    Test a control set to exactly 15km
    Should return exactly one hour later
    """
    assert nearly(close_time(15, 200, "2017-10-18T06:00:00-08:00"), "2017-10-18T07:00:00-08:00")

def test_edge_case():
    """
    Test controls at 590km, 600km, and 610km on 1000km
    brevet open and close at the correct times
    """
    assert nearly(open_time(590, 1000, "2018-01-01T00:00:00+00:00"), "2018-01-01T18:28:00+00:00")
    assert nearly(open_time(600, 1000, "2018-01-01T00:00:00+00:00"), "2018-01-01T18:48:00+00:00")
    assert nearly(open_time(610, 1000, "2018-01-01T00:00:00+00:00"), "2018-01-01T19:09:00+00:00")

    assert nearly(close_time(590, 1000, "2018-01-01T00:00:00+00:00"), "2018-01-02T15:20:00+00:00")
    assert nearly(close_time(600, 1000, "2018-01-01T00:00:00+00:00"), "2018-01-02T16:00:00+00:00")
    assert nearly(close_time(610, 1000, "2018-01-01T00:00:00+00:00"), "2018-01-02T16:53:00+00:00")

def test_bad_input_string():
    """
    Test that the algorithms can properly handle bad time strings
    """
    assert not close_time(590, 1000, "") == "2018-01-02T15:20:00+00:00"
    assert not close_time(200, 200, "abcdefg") == "2018-01-02T16:53:00+00:00"
    assert not open_time(590, 1000, "") == "2018-01-02T15:20:00+00:00"
    assert not open_time(200, 200, "abcdefg") == "2018-01-02T16:53:00+00:00"

def test_bad_input_nums():
    """
    Test that the algorithms can handle bad nums
    """
    assert not close_time(-5, 150, "2018-01-02T16:53:00+00:00") == "2018-01-02T16:53:00+00:00"
