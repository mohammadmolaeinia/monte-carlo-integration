import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

def f(x):
    return 3*(x**3)-4*(x**2)+7*x-18

xForExt = np.linspace(-4, 6, 1000)
yForExt = f(xForExt)
iMax = np.argmax(yForExt)
iMin = np.argmin(yForExt)
yMax = yForExt[iMax]
yMin = yForExt[iMin]

means = []
errs = []
qty = []

for n in range(5, 4001, 5):

    results = []

    for _ in range(10):

        nPls = round(n*yMax/(yMax-yMin))
        nNeg = round(-n*yMin/(yMax-yMin))

        xPls=((np.random.rand(nPls,1))*10)-4.0
        xNeg=((np.random.rand(nNeg,1))*10)-4.0
        yPls = ((np.random.rand(nPls,1)))*yMax
        yNeg = ((np.random.rand(nNeg,1)))*yMin

        rPls=yPls-(3*(xPls**3)-4*(xPls**2)+7*xPls-18)
        rNeg=-yNeg+(3*(xNeg**3)-4*(xNeg**2)+7*xNeg-18)

        dumPls=np.where(rPls<=0,1.0,0.0)
        dumNeg=np.where(rNeg<=0,-1.0,0.0)

        Ant=(sum(dumPls)+sum(dumNeg))/(n)*(10*(yMax-yMin))

        results.append(Ant)

    mean = np.mean(results)
    err = abs(296.6667-mean)
    means.append(mean)
    errs.append(err)
    qty.append(n)

iBestAnt = np.argmin(errs)
bestAnt = means[iBestAnt]
bestn = qty[iBestAnt]

#printing what Problem want
print(f"The Best Ant : {bestAnt:.4f}")
print(f"The Best n : {bestn:.4f}")
#making figure of Errors
chartErrors, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot(qty, errs, color='red', linewidth=2, linestyle='-')
ax3.set_xlabel('Qty of n')
ax3.set_ylabel('Errors')
ax3.xaxis.set_tick_params(labelsize=6.5)
ax3.yaxis.set_tick_params(labelsize=6.5)
plt.title('Errors')
ax3.grid(True, linestyle='--', alpha=0.6)
chartErrors.tight_layout()

plt.show()
