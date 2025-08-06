
import folium
from folium.plugins import GroupedLayerControl, MousePosition,MeasureControl,HeatMap
import geopandas as gpd
from branca.colormap import linear, LinearColormap, StepColormap
import pandas as pd
import io
import os
from PIL import Image
import math




#--------------------------------------INIZIO DATI METEO----------------------------------------------------

#elabora la mappa visualizzando i valori previsionali della temperatura nella provincia scelta (previsione 3gg)
def elabora_solo_meteo_temperatura_provincia(rete, dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap= LinearColormap(colors=["violet", "darkblue", "blue", "cyan","green", "yellow", "orange", "red"],
                             index=[-20, -10, -5, 0, 11, 22, 33, 40],
                             tick_labels=[-20, -10, -5, 0, 11, 22, 33, 40],
                             vmin=-20, vmax=50)
         colormap.caption = "Temperatura massima prevista (°C)"
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap= LinearColormap(colors=["violet", "darkblue", "blue", "cyan","green", "yellow", "orange", "red"],
                             index=[-20, -10, -5, 0, 11, 22, 33, 40],
                             tick_labels=[-20, -10, -5, 0, 11, 22, 33, 40],
                             vmin=-20, vmax=50)
         colormap.caption = "Temperatura massima prevista (°C)"
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap= LinearColormap(colors=["violet", "darkblue", "blue", "cyan","green", "yellow", "orange", "red"],
                             index=[-20, -10, -5, 0, 11, 22, 33, 40],
                             tick_labels=[-20, -10, -5, 0, 11, 22, 33, 40],
                             vmin=-20, vmax=50)
         colormap.caption = "Temperatura massima prevista (°C)"
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap= LinearColormap(colors=["violet", "darkblue", "blue", "cyan","green", "yellow", "orange", "red"],
                             index=[-20, -10, -5, 0, 11, 22, 33, 40],
                             tick_labels=[-20, -10, -5, 0, 11, 22, 33, 40],
                             vmin=-20, vmax=50)
         colormap.caption = "Temperatura massima prevista (°C)"
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap= LinearColormap(colors=["violet", "darkblue", "blue", "cyan","green", "yellow", "orange", "red"],
                             index=[-20, -10, -5, 0, 11, 22, 33, 40],
                             tick_labels=[-20, -10, -5, 0, 11, 22, 33, 40],
                             vmin=-20, vmax=50)
         colormap.caption = "Temperatura massima prevista (°C)"
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
              )
           geo_j.add_child(folium.Tooltip("temp °C "+str(temperatura)))
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
           geo_j.add_child(folium.Tooltip("temp °C "+str(temperatura)))
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
           geo_j.add_child(folium.Tooltip("temp °C "+str(temperatura)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    

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
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">'''+ testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')
    








#elabora la mappa visualizzando i valori previsionali del vento nella provincia scelta (previsione 3gg)
def elabora_solo_meteo_vento_provincia(rete, dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["darkgreen", "forestgreen","lightgreen","greenyellow","lemonchiffon","khaki","yellow","orange","darkorange","orangered","red","firebrick","mediumvioletred"], 
                       vmin=0, vmax=40, index=[0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7], caption="step")
         step.caption = "Vento massimo previsto (m/s)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["darkgreen", "forestgreen","lightgreen","greenyellow","lemonchiffon","khaki","yellow","orange","darkorange","orangered","red","firebrick","mediumvioletred"], 
                       vmin=0, vmax=40, index=[0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7], caption="step")
         step.caption = "Vento massimo previsto (m/s)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["darkgreen", "forestgreen","lightgreen","greenyellow","lemonchiffon","khaki","yellow","orange","darkorange","orangered","red","firebrick","mediumvioletred"], 
                       vmin=0, vmax=40, index=[0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7], caption="step")
         step.caption = "Vento massimo previsto (m/s)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["darkgreen", "forestgreen","lightgreen","greenyellow","lemonchiffon","khaki","yellow","orange","darkorange","orangered","red","firebrick","mediumvioletred"], 
                       vmin=0, vmax=40, index=[0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7], caption="step")
         step.caption = "Vento massimo previsto (m/s)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["darkgreen", "forestgreen","lightgreen","greenyellow","lemonchiffon","khaki","yellow","orange","darkorange","orangered","red","firebrick","mediumvioletred"], 
                       vmin=0, vmax=40, index=[0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7], caption="step")
         step.caption = "Vento massimo previsto (m/s)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
              )
           geo_j.add_child(folium.Tooltip("m/s "+str(vento)))
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
           geo_j.add_child(folium.Tooltip("m/s "+str(vento)))
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
           geo_j.add_child(folium.Tooltip("m/s "+str(vento)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')







#elabora la mappa visualizzando i valori previsionali della pioggia caduta nella provincia scelta (previsione 3gg)
def elabora_solo_meteo_pioggia_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,60)
         colormap.caption=("Tot pioggia giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,60)
         colormap.caption=("Tot pioggia giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,60)
         colormap.caption=("Tot pioggia giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,60)
         colormap.caption=("Tot pioggia giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,60)
         colormap.caption=("Tot pioggia giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("mm "+str(pioggia_sum)))
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
           geo_j.add_child(folium.Tooltip("mm "+str(pioggia_sum)))
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
           geo_j.add_child(folium.Tooltip("mm "+str(pioggia_sum)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    

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
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')








#elabora la mappa visualizzando i valori previsionali della neve caduta nella provincia scelta (previsioni 3gg)
def elabora_solo_meteo_neve_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,100)
         colormap.caption=("Tot neve giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,100)
         colormap.caption=("Tot neve giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,100)
         colormap.caption=("Tot neve giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,100)
         colormap.caption=("Tot neve giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Greys_09.scale(0,100)
         colormap.caption=("Tot neve giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("mm "+str(neve_sum)))
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
           geo_j.add_child(folium.Tooltip("mm "+str(neve_sum)))
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
           geo_j.add_child(folium.Tooltip("mm "+str(neve_sum)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')








#elabora la mappa visualizzando i valori delle precipitazioni cadute nella provincia scelta (tot pioggia, neve, grandine....previsione 3gg)
def elabora_solo_meteo_precipitazioni_provincia(rete, dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Blues_09.scale(0,50)
         colormap.caption=("Tot precipitazioni giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Blues_09.scale(0,50)
         colormap.caption=("Tot precipitazioni giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Blues_09.scale(0,50)
         colormap.caption=("Tot precipitazioni giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Blues_09.scale(0,50)
         colormap.caption=("Tot precipitazioni giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         colormap = linear.Blues_09.scale(0,50)
         colormap.caption=("Tot precipitazioni giorno (mm)")
         colormap.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("mm "+str(precipitation_sum)))
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
           geo_j.add_child(folium.Tooltip("mm "+str(precipitation_sum)))
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
           geo_j.add_child(folium.Tooltip("mm "+str(precipitation_sum)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    

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
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')












#elabora la mappa visualizzando i valori previsti della portata dei corsi d'acqua presenti nella provincia scelta (previsioni 3gg)
def elabora_solo_meteo_discharge_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)

    def get_color(dato):
         step_dis= StepColormap(["whitesmoke","paleturquoise","skyblue","cornflowerblue","royalblue","darkblue"], 
                       vmin=0, vmax=120, index=[0, 1, 3, 10, 50, 100, 120], caption="step")
         if math.isnan(dato):
              return "#000000" # DATO MANCANTE -> gray
         else:
              return step_dis(int(dato))
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step_dis= StepColormap(["whitesmoke","paleturquoise","skyblue","cornflowerblue","royalblue","darkblue"], 
                       vmin=0, vmax=120, index=[0, 1, 3, 10, 50, 100, 120], caption="step")
         step_dis.caption = "Portata media (mc/sec)"
         step_dis.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step_dis= StepColormap(["whitesmoke","paleturquoise","skyblue","cornflowerblue","royalblue","darkblue"], 
                       vmin=0, vmax=120, index=[0, 1, 3, 10, 50, 100, 120], caption="step")
         step_dis.caption = "Portata media (mc/sec)"
         step_dis.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step_dis= StepColormap(["whitesmoke","paleturquoise","skyblue","cornflowerblue","royalblue","darkblue"], 
                       vmin=0, vmax=120, index=[0, 1, 3, 10, 50, 100, 120], caption="step")
         step_dis.caption = "Portata media (mc/sec)"
         step_dis.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step_dis= StepColormap(["whitesmoke","paleturquoise","skyblue","cornflowerblue","royalblue","darkblue"], 
                       vmin=0, vmax=120, index=[0, 1, 3, 10, 50, 100, 120], caption="step")
         step_dis.caption = "Portata media (mc/sec)"
         step_dis.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step_dis= StepColormap(["whitesmoke","paleturquoise","skyblue","cornflowerblue","royalblue","darkblue"], 
                       vmin=0, vmax=120, index=[0, 1, 3, 10, 50, 100, 120], caption="step")
         step_dis.caption = "Portata media (mc/sec)"
         step_dis.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           discharge=dataframe.at[i,'river_discharge']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= get_color(discharge),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("mc/sec "+str(discharge)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           discharge=dataframe.at[i,'river_discharge']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= get_color(discharge),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("mc/sec "+str(discharge)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           discharge=dataframe.at[i,'river_discharge']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= get_color(discharge),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("mc/sec "+str(discharge)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 200px; height: 170px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Portata media (mc/sec)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:whitesmoke"></i>&nbsp;0->1
    <br>&nbsp;<i class="fa fa-circle" style="color:paleturquoise"></i>&nbsp;1->3
    <br>&nbsp;<i class="fa fa-circle" style="color:skyblue"></i>&nbsp;3->10
    <br>&nbsp;<i class="fa fa-circle" style="color:cornflowerblue"></i>&nbsp;10->50
    <br>&nbsp;<i class="fa fa-circle" style="color:royalblue"></i>&nbsp;50->100
    <br>&nbsp;<i class="fa fa-circle" style="color:darkblue"></i>&nbsp;>100
    <br>&nbsp;<i class="fa fa-circle" style="color:grey"></i>&nbsp;Non disp.
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    testo=""
    for i in range(0,num_rows):
        if (math.isnan(dataframe.at[i,'bk_river_discharge'])==False):
           if (dataframe.at[i,'bk_river_discharge']!=dataframe.at[i,'river_discharge']):
               testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 700px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>Portata media corsi d'acqua prossimi 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')



#-----------------------------------FINE DATI METEO--------------------------------------------------











#----------------------------------INIZIO ANALISI RISCHIO---------------------------------------------
#elabora la mappa visualizzando i valori dell'ondata di calore prevista nella provincia scelta (indice 3gg, no ARERA)
def elabora_evento_hw_provincia(rete, dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    grouped=dataframe.groupby(by=['lat','lon','geometry']).agg(hw3gi=('hwdi', 'sum'),hw3gi_HM=('hwdi_HM','sum'))
    grouped_dataframe=grouped.reset_index()
    num_rows=len(dataframe)

    step_color= StepColormap(["green","orange","red"], vmin=0, vmax=6, index=[0, 5, 6], caption="step")
    step_color.caption = "Indice ondata di calore 3gg"
     

    if num_rows==4818:#provincia Roma
         step=1606
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)
         step_color.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
         
         
    if num_rows==2205:#provincia Latina
         step=735
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA'
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)
         step_color.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)

    if num_rows==3273:#provincia Viterbo
         step=1091
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)
         step_color.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)

    if num_rows==2529:#provincia Rieti
         step=843 
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)
         step_color.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)

    if num_rows==2889:#provincia Frosinone
         step=963
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)
         step_color.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
    

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
    
    
    layer_HW = folium.FeatureGroup('Indice heat wave',overlay=False).add_to(my_map)
    for i in range (0,step):
           poligono=(grouped_dataframe.at[i,'geometry'])
           indice_hw_3g=grouped_dataframe.at[i,'hw3gi']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step_color(indice_hw_3g),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("hw3gi "+str(indice_hw_3g)))
           geo_j.add_to(layer_HW)
    GroupedLayerControl(groups={'Ondata di calore': [layer_HW]},collapsed=False,).add_to(my_map)
    
    #GENERA HEAT MAP PER IMMAGINE RISCHIO (box in alto a dx)
    if (num_rows==4818):#Roma
        heat_map_rischio = folium.Map(location=[41.92, 12.50],width=600,height=600,tiles='cartodbpositron', zoom_start=9, zoom_control=False)
        layer_provincia_roma = folium.FeatureGroup("Provincia Roma confini", control=False).add_to(heat_map_rischio)    
        gradiente={'0':'Navy','0.14':'Darkblue','0.28':'Blue','0.42':'Cyan','0.57':'Green','0.71':'Yellow','0.85':'Orange','1':'Red'}
        HeatMap(grouped_dataframe[['lat','lon','hw3gi_HM']],  
              min_opacity=0,
              max_zoom=8,
              radius=17,
              blur = 15,
              scale_radius=True,
              gradient=gradiente,
              overlay=True,
               ).add_to(heat_map_rischio)        
        png=heat_map_rischio._to_png()
        image = Image.open(io.BytesIO(png))
        filename = os.path.join("./conf/img/", "hw_ondata_calore.png".format(i))
        image.save(filename, "PNG")
    if (num_rows==2205):#Latina
        heat_map_rischio = folium.Map(location=[41.30, 13.20],width=600,height=600,tiles='cartodbpositron', zoom_start=9, zoom_control=False)
        layer_provincia_latina = folium.FeatureGroup("Provincia Latina confini", control=False).add_to(heat_map_rischio)    
        gradiente={'0':'Navy','0.14':'Darkblue','0.28':'Blue','0.42':'Cyan','0.57':'Green','0.71':'Yellow','0.85':'Orange','1':'Red'}
        HeatMap(grouped_dataframe[['lat','lon','hw3gi_HM']],  
              min_opacity=0,
              max_zoom=8,
              radius=15,
              blur = 15,
              scale_radius=True,
              gradient=gradiente,
              overlay=True,
               ).add_to(heat_map_rischio)        
        png=heat_map_rischio._to_png()
        image = Image.open(io.BytesIO(png))
        filename = os.path.join("./conf/img/", "hw_ondata_calore.png".format(i))
        image.save(filename, "PNG")
    if (num_rows==3273):#Viterbo
        heat_map_rischio = folium.Map(location=[42.42, 11.98],width=600,height=600,tiles='cartodbpositron', zoom_start=9, zoom_control=False)
        layer_provincia_viterbo = folium.FeatureGroup("Provincia Viterbo confini", control=False).add_to(heat_map_rischio)    
        gradiente={'0':'Navy','0.14':'Darkblue','0.28':'Blue','0.42':'Cyan','0.57':'Green','0.71':'Yellow','0.85':'Orange','1':'Red'}
        HeatMap(grouped_dataframe[['lat','lon','hw3gi_HM']],  
              min_opacity=0,
              max_zoom=8,
              radius=15,
              blur = 15,
              scale_radius=True,
              gradient=gradiente,
              overlay=True,
               ).add_to(heat_map_rischio)        
        png=heat_map_rischio._to_png()
        image = Image.open(io.BytesIO(png))
        filename = os.path.join("./conf/img/", "hw_ondata_calore.png".format(i))
        image.save(filename, "PNG")
    if (num_rows==2529):#Rieti
        heat_map_rischio = folium.Map(location=[42.35, 12.91],width=600,height=600,tiles='cartodbpositron', zoom_start=9, zoom_control=False)
        layer_provincia_rieti = folium.FeatureGroup("Provincia Rieti confini", control=False).add_to(heat_map_rischio)    
        gradiente={'0':'Navy','0.14':'Darkblue','0.28':'Blue','0.42':'Cyan','0.57':'Green','0.71':'Yellow','0.85':'Orange','1':'Red'}
        HeatMap(grouped_dataframe[['lat','lon','hw3gi_HM']],  
              min_opacity=0,
              max_zoom=8,
              radius=15,
              blur = 15,
              scale_radius=True,
              gradient=gradiente,
              overlay=True,
               ).add_to(heat_map_rischio)        
        png=heat_map_rischio._to_png()
        image = Image.open(io.BytesIO(png))
        filename = os.path.join("./conf/img/", "hw_ondata_calore.png".format(i))
        image.save(filename, "PNG")
    if (num_rows==2889):#Frosinone
        heat_map_rischio = folium.Map(location=[41.62, 13.50],width=600,height=600,tiles='cartodbpositron', zoom_start=9, zoom_control=False)
        layer_provincia_frosinone = folium.FeatureGroup("Provincia Frosinone confini", control=False).add_to(heat_map_rischio)    
        gradiente={'0':'Navy','0.14':'Darkblue','0.28':'Blue','0.42':'Cyan','0.57':'Green','0.71':'Yellow','0.85':'Orange','1':'Red'}
        HeatMap(grouped_dataframe[['lat','lon','hw3gi_HM']],  
              min_opacity=0,
              max_zoom=8,
              radius=15,
              blur = 15,
              scale_radius=True,
              gradient=gradiente,
              overlay=True,
               ).add_to(heat_map_rischio)        
        png=heat_map_rischio._to_png()
        image = Image.open(io.BytesIO(png))
        filename = os.path.join("./conf/img/", "hw_ondata_calore.png".format(i))
        image.save(filename, "PNG")
    #FINE ---- GENERA HEAT MAP PER IMMAGINE RISCHIO
    
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
    if((dataframe.at[1,'bk_temperature_2m_max']!=dataframe.at[1,'temperature_2m_max']) or
           (dataframe.at[1,'bk_precipitation_sum']!=dataframe.at[1,'precipitation_sum'])):
                testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 650px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ONDATA DI CALORE - Rischio guasti linea interrata prossimi 3gg</b> 
    <br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    
    my_map.save('./conf/analisi_corrente/analisi_map.html')






#elabora la mappa visualizzando la riduzione di vita prevista per i trasformatori di potenza nella provincia scelta (previsione 3gg)
def elabora_evento_hw_trasformatore_p_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di potenza 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di potenza 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di potenza 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di potenza 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di potenza 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("% "+str(life_tp65)))
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
           geo_j.add_child(folium.Tooltip("% "+str(life_tp65)))
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
           geo_j.add_child(folium.Tooltip("% "+str(life_tp65)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ONDATA DI CALORE - Previsione riduzione vita trasformatori di potenza (65rise) 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')






#elabora la mappa visualizzando la riduzione di vita prevista per i trasformatori di distribuzione nella provincia scelta (previsione 3gg)
def elabora_evento_hw_trasformatore_d_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di distribuzione 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di distribuzione 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di distribuzione 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di distribuzione 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Decadimento prestazioni trasformatore di distribuzione 65 rise (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("% "+str(life_td65)))
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
           geo_j.add_child(folium.Tooltip("% "+str(life_td65)))
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
           geo_j.add_child(folium.Tooltip("% "+str(life_td65)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ONDATA DI CALORE - Previsione riduzione vita trasformatori di distribuzione (65rise) 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')




#elabora la mappa visualizzando la probabilità di failure dei tralicci nella provincia scelta (previsioni 3gg)
def elabora_evento_vento_tralicci_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto tralicci (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto tralicci (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto tralicci (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto tralicci (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto tralicci (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_tralicci)))
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_tralicci)))
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_tralicci)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 700px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>VENTO - Previsione rischio guasti tralicci prossimi 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')




#elabora la mappa visualizzando la probabilità di failure della linea esterna nella provincia scelta (previsione 3gg)
def elabora_evento_vento_linea_esterna_provincia(rete,dataframe):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto linea esterna (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto linea esterna (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto linea esterna (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto linea esterna (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto linea esterna (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_linea_esterna)))
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_linea_esterna)))
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_linea_esterna)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>VENTO - Previsione rischio guasti linea esterna prossimi 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')






#elabora la mappa visualizzando la probabilità di failure dei pali di servizio nella provincia scelta (previsione 3gg)
def elabora_evento_vento_pali_provincia(rete, dataframe,tipo_palo, pali_anni):
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
    
    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto pali di servizio (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto pali di servizio (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
    
            
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto pali di servizio (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         
    

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto pali di servizio (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto pali di servizio (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)
                      
    
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
              )
           geo_j.add_child(folium.Tooltip("% "+str(prob_pali)))
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_pali)))
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
           geo_j.add_child(folium.Tooltip("% "+str(prob_pali)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)      
    
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
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 850px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>VENTO - Previsione rischio guasti pali ''' + tipo_palo + ''' ''' + str(pali_anni) + '''anni prossimi 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')




#elabora la mappa visualizzando la probabilità di failure delle cabine primarie nella provincia scelta (previsione 3gg)
def elabora_evento_alluvione_cabine_provincia(rete,dataframe):# la mappa rischio https://aubac.it/piani-di-bacino/mappe-pgra-2021-ii-ciclo
    import math
    df = gpd.read_feather('./conf/confini/confini_comuni_lazio.feather')
    dfp = gpd.read_feather('./conf/confini/confini_province_lazio.feather')
    num_rows=len(dataframe)
          
    
    if num_rows==2205:#provincia Latina
         step=735;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/LATINA_rete_elettrica.feather'   
         provincia='LATINA' 
         my_map = folium.Map(location=[41.40, 13.10],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["whitesmoke","green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 1, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto cabine (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_latina= folium.FeatureGroup("Latina comuni").add_to(my_map)
         layer_provincia_latina= folium.FeatureGroup("LT confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_latina)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==59:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_latina)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_latina,layer_provincia_latina]},collapsed=False,).add_to(my_map)
         dataframe_pericolo_alluvione = gpd.read_feather('./conf/aree_pericolo_alluvione/pgra_pericolo_latina.feather')

    if num_rows==2889:#provincia Frosinone
         step=963;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/FROSINONE_rete_elettrica.feather'  
         provincia='FROSINONE' 
         my_map = folium.Map(location=[41.62, 13.50],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["whitesmoke","green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 1, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto cabine (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_frosinone= folium.FeatureGroup("Frosinone comuni").add_to(my_map)
         layer_provincia_frosinone= folium.FeatureGroup("FR confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_frosinone)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==60:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_frosinone)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_frosinone,layer_provincia_frosinone]},collapsed=False,).add_to(my_map)
         dataframe_pericolo_alluvione = gpd.read_feather('./conf/aree_pericolo_alluvione/pgra_pericolo_frosinone.feather')

    if num_rows==4818:#provincia Roma
         step=1606;g1=0;g2=g1+step;g3=g2+step;g4=g3+step
         percorso='./conf/rete_elettrica/ROMA_rete_elettrica.feather' 
         provincia='ROMA'
         my_map = folium.Map(location=[41.92, 12.44],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["whitesmoke","green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 1, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto cabine (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_roma= folium.FeatureGroup("Roma comuni").add_to(my_map)
         layer_provincia_roma= folium.FeatureGroup("RM confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_roma)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==58:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_roma)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_roma,layer_provincia_roma]},collapsed=False,).add_to(my_map)
         dataframe_pericolo_alluvione = gpd.read_feather('./conf/aree_pericolo_alluvione/pgra_pericolo_roma.feather')

    if num_rows==2529:#provincia Rieti
         step=843;g1=0;g2=g1+step;g3=g2+step;g4=g3+step   
         percorso='./conf/rete_elettrica/RIETI_rete_elettrica.feather' 
         provincia='RIETI'
         my_map = folium.Map(location=[42.35, 12.91],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["whitesmoke","green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 1, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto cabine (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_rieti= folium.FeatureGroup("Rieti comuni").add_to(my_map)
         layer_provincia_rieti= folium.FeatureGroup("RI confini").add_to(my_map)
         for _, r in df.iterrows():
                 if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_rieti)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==57:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_rieti)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_rieti,layer_provincia_rieti]},collapsed=False,).add_to(my_map)
         dataframe_pericolo_alluvione = gpd.read_feather('./conf/aree_pericolo_alluvione/pgra_pericolo_rieti.feather')
         

    if num_rows==3273:#provincia Viterbo
         step=1091;g1=0;g2=g1+step;g3=g2+step;g4=g3+step  
         percorso='./conf/rete_elettrica/VITERBO_rete_elettrica.feather'  
         provincia='VITERBO'
         my_map = folium.Map(location=[42.42, 11.98],min_zoom=8, max_zoom=14, zoom_start=10)
         folium.TileLayer(tiles='cartodbpositron', overlay=False).add_to(my_map)  
         step= StepColormap(["whitesmoke","green","greenyellow","yellow","orange","red"], 
                       vmin=0, vmax=100, index=[0, 1, 20, 40, 60, 80, 100], caption="step")
         step.caption = "Probabilità guasto cabine (%)"
         step.add_to(my_map)
         folium.LayerControl(collapsed=False).add_to(my_map)
         layer_comuni_provincia_viterbo= folium.FeatureGroup("Viterbo comuni").add_to(my_map)
         layer_provincia_viterbo= folium.FeatureGroup("VT confini").add_to(my_map)
         for _, r in df.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   folium.Popup(r["COMUNE"]).add_to(geo_j)
                   geo_j.add_to(layer_comuni_provincia_viterbo)
         for _, r in dfp.iterrows():
               if(r["COD_PROV"])==56:
                   sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
                   geo_j = sim_geo.to_json()
                   geo_j = folium.GeoJson(data=geo_j, color='blue', weight=2, fillColor= '#00000000')
                   geo_j.add_to(layer_provincia_viterbo)
         GroupedLayerControl(groups={'confini': [layer_comuni_provincia_viterbo,layer_provincia_viterbo]},collapsed=False,).add_to(my_map)
         dataframe_pericolo_alluvione = gpd.read_feather('./conf/aree_pericolo_alluvione/pgra_pericolo_viterbo.feather')

    if rete==1:
         layer_rete_elettrica = folium.FeatureGroup("Rete elettrica",overlay=True, show=False).add_to(my_map)
         dataframe_rete_elettrica = pd.read_feather(percorso)
         serie_elettrica=pd.DataFrame(dataframe_rete_elettrica)
         coordinate_per_rete_elettrica=serie_elettrica['geometry']
         linee_elettriche=folium.PolyLine(locations=coordinate_per_rete_elettrica, color='black', weight=2, opacity=1)
         linee_elettriche.add_to(layer_rete_elettrica)
         
         layer_cabine_primarie = folium.FeatureGroup("Cabine primarie",overlay=True, show=False).add_to(my_map)
         df = pd.read_excel('./conf/rete_elettrica/cabine_primarie.xlsx')
         df_filtrato = df[df['Provincia'] == provincia]
         if not df_filtrato.empty:
              gdf = gpd.GeoDataFrame(df_filtrato, geometry=gpd.points_from_xy(df_filtrato.Lon, df_filtrato.Lat), crs="EPSG:4326")
              folium.GeoJson(gdf,
              marker=folium.CircleMarker(radius=10, fill_color="red", fill_opacity=0.8, color="black", weight=2),
              tooltip=folium.GeoJsonTooltip(fields=["Ragione Sociale GdR"]),).add_to(layer_cabine_primarie)
         GroupedLayerControl(groups={'rete elettrica': [layer_rete_elettrica,layer_cabine_primarie]},collapsed=False,exclusive_groups=False).add_to(my_map)


    
    layer_pericolo_alluvione = folium.FeatureGroup("Aree pericolo alluvione",overlay=True, show=False).add_to(my_map)
        
    for _, r in dataframe_pericolo_alluvione.iterrows():
         sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
         geo_j = sim_geo.to_json()
         geo_j = folium.GeoJson(data=geo_j, weight=0.5, color="black", style_function=lambda x: {"fillColor": "orange"})
         folium.Popup(r["PERICOLO"]).add_to(geo_j)
         folium.Tooltip(r["LEGENDA"]).add_to(geo_j)
         geo_j.add_to(layer_pericolo_alluvione)
    GroupedLayerControl(groups={'Aree pericolo alluvione': [layer_pericolo_alluvione]},collapsed=False,exclusive_groups=False).add_to(my_map)


    giorno1=(dataframe.at[g1,'giorno'])
    layer_giorno1 = folium.FeatureGroup(str(giorno1),overlay=False).add_to(my_map)
    for i in range (g1,g2):
           poligono=(dataframe.at[i,'geometry'])
           rischio_cabine=dataframe.at[i,'flood_risk_cabina']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(rischio_cabine),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("% "+str(rischio_cabine)))
           geo_j.add_to(layer_giorno1)
           
    giorno2=(dataframe.at[g2,'giorno'])
    layer_giorno2 = folium.FeatureGroup(str(giorno2),overlay=False).add_to(my_map)
    for i in range (g2,g3):
           poligono=(dataframe.at[i,'geometry'])
           rischio_cabine=dataframe.at[i,'flood_risk_cabina']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(rischio_cabine),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("% "+str(rischio_cabine)))
           geo_j.add_to(layer_giorno2)
           
    giorno3=(dataframe.at[g3,'giorno'])
    layer_giorno3 = folium.FeatureGroup(str(giorno3),overlay=False).add_to(my_map)
    for i in range (g3,g4):
           poligono=(dataframe.at[i,'geometry'])
           rischio_cabine=dataframe.at[i,'flood_risk_cabina']
           sim_geo = gpd.GeoSeries(poligono).simplify(tolerance=0.001)
           geo_j = sim_geo.to_json()
           geo_j = folium.GeoJson(
               data=geo_j,
               fillColor= step(rischio_cabine),
               fillOpacity= 0.5,
               color='black',
               weight=0.1,
               line_opacity=0.1,
              )
           geo_j.add_child(folium.Tooltip("% "+str(rischio_cabine)))
           geo_j.add_to(layer_giorno3)    
           
    GroupedLayerControl(groups={'giorno': [layer_giorno1, layer_giorno2, layer_giorno3]},collapsed=False,).add_to(my_map)    

    
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

    legend_html='''<div style="position: fixed;bottom: 50px; left: 50px; width: 220px; height: 150px;border:2px solid grey; z-index:9999; font-size:14px;background-color:white;opacity: 0.85;">&nbsp; <b>Prob. guasto (%)</b> 
    <br>&nbsp;<i class="fa fa-circle" style="color:whitesmoke"></i>&nbsp;Nulla (0%)
    <br>&nbsp;<i class="fa fa-circle" style="color:green"></i>&nbsp;Molto bassa (1-20%)
    <br>&nbsp;<i class="fa fa-circle" style="color:greenyellow"></i>&nbsp;Bassa (21-40%)
    <br>&nbsp;<i class="fa fa-circle" style="color:yellow"></i>&nbsp;Moderata (41-60%)
    <br>&nbsp;<i class="fa fa-circle" style="color:orange"></i>&nbsp;Alta (61-80%)
    <br>&nbsp;<i class="fa fa-circle" style="color:red"></i>&nbsp;Molto alta (81-100%)
    <br></div>'''
    my_map.get_root().html.add_child(folium.Element(legend_html))

    testo=""
    for i in range(0,num_rows):
        if (math.isnan(dataframe.at[i,'river_discharge'])==False) and (math.isnan(dataframe.at[i,'bk_river_discharge'])==False):
           if(dataframe.at[i,'river_discharge']!=dataframe.at[i,'bk_river_discharge']):
               testo="Simulazione"
    titolo_html='''<div style="position: fixed; top: 50px; left: 50px; width: 750px; height: 50px; border:2px solid grey; 
    z-index:9999; font-size:18px;background-color:white;opacity: 0.85;"><b>ALLUVIONE - Previsione rischio guasto cabine 3gg</b> 
    <b>&nbsp;''' + str(giorno1) + '''-->'''+ str(giorno3) + '''</b><br><font color="red", size="3">''' + testo + '''</div>'''
    my_map.get_root().html.add_child(folium.Element(titolo_html))
    my_map.save('./conf/analisi_corrente/analisi_map.html')