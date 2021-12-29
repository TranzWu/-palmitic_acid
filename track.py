#chunzhiwu
#place holder info
import numpy as np
import matplotlib.pyplot as plt


class Parse():
    count = 0

    def __init__(self, file):
        self.trajectory = file
        self.traj = []

    def parse_cordinates(self, n, f, atomType):
        pos = []
        for i in range(n):
            line = f.readline()
            clean = [int(i) if e == 0 or e == 1 else float(i) for e, i in enumerate(line.split())]

            if clean[1] == atomType:
                pos.append(clean[4])

        self.traj.append(pos)



    def header(self, f, atomType):
        for i in range(2):
            f.readline()
        n = int(f.readline())

        for i in range(5):
            a = f.readline()

        assert("ITEM: ATOMS id type x y z" in a)
        self.parse_cordinates(n, f, atomType)

    def track(self, atomType):
        with open(self.trajectory, 'r') as rad:
            while True:
                line = rad.readline()

                if not line:
                    break
                assert(line == "ITEM: TIMESTEP\n")
                self.header(rad, atomType)

    def write_to_file(self, max_t=None):
        if max_t:
            if max_t < len(self.traj):
                self.traj = self.traj[:max_t]
        with open('tracer.traj_s', 'w') as rad:
            for n in range(len(self.traj[0])):
                rad.write(f'tracer {n}\n')
                data = []
                for i in self.traj:
                    data.append(i[n])
                    rad.write(f'{i[n]}\n')

                plt.plot([i for i in range(len(self.traj))], data, label=f'tracer {n}')

        plt.legend()
        plt.xlabel('t/ps')
        plt.ylabel('z component/Angstrom')
        plt.savefig('tracer_full_small.png')
