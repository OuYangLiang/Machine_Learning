from trees import *
import treePlotter

fr=open('./lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = createTree(lenses,lensesLabels[:])
print(lensesTree)
treePlotter.createPlot(lensesTree)