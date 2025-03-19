# Figure Reproducibility

The directory `figure_reproducibility/` contains Python scripts for reproducing figures and analysis from the paper "PIONEER: a virtual platform for iterative improvement of genomic deep learning". The scripts handle data processing, analysis, and visualization of results.

## Scripts

### Data Processing
- `make_histograms.py` - Generates histograms of test data distributions across different covariate shifts
- `make_uncertainties.py` - Calculates uncertainty metrics for model predictions using MC Dropout
- `make_performance_on_shifts.py` - Evaluates model performance across different covariate shift conditions

### Visualization Scripts
- `plot_Fig2A-SuppFig6_performance_across_cycles.py` - Plots model performance across training cycles
- `plot_Fig2B_generalization_across_covariate_shifts.py` - Visualizes model generalization across different covariate shifts
- `plot_Fig2C_LCMD_batch_selection_per_cycle.py` - Shows batch selection statistics per cycle using LCMD
- `plot_SuppFig1_CDF.py` - Generates cumulative distribution function plots
- `plot_SuppFig1_KL_divergence_6mer.py` - Plots KL divergence for 6-mer sequences
- `plot_SuppFig3_mean_activity_mean_uncertainty.py` - Visualizes mean activity and uncertainty metrics
- `plot_SuppFig4_fair_cost_comparison.py` - Compares costs across different experimental conditions

### Utilities
- `utils.py` - Contains shared utility functions, experiment configurations, and plotting helpers used across multiple scripts

## Dependencies

- numpy
- matplotlib
- seaborn
- h5py
- torch
- warnings