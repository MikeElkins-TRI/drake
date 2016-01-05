function testRBTCoM()
r = dragon.RigidBodyTree(fullfile(getDrakePath(), 'examples/Pendulum/Pendulum.urdf'));

kinsol = r.doKinematics(zeros(7,1), zeros(7,1));

c = r.centerOfMass(kinsol);

valuecheck(c, [0; 0; -0.2425], 1e-4);

end