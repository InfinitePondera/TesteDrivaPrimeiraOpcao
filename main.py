import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_columns', 16)
    pd.set_option('display.width', 300)
    df = pd.read_csv('C:\Users\Usuario\Downloads\DadosEmpresa.csv', sep=',')
    dfextra = pd.read_csv('C:\Users\Usuario\Downloads\DadosEndereco.csv', sep=',')
    for col in df.columns:  # print das colunas
        print col
    print df.head(n=10)  # print das primeiras 10 linhas
    dfaux = df.apply(lambda a: True if a['opcao_pelo_simples'] == "SIM" else False,
                     axis=1)  # dataFrame auxiliar na contagem
    print len(dfaux[dfaux == True].index)  # print do numero de emrpesas que optaram pelo Simples
    print df['capital_social'].sum()  # soma dos capitais sociais
    print df.loc[(df['capital_social'] > 10000) & (
            df['capital_social'] < 20000)]  # print das empresas com capital entre 10000 e 20000
    dfaux2 = pd.merge(df, dfextra, how='inner', on='cnpj')  # merge das tabelas
    dfaux3 = dfaux2.loc[dfaux2['municipio'] == 'CURITIBA']
    dfaux3.to_csv('csv_teste', sep=',', index=False)
