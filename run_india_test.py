import traceback
from backtesting.test.test_india_fixed import test_default_holidays_and_expiry
from backtesting.test.test_broker_india import test_broker_lot_and_tick_enforcement

if __name__ == '__main__':
    try:
        test_default_holidays_and_expiry()
        test_broker_lot_and_tick_enforcement()
        print('TESTS OK')
    except AssertionError as e:
        print('TEST FAIL: AssertionError')
        traceback.print_exc()
    except Exception:
        print('TEST FAIL: Exception')
        traceback.print_exc()
