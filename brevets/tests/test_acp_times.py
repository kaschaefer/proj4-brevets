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
def nearly(time_one, time_two):
    if time_one < time_two:
        diff = arrow.get(time_two) - arrow.get(time_one)
    else:
        diff = arrow.get(time_one) - arrow.get(time_two)
    minutes = diff.seconds/60
    return int(minutes) <= 1

"""
Testing Opening Times
"""

def test_short_control():
    """
    Test a control set to exactly 15km
    """
    assert nearly(open_time(15, 200, "2018-01-01T00:00:00+00:00"), "2018-01-01T00:26:00+00:00")
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

def test_late_start_time():
    """
    Test a control on a late start time 
    to show days roll over correctly
    """
    assert nearly(open_time(100, 200, "2018-01-01T23:00:00+00:00"), "2018-01-02T01:56:00+00:00")
    assert nearly(close_time(100, 200, "2018-01-01T23:00:00+00:00"), "2018-01-02T05:40:00+00:00")

def test_ending_control():
    """
    A control that is larger than the total brevet distance but smaller than
    total distance + 10% should return the same open/close times as the total distance
    """
    assert nearly(close_time(200, 200, "2018-01-01T23:00:00+00:00"), close_time(210, 200, "2018-01-01T23:00:00+00:00"))
    assert nearly(open_time(200, 200, "2018-01-01T23:00:00+00:00"), open_time(210, 200, "2018-01-01T23:00:00+00:00"))

def test_very_short_control_oddity():
    """
    Testing example 3 from the algorithm description
    An 890km control on a 1000km brevet
    """
    assert nearly(close_time(10, 200, "2018-01-01T00:00:00+00:00"), "2018-01-01T00:40:00+00:00")
    
    