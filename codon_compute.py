#I'm new to Python and programming and I especially struggled with this one... the code is a bit ugly but I think it's working. I'm sure there is a way that I could just use one for loop for each species, but I couldn't get it to work so I split it into different loops for each question.

import os, gzip, itertools

# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence

url1="ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2/cds/Salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2.ASM694v2.cds.all.fa.gz"
url2="ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/mycobacterium_tuberculosis_h37rv/cds/Mycobacterium_tuberculosis_h37rv.ASM19595v2.cds.all.fa.gz"
file1="Salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2.ASM694v2.cds.all.fa.gz"
file2="Mycobacterium_tuberculosis_h37rv.ASM19595v2.cds.all.fa.gz"

if not os.path.exists(file1):
    os.system("curl -O %s"%(url1))

if not os.path.exists(file2):
    os.system("curl -O %s"%(url2))
    
# What is the total number and length of genes?

with gzip.open(file1,"rt") as fh:
    seqs = dict(aspairs(fh))
    number_of_genes = 0
    total_length_of_genes = 0
    
    for seq in seqs:
        number_of_genes += 1
        number_of_bases = seqs[seq]
        add_the_lengths = len(number_of_bases)
        total_length_of_genes += add_the_lengths

            

with gzip.open(file2,"rt") as fh:
    seqsmyco = dict(aspairs(fh))
    number_of_myco_genes = 0
    total_length_of_myco_genes = 0

    
    for seq in seqsmyco:
        number_of_myco_genes += 1
        number_of_myco_bases = seqsmyco[seq]
        add_the_myco_lengths = len(number_of_myco_bases)
        total_length_of_myco_genes += add_the_myco_lengths
         
#Looking into GC in the genome
with gzip.open(file1,"rt") as fh:
    seqs = aspairs(fh)
    count_gc = 0
    
    for seq in seqs:
        seqname  = seq[0]
        seqstring= seq[1]
        for i in seqstring:
            if i == "G" or i == "C":
                count_gc += 1
        
                        
with gzip.open(file2,"rt") as fh:
    seqsmyco = aspairs(fh)
    count_myco_gc = 0
    
    for seq in seqsmyco:
        seqnamemyco  = seq[0]
        seqstringmyco= seq[1]
        for i in seqstringmyco:
            if i == "G" or i == "C":
                count_myco_gc += 1

#Practice code from workshop looking at first codon only            
with gzip.open(file1,"rt") as fh:
    seqs = dict(aspairs(fh))
    first_codon = {}
    for seqname in seqs:
        firstcodon = seqs[seqname][0:3]
        if firstcodon in first_codon:
            first_codon[firstcodon] +=1
        else:
            first_codon[firstcodon] = 1
            
#print(first_codon)

#Now try to look at all codons
with gzip.open(file1,"rt") as fh:
    seqs = dict(aspairs(fh))
    all_the_codons = {}
    for seq in seqs:
        for i in range(len(seq)):
            allcodons = seqs[seq][i:i+3]
            if allcodons in all_the_codons:
                all_the_codons[allcodons] +=1
            else:
                all_the_codons[allcodons] = 1
            
#print(all_the_codons)


with gzip.open(file2,"rt") as fh:
    seqs = dict(aspairs(fh))
    all_the_myco_codons = {}
    for seq in seqs:
        for i in range(len(seq)):
            allcodons = seqs[seq][i:i+3]
            if allcodons in all_the_myco_codons:
                all_the_myco_codons[allcodons] +=1
            else:
                all_the_myco_codons[allcodons] = 1
                
            
#print(all_the_myco_codons)


print("1A: Salmonella genes")            
print("The number of genes for Salmonella is {}".format(number_of_genes))
print("1B: Mycobacterium genes")
print("The number of genes for Mycobacterium is {}".format(number_of_myco_genes))
print("-----")
print("2A: Salmonella gene lengths")  
print("The total length of genes for Salmonella is {}".format(total_length_of_genes))
print("2B: Mycobacterium gene length")
print("The total length of genes for Mycobacterium is {}".format(total_length_of_myco_genes))
print("-----")
print("3A: What's the GC percentage for Salmonella?")
print("For Salmonella the number of bases that are G or C is {}".format(count_gc))
print("For Salmonella the percentage of GC is {}".format(100 * (count_gc/total_length_of_genes)))
print("3B: What's the GC percentage for Mycobacterium?")
print("For Mycobacterium the number of bases that are G or C is {}".format(count_myco_gc))
print("For Mycobacterium the percentage of GC is {}".format(100 * (count_myco_gc/total_length_of_myco_genes)))
print("-----")
print("4A: Number of codons in Salmonella")
print("The number of Salmonella codons is {}".format(total_length_of_genes/3))
print("4B: Number of codons in Mycobacterium")
print("The number of Mycobacterium codons is {}".format(total_length_of_myco_genes/3))
print("-----")

sal_all_the_codons = total_length_of_genes/3
myco_all_the_codons = total_length_of_myco_genes/3

print("5A: This is a table showing the number of times each codon appears")
print("-----")
print ("{:<5} {:<15} {:<10}".format('Codon', 'Salmonella', 'Mycobacterium'))
for key, value in all_the_codons.items() and all_the_myco_codons.items():
    print("\t".join([key, str(all_the_codons[key]), "\t", str(all_the_myco_codons[key])]))
print("-----")

print("5B: This is a table showing the frequency of each codon")
print("-----")
print ("{:<15} {:<25} {:<15}".format('Codon', 'Salmonella Freq', 'Mycobacterium Freq'))
for key, value in all_the_codons.items() and all_the_myco_codons.items():
    print("\t".join([key, str(all_the_codons[key]/sal_all_the_codons), "\t", str(all_the_myco_codons[key]/myco_all_the_codons)]))
print("-----")