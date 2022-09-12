# =======================================================================================================================================================
# Importação de bibliotecas
# =======================================================================================================================================================
#from operator import index
import pandas as pd
# pd.set_option( 'display.max_columns', None )
import matplotlib.pyplot as plt
# =======================================================================================================================================================
# Criação de DATAFRAMES/DICIONÁRIOS sobre posições de campo, países e informações básicas dos clubes participantes da UCL 21/22
# =======================================================================================================================================================
df_InfosTimes = pd.DataFrame( { 
    'NM_TIME' : [ 
            'Ajax', 
            'Atalanta', 
            'Atlético', 
            'Barcelona', 
            'Bayern', 
            'Benfica', 
            'Beşiktaş', 
            'Chelsea', 
            'Club Brugge', 
            'Dortmund', 
            'Dynamo Kyiv', 
            'Inter', 
            'Juventus', 
            'LOSC', 
            'Leipzig', 
            'Liverpool', 
            'Malmö', 
            'Man. City', 
            'Man. United', 
            'Milan', 
            'Paris', 
            'Porto', 
            'Real Madrid', 
            'Salzburg', 
            'Sevilla', 
            'Shakhtar Donetsk', 
            'Sheriff', 
            'Sporting CP', 
            'Villarreal', 
            'Wolfsburg', 
            'Young Boys', 
            'Zenit' 
        ],
    'NM_REAL' : [ 
            'AFC Ajax' , 
            'Atalanta BC' , 
            'Atletico' , 
            'FC Barcelona' , 
            'FC Bayern Munchen' , 
            'SL Benfica' , 
            'Besiktas JK' , 
            'Chelsea FC' , 
            'Club Brugge KV' ,
            'Borussia Dortmund' , 
            'FK Dynamo Kyiv' , 
            'FC Internazionale Milano' , 
            'Juventus FC' , 
            'Lille OSC' , 
            'RB Leipzig' , 
            'Liverpool FC' , 
            'Malmo FF',
            'Manchester City FC' , 
            'Manchester United FC' , 
            'AC Milan' , 
            'Paris Saint-Germain FC' , 
            'FC Porto' , 
            'Real Madrid CF' , 
            'FC Red Bull Salzburg' ,
            'Sevilla FC' , 
            'FK Shakhtar' , 
            'FC Sheriff' , 
            'Sporting CP' , 
            'Villarreal FC' , 
            'VFL Wolfsburg' , 
            'BSC Young Boys' , 
            'FC Zenit' 
        ],
    'SIGLA' : [ 
            'AFC', 
            'ATA', 
            'ATL', 
            'BAR', 
            'BAY', 
            'BEN', 
            'BES', 
            'CHE', 
            'BRU', 
            'DOR', 
            'DYN', 
            'INT', 
            'JUV', 
            'LSC', 
            'LEI', 
            'LIV', 
            'MAL', 
            'CIT', 
            'UNI', 
            'MIL', 
            'PSG', 
            'POR', 
            'RMD', 
            'RBS', 
            'SEV', 
            'SHA', 
            'SHE', 
            'SCP', 
            'VFC', 
            'WOL', 
            'BSC', 
            'ZEN' 
        ],
    'SIGLA_PAIS' : [ 
            'HOL', 
            'ITA', 
            'ESP', 
            'ESP', 
            'ALE', 
            'POR', 
            'TUR', 
            'ING', 
            'BEL', 
            'ALE', 
            'UCR', 
            'ITA', 
            'ITA', 
            'FRA', 
            'ALE', 
            'ING', 
            'SUE', 
            'ING', 
            'ING', 
            'ITA', 
            'FRA', 
            'POR', 
            'ESP', 
            'AUS', 
            'ESP', 
            'UCR', 
            'MOL', 
            'POR', 
            'ESP', 
            'ALE', 
            'SUE', 
            'RUS' 
        ]
}
)
dc_InfosPaises = {
    'ALE' : 'Alemanha' ,
    'AUS' : 'Austria' ,
    'BEL' : 'Belgica' ,
    'ESP' : 'Espanha' ,
    'FRA' : 'Franca' ,
    'HOL' : 'Holanda' ,
    'ING' : 'Inglaterra' ,
    'ITA' : 'Italia' ,
    'MOL' : 'Moldavia' ,
    'POR' : 'Portugal' ,
    'RUS' : 'Russia' ,
    'SUE' : 'Suecia' , 
    'TUR' : 'Turquia' ,
    'UCR' : 'Ucrania'
}
dc_InfosPos = {
    'Defender': 'DF', 
    'Forward': 'FW', 
    'Goalkeeper': 'GK',
    'Midfielder':'MD'
}
# =======================================================================================================================================================
# Definindo caminho e arquivo a ser utilizado:
# =======================================================================================================================================================
# vIpt = input('Favor informar o caminho onde o arquivo "key_stats.csv" está localizado: ')
vPatch = 'C:\\Users\\andre.holanda\\OneDrive - Mob Serviços de Telecomunicações Ltda\\03_Pessoal\\Educação\\DIO\\WORKSPACE\\Main\\PROJ01_DIO_Analise' + \
    ' de dados com Python e Pandas'
vFile = '\\key_stats.csv'
# =======================================================================================================================================================
# Importação de database inicial :
# =======================================================================================================================================================
DBI = pd.read_csv( vPatch + vFile )
# =======================================================================================================================================================
# Main Dataframe - Jogadores:
# =======================================================================================================================================================
DBI = DBI.rename( columns = {
    'player_name' : 'NM_JOG', 
    'club' : 'NM_TIME', 
    'position' : 'POS', 
    'minutes_played' : 'TMP_JGD', 
    'match_played' : 'JOGOS', 
    'goals' : 'GOLS', 
    'assists' : 'ASSIST', 
    'distance_covered' : 'DIST_PERC'}
)
DBI[ 'DIST_PERC' ].replace( '-', 0.0, inplace = True)
DBI[ 'DIST_PERC' ] = DBI[ 'DIST_PERC' ].astype( 'float64' )
DBI = DBI.merge( df_InfosTimes, on = 'NM_TIME', how = 'outer' )
DBI[ 'PAIS' ] = [ dc_InfosPaises[ resp_InfosPaises ] for resp_InfosPaises in DBI.SIGLA_PAIS ]
DBI[ 'SIGLA_POS' ] = [ dc_InfosPos[ resp_dc_InfosPos ] for resp_dc_InfosPos in DBI.POS ]
DBI[ 'DESC_JOG' ] = DBI['NM_JOG' ] + ' (' + DBI[ 'SIGLA_POS' ] + '_' + DBI[ 'SIGLA' ] + '/' + DBI[ 'SIGLA_PAIS' ] + ')'
DBI[ 'PART_GOLS' ] = DBI[ 'GOLS' ] + DBI[ 'ASSIST' ]
DBI[ 'MED_GOLS' ] = round( DBI[ 'GOLS' ] / DBI[ 'JOGOS' ], 2 )
DBI[ 'MED_ASSIST' ] = round( DBI[ 'ASSIST' ] / DBI[ 'JOGOS' ], 2 )
DBI[ 'MIN_P_GOL' ] = round( DBI[ 'TMP_JGD' ] / DBI[ 'PART_GOLS' ], 2 )
DBI[ 'MED_DIST_PERC' ] = round( DBI[ 'DIST_PERC' ] / DBI[ 'JOGOS' ], 2 )
# =======================================================================================================================================================
# Criação de dataframes e inclusão de colunas para as análises na visão por 'PAÍS':
# =======================================================================================================================================================

#   Main Dataframe - Países:
# =======================================================================================================================================================

vGroupByCountry = pd.DataFrame( DBI.groupby( 'PAIS' ).agg( { 
        'TMP_JGD' : 'max', 
        'JOGOS' : 'max', 
        'GOLS' : 'sum', 
        'ASSIST' : 'sum' ,
        'DIST_PERC' : 'sum'
    } ).reset_index( ) )
vGroupByCountry[ 'JOGOS' ].replace( 5, 6, inplace = True)
vGroupByCountry[ 'JOGOS' ].replace( 7, 8, inplace = True)
vGroupByCountry[ 'JOGOS' ].replace( 9, 10, inplace = True)
vGroupByCountry[ 'MED_GOLS' ] = round( vGroupByCountry[ 'GOLS' ] / vGroupByCountry[ 'JOGOS' ], 2 )
vGroupByCountry[ 'MED_ASSIST' ] = round( vGroupByCountry[ 'ASSIST' ] / vGroupByCountry[ 'JOGOS' ], 2 )
vGroupByCountry[ 'MIN_P_GOL' ] = round( vGroupByCountry[ 'TMP_JGD' ] / vGroupByCountry[ 'GOLS' ], 2 )
vGroupByCountry[ 'MED_DIST_PERC' ] = round( vGroupByCountry[ 'DIST_PERC' ] / vGroupByCountry[ 'JOGOS' ], 2 )

#   Dataframes auxiliares:
# =======================================================================================================================================================

vGoalsByCountry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'GOLS' } ).sort_values( by = [ 'GOLS', 'PAIS' ], ascending=[ False, True ] ) \
    .reset_index( drop = True )
vAssistsByCountry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'ASSIST' } ).sort_values( by = [ 'ASSIST', 'PAIS' ], ascending=[ False, True\
      ] ).reset_index( drop = True )
vAvgGoalsByCountry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'MED_GOLS' } ).sort_values( by = [ 'MED_GOLS', 'PAIS' ], ascending=[ False,\
     True ] ).reset_index( drop = True )
vAvgAssistsByCountry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'MED_ASSIST' } ).sort_values( by = [ 'MED_ASSIST', 'PAIS' ], ascending=[ \
    False, True ] ).reset_index( drop = True )
vDistPercbyContry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'DIST_PERC' } ).sort_values( by = [ 'DIST_PERC', 'PAIS' ], ascending=[ \
    False, True ] ).reset_index( drop = True )
vAvgDistPercbyCountry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'MED_DIST_PERC' } ).sort_values( by = [ 'MED_DIST_PERC', 'PAIS' ], ascending=[\
    False, True ] ).reset_index( drop = True )
vMinToGoalbyCountry = vGroupByCountry.filter( items = { 'PAIS', 'SIGLA_PAIS', 'MIN_P_GOL' } ).sort_values( by = [ 'MIN_P_GOL', 'PAIS' ], ascending=[\
    True, True ] ).reset_index( drop = True )

# =======================================================================================================================================================
# Criação de dataframes e inclusão de colunas para as análises na visão por 'TIMES':
# =======================================================================================================================================================

#   Main Dataframe - Times:
# =======================================================================================================================================================

vGroupByTeam = pd.DataFrame( DBI.groupby( 'NM_TIME' ).agg( { 
        'TMP_JGD' : 'max', 
        'JOGOS' : 'max', 
        'GOLS' : 'sum', 
        'ASSIST' : 'sum' ,
        'DIST_PERC' : 'sum'
    } ).reset_index( ) )
vGroupByTeam = vGroupByTeam.merge( df_InfosTimes, on = 'NM_TIME', how = 'outer' )
vGroupByTeam[ 'JOGOS' ].replace( 5, 6, inplace = True)
vGroupByTeam[ 'JOGOS' ].replace( 7, 8, inplace = True)
vGroupByTeam[ 'JOGOS' ].replace( 9, 10, inplace = True)
vGroupByTeam[ 'MED_GOLS' ] = round( vGroupByTeam[ 'GOLS' ] / vGroupByTeam[ 'JOGOS' ], 2 )
vGroupByTeam[ 'MED_ASSIST' ] = round( vGroupByTeam[ 'ASSIST' ] / vGroupByTeam[ 'JOGOS' ], 2 )
vGroupByTeam[ 'MIN_P_GOL' ] = round( vGroupByTeam[ 'TMP_JGD' ] / vGroupByTeam[ 'GOLS' ], 2 )
vGroupByTeam[ 'MED_DIST_PERC' ] = round( vGroupByTeam[ 'DIST_PERC' ] / vGroupByTeam[ 'JOGOS' ], 2 )

#   Dataframes auxiliares:
# =======================================================================================================================================================

vGoalsByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'GOLS' } ).sort_values( by = [ 'GOLS', 'NM_REAL' ], ascending=[ False, True ] ) \
    .reset_index( drop = True )
vAssistsByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'ASSIST' } ).sort_values( by = [ 'ASSIST', 'NM_REAL' ], ascending=[ False, True\
      ] ).reset_index( drop = True )
vAvgGoalsByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'MED_GOLS' } ).sort_values( by = [ 'MED_GOLS', 'NM_REAL' ], ascending=[ False,\
     True ] ).reset_index( drop = True )
vAvgAssistsByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'MED_ASSIST' } ).sort_values( by = [ 'MED_ASSIST', 'NM_REAL' ], ascending=[ \
    False, True ] ).reset_index( drop = True )
vDistPercTotalByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'DIST_PERC' } ).sort_values( by = [ 'DIST_PERC', 'NM_REAL' ], ascending=[ \
    False, True ] ).reset_index( drop = True )
vAvgDistPercByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'MED_DIST_PERC' } ).sort_values( by = [ 'MED_DIST_PERC', 'NM_REAL' ], ascending=[\
    False, True ] ).reset_index( drop = True )
vMinToGoalByTeam = vGroupByTeam.filter( items = { 'NM_REAL', 'SIGLA_PAIS', 'MIN_P_GOL' } ).sort_values( by = [ 'MIN_P_GOL', 'NM_REAL' ], ascending=[\
    True, True ] ).reset_index( drop = True )
# =======================================================================================================================================================
# Criação de dataframes e inclusão de colunas para as análises na visão por 'JOGADOR':
# =======================================================================================================================================================

#   Dataframes auxiliares:
# =======================================================================================================================================================

vGoalsByPlayer = DBI.filter( items = { 'DESC_JOG', 'GOLS' } ).sort_values( by = [ 'GOLS', 'DESC_JOG' ], ascending=[ False, True ] ) \
    .reset_index( drop = True )
vAssistsByPlayer = DBI.filter( items = { 'DESC_JOG', 'ASSIST' } ).sort_values( by = [ 'ASSIST', 'DESC_JOG' ], ascending=[ False, True\
      ] ).reset_index( drop = True )
vAvgGoalsByPlayer = DBI.filter( items = { 'DESC_JOG', 'MED_GOLS' } ).sort_values( by = [ 'MED_GOLS', 'DESC_JOG' ], ascending=[ False,\
     True ] ).reset_index( drop = True )
vAvgAssistsByPlayer = DBI.filter( items = { 'DESC_JOG', 'MED_ASSIST' } ).sort_values( by = [ 'MED_ASSIST', 'DESC_JOG' ], ascending=[ \
    False, True ] ).reset_index( drop = True )
vDistPercByPlayer = DBI.filter( items = { 'DESC_JOG', 'DIST_PERC' } ).sort_values( by = [ 'DIST_PERC', 'DESC_JOG' ], ascending=[ \
    False, True ] ).reset_index( drop = True )
vAvgDistPercByPlayer = DBI.filter( items = { 'DESC_JOG', 'MED_DIST_PERC' } ).sort_values( by = [ 'MED_DIST_PERC', 'DESC_JOG' ], ascending=[\
    False, True ] ).reset_index( drop = True )
vMinToGoalByPlayer = DBI.filter( items = { 'DESC_JOG', 'MIN_P_GOL' } ).sort_values( by = [ 'MIN_P_GOL', 'DESC_JOG' ], ascending=[\
    True, True ] ).reset_index( drop = True )

# =======================================================================================================================================================
# IMPRESSÃO DOS RESULTADOS DAS ANÁLISES:
# =======================================================================================================================================================

print('Análise de Indicadores - UCL 21/22; ')
print('Visão / Times: ')
print('-')
print('#01 - Maior número de Gols: ' + vGoalsByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vGoalsByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' + str( \
    vGoalsByTeam[ 'GOLS' ].iloc[ 0 ] ) + ') ;' )
print('#02 - Maior número de Assist.: ' + vAssistsByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vAssistsByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' + str( \
    vAssistsByTeam[ 'ASSIST' ].iloc[ 0 ] ) + ') ;' )
print('#03 - Maior média de Gols: ' + vAvgGoalsByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vAvgGoalsByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' + str( \
    vAvgGoalsByTeam[ 'MED_GOLS' ].iloc[ 0 ] ) + ') ;' )
print('#04 - Maior média de Assist.: ' + vAvgAssistsByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vAvgAssistsByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' + \
    str( vAvgAssistsByTeam[ 'MED_ASSIST' ].iloc[ 0 ] ) + ') ;' )
print('#05 - Maior distância corrida: ' + vDistPercTotalByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vDistPercTotalByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' +\
    str( vDistPercTotalByTeam[ 'DIST_PERC' ].iloc[ 0 ] ) + ') ;' )
print('#06 - Maior média de dist. corrida: ' + vAvgDistPercByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vAvgDistPercByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' +\
    str( vAvgDistPercByTeam[ 'MED_DIST_PERC' ].iloc[ 0 ] ) + ') ;' )
print('#07 - Menor tempo para marcar Gol: ' + vMinToGoalByTeam[ 'NM_REAL' ].iloc[ 0 ] + '/' + vMinToGoalByTeam[ 'SIGLA_PAIS' ].iloc[ 0 ] + ' (' +\
    str( vMinToGoalByTeam[ 'MIN_P_GOL' ].iloc[ 0 ] ) + ') ;' )
print('-')
print('=====================================================================================================================================')
print('-')
print('Visão / Países: ')
print('-')
print('#01 - Maior número de Gols: ' + vGoalsByCountry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vGoalsByCountry[ 'GOLS' ].iloc[ 0 ] ) + ') ;' )
print('#02 - Maior número de Assist.: ' + vAssistsByCountry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vAssistsByCountry[ 'ASSIST' ].iloc[ 0 ] ) + ') ;' )
print('#03 - Maior média de Gols: ' + vAvgGoalsByCountry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vAvgGoalsByCountry[ 'MED_GOLS' ].iloc[ 0 ] ) + ') ;' )
print('#04 - Maior média de Assist.: ' + vAvgAssistsByCountry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vAvgAssistsByCountry[ 'MED_ASSIST' ].iloc[ 0 ] ) + ') ;' )
print('#05 - Maior distância corrida: ' + vDistPercbyContry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vDistPercbyContry[ 'DIST_PERC' ].iloc[ 0 ] ) + ') ;' )
print('#06 - Maior média de dist. corrida: ' + vAvgDistPercbyCountry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vAvgDistPercbyCountry[ 'MED_DIST_PERC' ].iloc[ 0 ] ) + ') ;' )
print('#07 - Menor tempo para marcar Gol: ' + vMinToGoalbyCountry[ 'PAIS' ].iloc[ 0 ] + ' (' + str( vMinToGoalbyCountry[ 'MIN_P_GOL' ].iloc[ 0 ] ) + ') ;' )
print('-')
print('=====================================================================================================================================')
print('-')
print('Visão / Jogadores: ')
print('-')
print('#01 - Maior número de Gols: ' + vGoalsByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vGoalsByPlayer[ 'GOLS' ].iloc[ 0 ] ) + ') ;' )
print('#02 - Maior número de Assist.: ' + vAssistsByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vAssistsByPlayer[ 'ASSIST' ].iloc[ 0 ] ) + ') ;' )
print('#03 - Maior média de Gols: ' + vAvgGoalsByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vAvgGoalsByPlayer[ 'MED_GOLS' ].iloc[ 0 ] ) + ') ;' )
print('#04 - Maior média de Assist.: ' + vAvgAssistsByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vAvgAssistsByPlayer[ 'MED_ASSIST' ].iloc[ 0 ] ) + ') ;' )
print('#05 - Maior distância corrida: ' + vDistPercByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vDistPercByPlayer[ 'DIST_PERC' ].iloc[ 0 ] ) + ') ;' )
print('#06 - Maior média de dist. corrida: ' + vAvgDistPercByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vAvgDistPercByPlayer[ 'MED_DIST_PERC' ].iloc[ 0 ] ) + ') ;' )
print('#07 - Menor tempo para marcar Gol: ' + vMinToGoalByPlayer[ 'DESC_JOG' ].iloc[ 0 ] + ' (' + str( vMinToGoalByPlayer[ 'MIN_P_GOL' ].iloc[ 0 ] ) + ') ;' )
print('-')