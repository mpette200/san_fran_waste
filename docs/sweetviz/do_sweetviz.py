import pandas as pd
import sweetviz as sv

# df = pd.read_csv('data/san_fran_waste.zip')
df = pd.read_csv('data/san_fran_waste_large.zip')
report = sv.analyze(df)
# report.show_html('docs/sweetviz/SWEETVIZ_REPORT.html')
report.show_html('docs/sweetviz/SWEETVIZ_REPORT_L.html')
