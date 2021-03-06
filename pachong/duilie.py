import threading
from queue import queue

def job(l,w):
	for i in range(len(l)):
		l[i] = l[i]**2
	w.put(l)

def multithreading(data):
	w = queue()
	threads = []
	data = [[1,2,3],[2,2,2],[3,3,3],[4,4,4]]
	for i in range(4):
		t = threading.Thread(target=job,aegs=(data[i], w)) 
		t.start()
		threads.append(t)
	for thread in threads:
		thread.join()
	results = []
	for j in range(4):
		results.append(w.get())
	print(results)

if __name__ == '__main__':
	multithreading(data)
