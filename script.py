import os
modelofile = 'vamosTrabalhar_cracha'+'.svg'
csvfile = 'bancoDeDados+monitores'+'.csv'
pdffile = 'output'

os.system(f'inkscape_merge -f {modelofile} -d {csvfile} -o output/{pdffile}%d.pdf')

#sh 