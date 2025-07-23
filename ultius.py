from dataset import df

def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f}  {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

#Criando um grafico de soma e agrupamento
df_receita_estado = df.groupby('Local da compra')[['Preço']].sum()
#Eliminar os registros duplicados
df_receita_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_receita_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False )

#Ver se deu bom
print(df_receita_estado)