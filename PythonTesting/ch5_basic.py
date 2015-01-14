from unittest import mock
import unittest
import pid

class AClass():
    def __init__(self):
        self.title = None
        pass

    def getTitle(self):
        return self.title


class TestAClass(unittest.TestCase):
    def setUp(self):
        self.x = AClass()
        self.x.title = "test"

    def test_TitleIsTest(self):
        self.assertEqual(self.x.getTitle(), "test")


class FailingTests(unittest.TestCase):
    def test_assertTrue(self):
        self.assertFalse(1 == 1 + 1)

    def test_equals(self):
        self.assertEqual(1, 1 + 1 - 1)


class TestPidConstructor(unittest.TestCase):
    def ignore_test_without_when(self):
        #time = MagicMock()
        time = mock.MagicMock()
        time.time.return_value = 1
        controller = pid.PID(P=0.5, I=0.5, D=0.5, setpoint=0, initial=12)
        self.assertEqual(controller.gains, (0.5, 0.5, 0.5))
        self.assertAlmostEqual(controller.setpoint[0], 0.0)
        self.assertEqual(len(controller.setpoint), 1)
        self.assertAlmostEqual(controller.previous_time, 1.0)
        self.assertAlmostEqual(controller.previous_error, -12.0)
        self.assertAlmostEqual(controller.integrated_error, 0)

    def test_with_when(self):
        controller = pid.PID(P=0.5, I=0.5, D=0.5,setpoint=1, initial=12, when=43)
        self.assertEqual(controller.gains, (0.5, 0.5, 0.5))
        self.assertAlmostEqual(controller.setpoint[0], 1.0)
        self.assertEqual(len(controller.setpoint), 1)
        self.assertAlmostEqual(controller.previous_time, 43.0)
        self.assertAlmostEqual(controller.previous_error, -11.0)
        self.assertAlmostEqual(controller.integrated_error, 0)

class time

class TestCalculateResponse(unittest.TestCase):
    def ignore_test_without_when(self):
        mocker = mock.MagicMock()
        mock_time = mocker.replace('time.time')
        mock_time()
        mocker.result(1.0)
        mock_time()
        mocker.result(2.0)
        mock_time()
        mocker.result(3.0)
        mock_time()
        mocker.result(4.0)
        mock_time()
        mocker.result(5.0)
        mocker.replay()
        controller = pid.PID(P=0.5, I=0.5, D=0.5, setpoint=0, initial=12)
        self.assertEqual(controller.calculate_response(6), -3)
        self.assertEqual(controller.calculate_response(3), -4.5)
        self.assertEqual(controller.calculate_response(-1.5), -0.75)
        self.assertEqual(controller.calculate_response(-2.25), -1.125)
        mocker.restore()
        mocker.verify()

    def test_with_when(self):
        controller = pid.PID(P=0.5, I=0.5, D=0.5, setpoint=0, initial=12, when=1)
        self.assertEqual(controller.calculate_response(6, 2), -3)
        self.assertEqual(controller.calculate_response(3, 3), -4.5)
        self.assertEqual(controller.calculate_response(-1.5, 4), -0.75)
        self.assertEqual(controller.calculate_response(-2.25, 5), -1.125)

class RaiseAssert(unittest.TestCase):
    def test_assert_raises(self):
        self.assertRaises(ValueError, int, '8cz2', base=16)

    def test_fails_with_message(self):
        if not (2 < 5):
            self.fail('2 should really be less than 5')

if __name__ == '__main__':
    unittest.main()

