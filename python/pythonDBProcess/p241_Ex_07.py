import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'malgun Gothic'
filename = 'mygraph.csv'

myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
myframe.index.name = '이름'
myframe.columns.name = '시험 과목'

myframe.plot(kind='bar', rot=0, stacked=True, title='학생별 누적 시험 점수', legend=True)  # stacked=True : 막대가 서로 위에 쌓임
filename = 'dataframeGraph02_04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다.')
print('-' * 40)

plt.show()
