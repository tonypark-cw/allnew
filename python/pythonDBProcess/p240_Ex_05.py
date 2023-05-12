import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "malgun Gothic"

filename = 'ex802.csv'

myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(City)'

myframe.plot(kind='line', title = '지역별 차종 교통량', legend=True)
print(myframe)

filename = 'dataframeGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()
