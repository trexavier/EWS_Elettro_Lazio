# Questo modulo gestisce la creazione degli scenari con risoluzione 0.25 e 0.1 gradi
# su scala regionale

# Importa moduli Python
import folium
from folium.plugins import GroupedLayerControl, MousePosition,MeasureControl,HeatMap
import geopandas as gpd
from branca.colormap import linear, LinearColormap, StepColormap
import pandas as pd
import io
import os
from PIL import Image

# Per le ondate di calore non è disponibile una statistica dei guasti. I guasti attesi vengono
# stimati moltiplicando il generico "guasti medi" per il valore restituito dalla funzione sotto,
# che riceve come argomento l'indice settimanale dell'ondata di calore
def guasti_hw(indice):
       if (indice<=10): return 1 # guasti medi del periodo
       if (indice==11): return 2 # il doppio dei guasti medi del periodo
       if (indice==12): return 3 # ....il triplo
       if (indice==13): return 4 # ....quadruplo
       if (indice==14): return 5 # massima ondata di calore, 5 volte i guasti medi

# Restituisce la stima degli elementi elettrici che subiranno un guasti (vulnerabilità)
def elementi_prob_guasto(percentuale, tot_elementi):
       if (percentuale==0): return 0
       else:
           return round((tot_elementi/100)*percentuale)


#--------------------------------------INIZIO DATI METEO----------------------------------------------------

# Elabora la mappa visualizzando i valori previsionali della temperatura nella regione (previsione 7gg)
def elabora_solo_meteo_temperatura(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    colormap= LinearColormap(colors=["violet", "darkblue", "blue", "cyan","green", "yellow", "orange", "red"],
                             index=[-20, -10, -5, 0, 11, 22, 33, 40],
                             tick_labels=[-20, -10, -5, 0, 11, 22, 33, 40],
                             vmin=-20, vmax=50)
    colormap.caption = "Temperatura massima prevista (°C)"
    colormap.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather('./conf/rete_elettrica/LAZIO_rete_elettrica.feather')
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         #vecchio codice per le cabine primarie
         #layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         #df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         #gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Lon, df.Lat), crs="EPSG:4326")
         #folium.GeoJson(
         #gdf,
         #marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
         #tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )#.add_to(layer_giorno1)
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           temperatura=dataframe.at[i,'temperature_2m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(temperatura),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())
    testo=""
    if(dataframe.at[1,'bk_temperature_2m_max']!=dataframe.at[1,'temperature_2m_max']):
                testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>Temperature massime previste (°C)</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno7) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')    
    





# Elabora la mappa visualizzando i valori previsionali del vento nella regione (previsione 7gg)
def elabora_solo_meteo_vento(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["darkgreen", "forestgreen","lightgreen","greenyellow","lemonchiffon","khaki","yellow","orange","darkorange","orangered","red","firebrick","mediumvioletred"], 
                       vmin=0, vmax=40, index=[0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7], caption="step")
    step.caption = "Vento massimo previsto (m/s)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather('./conf/rete_elettrica/LAZIO_rete_elettrica.feather')
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)

         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )#.add_to(layer_giorno1)
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           vento=dataframe.at[i,'wind_speed_10m_max']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(vento),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "m/s "+str(vento)))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 310px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Scala Beaufort (m/s)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:darkgreen"></i>&nbsp;Calma (<0.3)
    <br>&nbsp;<i class="fa fa-circle" style="color:forestgreen"></i>&nbsp;Bava di vento (0.3-1.5)
    <br>&nbsp;<i class="fa fa-circle" style="color:lightgreen"></i>&nbsp;Brezza leggera (1.6-3.3)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Brezza (3.4-5.4)
    <br>&nbsp;<i class="fa fa-circle" style="color:lemonchiffon"></i>&nbsp;Brezza vivace (5.5-7.9)
    <br>&nbsp;<i class="fa fa-circle" style="color:khaki"></i>&nbsp;Brezza tesa (8-10.7)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Vento fresco (10.8-13.8)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Vento forte (13.9-17.1)
    <br>&nbsp;<i class="fa fa-circle" style="color:darkorange"></i>&nbsp;Burrasca moderata (17.2-20.7)
    <br>&nbsp;<i class="fa fa-circle" style="color:orangered"></i>&nbsp;Burrasca forte (20.8-24.4)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Tempesta (24.5-28.4)
    <br>&nbsp;<i class="fa fa-circle" style="color:firebrick"></i>&nbsp;Fortunale (28.5-32.6)
    <br>&nbsp;<i class="fa fa-circle" style="color:mediumvioletred"></i>&nbsp;Uragano (>32.7))
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))

    testo=""
    if(dataframe.at[1,'bk_wind_speed_10m_max']!=dataframe.at[1,'wind_speed_10m_max']):
            testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>Vento massimo previsto (m/s)</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno7) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')    








# Elabora la mappa visualizzando i valori previsionali della pioggia caduta nella regione (previsione 7gg)
def elabora_solo_meteo_pioggia(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    colormap = linear.Greys_09.scale(0,60)
    colormap.caption=("Tot pioggia giorno (mm)")
    colormap.add_to(my_map)
    
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather('./conf/rete_elettrica/LAZIO_rete_elettrica.feather')
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)

         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           pioggia_sum=dataframe.at[i,'rain_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(pioggia_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())
    testo=""
    if(dataframe.at[1,'bk_rain_sum']!=dataframe.at[1,'rain_sum']):
                testo="Simulazione"
             
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>Totale pioggia prevista (mm)</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno7) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')








# Elabora la mappa visualizzando i valori previsionali della neve caduta nella regione (previsioni 7gg)
def elabora_solo_meteo_neve(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    colormap = linear.Greys_09.scale(0,100)
    colormap.caption=("Tot neve giorno (mm)")
    colormap.add_to(my_map)
    
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather('./conf/rete_elettrica/LAZIO_rete_elettrica.feather')
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)

         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           neve_sum=dataframe.at[i,'snowfall_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(neve_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())
    testo=""
    if(dataframe.at[1,'bk_snowfall_sum']!=dataframe.at[1,'snowfall_sum']):
                testo="Simulazione"
             
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>Totale neve prevista (mm)</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno7) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')





# Elabora la mappa visualizzando i valori delle precipitazioni cadute nella regione (tot pioggia, neve, grandine....previsione 7gg)
def elabora_solo_meteo_precipitazioni(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    colormap = linear.Blues_09.scale(0,60)
    colormap.caption=("Tot precipitazioni giorno (mm)")
    colormap.add_to(my_map)
    
    
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather('./conf/rete_elettrica/LAZIO_rete_elettrica.feather')
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)

         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           precipitation_sum=dataframe.at[i,'precipitation_sum']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= colormap(precipitation_sum),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + "mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())
    testo=""
    if(dataframe.at[1,'bk_precipitation_sum']!=dataframe.at[1,'precipitation_sum']):
                testo="Simulazione"
             
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>Totali precipitazioni previste (mm)</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno7) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')
    
#--------------------------------------FINE DATI METEO----------------------------------------------------















#-------------------------------------- ANALISI VULNERABILITA' --------------------------------------
# ONDATA DI CALORE LINEA INTERRATA
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata all'indice settimanale
# dell'ondata di calore prevista (indice ARERA 7gg),
# -Tooltip con estensione linea interrata presente (metri), indice ondata di calore, guasti attesi
def elabora_evento_hw(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', min_zoom=8, max_zoom=14, zoom_start=9,overlay=False).add_to(my_map)  

    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)

    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)

    

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    grouped=dataframe.groupby(by=['lat','lon','geometry']).agg(hwwi=('hwdi', 'sum'),hwwi_HM=('hwdi_HM','sum'), linea_presente=('m_power_cable','first'))
    grouped_dataframe=grouped.reset_index()
    
    step_color= StepColormap(["green","orange","red"], vmin=0, vmax=14, index=[0, 11, 13], caption="step")
    step_color.caption = "Indice settimanale ondata di calore"
    step_color.add_to(my_map)
            
    layer_HW = folium.FeatureGroup('Indice heat wave',overlay=False).add_to(my_map)
    for i in range (0,step):
           linea=(grouped_dataframe.at[i,'linea_presente'])
           poligono=(grouped_dataframe.at[i,'geometry'])
           indice_settimanale_hwwi=grouped_dataframe.at[i,'hwwi']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step_color(indice_settimanale_hwwi),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>"+"hwwi: " + str(indice_settimanale_hwwi) + "<br>" + 
                                          "linea (m): " + str(linea) + "<br>" +
                                          "guasti previsti: guasti medi x " + str(guasti_hw(indice_settimanale_hwwi))))
           geo_j.add_to(layer_HW)


    #GENERA HEAT MAP PER IMMAGINE RISCHIO
    if num_rows==385:#poligoni 025
         heat_map_rischio = folium.Map(location=[41.8, 12.7],width=300,height=300,tiles='cartodbpositron', zoom_start=7, zoom_control=False)
    if num_rows==1155: #poligoni 01
         heat_map_rischio = folium.Map(location=[41.8, 12.7],width=600,height=600,tiles='cartodbpositron', zoom_start=8, zoom_control=False)        

    layer_confini_regione_hw = folium.FeatureGroup("Lazio confini", control=False).add_to(heat_map_rischio)
    
    gradiente={'0':'Navy','0.14':'Darkblue','0.28':'Blue','0.42':'Cyan','0.57':'Green','0.71':'Yellow','0.85':'Orange','1':'Red'}
    HeatMap(grouped_dataframe[['lat','lon','hwwi_HM']],         
        min_opacity=0,
        max_zoom=8,
        radius=20,
        blur = 15,
        scale_radius=True,
        gradient=gradiente,
        overlay=True,
               ).add_to(heat_map_rischio)    
    
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione_hw)
    
    png=heat_map_rischio._to_png()
    image = Image.open(io.BytesIO(png))
    filename = os.path.join("./conf/img/", "hw_ondata_calore.png".format(i))
    image.save(filename, "PNG")
    #FINE ---- GENERA HEAT MAP PER IMMAGINE RISCHIO

    folium.LayerControl(collapsed=False).add_to(my_map)
    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    if rete==1:
         
         layer_linea_interrata = folium.FeatureGroup("Linea interrata",overlay=True, show=False).add_to(my_map)
         dataframe_linea_interrata = gpd.read_feather('./conf/rete_elettrica/Lazio_power_cable.feather')
         folium.GeoJson(dataframe_linea_interrata,
                        style_function=lambda feature: {
                        "color": "red",
                        "weight": 1,
                        "fillOpacity": 0.9},
                        zoom_on_click=True).add_to(layer_linea_interrata)

         GroupedLayerControl(groups={'rete elettrica': [layer_linea_interrata]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    
    GroupedLayerControl(groups={'Ondata di calore': [layer_HW]},collapsed=False,).add_to(my_map)    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())
    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 200px; height: 100px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Ondata di calore</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Bassa (0-10)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Moderata (11-12)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Intensa (13-14)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_temperature_2m_max']!=dataframe.at[1,'temperature_2m_max']) or (dataframe.at[1,'bk_precipitation_sum']!=dataframe.at[1,'precipitation_sum']):
                testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 650px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ONDATA DI CALORE - Rischio guasti linea interrata prossimi 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')







# TEMPERATURE ELEVATE TRASFORMATORI DI POTENZA
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata alla riduzione vita dei componenti presenti (7gg)
# -Tooltip con max temp raggiunte (°C), % riduz vita, numero di trasformatori impattati
def elabora_evento_hw_trasformatore_p(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
    step.caption = "Decadimento prestazioni trasformatore di potenza 65 rise (%)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor='#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_trasformatori_potenza = folium.FeatureGroup("Tras. potenza",overlay=True, show=False).add_to(my_map)
         dataframe_trasformatori_potenza = gpd.read_feather('./conf/rete_elettrica/LAZIO_trasformatori_potenza.feather')
         geodataframe_trasformatori_potenza = gpd.GeoDataFrame(dataframe_trasformatori_potenza)
         folium.GeoJson(geodataframe_trasformatori_potenza,marker=folium.CircleMarker(radius=2, fill_color="red", 
                                                                         fill_opacity=0.8, color="black", weight=2)).add_to(layer_trasformatori_potenza)
         
         GroupedLayerControl(groups={'rete elettrica': [layer_trasformatori_potenza]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           life_tp65=dataframe.at[i,'tp65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_tp65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_tp65) + "<br>" +
                                          "trasf. potenza impattati: " + str(dataframe.at[i,'num_tp'])))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 140px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Riduzione vita (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (0-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (20-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (40-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (60-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (80-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_temperature_2m_max']!=dataframe.at[1,'temperature_2m_max']):
             testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 750px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ONDATA DI CALORE - Previsione riduzione vita trasformatori di potenza (65rise) 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')







# TEMPERATURE ELEVATE TRASFORMATORI DI DISTRIBUZIONE
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata alla riduzione vita dei componenti presenti (7gg)
# -Tooltip con max temp raggiunte (°C), % riduz vita, numero di trasformatori impattati
def elabora_evento_hw_trasformatore_d(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
    step.caption = "Decadimento prestazioni trasformatore di distribuzione 65 rise (%)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor='#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_trasformatori_distribuzione = folium.FeatureGroup("Tras. distribuzione",overlay=True, show=False).add_to(my_map)
         dataframe_trasformatori_distribuzione = gpd.read_feather('./conf/rete_elettrica/LAZIO_trasformatori_distribuzione.feather')
         geodataframe_trasformatori_distribuzione = gpd.GeoDataFrame(dataframe_trasformatori_distribuzione)
         folium.GeoJson(geodataframe_trasformatori_distribuzione, marker=folium.CircleMarker(radius=2, fill_color="red", 
                                                                         fill_opacity=0.8, color="black", weight=2)).add_to(layer_trasformatori_distribuzione)
         GroupedLayerControl(groups={'rete elettrica': [layer_trasformatori_distribuzione]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           life_td65=dataframe.at[i,'td65']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(life_td65),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "max temp °C: " + str(dataframe.at[i,'temperature_2m_max']) + "<br>" +
                                          "riduz. vita %: " + str(life_td65) + "<br>" +
                                          "trasf. distribuzione impattati: " + str(dataframe.at[i,'num_td'])))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 140px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Riduzione vita (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (0-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (20-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (40-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (60-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (80-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_temperature_2m_max']!=dataframe.at[1,'temperature_2m_max']):
             testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 780px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ONDATA DI CALORE - Previsione riduzione vita trasformatori di distribuzione (65rise) 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')
    




# FORTE VENTO TRALICCI
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata alla probabilità di guasto dei componenti presenti (7gg)
# -Tooltip con max velocità vento (m/s), % prob guasto, numero tralicci presenti, stima num tralicci guasti
def elabora_evento_vento_tralicci(rete,dataframe):
        
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
    step.caption = "Probabilità guasto tralicci (%)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor='#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_tralicci = folium.FeatureGroup("Tralicci",overlay=True, show=False).add_to(my_map)
         dataframe_tralicci = gpd.read_feather('./conf/rete_elettrica/Lazio_tralicci.feather')
         geodataframe_tralicci = gpd.GeoDataFrame(dataframe_tralicci)
         folium.GeoJson(geodataframe_tralicci,marker=folium.CircleMarker(radius=2, fill_color="red", fill_opacity=0.8, color="black", weight=2)).add_to(layer_tralicci)         
         
         GroupedLayerControl(groups={'rete elettrica': [layer_tralicci]},collapsed=False,exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           prob_tralicci=dataframe.at[i,'prob_tralicci']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_tralicci),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_tralicci) + "<br>" +
                                          "Tralicci presenti: " + str(dataframe.at[i,'num_tralicci']) + "<br>" +
                                          "Tralicci guasti (stima): " + str(elementi_prob_guasto(prob_tralicci, dataframe.at[i,'num_tralicci']))))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 140px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Prob. guasto (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (0-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (20-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (40-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (60-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (80-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_wind_speed_10m_max']!=dataframe.at[1,'wind_speed_10m_max']):
             testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>VENTO - Previsione rischio guasti tralicci prossimi 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')






# FORTE VENTO LINEA SOSPESA (LINEA ESTERNA)
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata alla probabilità di guasto della linea esterna presente (7gg)
# -Tooltip con max velocità vento (m/s), % prob guasto, 
# metri linea esterna presente, stima metri linea esterna guasta
def elabora_evento_vento_linea_esterna(rete,dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
    step.caption = "Probabilità guasto linea esterna (%)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_power_line = folium.FeatureGroup("Linea AT/MT",overlay=True, show=False).add_to(my_map)
         dataframe_power_line = gpd.read_feather('./conf/rete_elettrica/Lazio_power_line.feather')
         folium.GeoJson(dataframe_power_line,
                        style_function=lambda feature: {
                        "color": "black",
                        "weight": 1,
                        "fillOpacity": 0.9},
                        zoom_on_click=True).add_to(layer_power_line)

         GroupedLayerControl(groups={'rete elettrica': [layer_power_line]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna=dataframe.at[i,'prob_linea_esterna']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (stima m): " + str(elementi_prob_guasto(prob_linea_esterna, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 140px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Prob. guasto (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (0-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (20-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (40-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (60-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (80-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_wind_speed_10m_max']!=dataframe.at[1,'wind_speed_10m_max']):
             testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 550px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>VENTO - Previsione rischio guasti linea esterna prossimi 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')




# GHIACCIO LINEA SOSPESA (LINEA ESTERNA)
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata alla probabilità di guasto della linea esterna presente (7gg)
# -Tooltip con stima ghiaccio accumulato (mm), % prob guasto, 
# metri linea esterna presente, stima metri linea esterna guasta
def elabora_evento_ghiaccio_linea_esterna(rete, dataframe):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
    step.caption = "Probabilità guasto linea esterna (%)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_power_line = folium.FeatureGroup("Linea elettrica AT/MT",overlay=True, show=False).add_to(my_map)
         dataframe_power_line = gpd.read_feather('./conf/rete_elettrica/Lazio_power_line.feather')
         folium.GeoJson(dataframe_power_line,
                        style_function=lambda feature: {
                        "color": "black",
                        "weight": 1,
                        "fillOpacity": 0.9},
                        zoom_on_click=True).add_to(layer_power_line)

         GroupedLayerControl(groups={'rete elettrica': [layer_power_line]},collapsed=False,
                             exclusive_groups=False).add_to(my_map)
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )#.add_to(layer_giorno1)
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" +
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           prob_linea_esterna_ice=dataframe.at[i,'prob_linea_esterna_ice']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_linea_esterna_ice),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Ghiaccio sui cavi mm:" + str(dataframe.at[i,'m_mm']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_linea_esterna_ice) + "<br>" +
                                          "Tot linea sospesa (m): " + str(dataframe.at[i,'m_power_line']) + "<br>" +
                                          "Linea guasta (m): " + str(elementi_prob_guasto(prob_linea_esterna_ice, dataframe.at[i,'m_power_line']))))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 140px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Prob. guasto (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (0-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (20-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (40-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (60-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (80-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_wind_speed_10m_max']!=dataframe.at[1,'wind_speed_10m_max']) or \
          (dataframe.at[1,'bk_precipitation_sum']!=dataframe.at[1,'precipitation_sum']) or \
          (dataframe.at[1,'bk_precipitation_hours']!=dataframe.at[1,'precipitation_hours']) or \
          (dataframe.at[1,'M_mm']!=15):
             testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 600px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>GHIACCIO - Previsione probabilità guasto linea esterna prossimi 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')




# VENTO PALI DI SERVIZIO
# Elabora la mappa visualizzando poligoni di superficie 0.25 o 0.1 gradi.
# Per ciascun poligono:
# -Colorato con scala cromatica correlata alla probabilità di guasto dei pali di servizio presente (7gg)
# -Tooltip con max velocità del vento (m/s), % prob guasto, 
# numero pali presenti, stima numero pali guasti
def elabora_evento_vento_pali(rete, dataframe, tipo_palo, pali_anni):
    num_rows=len(dataframe)
    if num_rows==385:#poligoni 025
         step=55;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step
    if num_rows==1155: #poligoni 01
         step=165;g1=0;g2=g1+step;g3=g2+step;g4=g3+step;g5=g4+step;g6=g5+step;g7=g6+step;g8=g7+step

    my_map = folium.Map(location=[42.00, 13.00],min_zoom=8, max_zoom=14, zoom_start=9)
    folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
    step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
    step.caption = "Probabilità guasto pali di servizio (%)"
    step.add_to(my_map)
    layer_confini_regione = folium.FeatureGroup("Lazio confini", control=False, show=True).add_to(my_map)
    df = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    for _, r in df.iterrows():
           sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(data=geo_j, color='black', weight=2, fillColor= '#00000000')
           geo_j.add_to(layer_confini_regione)
    folium.LayerControl(collapsed=False).add_to(my_map)
    
    layer_comuni_regione = folium.FeatureGroup("Lazio comuni").add_to(my_map)    
    layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
    layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
    layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
    layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
    layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
    layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
    layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
    layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
    layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
    layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)

    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    for _, r in df.iterrows():
               sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
               geo_j = sim_geo.to_json()
               geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
               folium.Popup(r["COMUNE"]).add_to(geo_j)
               geo_j.add_to(layer_comuni_regione)
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)

    
    df = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    for _, r in df.iterrows():
           if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
           if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
           if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
           if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
           if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)

    GroupedLayerControl(groups={'confini': [layer_confini_regione,layer_comuni_regione,\
                                            layer_comuni_provincia_viterbo,layer_comuni_provincia_rieti,layer_comuni_provincia_roma,\
                                            layer_comuni_provincia_latina,layer_comuni_provincia_frosinone,\
                                            layer_provincia_viterbo,layer_provincia_rieti, layer_provincia_roma,\
                                            layer_provincia_latina,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    
    if rete==1:
         layer_pali = folium.FeatureGroup("Pali",overlay=True, show=False).add_to(my_map)
         dataframe_pali = gpd.read_feather('./conf/rete_elettrica/Lazio_pali.feather')
         geodataframe_pali = gpd.GeoDataFrame(dataframe_pali)
         folium.GeoJson(geodataframe_pali,marker=folium.CircleMarker(radius=2, fill_color="red", fill_opacity=0.8, color="black", weight=2)).add_to(layer_pali)         
         
         GroupedLayerControl(groups={'rete elettrica': [layer_pali]},collapsed=False,exclusive_groups=False).add_to(my_map)
                  
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )#.add_to(layer_giorno1)
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno3)
    
    giorno4=(dataframe.at[g4,'giorno'])
    layer_giorno4 = folium.FeatureGroup(str(giorno4),overlay=False).add_to(my_map)
    for i in range (g4,g5):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno4)
    
    giorno5=(dataframe.at[g5,'giorno'])
    layer_giorno5 = folium.FeatureGroup(str(giorno5),overlay=False).add_to(my_map)
    for i in range (g5,g6):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno5)
              
    giorno6=(dataframe.at[g6,'giorno'])
    layer_giorno6 = folium.FeatureGroup(str(giorno6),overlay=False).add_to(my_map)
    for i in range (g6,g7):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno6)

    giorno7=(dataframe.at[g7,'giorno'])
    layer_giorno7 = folium.FeatureGroup(str(giorno7),overlay=False).add_to(my_map)
    for i in range (g7,g8):
           poligono=(dataframe.at[i,'geometry'])
           if (tipo_palo=="legno_acciaio" and pali_anni==0): prob_pali=dataframe.at[i,'prob_pali_la_nuovi']
           if (tipo_palo=="legno" and pali_anni==20): prob_pali=dataframe.at[i,'prob_pali_l_20']
           if (tipo_palo=="legno" and pali_anni==40): prob_pali=dataframe.at[i,'prob_pali_l_40']
           if (tipo_palo=="legno" and pali_anni==60): prob_pali=dataframe.at[i,'prob_pali_l_60']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(prob_pali),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
               )
           geo_j.add_child(folium.Tooltip("<font size='4'>" + 
                                          "Max vel. vento m/s:" + str(dataframe.at[i,'wind_speed_10m_max']) + "<br>" +
                                          "Prob. guasto (%) " + str(prob_pali) + "<br>" +
                                          "Pali presenti: " + str(dataframe.at[i,'num_pali']) + "<br>" +
                                          "Pali guasti (stima): " + str(elementi_prob_guasto(prob_pali, dataframe.at[i,'num_pali']))))
           geo_j.add_to(layer_giorno7)    
    
    
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3, layer_giorno4, \
                                                layer_giorno5, layer_giorno6, layer_giorno7]},collapsed=False,).add_to(my_map)      
    

    formatter = "function(num) {return L.Util.formatNum(num, 2) + ' &deg; ';};"
    MousePosition(
    position="bottomright",
    separator=" | ",
    empty_string="NaN",
    lng_first=False,
    num_digits=20,
    prefix="Coordinate:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(my_map)

    my_map.add_child(MeasureControl())

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 140px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Prob. guasto (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (0-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (20-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (40-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (60-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (80-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    if(dataframe.at[1,'bk_wind_speed_10m_max']!=dataframe.at[1,'wind_speed_10m_max']):
             testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 750px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>VENTO - Previsione rischio guasti pali ''' + tipo_palo + ''' ''' + str(pali_anni) + '''anni prossimi 7gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')