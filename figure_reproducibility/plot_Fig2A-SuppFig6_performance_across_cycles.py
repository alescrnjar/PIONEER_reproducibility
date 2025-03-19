import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import utils
from typing import Tuple, List, Any

def load_experiment_data(experiment_name: str, input_dir: str) -> Tuple[np.ndarray, np.ndarray]:
    """Load average and standard deviation data for an experiment."""
    base_path = f"{input_dir}/npy/{utils.get_path(experiment_name)}/PearsonR"
    avg = np.load(f"{base_path}_average.npy")
    std = np.load(f"{base_path}_std.npy")
    return np.squeeze(avg), np.squeeze(std)

def create_performance_plot(
    plot_name: str,
    experiment_names: List[str],
    y_range: Tuple[float, float],
    input_dir: str,
    output_path: str,
    title: str = "Performance across cycles",
    figsize: Tuple[int, int] = (3, 3),
    fontsize: int = 9,
    dpi: int = 300
) -> None:
    """Create a performance plot for multiple experiments."""
    
    plt.figure(figsize=figsize)
    plt.rcParams.update({'font.size': fontsize})

    # Plot each experiment
    for experiment_name in experiment_names:
        infos=utils.get_plot_info(experiment_name,request=plot_name)
        label=infos['plotname']
        color=infos['color']
        avg, std = load_experiment_data(experiment_name, input_dir)
        x = np.arange(len(avg))
        
        plt.plot(x, avg, color=color, lw=1, label=label)
        plt.scatter(x, avg, color=color, lw=1, s=8)
        plt.fill_between(x, avg - std, avg + std, alpha=0.5, color=color)

    # Customize plot
    plt.xlabel('Cycle')
    plt.ylabel("Pearson's r")
    plt.title(title, fontsize=fontsize)
    plt.legend(loc='lower right', prop={'size': fontsize}, frameon=False, 
              markerfirst=False, alignment='right')
    plt.ylim(y_range)
    plt.xticks(np.arange(6))

    # Remove top and right spines
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Save plot
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight')
    print("DONE:",output_path)
    plt.close()

def main():
    # Define experiment configurations
    EXPERIMENTS = { 
    'PCC_4Methods_LentiMPRA':{'y_range':(0.75,0.98),'experiment_names':['LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection',
                                                                'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection',
                                                                'LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection',
                                                                'LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection',
                                                                'LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection']},
    'PCC_4Methods_STARR-seq':{'y_range':(0.65,0.98),'experiment_names':['DeepSTARR_STARR-seq_Pool_generate-20000_final-20000_random-selection',
                                                                'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection',
                                                                'DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection',
                                                                'DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection',
                                                                'DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection']},
    'SI_Single_VS_EnsembleOracle':{'y_range':(0.75,0.98),'experiment_names':["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection_SingleOracle",
                                                                          "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection"]},
    'SI_MCDropout_VS_DeepEnsemble':{'y_range':(0.75,0.98),'experiment_names':["LegNet_LentiMPRA_UGM-DeepEnsemble-rate-5_generate-20000_final-20000_random-selection",
                                                                           "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection"]},
    'SI_5-10-25perc_UGM':{'y_range':(0.75,0.98),'experiment_names':["LegNet_LentiMPRA_UGM-rate-25_generate-20000_final-20000_random-selection",
                                                                 "LegNet_LentiMPRA_UGM-rate-10_generate-20000_final-20000_random-selection",
                                                                 "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection"]},
    'SI_5-10-25perc_Mut':{'y_range':(0.75,0.98),'experiment_names':["LegNet_LentiMPRA_Mutagenesis-rate-25_generate-20000_final-20000_random-selection",
                                                                 "LegNet_LentiMPRA_Mutagenesis-rate-10_generate-20000_final-20000_random-selection",
                                                                 "LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection"]},  
    }


    input_dir = '../../data_PIONEER'
    output_dir = '../../data_PIONEER'

    
    # Create plots for each experiment
    for plot_name, config in EXPERIMENTS.items():
        output_path = f"{input_dir}/PearsonsR_over_cycles_{plot_name}.pdf"
        
        create_performance_plot(
            plot_name=plot_name,
            experiment_names=config['experiment_names'],
            y_range=config['y_range'],
            input_dir=input_dir,
            output_path=output_path
        )

if __name__ == '__main__':
    main()