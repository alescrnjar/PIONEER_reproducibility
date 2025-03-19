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
    general_fontsize=9 
    general_figsize=(4.5,2) 
    general_dpi=300 
    general_figureformat='pdf' 

    spacing=3

    pioneer_cycles=['last']

    plt.rcParams.update({'font.size': general_fontsize})

    output_dir='../../data_PIONEER/'

    for case in ['LentiMPRA','STARR-seq']:
        fig = plt.figure(figsize=general_figsize) 
        for i_subpl,sub_plot in enumerate([
                        'SuppFig4_NoShift_'+case, 'SuppFig4_SmallShift_'+case, 'SuppFig4_LargeShiftHigh_'+case, 'SuppFig4_LargeShiftLow_'+case, 
                        ]):
            ax = plt.subplot(1, 4, i_subpl + 1)  

            test_shifts=['no_shift','small_shift','large_shift_high','large_shift_low'] 

            if 'NoShift' in sub_plot:
                test_shifts=['no_shift']
                txtitle=['No shift']
            if 'SmallShift' in sub_plot:
                test_shifts=['small_shift']
                txtitle=['Small shift']
            if 'LargeShiftHigh' in sub_plot:
                test_shifts=['large_shift_high']
                txtitle=['Large shift\n(high)']
            if 'LargeShiftLow' in sub_plot:
                test_shifts=['large_shift_low']
                txtitle=['Large shift\n(low)']

            legend_lower=False

            vertical_lines=[]

            xtickslist=[]
            voidxtickslist=[]
            for i_sq,test_shift in enumerate(test_shifts):

                experiments_of_plot=utils.get_experiments_for_plot(sub_plot)
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

                    if test_shift!='no_shift':
                        testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"
                    if not (test_shift!='no_shift' and len(glob.glob(testfile))==0):
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
                    
                            curr_idx=i_n+i_sq*(len(experiments_of_plot)+spacing) 
                            positions=np.arange(len(avgs[experiment_name]))+curr_idx
                                
                            snsdata=np.array([pcc[0] for pcc in pccs])
                            ax_boxplot=sns.boxplot(x=[curr_idx]*len(snsdata),y=snsdata, color=infos['color'], native_scale=True) # seaborn version: 0.13.2
                            if infos['hatch']!='':
                                for i_pat, patch in enumerate(ax_boxplot.patches):
                                    if i_pat==(len(ax_boxplot.patches)-1):
                                        patch.set_hatch(infos['hatch'])      
                            sns.stripplot(x=[curr_idx]*len(snsdata),y=snsdata, jitter=True, color='black', alpha=0.5, native_scale=True, size=3.0) # seaborn version: 0.13.2
                
                                    
            current_ticks=plt.xticks(np.array([i for i in range(len(xtickslist)) if xtickslist[i]!='']), 
                        [xtickslist[i] for i in range(len(xtickslist)) if xtickslist[i]!=''], 
                        rotation=45, ha='right')

            outfile=sub_plot+'.'+general_figureformat
            if 'NoShift' in sub_plot:
                plt.ylabel("Pearson's r")
            else:
                plt.ylabel("")
                ax.set_yticklabels([])
            

            plt.ylim(0.845,0.975)
            if sub_plot=='initial': plt.ylim(0.3,0.975)
            text_positions=[(0.5*len(experiments_of_plot)-0.5+i_sq*(len(experiments_of_plot)+spacing)) for i_sq in range(len(test_shifts))]    # text_positions=[1.5, 8.5, 15.5]      
            text_positions=[(0.5*len(experiments_of_plot)-0.5+i_sq*(len(experiments_of_plot)+spacing)-1.5-1.0*(i_sq)) for i_sq in range(len(test_shifts))] 
            if 'Price' in sub_plot: text_positions=[-1.0, 6.0, 14.0, 20.0]
            if 'method-mutation' in sub_plot: text_positions=[-1.0, 5.5, 13.0, 21.0]
            if 'method-UGM' in sub_plot: text_positions=[-1.0, 5.5, 13.0, 21.0]
            if 'method-RandomSeq' in sub_plot: text_positions=[-1.0, 5.5, 13.0, 21.0]
            if 'method-All' in sub_plot: text_positions=[-1.0, 5.0, 11.0, 17.5]
            if 'PanelG' in sub_plot: text_positions=[0.6]

            plt.title(txtitle[0],{'fontsize':general_fontsize})
            
            for vl in vertical_lines:
                plt.vlines(vl['x'],ymin=0.0,ymax=1.0, color='black')

            if 'Price' not in sub_plot:
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
        fig.savefig(output_dir+'SuppFig4_'+case+'.'+general_figureformat, format=general_figureformat, dpi=general_dpi, bbox_inches='tight')
        print("DONE:",output_dir+'SuppFig4_'+case+'.'+general_figureformat)
        plt.clf()

print("SCRIPT END.")
