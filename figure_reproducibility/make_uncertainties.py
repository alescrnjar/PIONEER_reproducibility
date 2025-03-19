import warnings
warnings.filterwarnings("ignore")
import numpy as np

import h5py
import torch
import os
import utils
import math

from pioneer-nn import uncertainty, surrogate, predictor

import sys
sys.path.append('./Models/')
import pytorchlightning_models

if __name__=='__main__':

    myfontsize=9 
    myfigsize=(3,3) 
    mydpi=300 
    myfigureformat='pdf' 

    pioneer_cycles=['initial','0','1','2','3','4']
    surrogate_indexes=[41,42,43,44,45]

    output_dir='../../data_PIONEER/'

    batch_size=100

    uncertainty = uncertainty.MCDropout(n_samples=5)

    for case in ['K562','STARR-seq']:
        sub_plot='SuppFig3_'+case
        
        experiments_of_plot=utils.get_experiments_for_plot(sub_plot)
        for i_n, experiment_name in enumerate(experiments_of_plot):
            
            for model_index in [0]:
                for i_f,surrogate_index in enumerate(surrogate_indexes):

                    for i_pioneer,pioneer_cycle in enumerate(pioneer_cycles):

                        if os.path.isdir(output_dir+experiment_name):
                            if pioneer_cycle=='initial':
                                input_h5_file=output_dir+experiment_name+"/initial_train_dataset.h5" 
                            else:
                                input_h5_file=output_dir+experiment_name+"/proposed_cycle-"+str(pioneer_cycle)+"_model-"+str(surrogate_index)+".h5"
                            data = h5py.File(input_h5_file, 'r')
                            Xs=torch.tensor(np.array(data['X_train']))
                            Ys=np.array(data['Y_train'])
                            
                            if pioneer_cycle!='initial':

                                if case=='K562': Surrogate_Model = pytorchlightning_models.PL_LegNet_Custom(input_h5_file=input_h5_file)
                                if case=='STARR-seq': Surrogate_Model = pytorchlightning_models.PL_LegNet_Custom(input_h5_file=input_h5_file)
                                Surrogate_Model=Surrogate_Model.load_from_checkpoint(ckpt_file=output_dir+experiment_name+'/weights_cycle-'+str(pioneer_cycle)+'_model-'+str(surrogate_index)+'.ckpt', 
                                                                                    input_h5_file=input_h5_file)  
        
                                wrapper = surrogate.ModelWrapper(Surrogate_Model, predictor, uncertainty) 
                                
                                uncertainties=np.empty(0)
                                #predictions=np.empty(0)
                                for xbatch in np.array_split(Xs, math.ceil(len(Xs)/batch_size)):
                                    unc_x = wrapper.uncertainty(xbatch)
                                    preds_x = wrapper.predict(xbatch)
                                    uncertainties=np.concatenate((uncertainties,unc_x.detach().cpu().numpy()),axis=0)
                                    #predictions=np.concatenate((predictions,preds_x_.detach().cpu().numpy()),axis=0)

                                np.save(output_dir+'/npy/'+utils.get_path(experiment_name)+"/uncertainty-of-proposed_cycle-"+str(pioneer_cycle)+"_model-"+str(surrogate_index)+".npy",np.array(uncertainties)) 

    print("SCRIPT END.")
