import warnings
warnings.filterwarnings("ignore")

import numpy as np
import sys
sys.path.append('../')
import utils
import matplotlib.pyplot as plt
import os
import glob
import seaborn as sns
import matplotlib.patches as mpatches

def load_pearson(
                    experiment_name, test_shift, 
                    output_dir='../../data_PIONEER/',
                    surrogate_indexes=[41,42,43,44,45],
                    pioneer_cycles=['4'],
                    cycle_index='9',
                ):
    """
    Loads Pearson correlation coefficients from saved numpy files for different model surrogates
    Args:
        experiment_name: Name of the experiment
        test_shift: Type of distribution shift ('no_shift', 'small_shift', etc.)
        output_dir: Directory containing the data
        surrogate_indexes: List of surrogate model indices to load
        pioneer_cycles: List of PIONEER cycles to consider
        cycle_index: Specific cycle index to use
    Returns:
        List of Pearson correlation coefficients
    """
    pccs=[]
    for surrogate_index in surrogate_indexes:        
        pcc_per_al=[]
        for pioneer_cycle in pioneer_cycles:
            pcc_noshift_file=output_dir+"npy/"+utils.get_path(experiment_name)+"/PearsonR_model-"+str(surrogate_index)+".npy"
            pcc_file=output_dir+"npy/"+utils.get_path(experiment_name)+"/TestShiftPearsonR_"+test_shift+"_cycle-"+str(cycle_index)+"_model-"+str(surrogate_index)+".npy"
            if test_shift!='no_shift':
                pcc_per_al=np.load(pcc_file)
            else:
                pcc_per_al=np.array([np.load(pcc_noshift_file)[-1]])
        pccs.append(np.array(pcc_per_al[0])) 
    return pccs


if __name__=='__main__':
    # Set general plotting parameters
    general_fontsize=9 
    general_figsize=(5,7) 
    general_dpi=300 
    general_figureformat='pdf' 

    pioneer_cycles=['last']
    which_set='X_test'

    spacing=3

    plt.rcParams.update({'font.size': general_fontsize})

    output_dir='../../data_PIONEER/'

    # Iterate through two experimental cases: LentiMPRA and STARR-seq
    for case in ['LentiMPRA','STARR-seq']:
        fig = plt.figure(figsize=general_figsize) 
        
        # Create subplots for different acquisition functions and shift conditions
        for i_subpl,sub_plot in enumerate([
                        'Fig2D_Mutagenesis_NoShift_'+case, 
                        'Fig2D_Random_NoShift_'+case, 
                        'Fig2D_UGM_NoShift_'+case, 
                        'Fig2D_All_NoShift_'+case, 
                        
                        'Fig2D_Mutagenesis_SmallShift_'+case, 
                        'Fig2D_Random_SmallShift_'+case, 
                        'Fig2D_UGM_SmallShift_'+case, 
                        'Fig2D_All_SmallShift_'+case, 
                        
                        'Fig2D_Mutagenesis_LargeShiftHigh_'+case, 
                        'Fig2D_Random_LargeShiftHigh_'+case, 
                        'Fig2D_UGM_LargeShiftHigh_'+case, 
                        'Fig2D_All_LargeShiftHigh_'+case, 
                        
                        'Fig2D_Mutagenesis_LargeShiftLow_'+case,  
                        'Fig2D_Random_LargeShiftLow_'+case,  
                        'Fig2D_UGM_LargeShiftLow_'+case, 
                        'Fig2D_All_LargeShiftLow_'+case, 
                        
                        ]):
            ax = plt.subplot(4, 4, i_subpl + 1)  

            # Determine which test shift to use based on subplot name
            test_shifts=['no_shift','small_shift','large_shift_high','large_shift_low'] 
            if 'NoShift' in sub_plot:
                test_shifts=['no_shift']
                txtitle=['No shift']
            if 'SmallShift' in sub_plot:
                test_shifts=['small_shift']
                txtitle=['Small shift']
            if 'LargeShiftHigh' in sub_plot:
                test_shifts=['large_shift_high']
                txtitle=['Large shift (high)']
            if 'LargeShiftLow' in sub_plot:
                test_shifts=['large_shift_low']
                txtitle=['Large shift (low)']

            legend_lower=False

            xtickslist=[]
            voidxtickslist=[]
            for i_sq,test_shift in enumerate(test_shifts):
                # Get experiments for current plot
                experiments_of_plot=utils.get_experiments_for_plot(sub_plot)
                
                # Process each experiment
                for i_n, experiment_name in enumerate(experiments_of_plot):

                    cycle_index=4

                    infos=utils.get_plot_info(experiment_name,request=sub_plot)

                    xtickslist.append(infos['plotname'])
                    voidxtickslist.append('')
                    if experiment_name==experiments_of_plot[-1]:
                        for _ in range(spacing):
                            xtickslist.append('')
                            voidxtickslist.append('')

                    avgs={}
                    stds={}

                    test_set_index=51
                    if test_shift!='no_shift':
                        testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"
                    if not (test_shift!='no_shift' and len(glob.glob(testfile))==0):
                        nfiles=len(glob.glob(output_dir+"npy/"+utils.get_path(experiment_name)+"/TestShiftPearsonR_*npy"))
                        nfiles1=len(glob.glob(output_dir+"npy/"+utils.get_path(experiment_name)+"/PearsonR_model-*.npy"))

                        condition=False
                        if test_shift!='no_shift':
                            if nfiles==0:
                                condition=True
                        else:
                            if nfiles1<1:   
                                condition=True
                        if not condition:
                            for model_index in [0]:
                                pccs=[]
                                for surrogate_index in range(5):
                                    pcc_per_al=[]
                                    for pioneer_cycle in pioneer_cycles:
                                        pcc_noshift_file=output_dir+"npy/"+utils.get_path(experiment_name)+"/PearsonR_model-"+str(surrogate_index)+".npy"
                                        pcc_file=output_dir+"npy/"+utils.get_path(experiment_name)+"/TestShiftPearsonR_"+test_shift+"_cycle-"+str(cycle_index)+"_model-"+str(surrogate_index)+".npy"

                                        if test_shift!='no_shift':
                                            pcc_per_al=np.load(pcc_file)
                                            
                                        else:
                                            pcc_per_al=np.array([np.load(pcc_noshift_file)[-1]])

                                    pccs.append(np.array(pcc_per_al))

                                if True in [pcc[0]>0.95 for pcc in pccs]: 
                                    legend_lower=True
                                avgs[experiment_name],stds[experiment_name],any_outlier=utils.average_curve(pccs,no_outliers=False)
                        
                                # Create box plots and strip plots for the data
                                curr_idx=i_n+i_sq*(len(experiments_of_plot)+spacing) 
                                positions=np.arange(len(avgs[experiment_name]))+curr_idx

                                # Create visualization using seaborn
                                snsdata=np.array([pcc[0] for pcc in pccs])
                                ax_boxplot=sns.boxplot(x=[curr_idx]*len(snsdata),y=snsdata, color=infos['color'], native_scale=True) # seaborn version: 0.13.2
                                
                                # Add hatching patterns if specified
                                if infos['hatch']!='':
                                    for i_pat, patch in enumerate(ax_boxplot.patches):
                                        if i_pat==(len(ax_boxplot.patches)-1):
                                            patch.set_hatch(infos['hatch'])      
                                
                                # Add individual points on top of box plot
                                sns.stripplot(x=[curr_idx]*len(snsdata),y=snsdata, jitter=True, color='black', alpha=0.5, native_scale=True, size=3.0) # seaborn version: 0.13.2
                
                if 'LegNet_LentiMPRA' in experiment_name: 
                    genome_experiment_name='LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection'
                if 'DeepSTARR_STARR-seq' in experiment_name: 
                    genome_experiment_name='DeepSTARR_STARR-seq_Pool_generate-20000_final-20000_random-selection'
                av_pcc_genome=load_pearson(genome_experiment_name, test_shift, 
                        output_dir=output_dir, 
                        surrogate_indexes=range(5), 
                        pioneer_cycles=pioneer_cycles,
                        cycle_index=cycle_index,
                            )
                plt.plot(np.array([-0.5,len(experiments_of_plot)]),np.array(2*[np.mean(av_pcc_genome)]), color='red',linestyle='-.')


            if 'LargeShiftLow' in sub_plot:
                current_ticks=plt.xticks(np.array([i for i in range(len(xtickslist)) if xtickslist[i]!='']), 
                        [xtickslist[i] for i in range(len(xtickslist)) if xtickslist[i]!=''], 
                        rotation=45, ha='right')
            else:
                current_ticks=plt.xticks(np.array([i for i in range(len(xtickslist)) if xtickslist[i]!='']), 
                        ['' for i in range(len(xtickslist)) if xtickslist[i]!=''], 
                        rotation=45, ha='right')

            # Format plot appearance and add labels
            if 'Mutagenesis' in sub_plot:
                plt.ylabel("Pearson's r")
            else:
                plt.ylabel("")
                ax.set_yticklabels([])

            if 'All' in sub_plot:
                plt.text(2.7,0.82,txtitle[0],color='black', fontsize=general_fontsize, rotation='vertical') 

            if 'NoShift' in sub_plot:
                if 'Fig2D_Mutagenesis' in sub_plot: plt.text(0.0,0.99,'Mutagenesis',color='black', fontsize=general_fontsize) 
                if 'Fig2D_UGM' in sub_plot: plt.text(0.5,0.99,'UGM',color='black', fontsize=general_fontsize) 
                if 'Fig2D_Random' in sub_plot: plt.text(0.3,0.99,'Random',color='black', fontsize=general_fontsize) 
                if 'Fig2D_All' in sub_plot: plt.text(0.5,0.99,'All',color='black', fontsize=general_fontsize) 

            plt.xlim(-0.5,2.5)
            plt.ylim(0.775,0.975)
            if sub_plot=='initial': plt.ylim(0.3,0.975)

            # Create legend for different selection methods
            boxes = [
                ('Standard',''),
                ('Unc. Subselection','//'),
                ('Batch Selection','\\\\'),
                ('Deep Ensemble','|'),
                ]
            
            # Set legend position based on data
            if legend_lower:
                general_loc='lower center'
            else:
                general_loc='upper center'
            patches = [mpatches.Patch(label=label, hatch=hatch, facecolor='none', edgecolor='black') for label, hatch in boxes]
            
            # Remove top and right axis 
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

        # Save the figure
        fig.savefig(output_dir+'Fig2-D_'+case+'.'+general_figureformat, format=general_figureformat, dpi=general_dpi, bbox_inches='tight')
        print("DONE:",output_dir+'Fig2-D_'+case+'.'+general_figureformat)
        fig=plt.clf()

print("SCRIPT END.")
