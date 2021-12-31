class Interval():
	def __init__(self, file='tracer.traj_s'):
		self.input = file


		with open('tracer.traj_s', 'r') as f:
			rad = f.readlines()
		rad = rad[1:]
		self.clean = [float(i.split()[0]) for i in rad]


    #mark is the height of the box where we start record the time intercval
    #delta is the error tolerance
	def cal_interval(self, mark, delta):
		draft = [i for i, e in enumerate(self.clean) if abs(int(e)-mark) < delta or abs(int(e)+15) < delta]
		#print('draft is', draft)


		interval = []
		for i in range(len(draft)-2):
			diff = draft[i+1] - draft[i]
			if diff > 20:
				interval.append(diff)
		return interval

	def cal_penetration_time(self, mark, delta):
		draft = [i for i, e in enumerate(self.clean) if abs(int(e)-mark) < delta or abs(int(e)+15) < delta]
		#print('draft is', draft)

		count = 1
		linger = []
		for i in range(len(draft)-1):
			if draft[i+1] - draft[i] < 30:
				count += 1

			else:
				linger.append(count)
				count = 1

		return linger

if __name__ == '__main__':

	itval = Interval()

	inv = itval.cal_interval(24, 3)
	lng = itval.cal_penetration_time(24, 3)
	print(lng)


