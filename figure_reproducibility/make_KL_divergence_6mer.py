import os
import numpy as np
import torch
import h5py
from itertools import product
from scipy.special import softmax, kl_div, rel_entr

class kmer_featurization:

    def __init__(self, k):
        """
        seqs: a list of DNA sequences
        k: the "k" in k-mer
        """
        self.k = k
        self.letters = ['A', 'C', 'G', 'T']
        self.multiplyBy = 4 ** np.arange(k-1, -1, -1) # the multiplying number for each digit position in the k-number system
        self.n = 4**k # number of possible k-mers

    def obtain_kmer_feature_for_a_list_of_sequences(self, seqs, write_number_of_occurrences=False):
        """
        Given a list of m DNA sequences, return a 2-d array with shape (m, 4**k) for the 1-hot representation of the kmer features.
        Args:
          write_number_of_occurrences:
            a boolean. If False, then in the 1-hot representation, the percentage of the occurrence of a kmer will be recorded; otherwise the number of occurrences will be recorded. Default False.
        """
        kmer_features = []
        for seq in seqs:
            this_kmer_feature = self.obtain_kmer_feature_for_one_sequence(seq.upper(), write_number_of_occurrences=write_number_of_occurrences)
            kmer_features.append(this_kmer_feature)

        kmer_features = np.array(kmer_features)

        return kmer_features

    def obtain_kmer_feature_for_one_sequence(self, seq, write_number_of_occurrences=False):
        """
        Given a DNA sequence, return the 1-hot representation of its kmer feature.
        Args:
          seq:
            a string, a DNA sequence
          write_number_of_occurrences:
            a boolean. If False, then in the 1-hot representation, the percentage of the occurrence of a kmer will be recorded; otherwise the number of occurrences will be recorded. Default False.
        """
        number_of_kmers = len(seq) - self.k + 1

        kmer_feature = np.zeros(self.n)

        for i in range(number_of_kmers):
            this_kmer = seq[i:(i+self.k)]
            this_numbering = self.kmer_numbering_for_one_kmer(this_kmer)
            kmer_feature[this_numbering] += 1

        if not write_number_of_occurrences:
            kmer_feature = kmer_feature / number_of_kmers

        return kmer_feature

    def kmer_numbering_for_one_kmer(self, kmer):
        """
        Given a k-mer, return its numbering (the 0-based position in 1-hot representation)
        """
        digits = []
        for letter in kmer:
            digits.append(self.letters.index(letter))

        digits = np.array(digits)

        numbering = (digits * self.multiplyBy).sum()

        return numbering

def convert_one_hot_to_ACGT(X, dna_dict = {0: "A", 1: "C", 2: "G", 3: "T"}):
    # convert one hot to A,C,G,T
    seq_list = []
    for index in range(len(X)):
        seq = X[index]
        seq_list += ["".join([dna_dict[np.where(i)[0][0]] for i in seq])]
    return seq_list

def compute_kmer_spectra(X, kmer_length=3, dna_dict = {0: "A", 1: "C", 2: "G", 3: "T"}):
    seq_list=convert_one_hot_to_ACGT(X,dna_dict)
    obj = kmer_featurization(kmer_length)  # initialize a kmer_featurization object
    kmer_features = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=True)
    kmer_permutations = ["".join(p) for p in product(["A", "C", "G", "T"], repeat=kmer_length)]
    kmer_dict = {}
    for kmer in kmer_permutations:
        n = obj.kmer_numbering_for_one_kmer(kmer)
        kmer_dict[n] = kmer
    global_counts = np.sum(np.array(kmer_features), axis=0)
    global_counts_normalized = global_counts / sum(global_counts) # this is the distribution of kmers in the testset
    return global_counts_normalized

if __name__=='__main__':

    kmer_length=6

    test_shifts=['no_shift','small_shift','large_shift_low','large_shift_high']
    
    output_dir='../../data_PIONEER/'

    for i_sq,test_shift in enumerate(test_shifts):
        for case in ['LentiMPRA','STARR-seq']:
            testfile=output_dir+"data/covariate_shift_test/"+"TestShiftData_"+case+"_"+test_shift+".h5"
            if os.path.isfile(testfile) and testfile!='no_shift':
                if test_shift!='no_shift':
                    testdata=h5py.File(testfile, 'r') 
                    X_ood=torch.tensor(np.array(testdata['X_test']))
                    y_ood_gt=torch.tensor(np.array(testdata['Y_test'])).numpy()

                for surrogate_index in range(5):
                    input_h5_file=output_dir+"data/"+case+"/initial_train_dataset.h5" 
                    for ii_al,i_al in enumerate(['dummy']):
                        data = h5py.File(input_h5_file, 'r')
                        if test_shift=='no_shift':
                            X_ood=torch.tensor(np.array(data['X_test']))

                        Xs=torch.tensor(np.array(data['X_test']))
                        Ys=np.array(data['Y_test']).squeeze(1)

                        kldiv_file=output_dir+"npy2/oracles/"+"/KLdiv_6mer_"+test_shift+"_model-"+str(surrogate_index)+".npy"
                        if not (os.path.isfile(kldiv_file)):                                                
                            
                            X_train_1=Xs 
                            X_train_perm_numpy=X_train_1.permute(0,2,1).numpy() 
                            kmer_dist_train = compute_kmer_spectra(X_train_perm_numpy, kmer_length) 

                            X_ood_1=X_ood 
                            X_ood_perm_numpy=X_ood_1.permute(0,2,1).numpy() 
                            kmer_dist_ood = compute_kmer_spectra(X_ood_perm_numpy, kmer_length) 

                            kldiv = kl_div(kmer_dist_ood, kmer_dist_train)
                            np.save(kldiv_file,kldiv)
                            print("DONE:",kldiv_file)

    print("SCRIPT END.")
