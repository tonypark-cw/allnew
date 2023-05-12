from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "malgun Gothic"

mylist = [30, 20, 40, 30, 60, 50]
myindex = ['강감찬', '김유신', '이순신', '서민희', '윤동주', '홍길동']

print(myindex)
print(mylist)
print('-' * 50)

myseires = Series(data=mylist, index=myindex)
myylim = [0, myseires.max() + 10]
myseires.plot(title = '시험 점수', kind='line', ylim=myylim, grid=True, rot=10, use_index=True)

filename = 'seriesGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()