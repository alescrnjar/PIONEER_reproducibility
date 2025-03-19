import os
import numpy as np
import torch
import h5py

if __name__=='__main__':
    # Define the different types of shifts to test
    test_shifts=['no_shift','small_shift','large_shift_low','large_shift_high']
    
    # Set the device to GPU if available, otherwise use CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Define the pioneer cycles to be used in the analysis
    pioneer_cycles=['4']

    #####

    # Specify the output directory for saving results
    output_dir='../../data_PIONEER/'

    for i_sq,test_shift in enumerate(test_shifts):
        for case in ['LentiMPRA','STARR-seq']:
            testfile=output_dir+"TestShiftData_"+case+"_"+test_shift+".h5"
            if os.path.isfile(testfile) and test_shift!='no_shift':
                if test_shift!='no_shift':
                    testdata=h5py.File(testfile, 'r') 
                    X_ood=torch.tensor(np.array(testdata['X_test']))
                    Xs=X_ood 
                    y_ood_gt=torch.tensor(np.array(testdata['Y_test'])).numpy()

                for  surrogate_index in range(5):
                    for pioneer_cycle in pioneer_cycles:
                        testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"
                        data = h5py.File(testfile, 'r')
                        y_ood_gt=np.array(data['Y_test']).squeeze(1)
                        # Create a histogram of the ground truth labels
                        hist,bin_edges=np.histogram(y_ood_gt, bins=100, range=[-5.,12.], density=False) 
                        bin_centers=[]
                        for i in range(len(bin_edges)-1):
                            bin_centers.append((bin_edges[i]+bin_edges[i+1])/2)
                        bin_centers=np.array(bin_centers)
                        np.save(output_dir+"/npy/oracles/oracle_activity_histogram_"+test_shift+".npy",hist)
                        np.save(output_dir+"/npy/oracles/oracle_bins_histogram_"+test_shift+".npy",bin_centers)

    print("SCRIPT END.")

