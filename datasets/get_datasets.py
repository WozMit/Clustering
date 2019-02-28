import numpy as np;
import matplotlib.pyplot as plt;

def generate_points_click():
	fig, ax = plt.subplots()
	plt.xlim((0, 5));
	plt.ylim((0, 5));

	x = [];
	y = [];

	fig, ax = plt.subplots()

	plt.plot(0, 0, 'b.');
	plt.plot(0, 5, 'b.');
	plt.plot(5, 0, 'b.');
	plt.plot(5, 5, 'b.');

	def onclick(event):
		ax.clear();
		plt.plot(0, 0, 'b.');
		plt.plot(0, 5, 'b.');
		plt.plot(5, 0, 'b.');
		plt.plot(5, 5, 'b.');
		x.append(event.xdata);
		y.append(event.ydata);
		print(event.xdata, event.ydata);
		plt.plot(x, y, 'b.');
		plt.gcf().canvas.draw_idle();

	cid = fig.canvas.mpl_connect('button_press_event', onclick)

	plt.show();

	data = np.zeros((len(x), 2));
	for i in range(len(x)):
		data[i] = x[i], y[i];

	return data;

def generate_on_distribution():
	x = [];
	y = [];

	x1 = np.random.normal(-2, 1.3, 100);
	y1 = np.random.normal(2, 1.3, 100);
	for a, b in zip(x1, y1):
		x.append(a);
		y.append(b);

	x2 = np.random.normal(0, 1.3, 100);
	y2 = np.random.normal(2, 1.3, 100);
	for a, b in zip(x2, y2):
		x.append(a);
		y.append(b);

	x3 = np.random.normal(2, 1.3, 100);
	y3 = np.random.normal(2, 1.3, 100);
	for a, b in zip(x3, y3):
		x.append(a);
		y.append(b);

	x4 = np.random.normal(-2, 1.3, 100);
	y4 = np.random.normal(0, 1.3, 100);
	for a, b in zip(x4, y4):
		x.append(a);
		y.append(b);

	x5 = np.random.normal(0, 1.3, 100);
	y5 = np.random.normal(0, 1.3, 100);
	for a, b in zip(x5, y5):
		x.append(a);
		y.append(b);

	x6 = np.random.normal(2, 1.3, 100);
	y6 = np.random.normal(0, 1.3, 100);
	for a, b in zip(x6, y6):
		x.append(a);
		y.append(b);

	x7 = np.random.normal(-2, 1.3, 100);
	y7 = np.random.normal(-2, 1.3, 100);
	for a, b in zip(x7, y7):
		x.append(a);
		y.append(b);

	x8 = np.random.normal(0, 1.3, 100);
	y8 = np.random.normal(-2, 1.3, 100);
	for a, b in zip(x8, y8):
		x.append(a);
		y.append(b);

	x9 = np.random.normal(2, 1.3, 100);
	y9 = np.random.normal(-2, 1.3, 100);
	for a, b in zip(x9, y9):
		x.append(a);
		y.append(b);

	"""x1 = np.random.gamma(2, 2, 100);
	y1 = np.random.gamma(2, 2, 100);
	for a, b in zip(x1, y1):
		x.append(a);
		y.append(b);

	x2 = -np.random.gamma(2, 1, 100);
	y2 = -np.random.gamma(2, 1, 100);
	for a, b in zip(x2, y2):
		x.append(a);
		y.append(b);

	x3 = np.random.gamma(2, 1.5, 100);
	y3 = -np.random.gamma(2, 1.5, 100);
	for a, b in zip(x3, y3):
		x.append(a);
		y.append(b);"""

	#plt.plot(x1, y1, 'b.');
	#plt.plot(x2, y2, 'r.');
	#plt.plot(x3, y3, 'g.');
	plt.title("Dataset sintético 3(b)");
	plt.plot(x1, y1, 'k.');
	plt.plot(x2, y2, 'k_');
	plt.plot(x3, y3, 'k3');
	plt.plot(x4, y4, 'k1');
	plt.plot(x5, y5, 'k^');
	plt.plot(x6, y6, 'k+');
	plt.plot(x7, y7, 'kx');
	plt.plot(x8, y8, 'k<');
	plt.plot(x9, y9, 'k|');
	plt.show();
	data = np.zeros((900, 2));
	for i in range(900):
		data[i][0] = x[i];
		data[i][1] = y[i];
	return data;

#data = generate_points_click();
data = generate_on_distribution();
#print(data);
print(data.shape);
#np.save('temp.npy', data);

#data = np.load('temp.npy');

#print(data);
#print(data.shape);

#plt.plot(data[:60, 0], data[:60, 1], 'b.');
#plt.plot(data[60:, 0], data[60:, 1], 'r.');
#plt.plot(data[100:, 0], data[100:, 1], 'g.');
#plt.show();

print(len(data), len(data[0]), 3);
for i in range(len(data)):
	if(i < 100): x = 0;
	elif (i < 200): x = 1;
	else: x = 2;
	print(round(data[i, 0], 5), round(data[i, 1], 5), x);