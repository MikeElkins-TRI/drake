from __future__ import print_function
import unittest
import numpy as np
import dragon.rbtree
import os.path

class TestRBTCoM(unittest.TestCase):
    def testCoM0(self):
        r = dragon.rbtree.RigidBodyTree(os.path.join(dragon.getDrakePath(), "examples/Pendulum/Pendulum.urdf"))

        kinsol = r.doKinematics(np.zeros((7,1)), np.zeros((7,1)))

        c = r.centerOfMass(kinsol)

        self.assertTrue(np.allclose(c.flat, [0.0, 0.0, -0.2425], atol=1e-4))


if __name__ == '__main__':
    unittest.main()