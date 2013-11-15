from datetime import datetime
from unittest import TestCase
from PythonTesting.ch7.data import Activities, TaskError


class ConstructorTests(TestCase):
    def test_valid(self):
        activity = Activities('activity name', datetime(year=2007, month=9, day=11), datetime(year=2008, month=4, day=27))
        self.assertEqual(activity.name, 'activity name')
        self.assertEqual(activity.begins, datetime(year=2007, month=9, day=11))
        self.assertEqual(activity.ends, datetime(year=2008, month=4, day=27))

    def test_backwards_times(self):
        self.assertRaises(TaskError, Activities, 'activity name',
                          datetime(year=2008, month=1, day=1),
                          datetime(year=2007, month=1, day=1))

    def test_time_frame_too_short(self):
        self.assertRaises(TaskError, Activities, 'activity',
                          datetime(year=2007, month=1, day=1, hour=13, minute=0),
                          datetime(year=2007, month=1, day=1, hour=13, minute=1))