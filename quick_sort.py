import matplotlib.pyplot as plt
import matplotlib
import numpy as np

N = 100
ignore = N/2
visualize = True
comparison = True



ch1 = None
counter = 0
def main():
	arr = np.arange(1, N+1, 1)
	np.random.shuffle(arr)
	if visualize:
		global ch1
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ch1 = ax.bar(np.arange(len(arr)), arr, 1, color='grey')
		plt.ion()
		plt.show()

	def updatePlt(A, pivot=None, border=None, start_end=None, base_sorted=False, force=False):
		global ignore, counter
		counter +=1
		if (not visualize or counter % ignore != 0) and (not force or comparison):
			return
		global ch1
		ch1.remove()
		colr = 'grey' if not base_sorted else 'green'
		ch1 = ax.bar(np.arange(len(A)), A, 1, color=colr)
		if start_end:
			for i in range(start_end[0]):
				ch1[i].set_color('green')
			for i in range(start_end[0], start_end[1]):
				ch1[i].set_color('SkyBlue')
		#ch1[start_end[1]].set_color('g')
		if pivot:
			ch1[pivot].set_color('r')
		if border:
			ch1[border].set_color('b')
		#ax.set_xticks(index + bar_width / 2)

		fig.canvas.draw()

	def get_pivot(A, low, hi):
		mid = (low+hi)//2
		pivot = hi
		if(A[low] < A[mid]):
			if(A[mid] < A[hi]):
				pivot = mid
		elif(A[low] > A[hi]):
			pivot = low
		return pivot


	def split_it(A, low, hi, cp_f):
		pivotIndex = get_pivot(A, low, hi)
		pivotValue = A[pivotIndex]
		A[pivotIndex], A[low] = A[low], A[pivotIndex]
		border = low
		for i in range(low, hi+1):
			updatePlt(A, pivotIndex, border, (low, hi))
			if cp_f(A[i],pivotValue):
				border+=1
				A[i], A[border] = A[border], A[i]
		A[low], A[border] = A[border], A[low]

		return border


	def quick_sort2(A, low, hi, cp_f):
		if low < hi:
			p = split_it(A, low, hi, cp_f) #returns border index
			quick_sort2(A, low, p-1, cp_f)
			quick_sort2(A, p+1, hi, cp_f)


	def quick_sort(A, compare=lambda x, y : x<y):
		T = A[:]
		quick_sort2(T, 0, len(T)-1, compare)
		global comparison
		comparison = False
		updatePlt(A, base_sorted=True, force=True)
		comparison = True
		return T

	arr2 = quick_sort(arr)
	with matplotlib.rc_context(rc={'interactive': False}):
		plt.show()

if __name__ == '__main__':
	main()