from PL_Models import *
import matplotlib.pyplot as plt
import os
import utils


if __name__=='__main__':

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    pioneer_cycles=[4]
    surrogate_indexes=range(5)

    #####

    output_dir='../../data_PIONEER/'

    test_shifts=['no_shift','small_shift','large_shift_high','large_shift_low'] 

    experiment_names=utils.get_experiments_for_plot('all')

    for experiment_name in experiment_names:
        if 'LentiMPRA' in experiment_name: case='LentiMPRA'
        if 'STARR-seq' in experiment_name: case='STARR-seq'
        for test_shift in test_shifts:
            testfile=output_dir+"TestShiftData_"+case+"_"+test_shift+".h5"
            if test_shift=='no_shift':
                testfile=output_dir+experiment_name+'/initial_train_dataset.h5' #pristine's X_test will be the in-distribution.
            
            if os.path.isfile(output_dir+testfile):
                testdata=h5py.File(output_dir+testfile, 'r') 
                X_test=torch.tensor(np.array(testdata['X_test']))
                y_test=np.array(testdata['Y_test'])

                for surrogate_index in surrogate_indexes:
                    for pioneer_cycle in pioneer_cycles:
                        ckpt_file=output_dir+experiment_name+'/weights_cycle-'+str(pioneer_cycle)+'_model-'+str(surrogate_index)+'.ckpt'

                        model=eval('PL_'+chosen_model+'(input_h5_file="'+testfile+'",initial_ds=True)')
                        model = model.load_from_checkpoint(ckpt_file, input_h5_file=testfile)
                        model=model.to(device)
                        pred=model.predict_custom(X_test.to(device))
                        metrics=model.metrics(pred, y_test)
                        
                        pcc_file=output_dir+experiment_name+"/TestShiftPearsonR_"+test_shift+"_cycle-"+str(pioneer_cycle)+"_model-"+str(surrogate_index)+".npy"
                        np.save(pcc_file,metrics['PCC']) 
                        print("DONE:",pcc_file)
                        
                        # pred_file=output_dir+experiment_name+"/TestShiftPredictions_"+test_shift+"_cycle-"+str(cycle_index)+"_model-"+str(surrogate_index)+".npy"
                        # np.save(predf,pred) 
                        # print("DONE:",pred_file)
                        
                        # gt_file=output_dir+experiment_name+"/TestShiftGroundTruths_"+test_shift+"_cycle-"+str(cycle_index)+"_model-"+str(surrogate_index)+".npy"
                        # np.save(gt_file,y_test) 
                        # print("DONE:",gt_file)

    print("SCRIPT END.")

