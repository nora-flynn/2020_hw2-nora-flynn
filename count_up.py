#Download the files
import os,gzip,itertools,csv,re,sys
gffurl="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
gfffile = os.path.basename(gffurl)
print("1A: What is the GFF filename?")
print("Gff filename is {}".format(gfffile))
print("-----")
if not os.path.exists(gffurl):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")


fastaurl="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"
fastafile= os.path.basename(fastaurl)
print("1B: What is the FASTA filename?")
print("Fasta filename is {}". format(fastafile))
print("-----")
if not os.path.exists(fastaurl):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
    
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
            
#Number and length of genes 
total_number_genes = 0
with gzip.open(gfffile,"rt") as fh:
    gfffile = csv.reader(fh,delimiter="\t")
    final_count = 0
    total_gene_length = 0
    CDS_count = 0
    CDS_length = 0
    for row in gfffile:
        if row[0].startswith("#"):
            continue
        #Original longer code below, == is much better
        #if "pseudogene" in row[2]:
            #continue
        #if "RNA" in row[2]:
            #continue
        if "gene" == row[2]:
            final_count += 1
            genelen = abs(int(row[4]) - int(row[3]))
            total_gene_length += genelen
        if "CDS" in row[2]:
            CDS_count += 1
            CDSlen = abs(int(row[4]) - int(row[3]))
            CDS_length += CDSlen

print("2: How many genes?")
print("Number of genes is {}". format(final_count))
print("-----")
print("3: What is the total length of the genes?")
print("Total length of genes is {}". format(total_gene_length))
print("-----")

#Genome length
with gzip.open(fastafile,"rt") as handle:
    seqs = dict(aspairs(handle))
    
    for base in seqs:
        number_bases = seqs[base]

print("4: What is the length of the genome?")
print("There are {} bases in the fasta file".format(len(number_bases)))
print("-----")

#Percentage coding
print("5A: How many CDS?")
print("Number of CDS is {}".format(CDS_count))
print("-----")
print("5B: What is the length of all CDS?")
print("Total length of CDS is {}".format(CDS_length))
print("-----")
print("5C: What percentage of the genome is coding?")
print("{} percent of the genome is coding".format(100 * (CDS_length / len(number_bases))))
print("-----")