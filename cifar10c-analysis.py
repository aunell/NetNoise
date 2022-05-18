import matplotlib.pyplot as plt
import pandas as pd

improvementDict= {}
results=pd.read_csv('/Users/alyssaunell/PycharmProjects/NetNoise/NetNoise/results/resnetcifar10c.csv')
arch = 'ResNet'
regimes=set(results['regime'])
# print(regimes)
# results.drop(results[results['regime'] == 'grayBlurColor'].index, inplace = True)
# print(results['degredation'])
# l=[0, 3, 4, 5, 10, 12, 13]
# al=[3, 5, 7, 10, 18]
# print(results)
for deg in results['degredation']:
    best = results.loc[(results['degredation'] == deg) & (results['regime'] != 'baseline')]
    # best = results.loc[(results['degredation'] == deg) & (results['regime'] == 'baseline')]
    bestAcc = best['accuracy'].max()
    bio = results.loc[(results['degredation'] == deg) & (results['regime'] == 'baseline')]
    bioAcc = bio['accuracy'].max()
    # gbc = results.loc[(results['degredation'] == deg) & (results['regime'] == 'grayBlurColor')]
    # gbcAcc = gbc['accuracy'].max()
    # bioAcc=max(bioAcc, gbcAcc)
    # bestAccScore=bestAcc['accuracy']
    diff = (bioAcc - bestAcc) / bestAcc
    improvementDict[deg] = (bioAcc - bestAcc) / bestAcc
# print(improvementDict)
# for r in regimes:
    # print(r, results.loc[(results['regime'] == r)]['accuracy'].mean())
    # print(results.loc[(results['regime'] == r)]['accuracy'])
    # id[r] = results.loc[(results['regime'] == r)]['accuracy'].var()
vals = list(improvementDict.values())
print(max(vals))
print(min(vals))
# print(id)
# mylist = [key for key, val in improvementDict.items() for _ in range(val)]
plt.figure(figsize=(10, 10))
plt.hist(vals, bins=[-.5, -.4, -.3, -.2, -.1, -.05, 0, .05, .1, .15, .2, .25, .3, .35, .4, .45])
plt.xlabel('% Bio-mimetic Improvement', fontsize=18)
plt.ylabel('Regimes with Improvement', fontsize=18)
plt.title(arch + ' Cifar-10-C Bio-mimetic Improvement Score', fontsize=20)
# figName = '/om/user/aunell/NetNoise/results/' + arch + '10c.pdf'
# plt.savefig(figName, format='pdf')
plt.show()
