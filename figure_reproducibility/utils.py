import numpy as np



paths={
        'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection':'LentiMPRA/Main/Mutagenesis_random-selection',
        'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection':'LentiMPRA/Main/Mutagenesis_uncertainty-selection',
        'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection':'LentiMPRA/Main/Mutagenesis_LCMD-selection', 
        #
        'LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection':'LentiMPRA/Main/Genome_random-selection',
        #
        'LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection':'LentiMPRA/Main/UGM_random-selection',
        'LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection':'LentiMPRA/Main/UGM_LCMD-selection', 
        #
        'LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection':'LentiMPRA/Main/Random_random-selection',
        'LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection':'LentiMPRA/Main/Random_uncertainty-selection',
        'LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection':'LentiMPRA/Main/Random_LCMD-selection', 
        #
        'LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection':'LentiMPRA/Main/All_random-selection',
        'LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection':'LentiMPRA/Main/All_LCMD-selection',  

        'LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection':'LentiMPRA/SI/FairCost_Random_random-selection', 
        'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection':'LentiMPRA/SI/FairCost_Mutagenesis_random-selection', 
        'LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection':'LentiMPRA/SI/FairCost_All_random-selection',

        #SI:
        'LegNet_LentiMPRA_UGM-DeepEnsemble-rate-5_generate-20000_final-20000_random-selection':'LentiMPRA/SI/UGM-DeepEnsemble_random-selection',
        'LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection_SingleOracle':'LentiMPRA/SI/UGM-SingleOracle_random-selection',
        'LegNet_LentiMPRA_UGM-rate-10_generate-20000_final-20000_random-selection':'LentiMPRA/SI/UGM-rate10_random-selection',
        'LegNet_LentiMPRA_UGM-rate-25_generate-20000_final-20000_random-selection':'LentiMPRA/SI/UGM-rate25_random-selection',
        'LegNet_LentiMPRA_Mutagenesis-rate-10_generate-20000_final-20000_random-selection':'LentiMPRA/SI/Mutagenesis-rate10_random-selection',
        'LegNet_LentiMPRA_Mutagenesis-rate-25_generate-20000_final-20000_random-selection':'LentiMPRA/SI/Mutagenesis-rate25_random-selection',
        }
        
def get_path(experiment_name):
    if 'STARR-seq' in experiment_name:
        return paths[experiment_name.replace('DeepSTARR_STARR-seq','LegNet_LentiMPRA')].replace('LentiMPRA/','STARR-seq/')
    else:
        return paths[experiment_name]

def all_paths():
    return paths.values()

def get_plot_info(experiment_name,request=''):
    hatch=''

    if experiment_name in ['LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection',      'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection',      
                'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection',      'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-100000_random-selection',     
                ]:
        plottitle='Mutagenesis' 
        mycolor='#ffae00ff'
    if experiment_name in ['LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection',      'LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection',        
                'DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection',     'DeepSTARR_STARR-seq_Random_generate-100000_final-100000_random-selection',
                ]:
        plottitle='Random'
        mycolor='C3' 

    if experiment_name in ['LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection', 'DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection']:
        plottitle='UGM' 
        mycolor='C0'

    if experiment_name in ['DeepSTARR_STARR-seq_Pool_generate-20000_final-20000_random-selection', 'LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection']:
        plottitle='Genome' 
        mycolor='grey'

    if experiment_name in ['LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection', 'DeepSTARR_STARR-seq_Random_generate-100000_final-20000_uncertainty-selection']:
        plottitle='Uncertainty'
        mycolor='C3'
        hatch='///'
    if experiment_name in ['LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection', 'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection']:
        plottitle='Uncertainty'
        mycolor='#ffae00ff'
        hatch='///'

    if experiment_name in ['LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection','DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection']:
        plottitle='Batch'
        mycolor='#ffae00ff'
        hatch='\\\\'
    if experiment_name in ['LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection','DeepSTARR_STARR-seq_Random_generate-100000_final-20000_LCMD-selection']:
        plottitle='Batch'
        mycolor='C3'
        hatch='\\\\'
    if experiment_name in ['LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection','DeepSTARR_STARR-seq_UGM-rate-5_generate-100000_final-20000_LCMD-selection']:
        plottitle='Batch'
        mycolor='C0'
        hatch='\\\\'

    if experiment_name in ['LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection','DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection']:
        plottitle='All'
        mycolor='blueviolet'
    if experiment_name in ['LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection','DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection']:
        plottitle='Batch'
        mycolor='blueviolet'
        hatch='\\\\'

    if experiment_name in ['LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection','DeepSTARR_STARR-seq_All-rate-5_generate-60000_final-60000_random-selection']:
        plottitle='All'
        mycolor='blueviolet'

    if request in ['SI_5perc_vs_25perc','SI_5-10-25perc_UGM','SI_5-10-25perc_Mut']:
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-25_generate-20000_final-20000_random-selection"]: plottitle='UGM, 25%'
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-10_generate-20000_final-20000_random-selection"]: plottitle='UGM, 10%'
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection"]: plottitle='UGM, 5%'
        if experiment_name in["LegNet_LentiMPRA_Mutagenesis-rate-25_generate-20000_final-20000_random-selection"]: plottitle='Mutagenesis, 25%'
        if experiment_name in["LegNet_LentiMPRA_Mutagenesis-rate-10_generate-20000_final-20000_random-selection"]: plottitle='Mutagenesis, 10%'
        if experiment_name in["LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection"]: plottitle='Mutagenesis, 5%'
        #
        #5%
        if experiment_name in["LegNet_LentiMPRA_Mutagenesis-rate-25_generate-20000_final-20000_random-selection"]: mycolor='cornflowerblue' #'C9'
        #
        #25%
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-25_generate-20000_final-20000_random-selection"]: mycolor='darkred' #'C9'
        if experiment_name in["LegNet_LentiMPRA_Mutagenesis-rate-25_generate-20000_final-20000_random-selection"]: mycolor='C3' #'goldenrod'
        #
        #10%
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-10_generate-20000_final-20000_random-selection"]: mycolor='darkgreen' #'darkblue'
        if experiment_name in["LegNet_LentiMPRA_Mutagenesis-rate-10_generate-20000_final-20000_random-selection"]: mycolor='C2' #'C1'
    #if request=='SI_M-O':
    if request in ['SI_Single_VS_EnsembleOracle']:
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection_SingleOracle"]: plottitle='UGM, single oracle'
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection"]: plottitle='UGM, oracle ensemble'
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection_SingleOracle"]: mycolor='limegreen' #'C9'
    if request in ['SI_MCDropout_VS_DeepEnsemble']:
        if experiment_name in["LegNet_LentiMPRA_UGM-DeepEnsemble-rate-5_generate-20000_final-20000_random-selection"]: plottitle='UGM, Deep ensemble'
        if experiment_name in["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection"]: plottitle='UGM, MC Dropout'
        if experiment_name in["LegNet_LentiMPRA_UGM-DeepEnsemble-rate-5_generate-20000_final-20000_random-selection"]: mycolor='peru' #'C9'
        
    if 'SuppFig4' in request:
        if experiment_name in ["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection"]: plottitle='UGM' # (+20K)'#PRE 3 FEB 2025

    if 'Fig2D' in request:
        if experiment_name in ["LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection"]: plottitle='Random' #'no selection' #'random' # Mutagenesis         -> ''
        if experiment_name in ["LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection"]: plottitle='Random' #'no selection' #'random' # UGM         -
        if experiment_name in ["LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection","JRZtNzt1O","DRZtNzt1O","LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection"]: plottitle='Random' #'no selection' #'random'
        if experiment_name in ['LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection','DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection']: plottitle='Random' #'no selection' #'random'

    if request=='Unc':
        if experiment_name in ["LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection","DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection"]: mycolor='pink'

    info={
            'plotname':plottitle, 
            'color':mycolor,
            'hatch':hatch,
            }
    return info






def get_experiments_for_plot(plot_name):
    experiments_for_plot={
        'Fig2B_UGM_LentiMPRA': ['LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection'], 
        'Fig2B_UGM_STARR-seq': ['DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection'], 
        'Fig2B_Mutagenesis_LentiMPRA': ['LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection'], 
        'Fig2B_Mutagenesis_STARR-seq': ['DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection'], 
        'Fig2B_Random_LentiMPRA': ['LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection'], 
        'Fig2B_Random_STARR-seq': ['DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection'], 
        'Fig2B_Genome_LentiMPRA': ['LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection'], 
        'Fig2B_Genome_STARR-seq': ['DeepSTARR_STARR-seq_Pool_generate-20000_final-20000_random-selection'], 
        'Fig2B_All_LentiMPRA': ['LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection'], 
        'Fig2B_All_STARR-seq': ['DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection'],

        'Fig2D_UGM_NoShift_LentiMPRA':        ['LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection','LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],
        'Fig2D_UGM_SmallShift_LentiMPRA':     ['LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection','LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],
        'Fig2D_UGM_LargeShiftHigh_LentiMPRA': ['LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection','LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],
        'Fig2D_UGM_LargeShiftLow_LentiMPRA':  ['LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection','LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],

        'Fig2D_Mutagenesis_NoShift_LentiMPRA':        ["LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Mutagenesis_SmallShift_LentiMPRA':     ["LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Mutagenesis_LargeShiftHigh_LentiMPRA': ["LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Mutagenesis_LargeShiftLow_LentiMPRA':  ["LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],

        'Fig2D_Random_NoShift_LentiMPRA':        ["LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Random_SmallShift_LentiMPRA':     ["LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Random_LargeShiftHigh_LentiMPRA': ["LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Random_LargeShiftLow_LentiMPRA':  ["LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection","LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection"],

        'Fig2D_All_NoShift_LentiMPRA':        ["LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_All_SmallShift_LentiMPRA':     ["LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_All_LargeShiftHigh_LentiMPRA': ["LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_All_LargeShiftLow_LentiMPRA':  ["LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection","LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection"],

        'Fig2D_UGM_NoShift_STARR-seq':        ['DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection','DeepSTARR_STARR-seq_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],
        'Fig2D_UGM_SmallShift_STARR-seq':     ['DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection','DeepSTARR_STARR-seq_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],
        'Fig2D_UGM_LargeShiftHigh_STARR-seq': ['DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection','DeepSTARR_STARR-seq_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],
        'Fig2D_UGM_LargeShiftLow_STARR-seq':  ['DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection','DeepSTARR_STARR-seq_UGM-rate-5_generate-100000_final-20000_LCMD-selection'],

        'Fig2D_Mutagenesis_NoShift_STARR-seq':        ["DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Mutagenesis_SmallShift_STARR-seq':     ["DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Mutagenesis_LargeShiftHigh_STARR-seq': ["DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Mutagenesis_LargeShiftLow_STARR-seq':  ["DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection"],

        'Fig2D_Random_NoShift_STARR-seq':        ["DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Random_SmallShift_STARR-seq':     ["DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Random_LargeShiftHigh_STARR-seq': ["DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_Random_LargeShiftLow_STARR-seq':  ["DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_uncertainty-selection","DeepSTARR_STARR-seq_Random_generate-100000_final-20000_LCMD-selection"],

        'Fig2D_All_NoShift_STARR-seq':        ["DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_All_SmallShift_STARR-seq':     ["DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_All_LargeShiftHigh_STARR-seq': ["DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection"],
        'Fig2D_All_LargeShiftLow_STARR-seq':  ["DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection","DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection"],

        ######

        'SuppFig3_LentiMPRA': ["LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection",       
                 "LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection",           
                 "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection",      
                 "LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection",      
                 "LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection"], 
        'SuppFig3_STARR-seq': ["DeepSTARR_STARR-seq_Pool_generate-20000_final-20000_random-selection",       
                               "DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection",         
                               "DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection",      
                               "DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection",      
                               "DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection"],

        ######

        'SuppFig4_NoShift_LentiMPRA':        ["LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection", "LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection"],
        'SuppFig4_SmallShift_LentiMPRA':     ["LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection", "LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection"],
        'SuppFig4_LargeShiftHigh_LentiMPRA': ["LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection", "LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection"],
        'SuppFig4_LargeShiftLow_LentiMPRA':  ["LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection", "LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection"],

        'SuppFig4_NoShift_STARR-seq':        ["DeepSTARR_STARR-seq_Random_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection", "DeepSTARR_STARR-seq_All-rate-5_generate-60000_final-60000_random-selection"],
        'SuppFig4_SmallShift_STARR-seq':     ["DeepSTARR_STARR-seq_Random_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection", "DeepSTARR_STARR-seq_All-rate-5_generate-60000_final-60000_random-selection"],
        'SuppFig4_LargeShiftHigh_STARR-seq': ["DeepSTARR_STARR-seq_Random_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection", "DeepSTARR_STARR-seq_All-rate-5_generate-60000_final-60000_random-selection"],
        'SuppFig4_LargeShiftLow_STARR-seq':  ["DeepSTARR_STARR-seq_Random_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-100000_random-selection", "DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection", "DeepSTARR_STARR-seq_All-rate-5_generate-60000_final-60000_random-selection"],

        ######

        'all': ['LegNet_LentiMPRA_Mutagenesis-rate-5_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection',
                'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection', 
                'LegNet_LentiMPRA_Pool_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_UGM-rate-5_generate-100000_final-20000_LCMD-selection',
                'LegNet_LentiMPRA_Random_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_Random_generate-100000_final-20000_uncertainty-selection',
                'LegNet_LentiMPRA_Random_generate-100000_final-20000_LCMD-selection', 
                'LegNet_LentiMPRA_All-rate-5_generate-20000_final-20000_random-selection', 
                'LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection',  
                'LegNet_LentiMPRA_Random_generate-100000_final-100000_random-selection', 
                'LegNet_LentiMPRA_Mutagenesis-rate-5_generate-100000_final-100000_random-selection', 
                'LegNet_LentiMPRA_All-rate-5_generate-60000_final-60000_random-selection',

                'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-20000_final-20000_random-selection',
                'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_uncertainty-selection',
                'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-20000_LCMD-selection', 
                'DeepSTARR_STARR-seq_Pool_generate-20000_final-20000_random-selection',
                'DeepSTARR_STARR-seq_UGM-rate-5_generate-20000_final-20000_random-selection',
                'DeepSTARR_STARR-seq_UGM-rate-5_generate-100000_final-20000_LCMD-selection',
                'DeepSTARR_STARR-seq_Random_generate-20000_final-20000_random-selection',
                'DeepSTARR_STARR-seq_Random_generate-100000_final-20000_uncertainty-selection',
                'DeepSTARR_STARR-seq_Random_generate-100000_final-20000_LCMD-selection', 
                'DeepSTARR_STARR-seq_All-rate-5_generate-20000_final-20000_random-selection', 
                'DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection',  
                'DeepSTARR_STARR-seq_Random_generate-100000_final-100000_random-selection', 
                'DeepSTARR_STARR-seq_Mutagenesis-rate-5_generate-100000_final-100000_random-selection', 
                'DeepSTARR_STARR-seq_All-rate-5_generate-60000_final-60000_random-selection',

                #SI:
                'LegNet_LentiMPRA_UGM-DeepEnsemble-rate-5_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_UGM-rate-5_generate-20000_final-20000_random-selection_SingleOracle',
                'LegNet_LentiMPRA_UGM-rate-10_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_UGM-rate-25_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_Mutagenesis-rate-10_generate-20000_final-20000_random-selection',
                'LegNet_LentiMPRA_Mutagenesis-rate-25_generate-20000_final-20000_random-selection']

        }
    return experiments_for_plot[plot_name]


def average_curve(list_of_curves, no_outliers=False):
    """
    Make average curve of a list of curves.
    Returns mean, standard deviation, and whether outliers were found.
    """
    if not no_outliers:
        return np.mean(list_of_curves, axis=0), np.std(list_of_curves, axis=0), False
    
    # Handle outlier removal (> 3 standard deviations from mean)
    curves = np.array(list_of_curves)
    means = np.mean(curves, axis=0)
    stds = np.std(curves, axis=0)
    z_scores = np.abs((curves - means) / stds)
    
    mask = z_scores <= 3
    filtered_means = np.array([np.mean(curves[mask[:, i], i]) for i in range(curves.shape[1])])
    filtered_stds = np.array([np.std(curves[mask[:, i], i]) for i in range(curves.shape[1])])
    
    any_outliers = not np.all(mask)
    
    return filtered_means, filtered_stds, any_outliers




if __name__=='__main__':
    make_plot_experiment_loops()
