import numpy as np
import matplotlib.pyplot as plt

X = ['Accuracy', 'Precision', 'F1', 'Recall']
KN = [0.9830760979679399, 0.9781822752468494, 0.9820056017362808, 0.9864734637041769]
LSVC = [0.9463679160955842, 0.9366729141025021, 0.9439476562431107, 0.9571844054804273]
NB = [0.8945235683213157, 0.8890282131661442, 0.8919272298218041, 0.9163199697428139]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.1, LSVC, 0.2, label='LSVC')
plt.bar(X_axis + 0.1, KN, 0.2, label='KN')
plt.bar(X_axis + 0.3, NB, 0.2, label='NB')

plt.xticks(X_axis, X)
plt.xlabel("Results")
plt.ylabel("Score")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0)
plt.show()
