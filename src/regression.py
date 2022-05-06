# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:02:05 2020

@author: lrass

Added several lines of comments and organized into classes to improve readability.
Everything else was my first foray into programming.
"""

from msilib.schema import Class
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd

def main():
    df = FileRead.read_csv_()
    x, y, model = BuildModel.model_build(df)
    vif = BuildModel.vif_testing(df)
    Display.display_results(x, y, model)
    Display.display_vif(x, vif)

class FileRead:
    #this class handles reading csv files
        def read_csv_():
            #this method will read a specific, predetermined file and create a dataframe
            file_name =  'lag2per.csv'
            dat = pd.read_csv(file_name)
            df = pd.DataFrame(dat)
    
            for i in df:
                print(df[i].describe())
                print('---------------------')
            return df
     
class BuildModel:
        #this class contains all modeling operations for the regression    
        def model_build(df):
            #this function builds all components of a regression model for a predetermined data set
            x = df[["Rent_PI_lag2","Rent_PI_lag3","PCPI","PCPI_lag1","PCPI_lag2","UER","UER_lag1","UER_lag2","NPHU","NPHU_lag1","NPHU_lag2","GDP","GDP_lag1","GDP_lag2"]]
            y = df["Rent_PI_dif"]
            x = sm.add_constant(x)
            model = sm.OLS(y,x).fit()
            predictions = model.predict(x)
            return x, y, model

        def vif_testing(x, df):
            vif = pd.DataFrame()
            vif["VIF Factor"] = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
            vif["features"] = x.columns
            return vif

class Display:
    def display_results(x , y , model):
        #this class handles displaying components of the model
        summary = model.summary()
        print('Dependent variables included:')
        for i in x:
            print(i)
            print(summary)
            print('------------------')
        adf,pval,usedlag,nobs,cv,icbest = sm.tsa.stattools.adfuller(y, maxlag=None, regression='ct', autolag='AIC', store=False, regresults=False)
        print('adf=%f' % adf)
        print('pvalue=%f' % pval)
        print('num of lags=%d' % usedlag)
        print('num of obs=%d' % nobs)
        print('crit values=',cv)
        print('-----------------')
        
    def display_vif(vif):
            #this method displays the vif test
            print("vif test")
            print(vif)
            
#TODO organize print statements into a Display Class     
main()