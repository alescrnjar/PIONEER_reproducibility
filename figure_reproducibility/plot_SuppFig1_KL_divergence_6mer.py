import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    general_fontsize=9 
    general_figsize=(3,3) 
    general_dpi=300 
    general_figureformat='pdf' 

    #####

    output_dir='../../data_PIONEER/'
    
    test_shifts=['small_shift','large_shift_low','large_shift_high']

    test_shift_colors={
        'STANDARD':'black',
        'small_shift':'#ffae00ff',
        'no_shift':'grey',
        'large_shift_low':'C3',
        'large_shift_high':'C2',
    }
    test_shift_labels={
        'STANDARD':'Train Distribution',
        'no_shift':'No shift', #'Held out test data',
        'small_shift':'Small shift', #'5% Mutagenesis',
        'large_shift_low':'Large shift (low)', #'Random Sequences',
        'large_shift_high':'Large shift (high)', #'Random-Evolve',
    }

    system_title={'LentiMPRA': 'lentiMPRA (K562)', 'DeepSTARR': 'STARR-seq (Dev)'}

    plt.rcParams.update({'font.size': general_fontsize})

    for case in ['LentiMPRA','STARR-seq']:

        fig=plt.figure(1, figsize=general_figsize)

        plt.ylabel('6-mer KL Divergence') 

        for i_sq,test_shift in enumerate(test_shifts):

            testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"

            surrogate_index=41
            kldiv_file=output_dir+"npy/oracles/"+"/KLdiv_6mer_"+test_shift+"_model-"+str(surrogate_index)+".npy"

            yaxis=np.load(kldiv_file)
            xaxis=np.array([i_sq])
                
            general_color=test_shift_colors[test_shift]
            general_label=test_shift_labels[test_shift]
            plt.bar(xaxis,yaxis,color=general_color, lw=2, label=general_label) 

        plt.xticks(np.arange(3),['Small shift','Large shift (low)','Large shift (high)'], rotation=45, ha='right')

        filename='SuppFig1_Kmer6KL_tests_'+case+'.'+general_figureformat

        plt.title(system_title[case])
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        fig.savefig(output_dir+filename,dpi=general_dpi,bbox_inches='tight')
        print("DONE:",output_dir+filename)
        plt.clf()


    print("SCRIPT DONE.") 

