import warnings
warnings.filterwarnings("ignore")

import numpy as np
import utils
import matplotlib.pyplot as plt
import os
import glob
import seaborn as sns
import matplotlib.patches as mpatches


if __name__=='__main__':
    # Set general plotting parameters
    general_fontsize=9 
    general_figsize=(7,2.5) 
    general_dpi=300 
    general_figureformat='pdf' 

    # Spacing between groups in the plot
    spacing=3

    # Only using the last cycle for analysis
    pioneer_cycles=['last']

    plt.rcParams.update({'font.size': general_fontsize})
    output_dir='../../data_PIONEER/'

    # Define different types of covariate shifts to test
    test_shifts=['no_shift','small_shift','large_shift_high','large_shift_low'] 
    shift_titles={'no_shift':'No shift',  'small_shift':'Small shift',   'large_shift_high':'Large shift (high)','large_shift_low':'Large shift (low)'}

    # Create plots for both LentiMPRA and STARR-seq datasets
    for case in ['LentiMPRA','STARR-seq']:
        fig = plt.figure(figsize=general_figsize) 
        
        # Create subplots for different experimental conditions
        for i_subpl,sub_plot in enumerate([
                        'Fig2B_Genome_'+case,  # Genomic sequences
                        'Fig2B_Mutagenesis_'+case,  # Mutagenesis experiments
                        'Fig2B_Random_'+case,  # Random sequences
                        'Fig2B_UGM_'+case,  # Uncertainty-guided mutagenesis
                        'Fig2B_All_'+case,  # Combined analysis
                        ]):
            
            ax = plt.subplot(1, 5, i_subpl + 1) 

            txtitle=['']
            if 'Fig2B' in sub_plot: txtitle=['Genome','Mutagenesis','Random','UGM','All']
            if 'Fig2B' in sub_plot and 'UGM' in sub_plot: txtitle=['UGM']
            if 'Fig2B' in sub_plot and 'Mutagenesis' in sub_plot: txtitle=['Mutagenesis']
            if 'Fig2B' in sub_plot and 'Random' in sub_plot: txtitle=['Random']
            if 'Fig2B' in sub_plot and 'Genome' in sub_plot: txtitle=['Genome']
            if 'Fig2B' in sub_plot and 'All' in sub_plot: txtitle=['All']

            legend_lower=False

            vertical_lines=[]

            xtickslist=[]
            voidxtickslist=[]

            # Process each experiment in the plot
            experiments_of_plot=utils.get_experiments_for_plot(sub_plot)
            for i_n, experiment_name in enumerate(experiments_of_plot):
                # Test each type of covariate shift
                for i_sq,test_shift in enumerate(test_shifts):

                    cycle_index=4
                    infos=utils.get_plot_info(experiment_name,request=sub_plot)

                    # Build x-axis labels with spacing between groups
                    xtickslist.append(shift_titles[test_shift])
                    voidxtickslist.append('')
                    if test_shift==test_shifts[-1]:
                        for _ in range(spacing):
                            xtickslist.append('')
                            voidxtickslist.append('')
                    
                    # Calculate performance metrics
                    avgs={}
                    stds={}
                    if test_shift!='no_shift':
                        testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"
                    
                    # Only process if test data exists
                    if not (test_shift!='no_shift' and len(glob.glob(testfile))==0):
                        for model_index in [0]:
                            # Collect Pearson correlation coefficients across surrogate models
                            pccs=[]
                            for surrogate_index in range(5):
                                pcc_per_al=[]
                                for pioneer_cycle in pioneer_cycles:
                                    # Load correlation coefficients for no-shift and shift conditions
                                    pcc_noshift_file=output_dir+"npy/"+utils.get_path(experiment_name)+"/PearsonR_model-"+str(surrogate_index)+".npy"
                                    pcc_file=output_dir+"npy/"+utils.get_path(experiment_name)+"/TestShiftPearsonR_"+test_shift+"_cycle-"+str(cycle_index)+"_model-"+str(surrogate_index)+".npy"
                                    
                                    if test_shift!='no_shift':
                                        pcc_per_al=np.load(pcc_file)
                                    else:
                                        pcc_per_al=np.array([np.load(pcc_noshift_file)[-1]])

                                pccs.append(np.array(pcc_per_al))

                            # Adjust legend position if high correlation detected
                            if True in [pcc[0]>0.95 for pcc in pccs]: 
                                legend_lower=True
                                
                            # Calculate average performance and create box plots
                            avgs[test_shift],stds[test_shift],any_outlier=utils.average_curve(pccs,no_outliers=False)
                            curr_idx=i_sq+i_n*(len(test_shifts)+spacing) 
                                
                            # Create box and strip plots for the data
                            snsdata=np.array([pcc[0] for pcc in pccs])
                            ax_boxplot=sns.boxplot(x=[curr_idx]*len(snsdata),y=snsdata, color=infos['color'], native_scale=True)
                            if infos['hatch']!='':
                                for i_pat, patch in enumerate(ax_boxplot.patches):
                                    if i_pat==(len(ax_boxplot.patches)-1):
                                        patch.set_hatch(infos['hatch'])      
                            sns.stripplot(x=[curr_idx]*len(snsdata),y=snsdata, jitter=True, color='black', alpha=0.5, native_scale=True, size=3.0) 

            current_ticks=plt.xticks(np.array([i for i in range(len(xtickslist)) if xtickslist[i]!='']), 
                        [xtickslist[i] for i in range(len(xtickslist)) if xtickslist[i]!=''], 
                        rotation=45, ha='right')
            
            if not ('Fig2B_UGM' in sub_plot or 'Fig2B_All' in sub_plot or 'Fig2B_Random' in sub_plot or 'Fig2B_Mutagenesis' in sub_plot):
                plt.ylabel("Pearson's r")
            else:
                plt.ylabel("")
                ax.set_yticklabels([])
            
            plt.ylim(0.775,0.975)
            if sub_plot=='initial': plt.ylim(0.3,0.975)
            text_positions=[(0.5*len(experiments_of_plot)-0.5+i_sq*(len(experiments_of_plot)+spacing)) for i_sq in range(len(test_shifts))]  
            text_positions=[(0.5*len(experiments_of_plot)-0.5+i_sq*(len(experiments_of_plot)+spacing)-1.5-1.0*(i_sq)) for i_sq in range(len(test_shifts))] 
            if 'Fig2B' in sub_plot: text_positions=[1.0]
            if 'Fig2B' in sub_plot and ('UGM' in sub_plot or 'All' in sub_plot): text_positions=[1.5]
            if sub_plot=='Fig2B_LentiMPRA' or sub_plot=='Fig2B_STARR-seq': text_positions=[-1.0, 5.0, 14.0, 21.0, 30.0]
            
            text_y=0.98
            for itx in range(len(txtitle)):
                plt.text(text_positions[itx],text_y,txtitle[itx],color='black', fontsize=general_fontsize)
           
            for vl in vertical_lines:
                plt.vlines(vl['x'],ymin=0.0,ymax=1.0, color='black')

            boxes = [
                ('Standard',''),
                ('Unc. Subselection','//'),
                ('Batch Selection','\\\\'),
                ('Deep Ensemble','|'),
                ]
            if legend_lower:
                general_loc='lower center'
            else:
                general_loc='upper center'
            patches = [mpatches.Patch(label=label, hatch=hatch, facecolor='none', edgecolor='black') for label, hatch in boxes]
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        fig.savefig(output_dir+'Fig2-B_'+case+'.'+general_figureformat, format=general_figureformat, dpi=general_dpi, bbox_inches='tight')

        print("DONE:",output_dir+'Fig2-B_'+case+'.'+general_figureformat)
        fig=plt.clf()

print("SCRIPT END.")
