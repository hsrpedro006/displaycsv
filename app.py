from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Ler o CSV
    csv_path = os.path.join('dados', 'ai_job_trends_dataset.csv') 
    
    try:
        # Tentar diferentes encodings
        try:
            df = pd.read_csv(csv_path, encoding='utf-8', sep=',')
        except:
            df = pd.read_csv(csv_path, encoding='latin-1', sep=';')
        
        # Converter DataFrame para HTML
        table_html = df.to_html(classes='table table-striped table-hover', 
                                index=False, 
                                border=0)
        
        # Estatísticas básicas
        total_registros = len(df)
        colunas = list(df.columns)
        
        return render_template('index.html', 
                             table=table_html, 
                             total=total_registros,
                             colunas=colunas)
    
    except Exception as e:
        return f"Erro ao carregar CSV: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

