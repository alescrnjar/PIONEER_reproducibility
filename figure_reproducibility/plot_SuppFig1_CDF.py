import warnings
warnings.filterwarnings("ignore")

import numpy as np
import utils
import matplotlib.pyplot as plt
import os

if __name__=='__main__':

    general_fontsize=9 
    general_figsize=(3,3) 
    general_dpi=300 
    general_figureformat='pdf' 

    normalize=True 

    cdf_wanted=True

    #####

    output_dir='../../data_PIONEER/'
    
    test_shifts=['no_shift','small_shift','large_shift_low','large_shift_high']

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
        if 'STARR-seq' in case:
            plt.xlim(-1.5,5.0)
        else:
            plt.xlim(-1.5,2.5)
        if not normalize:
            ylim=2000 
        else:
            ylim=0.21 
            if cdf_wanted:
                ylim=1.1

        plt.xlabel('Oracle CRE Activity') 
        
        plt.ylim(0,ylim)
        if not normalize:
            plt.ylabel('Frequency')
        else:
            plt.ylabel('Frequency')
            if cdf_wanted:
                plt.ylabel('Cumulative Distribution Function')

        for i_sq,test_shift in enumerate(test_shifts):
            testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"

            for pioneer_cycle in ['4']: 
                lists={'histogram':[],'bins':[]}
                avs={}
                stds={}
                any_outlier={}
                for what_file in ['histogram','bins']:
                    files=[output_dir+"npy/oracles/"+'oracle_activity_'+what_file+'_'+test_shift+'.npy']

                    for file in files: 
                        
                        if test_shift=='STANDARD':
                            toappend=np.load(output_dir+'/'+file)
                        else:
                            toappend=np.load(file)

                        if normalize and what_file=='histogram':
                            if not cdf_wanted:
                                lists[what_file].append(toappend/np.sum(toappend))
                            else:
                                lists[what_file].append(np.cumsum(toappend/np.sum(toappend)))
                        else:
                            lists[what_file].append(toappend)
                    avs[what_file],stds[what_file],any_outlier[what_file]=utils.average_curve(lists[what_file],no_outliers=False)
                
                xaxis=avs['bins']
                yaxis=avs['histogram']
                ystd=stds['histogram']
                
                if pioneer_cycle=='initial':
                    general_color='C0'
                    general_label='Initial'
                else:
                    general_color=test_shift_colors[test_shift]
                    general_label=test_shift_labels[test_shift]
                plt.plot(xaxis,yaxis,color=general_color, lw=2, label=general_label)  
                plt.fill_between(xaxis, yaxis-ystd, yaxis+ystd, alpha=0.5, color=general_color)  

        filename='SuppFig1_CDF_OracleActivity_'+case+'.'+general_figureformat 
        plt.legend(loc='lower right',prop={'size':general_fontsize},frameon=False,markerfirst=False, alignment='right') 

        plt.title(system_title[case])
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        fig.savefig(output_dir+filename,dpi=general_dpi,bbox_inches='tight')
        print("DONE:",output_dir+filename)
        plt.clf()

    print("SCRIPT DONE.")
