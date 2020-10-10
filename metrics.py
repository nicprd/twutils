from tensorflow.keras.callbacks import Callback
from sklearn.metrics import classification_report
import numpy as np

import matplotlib.pyplot as plt

class logger(Callback):
    
    def __init__(self, training, test):
        super(Callback,self).__init__()
        self.training = training
        self.test = test

        self.training_ev = []
        self.test_ev = []

    def on_epoch_end(self,epoch,logs={}):
        tpred = self.model.predict(self.training[0]).round()
        epred = self.model.predict(self.test[0]).round()

        trep = classification_report(tpred,self.training[1],output_dict=True)
        erep = classification_report(epred,self.test[1],output_dict=True)

        self.training_ev.append([epoch,trep["macro avg"]["f1-score"]])
        self.test_ev.append([epoch,erep["macro avg"]["f1-score"]])

        print(f"[{epoch}]training score: {self.training_ev[-1][1]:.2f}%; ev score {self.test_ev[-1][1]:.2f}")
    
    def plot_evolution(self):

        fig, ax = plt.subplots()

        ax.plot( (tr:=np.array(self.training_ev))[:,0],
                 tr[:,1])
        ax.plot( (ev:=np.array(self.test_ev))[:,0],
                 ev[:,1])

        ax.set( title = "evolución de f1" ) 

        return ax

    


















