
import unittest2

import testlib
import mitogen.core


class Thing():
    pass


class ListenFireTest(testlib.TestCase):
    def test_no_args(self):
        thing = Thing()
        latch = mitogen.core.Latch()
        mitogen.core.listen(thing, 'event',
            lambda: latch.put('event fired'))

        mitogen.core.fire(thing, 'event')
        self.assertEquals('event fired', latch.get())
        self.assertTrue(latch.empty())

    def test_with_args(self):
        thing = Thing()
        latch = mitogen.core.Latch()
        mitogen.core.listen(thing, 'event', latch.put)
        mitogen.core.fire(thing, 'event', 'event fired')
        self.assertEquals('event fired', latch.get())
        self.assertTrue(latch.empty())

    def test_two_listeners(self):
        thing = Thing()
        latch = mitogen.core.Latch()
        latch2 = mitogen.core.Latch()
        mitogen.core.listen(thing, 'event', latch.put)
        mitogen.core.listen(thing, 'event', latch2.put)
        mitogen.core.fire(thing, 'event', 'event fired')
        self.assertEquals('event fired', latch.get())
        self.assertEquals('event fired', latch2.get())
        self.assertTrue(latch.empty())
        self.assertTrue(latch2.empty())


if __name__ == '__main__':
    unittest2.main()
