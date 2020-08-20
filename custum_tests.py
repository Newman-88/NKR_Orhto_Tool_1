import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## defining linear regression test 
def linear_test(coef,infile):

    df = pd.read_csv(infile)
    df = df.dropna()
    
    X=df.iloc[:,1:-2]
    Y=df.iloc[:,-2]
    X=X.to_numpy()
    Y=Y.to_numpy()

    intercept=coef[0]
    coef=coef[1:]
    
    new_Y=X@coef+intercept
    diff_y=abs(new_Y-Y)
    rms = (sum((diff_y)**2)/len(diff_y))**(1/2)
    r2=(np.corrcoef(Y,new_Y)[0,1])**2

    plt.title("Multivariate Linear Regression to predict Constant score",fontsize=16)
    plt.axis((40,95,40,95))
    plt.scatter(Y,new_Y,label="Predicted scores")
    plt.plot([40,50,60,80,90,100],[40,50,60,80,90,100],c="black",label="Line x=y")
    for i in range (len(Y)):
        plt.plot([Y[i],Y[i]],[Y[i],new_Y[i]],c="gray",linestyle="-.")
    

    plt.xlabel("Actual constant score")
    plt.ylabel("Predicted constant score")
    plt.legend()

    outfile=infile.split(".")[0]
    plt.savefig(outfile+".svg",format="svg",bbox_inches="tight")
    plt.close()

    r2=round(r2,4)
    rms=round(rms,2)
    return (r2,rms)

## defining logistic regression test 
def log_test(coef,infile):
    df = pd.read_csv(infile)
    df = df.dropna()

    X=df.iloc[:,1:-2]
    Y=df.iloc[:,-1]
    X=X.to_numpy()
    Y=Y.to_numpy()

