import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("ntaxa-100-species-trees.csv")
#pd.read_csv("ntaxa-25-species-trees.csv")
#pd.read_csv("ntaxa-50-species-trees.csv")
#pd.read_csv("ntaxa-100-species-trees.csv")

NGEN = [25, 50, 100, 500]
SQLN = [0, 25, 50, 100, 250]
DLRT = [0.0, 0.0000000001, 0.0000000002, 0.0000000005]
PSIZ = [1000, 50000000]
TITLE = ["25 genes","50 genes","100 genes","500 genes"]
SIDE = ["DLRT=0.0", "DLRT=1e-10", "DLRT=2e-10", "DLRT=5e-10"]
colors = ['lightblue', 'lightgreen', 'orangered', 'pink', 'black']

#------
df1 = df1.dropna()
#------

plt.figure(0) #sqln = 25
for i in range(len(NGEN)):
    for j in range(len(DLRT)):
        ax = plt.subplot(len(DLRT), len(NGEN), j*len(NGEN)+i+1)
        plt.ylim(0,1)
        error_split_astrid = (df1[(df1["SQLN"] == 25) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split-astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_split_astral = (df1[(df1["SQLN"] == 25) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astrid = (df1[(df1["SQLN"] == 25) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astral = (df1[(df1["SQLN"] == 25) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astral") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_njst = (df1[(df1["SQLN"] == 25) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "njst") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        data_ = [error_split_astrid, error_astrid, error_split_astral, error_astral, error_njst]
        bplot = ax.boxplot(data_,  patch_artist=True)
        #----------------------------------------------------------
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        #----------------------------------------------------------
        ax.set_xticklabels(["split-astrid","ASTRID","split-astral","ASTRAL", "NJst"])
        ax.yaxis.grid(True)
        if(i==0):
            plt.ylabel(SIDE[j])
        if (j == 0):
            ax.set_title(TITLE[i])
plt.suptitle("Error rate of on simulation data set when number of taxa = 100, sequence length = 25")
#------------------------------------------
plt.figure(1) #sqln = 50
for i in range(len(NGEN)):
    for j in range(len(DLRT)):
        ax = plt.subplot(len(DLRT), len(NGEN), j*len(NGEN)+i+1)
        plt.ylim(0,1)
        error_split_astrid = (df1[(df1["SQLN"] == 50) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split-astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_split_astral = (df1[(df1["SQLN"] == 50) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astrid = (df1[(df1["SQLN"] == 50) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astral = (df1[(df1["SQLN"] == 50) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astral") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_njst = (df1[(df1["SQLN"] == 50) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "njst") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        data_ = [error_split_astrid, error_astrid, error_split_astral, error_astral, error_njst]
        bplot = ax.boxplot(data_,  patch_artist=True)
        #----------------------------------------------------------
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        #----------------------------------------------------------
        ax.set_xticklabels(["split-astrid","ASTRID","split-astral","ASTRAL", "NJst"])
        ax.yaxis.grid(True)
        if(i==0):
            plt.ylabel(SIDE[j])
        if (j == 0):
            ax.set_title(TITLE[i])
plt.suptitle("Error rate on simulation data set when number of taxa = 100, sequence length = 50")
#------------------------------------------
plt.figure(2) #sqln = 100
for i in range(len(NGEN)):
    for j in range(len(DLRT)):
        ax = plt.subplot(len(DLRT), len(NGEN), j*len(NGEN)+i+1)
        plt.ylim(0,1)
        error_split_astrid = (df1[(df1["SQLN"] == 100) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split-astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_split_astral = (df1[(df1["SQLN"] == 100) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astrid = (df1[(df1["SQLN"] == 100) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astral = (df1[(df1["SQLN"] == 100) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astral") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_njst = (df1[(df1["SQLN"] == 100) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "njst") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        data_ = [error_split_astrid, error_astrid, error_split_astral, error_astral, error_njst]
        bplot = ax.boxplot(data_,  patch_artist=True)
        #----------------------------------------------------------
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        #----------------------------------------------------------
        ax.set_xticklabels(["split-astrid","ASTRID","split-astral","ASTRAL", "NJst"])
        ax.yaxis.grid(True)
        if(i==0):
            plt.ylabel(SIDE[j])
        if (j == 0):
            ax.set_title(TITLE[i])
plt.suptitle("Error rate on simulation data set when number of taxa = 100, sequence length = 100")
#------------------------------------------
plt.figure(3) #sqln = 250
for i in range(len(NGEN)):
    for j in range(len(DLRT)):
        ax = plt.subplot(len(DLRT), len(NGEN), j*len(NGEN)+i+1)
        plt.ylim(0,1)
        error_split_astrid = (df1[(df1["SQLN"] == 250) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split-astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_split_astral = (df1[(df1["SQLN"] == 250) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "split") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astrid = (df1[(df1["SQLN"] == 250) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astrid") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_astral = (df1[(df1["SQLN"] == 250) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "astral") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        error_njst = (df1[(df1["SQLN"] == 250) & (df1["NGEN"] == NGEN[i]) & (df1["MTHD"] == "njst") & (df1["DLRT"] == DLRT[j])]["SERF"]).values
        data_ = [error_split_astrid, error_astrid, error_split_astral, error_astral, error_njst]
        bplot = ax.boxplot(data_,  patch_artist=True)
        #----------------------------------------------------------
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        #----------------------------------------------------------
        ax.set_xticklabels(["split-astrid","ASTRID","split-astral","ASTRAL","NJst"])
        ax.yaxis.grid(True)
        if(i==0):
            plt.ylabel(SIDE[j])
        if (j == 0):
            ax.set_title(TITLE[i])

plt.suptitle("Error rate on simulation data set when number of taxa = 100, sequence length = 250")
#------------------------------------------
plt.show()
