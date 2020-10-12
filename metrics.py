from tensorflow.keras.callbacks import Callback
from sklearn.metrics import classification_report
import numpy as np

import matplotlib.pyplot as plt

class logger(Callback):
    
    def __init__(self, training, test):
        super(Callback,self).__init__()
        self.training = training
        self.test = test

        self.training_ev = np.empty((0,2))
        self.test_ev = np.empty((0,2))

    def on_epoch_end(self,epoch,logs={}):
        tpred = self.model.predict(self.training[0]).round().astype(int)
        epred = self.model.predict(self.test[0]).round().astype(int)

        trep = classification_report(tpred,self.training[1],output_dict=True)
        erep = classification_report(epred,self.test[1],output_dict=True)

        self.training_ev = np.vstack((self.training_ev,[epoch,trep["macro avg"]["f1-score"]]))
        self.test_ev = np.vstack((self.test_ev,[epoch,erep["macro avg"]["f1-score"]]))

        print(f"[{epoch}]training score: {self.training_ev[-1][1]:.2f}%; ev score {self.test_ev[-1][1]:.2f}")
    
    def plot_evolution(self):

        fig, ax = plt.subplots()

        ax.plot( self.training_ev[:,0],
                 self.training_ev[:,1])

        ax.plot( self.test_ev[:,0],
                 self.test_ev[:,1])

        ax.set( title = "evolución de f1" ) 

        return ax

    


















