chcp 65001
python cleanup_before_pandoc.py CCAS.tex CCAS_cleaned.tex
pandoc --from=latex --to=markdown --output=CCAS_pandoc.md CCAS_cleaned.tex
python cleanup_after_pandoc.py CCAS_pandoc.md CCAS_pandoc_cleaned.md CCAS_pandoc_cleaned_png.md