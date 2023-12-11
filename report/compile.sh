rm nlp_report.aux
rm nlp_report.log
rm nlp_report.synctex.gz
rm nlp_report.bbl
pdflatex nlp_report.tex
bibtex nlp_report
pdflatex nlp_report.tex
pdflatex nlp_report.tex
