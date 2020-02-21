class DNA:
    def __init__(self, sequence):
        self.dna_seq = sequence.upper()
        bases = 'ATGCatgc'
        for base in set(sequence):
            if base not in bases:
                print("Not DNA sequence")
                break
        else:
            print('This is original sequence:', self.dna_seq)

    def gc_content(self): # создаем метод для рассчета GC
        g = self.dna_seq.count('G')
        c = self.dna_seq.count('C')
        l = len(self.dna_seq)
        gc = g+c
        print("GC count =", (gc/l)*100, "%")

    def reverse_complement(self): # создаем метод для обратного комплемента
        c_sequence = ''
        pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        for base in self.dna_seq:
            c_sequence += pairs[base] # создаем комплементарную строку по правилу из словаря pairs
            rc_sequence = c_sequence[::-1] # переворачиваем ее
        print("This is reverse complement sequence:",rc_sequence)

    def transcribe(self):
        RNA = ''
        pairs = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
        for base in self.dna_seq:
            RNA += pairs[base] # транслируем последовательность ДНК в РНК
        print('This is translated to RNA sequence:',RNA)




#a = DNA("agatacaca")
#a.gc_content()
#a.reverse_complement()
#a.transcribe()

class RNA:
    def __init__(self, sequence):
        bases = 'AUGCaugc'
        self.rna_seq = sequence.upper()
        for base in set(sequence):
            if base not in bases:
                print("Not RNA sequence")
                break
        else:
            print('This is original sequence:', self.rna_seq)

#b = RNA("acgugac")