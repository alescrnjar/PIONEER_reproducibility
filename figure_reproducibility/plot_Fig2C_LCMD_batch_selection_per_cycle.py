import os
import numpy as np
import matplotlib.pyplot as plt
import utils

if __name__=='__main__':
    
    general_fontsize=9 
    general_figsize=(3,3) 
    general_dpi=300
    general_figureformat='pdf' 
    
    output_dir='../../data_PIONEER/'
    
    plt.rcParams.update({'font.size': general_fontsize})
    for case in ['LentiMPRA','STARR-seq']:
        if case=='LentiMPRA': experiment_name='LegNet_LentiMPRA_All-rate-5_generate-100000_final-20000_LCMD-selection'
        if case=='STARR-seq': experiment_name='DeepSTARR_STARR-seq_All-rate-5_generate-100000_final-20000_LCMD-selection'
        fig = plt.figure(1, figsize=general_figsize)
        avg_rnd=[]
        avg_mut=[]
        avg_ugm=[]
        std_rnd=[]
        std_mut=[]
        std_ugm=[]
        for pioneer_cycle in range(5):
            rnd_peral=[]
            mut_peral=[]
            ugm_peral=[]
            for surrogate_indexes in range(5):
                lcmd_seq_file=output_dir+"npy/"+utils.get_path(experiment_name)+'/lcmd_seq_file_cycle-'+str(pioneer_cycle)+'_model-'+str(surrogate_indexes)+'.out'
                rnd=os.popen("grep -e 'Stats of concat' "+lcmd_seq_file+" | sed 's/=/ /g' | awk '{print $5}'").read().replace('\n','')
                if rnd!='': rnd=int(rnd)
                mut=os.popen("grep -e 'Stats of concat' "+lcmd_seq_file+" | sed 's/=/ /g' | awk '{print $7}'").read().replace('\n','')
                if mut!='': mut=int(mut)
                ugm=os.popen("grep -e 'Stats of concat' "+lcmd_seq_file+" | sed 's/=/ /g' | awk '{print $9}'").read().replace('\n','')
                if ugm!='': ugm=int(ugm)
                rnd_peral.append(rnd)
                mut_peral.append(mut)
                ugm_peral.append(ugm)

            avg_rnd.append(np.mean(rnd_peral))
            std_rnd.append(np.std(rnd_peral))
            avg_mut.append(np.mean(mut_peral))
            std_mut.append(np.std(mut_peral))
            avg_ugm.append(np.mean(ugm_peral))
            std_ugm.append(np.std(ugm_peral))

        avg_rnd=np.array(avg_rnd)
        avg_mut=np.array(avg_mut)
        avg_ugm=np.array(avg_ugm)
        std_rnd=np.array(std_rnd)
        std_mut=np.array(std_mut)
        std_ugm=np.array(std_ugm)

        xaxis=np.arange(len(avg_rnd))


        infos=utils.get_plot_info(experiment_name)
        general_color=infos['color']
        print(f"{case} rnd:{avg_rnd}+-{std_rnd} mut:{avg_mut}+-{std_mut} ugm:{avg_ugm}+-{std_ugm}")

        general_color_rnd='C3'
        general_color_mut='#ffae00ff'
        general_color_ugm='C0'

        plt.plot(xaxis,avg_rnd,color=general_color_rnd, lw=1, label='Rand.',alpha=1.0) 
        plt.fill_between(xaxis, avg_rnd-std_rnd, avg_rnd+std_rnd, alpha=0.5, color=general_color_rnd)
        plt.scatter(xaxis,avg_rnd,color=general_color_rnd, lw=1,alpha=1.0) 

        plt.plot(xaxis,avg_mut,color=general_color_mut, lw=1, label='Mut.',alpha=1.0) 
        plt.fill_between(xaxis, avg_mut-std_mut, avg_mut+std_mut, alpha=0.5, color=general_color_mut)
        plt.scatter(xaxis,avg_mut,color=general_color_mut, lw=1,alpha=1.0) 

        plt.plot(xaxis,avg_ugm,color=general_color_ugm, lw=1, label='UGM',alpha=1.0) 
        plt.fill_between(xaxis, avg_ugm-std_ugm, avg_ugm+std_ugm, alpha=0.5, color=general_color_ugm)
        plt.scatter(xaxis,avg_ugm,color=general_color_ugm, lw=1,alpha=1.0) 

        plt.legend(loc='upper center',prop={'size':general_fontsize}, fontsize=general_fontsize, frameon=False,markerfirst=False, alignment='right', ncol=3, handletextpad=0.5, columnspacing=0.8) #, expand=True)
        plt.xlabel('Cycles')
        plt.xticks(np.arange(5),['1','2','3','4','5'])
        plt.ylabel('# selected datapoints')
        plt.ylim(2900,13000)
        outfile=output_dir+'Fig2-C_'+case+'.'+general_figureformat
        plt.title('LCMD batch selection per cycle',fontsize=general_fontsize)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        fig.savefig(outfile,dpi=general_dpi, bbox_inches='tight') 
        print("DONE:",outfile)
        plt.clf()
    print("SCRIPT END.")


