
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QRadioButton, QGroupBox,QPushButton,QButtonGroup,\
QHBoxLayout,QVBoxLayout,QToolBar,QAction,QLabel,QFileDialog, QMessageBox, QCheckBox, QProgressBar, QSlider, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, QSize, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm
from datetime import datetime, timedelta
from shapely.geometry import Polygon
import math
import webbrowser
import shutil
from pathlib import PureWindowsPath
import elabora_scenario
import elabora_scenario_002

#from PyQt5 import QtCore
#import folium
#from folium import GeoJson
#from pyproj import Transformer
#import importlib
#import openpyxl


path = PureWindowsPath(os.getcwd()).as_posix()

#tronca numeri float
def tronca(numero_float, posizioni_decimali):
    if math.isnan(numero_float)==False:
         moltiplicatore = 10 ** posizioni_decimali
         return int(numero_float * moltiplicatore) / moltiplicatore

#----------------------------------------------FUNZIONI PULSANTI TOOLBAR-------------------------------------------------------
#genera un nuovo scenario (dati meteo o analisi rischio)
def elabora():
    rete=0

    if checkbox_opzioni_rete.isChecked(): rete=1
    geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')

    if(geo_dataframe_corrente.columns[31]=="poligono_002"):#si tratta di poligoni di superficie di 0.02 gradi
        if radio_analisi_meteo.isChecked() and radio_dato_temp.isChecked():   
           elabora_scenario_002.elabora_solo_meteo_temperatura_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_vento.isChecked():        
           elabora_scenario_002.elabora_solo_meteo_vento_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_pioggia.isChecked():        
           elabora_scenario_002.elabora_solo_meteo_pioggia_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_precip.isChecked():        
           elabora_scenario_002.elabora_solo_meteo_precipitazioni_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_neve.isChecked():        
           elabora_scenario_002.elabora_solo_meteo_neve_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_discharge.isChecked():        
           elabora_scenario_002.elabora_solo_meteo_discharge_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_default()


        if radio_analisi_rischio.isChecked() and radio_evento_hw.isChecked() and radio_componente_linea_interrata.isChecked():
           elabora_scenario_002.elabora_evento_hw_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_heat_wave()
        if radio_analisi_rischio.isChecked() and radio_evento_hw.isChecked() and radio_componente_trasformatore_p.isChecked():
           elabora_scenario_002.elabora_evento_hw_trasformatore_p_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_heat_wave_trasformatore_p()
        if radio_analisi_rischio.isChecked() and radio_evento_hw.isChecked() and radio_componente_trasformatore_d.isChecked():
           elabora_scenario_002.elabora_evento_hw_trasformatore_d_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_heat_wave_trasformatore_d()
        if radio_analisi_rischio.isChecked() and radio_evento_vento.isChecked() and radio_componente_tralicci.isChecked():
           elabora_scenario_002.elabora_evento_vento_tralicci_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_vento_tralicci()
        if radio_analisi_rischio.isChecked() and radio_evento_vento.isChecked() and radio_componente_linea_esterna.isChecked():
           elabora_scenario_002.elabora_evento_vento_linea_esterna_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_vento_linea_esterna()
        if radio_analisi_rischio.isChecked() and radio_evento_vento.isChecked() and radio_componente_pali.isChecked():
           if radio_pali_legno_off.isChecked(): tipo_palo="legno_acciaio"; pali_anni=0 
           if radio_pali_legno_20.isChecked(): tipo_palo="legno"; pali_anni=20
           if radio_pali_legno_40.isChecked(): tipo_palo="legno"; pali_anni=40
           if radio_pali_legno_60.isChecked(): tipo_palo="legno"; pali_anni=60
           elabora_scenario_002.elabora_evento_vento_pali_provincia(rete, geo_dataframe_corrente, tipo_palo, pali_anni)
           carica_immagine_rischio_vento_pali(tipo_palo, pali_anni)
        if radio_analisi_rischio.isChecked() and radio_evento_alluvione.isChecked() and radio_componente_cabina_primaria.isChecked():
           elabora_scenario_002.elabora_evento_alluvione_cabine_provincia(rete, geo_dataframe_corrente)
           carica_immagine_rischio_alluvione_cabine()


    
    else:#poligoni da 0.25 o 0.1 gradi
        if radio_analisi_meteo.isChecked() and radio_dato_temp.isChecked():        
           elabora_scenario.elabora_solo_meteo_temperatura(rete,geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_precip.isChecked():        
           elabora_scenario.elabora_solo_meteo_precipitazioni(rete,geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_pioggia.isChecked():        
           elabora_scenario.elabora_solo_meteo_pioggia(rete,geo_dataframe_corrente)
           carica_immagine_rischio_default()
        if radio_analisi_meteo.isChecked() and radio_dato_vento.isChecked():        
           elabora_scenario.elabora_solo_meteo_vento(rete,geo_dataframe_corrente)
           carica_immagine_rischio_default()        
        if radio_analisi_meteo.isChecked() and radio_dato_neve.isChecked():
           elabora_scenario.elabora_solo_meteo_neve(rete,geo_dataframe_corrente)
           carica_immagine_rischio_default()


        if radio_analisi_rischio.isChecked() and radio_evento_hw.isChecked() and radio_componente_linea_interrata.isChecked():
           elabora_scenario.elabora_evento_hw(rete,geo_dataframe_corrente)
           carica_immagine_rischio_heat_wave()
        if radio_analisi_rischio.isChecked() and radio_evento_hw.isChecked() and radio_componente_trasformatore_p.isChecked():
           elabora_scenario.elabora_evento_hw_trasformatore_p(rete,geo_dataframe_corrente)
           carica_immagine_rischio_heat_wave_trasformatore_p()
        if radio_analisi_rischio.isChecked() and radio_evento_hw.isChecked() and radio_componente_trasformatore_d.isChecked():
           elabora_scenario.elabora_evento_hw_trasformatore_d(rete,geo_dataframe_corrente)
           carica_immagine_rischio_heat_wave_trasformatore_d()
        if radio_analisi_rischio.isChecked() and radio_evento_vento.isChecked() and radio_componente_tralicci.isChecked():
           elabora_scenario.elabora_evento_vento_tralicci(rete,geo_dataframe_corrente)
           carica_immagine_rischio_vento_tralicci()
        if radio_analisi_rischio.isChecked() and radio_evento_vento.isChecked() and radio_componente_linea_esterna.isChecked():
           elabora_scenario.elabora_evento_vento_linea_esterna(rete,geo_dataframe_corrente)
           carica_immagine_rischio_vento_linea_esterna()
        if radio_analisi_rischio.isChecked() and radio_evento_ghiaccio.isChecked() and radio_componente_linea_esterna.isChecked():
           elabora_scenario.elabora_evento_ghiaccio_linea_esterna(rete,geo_dataframe_corrente)
           carica_immagine_rischio_ghiaccio_linea_esterna()
        if radio_analisi_rischio.isChecked() and radio_evento_vento.isChecked() and radio_componente_pali.isChecked():
           if radio_pali_legno_off.isChecked(): tipo_palo="legno_acciaio"; pali_anni=0 
           if radio_pali_legno_20.isChecked(): tipo_palo="legno"; pali_anni=20
           if radio_pali_legno_40.isChecked(): tipo_palo="legno"; pali_anni=40
           if radio_pali_legno_60.isChecked(): tipo_palo="legno"; pali_anni=60
           elabora_scenario.elabora_evento_vento_pali(rete, geo_dataframe_corrente, tipo_palo, pali_anni)
           carica_immagine_rischio_vento_pali(tipo_palo, pali_anni)
    
    mappa.browser.setUrl(QUrl.fromLocalFile("E:/0_Tesi/tool/conf/analisi_corrente/analisi_map.html"))



#chiede se si vuole uscire dallo scenario corrente e caricare un nuovo scenario salvato nella cartella SCENARI 
def pulsante_apri_scenario():
    if toolbar_pulsante_chiudi_scenario.isEnabled():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Uscire dallo scenario?")
        msg.setWindowTitle("Chiudi scenario")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        val=msg.exec()
        if val==1024:#codice del pulsante OK
           chiudi_scenario()
           carica_file_dati_scenario()
    else:
        carica_file_dati_scenario()

#carica un nuovo scenario dalla cartella SCENARI (file .feather)
def carica_file_dati_scenario():
    global file_dialog_carica
    file_dialog_carica=QFileDialog()
    file_dialog_carica.setDirectory('./scenari')
    path, _ = QFileDialog.getOpenFileName(file_dialog_carica,"Carica scenario", "","File scenario (*.feather)")

    if path:
       verifica_dataframe=gpd.read_feather(path)
       if verifica_dataframe.columns[0]=='index' and verifica_dataframe.columns[1]=='giorno' and verifica_dataframe.columns[2]=='lat' and \
          verifica_dataframe.columns[3]=='lon' and verifica_dataframe.columns[4]=='elev':
             verifica_dataframe.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
             verifica_dataframe.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')
             abilita_elabora_scenario()
       else:
          global msg
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setWindowTitle("Errore")
          msg.setText("Formato dati non valido!!")
          msg.setStandardButtons(QMessageBox.Ok)
          msg.show()

#salva lo scenario corrente nella cartella SCENARI
def pulsante_salva_scenario():
    global file_dialog_salva_scenario
    file_dialog_salva_scenario=QFileDialog()
    filename_scenario, _ = QFileDialog.getSaveFileName(file_dialog_salva_scenario,"Salva scenario","./scenari","File scenario (*.feather)")
    if filename_scenario:
            shutil.copy('./conf/analisi_corrente/geo_dataframe_base.feather', str(filename_scenario))

#chiede se si vuole uscire dallo scenario corrente
def pulsante_chiudi_scenario():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Question)
    msg.setText("Uscire dallo scenario?")
    msg.setWindowTitle("Chiudi scenario")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    val=msg.exec()
    if val==1024:#codice del pulsante OK
        chiudi_scenario()

#chiude lo scenario corrente
def chiudi_scenario():
    analisi.setDisabled(True)
    simulazione.setDisabled(True)    
    opzioni.setDisabled(True)
    dato_meteo.setDisabled(True)
    componente.setDisabled(True)
    img_rischio.setDisabled(True)
    toolbar_pulsante_salva_scenario.setDisabled(True)
    toolbar_pulsante_chiudi_scenario.setDisabled(True)
    toolbar_pulsante_dataframe_excel.setDisabled(True)
    toolbar_pulsante_elabora_scenario.setDisabled(True)
    toolbar_pulsante_ricarica_soglie.setDisabled(True)
    toolbar_pulsante_salva_mappa.setDisabled(True)
    radio_analisi_meteo.setChecked(True)
    radio_dato_temp.setChecked(True)
    pixmap = QPixmap('./conf/img/transmission-tower.ico')
    logoLabel.setPixmap(pixmap)
    radio_evento_hw.setChecked(True)
    radio_componente_linea_interrata.setChecked(True)
    pulsante_elabora_modello.setDisabled(True)
    mappa.browser.setUrl(QUrl("file:///" + path + "/conf/img/start_map.html"))
    mappa.show()
    toolbar_pulsante_scarica_dati_meteo_025.setDisabled(False)
    toolbar_pulsante_scarica_dati_meteo_01.setDisabled(False)
    toolbar_pulsante_scarica_dati_meteo_002.setDisabled(False)
    toolbar_combobox_scarica_dati_meteo_002_seleziona_provincia.setDisabled(False)


#scarica i dati meteo richiamando l'api per ciascun valore di coordinata presente nella lista coord_025_list e crea il dataframe
#completo delle probabilità di failure richiamando le funzioni delle curve di fragilità
def pulsante_scarica_dati_meteo_025():
    
    #crea un dataframe vuoto, solo con le intestazioni delle colonne
    pd_dataframe=pd.DataFrame(columns=['giorno',
                                       'lat',
                                       'lon',
                                       'elev',
                                       'temperature_2m_max',
                                       'wind_speed_10m_max',
                                       'snowfall_sum',
                                       'rain_sum',
                                       'precipitation_sum',
                                       'weather_code',
                                       'precipitation_hours',
                                       'river_discharge',
                                       'ts_discharge',
                                       'flood_factor',
                                       'hwdi',
                                       'hwdi_HM',
                                       'prob_tralicci',
                                       'prob_linea_esterna',
                                       'm_mm',
                                       'M_mm',
                                       'prob_linea_esterna_ice',
                                       'prob_pali_la_nuovi',
                                       'prob_pali_l_20',
                                       'prob_pali_l_40',
                                       'prob_pali_l_60',
                                       'tp65',
                                       'td65',
                                       'flood_warning',
                                       'flood_depth',
                                       'flood_risk_cabina',
                                       'poligono_025',
                                       'geometry',
                                       'bk_temperature_2m_max',
                                       'bk_wind_speed_10m_max',
                                       'bk_snowfall_sum',
                                       'bk_precipitation_sum',
                                       'bk_rain_sum',
                                       'bk_weather_code',
                                       'bk_precipitation_hours',
                                       'bk_river_discharge'])
    
    coord_025_list=[
        [42.75,11.75],[42.75,12.00],[42.75,12.25],[42.75,13.00],[42.75,13.25],[42.75,13.50],[42.50,11.50],[42.50,11.75],[42.50,12.00],[42.50,12.25],
        [42.50,12.50],[42.50,12.75],[42.50,13.00],[42.50,13.25],[42.50,13.50],[42.25,11.50],[42.25,11.75],[42.25,12.00],[42.25,12.25],[42.25,12.50],
        [42.25,12.75],[42.25,13.00],[42.25,13.25],[42.25,13.50],[42.00,11.75],[42.00,12.00],[42.00,12.25],[42.00,12.50],[42.00,12.75],[42.00,13.00],
        [42.00,13.25],[42.00,13.50],[41.75,12.25],[41.75,12.50],[41.75,12.75],[41.75,13.00],[41.75,13.25],[41.75,13.50],[41.75,13.75],[41.75,14.00],
        [41.50,12.50],[41.50,12.75],[41.50,13.00],[41.50,13.25],[41.50,13.50],[41.50,13.75],[41.50,14.00],[41.25,13.00],[41.25,13.25],[41.25,13.50],
        [41.25,13.75],[41.25,14.00],[41.00,12.75],[41.00,13.00],[40.75,13.50]#55
        ]
    avanzamento=0;elementi=len(coord_025_list)
    for coord in coord_025_list:
        latitudine=(coord[0])
        longitudine=(coord[1])
        dati_api, elev=api_025_ifs(latitudine, longitudine)        
        avanzamento=avanzamento+1
        coordinate_per_poligono = ((longitudine-0.125,latitudine+0.125), (longitudine+0.125,latitudine+0.125),
        (longitudine+0.125, latitudine-0.125), (longitudine-0.125, latitudine-0.125),(longitudine-0.125, latitudine+0.125))         

        for j in range(0,7):
                    data=dati_api["date"][j]
                    converti_giorno=datetime.date(data)
                    giorno = converti_giorno + timedelta(days=1)

                    pd_dataframe.loc[len(pd_dataframe)] = [giorno,
                                                           latitudine,
                                                           longitudine,
                                                           elev,
                                                           tronca(dati_api["temperature_2m_max"][j],1),
                                                           tronca(dati_api["wind_speed_10m_max"][j],1),
                                                           tronca(dati_api["snowfall_sum"][j],0),
                                                           tronca(dati_api["rain_sum"][j],0),
                                                           tronca(dati_api["precipitation_sum"][j],0),
                                                           dati_api["weather_code"][j],
                                                           dati_api["precipitation_hours"][j],
                                                           '',#river_discharge
                                                           '',#ts_discharge
                                                           '',#flood_factor
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           coordinate_per_poligono,
                                                           '',
                                                           tronca(dati_api["temperature_2m_max"][j],1),
                                                           tronca(dati_api["wind_speed_10m_max"][j],1),
                                                           tronca(dati_api["snowfall_sum"][j],0),
                                                           tronca(dati_api["precipitation_sum"][j],0),
                                                           tronca(dati_api["rain_sum"][j],0),
                                                           dati_api["weather_code"][j],
                                                           dati_api["precipitation_hours"][j],
                                                           '']
                    
        valore_bar=round((100/elementi)*avanzamento);bar.setValue(valore_bar)


    df_ordinato=pd_dataframe.sort_values(by=['giorno','lat','lon']).reset_index()
    #carica i confini regionali
    confini_regione = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    geo_confini = gpd.GeoSeries(confini_regione["geometry"]).simplify(tolerance=0.001)
    df2 = gpd.GeoDataFrame({'geometry': geo_confini}, crs=4326)
    
    #calcola le intersezioni tra i confini regionali ed i poligoni ifs 025, popola il dataframe con i valori cdf    
    num_rows = len(df_ordinato)
    avanzamento=0;elementi=num_rows
    for i in range(0,num_rows):
           avanzamento=avanzamento+1
           poligono_coord=(df_ordinato.at[i,'poligono_025'])
           poligono_geometria = Polygon(poligono_coord)
           poligono=gpd.GeoSeries(poligono_geometria)
           df1 = gpd.GeoDataFrame({'geometry': poligono}, crs=4326)
           intersezione = df2.overlay(df1, how='intersection')
           df_ordinato.at[i,'geometry']=intersezione.at[0, 'geometry']
           df_ordinato.at[i,'index']=i

           df_ordinato.at[i,'hwdi']=calcola_hwdi(df_ordinato.at[i,'temperature_2m_max'],df_ordinato.at[i,'precipitation_sum'])
           df_ordinato.at[i,'hwdi_HM']=df_ordinato.at[i,'hwdi']/14
           df_ordinato.at[i,'prob_tralicci']=calcola_prob_tralicci(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_linea_esterna']=calcola_prob_linea_esterna(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'m_mm']=calcola_stima_m_ice(df_ordinato.at[i,'weather_code'],df_ordinato.at[i,'precipitation_hours'],df_ordinato.at[i,'wind_speed_10m_max'],df_ordinato.at[i,'precipitation_sum'])
           df_ordinato.at[i,'M_mm']=15
           df_ordinato.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(df_ordinato.at[i,'m_mm'],df_ordinato.at[i,'M_mm'])
           df_ordinato.at[i,'prob_pali_la_nuovi']=calcola_prob_pali_legnoacciaio_nuovi(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_20']=calcola_prob_pali_legno_20(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_40']=calcola_prob_pali_legno_40(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_60']=calcola_prob_pali_legno_60(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'tp65']=calcola_tp65(df_ordinato.at[i,'temperature_2m_max'])
           df_ordinato.at[i,'td65']=calcola_td65(df_ordinato.at[i,'temperature_2m_max'])
           valore_bar=round((100/elementi)*avanzamento);bar.setValue(valore_bar)

    #crea il geodataframe con le geometrie (overlay)      
    geo=gpd.GeoDataFrame(df_ordinato, geometry='geometry')
    if len(geo)==385:
         geo.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
         geo.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')

         ct = datetime.now()
         timestamp = ct.timestamp()
         date_time = datetime.fromtimestamp(timestamp)
         data = date_time.strftime("%Y_%m_%d_%H%M%S_025deg")
         geo.to_feather('./scenari/' + 'Lazio_' + data + '.feather') #salva i dati nello storico
         abilita_elabora_scenario()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Errore")
        msg.setText("Dati incompleti/non disponibili sul server remoto. Riprovare all'inizio della prossima ora!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

#scarica i dati meteo richiamando l'api per ciascun valore di coordinata presente nella lista coord_01_list e crea il dataframe
#completo delle probabilità di failure richiamando le funzioni delle curve di fragilità
def pulsante_scarica_dati_meteo_01():
    pd_dataframe=pd.DataFrame(columns=['giorno',
                                       'lat',
                                       'lon',
                                       'elev',
                                       'temperature_2m_max',
                                       'wind_speed_10m_max',
                                       'snowfall_sum',
                                       'rain_sum',
                                       'precipitation_sum',
                                       'weather_code',
                                       'precipitation_hours',
                                       'river_discharge',
                                       'ts_discharge',
                                       'flood_factor',
                                       'hwdi',
                                       'hwdi_HM',
                                       'prob_tralicci',
                                       'prob_linea_esterna',
                                       'm_mm',
                                       'M_mm',
                                       'prob_linea_esterna_ice',
                                       'prob_pali_la_nuovi',
                                       'prob_pali_l_20',
                                       'prob_pali_l_40',
                                       'prob_pali_l_60',
                                       'tp65',
                                       'td65',
                                       'flood_warning',
                                       'flood_depth',
                                       'flood_risk_cabina',
                                       'poligono_01',
                                       'geometry',
                                       'bk_temperature_2m_max',
                                       'bk_wind_speed_10m_max',
                                       'bk_snowfall_sum',
                                       'bk_precipitation_sum',
                                       'bk_rain_sum',
                                       'bk_weather_code',
                                       'bk_precipitation_hours',
                                       'bk_river_discharge'])
    
    coord_01_list=[
                  [42.875,11.875],[42.875,11.750],[42.750,11.750],[42.750,11.875],[42.750,12.000],[42.750,13.125],[42.750,13.250],[42.750,13.375],[42.625,11.625],
                  [42.625,11.750],[42.625,11.875],[42.625,12.000],[42.625,12.125],[42.625,12.250],[42.625,12.875],[42.625,13.000],[42.625,13.125],[42.625,13.250],
                  [42.625,13.375],[42.500,11.625],[42.500,11.750],[42.500,11.875],[42.500,12.000],[42.500,12.125],[42.500,12.250],[42.500,12.375],[42.500,12.625],
                  [42.500,12.750],[42.500,12.875],[42.500,13.000],[42.500,13.125],[42.375,11.500],[42.375,11.625],[42.375,11.750],[42.375,11.875],[42.375,12.000],
                  [42.375,12.125],[42.375,12.250],[42.375,12.375],[42.375,12.500],[42.375,12.625],[42.375,12.750],[42.375,12.875],[42.375,13.000],[42.375,13.125],
                  [42.375,13.250],[42.250,11.625],[42.250,11.750],[42.250,11.875],[42.250,12.000],[42.250,12.125],[42.250,12.250],[42.250,12.375],[42.250,12.500],
                  [42.250,12.625],[42.250,12.750],[42.250,12.875],[42.250,13.000],[42.250,13.125],[42.250,13.250],[42.250,13.375],[42.000,11.875],[42.000,12.000],
                  [42.000,12.125],[42.000,12.250],[42.000,12.375],[42.000,12.500],[42.000,12.625],[42.000,12.750],[42.000,12.875],[42.000,13.000],[42.000,13.125],
                  [42.000,13.250],[42.000,13.375],[42.125,11.875],[42.125,12.000],[42.125,12.125],[42.125,12.250],[42.125,12.375],[42.125,12.500],[42.125,12.625],
                  [42.125,12.750],[42.125,12.875],[42.125,13.000],[42.125,11.750],[42.125,13.125],[42.125,13.250],[42.125,13.375],[41.875,12.125],[41.875,12.250],
                  [41.875,12.375],[41.875,12.500],[41.875,12.625],[41.875,12.750],[41.875,12.875],[41.875,13.000],[41.875,13.125],[41.875,13.250],[41.875,13.375],
                  [41.875,13.500],[41.750,12.250],[41.750,12.375],[41.750,12.500],[41.750,12.625],[41.750,12.750],[41.750,12.875],[41.750,13.000],[41.750,13.125],
                  [41.750,13.250],[41.750,13.375],[41.750,13.500],[41.750,13.625],[41.750,13.750],[41.750,13.875],[41.625,12.375],[41.625,12.500],[41.625,12.625],
                  [41.625,12.750],[41.625,12.875],[41.625,13.000],[41.625,13.125],[41.625,13.250],[41.625,13.375],[41.625,13.500],[41.625,13.625],[41.625,13.750],
                  [41.625,13.875],[41.625,14.000],[41.500,12.500],[41.500,12.625],[41.500,12.750],[41.500,12.875],[41.500,13.000],[41.500,13.125],[41.500,13.250],
                  [41.500,13.375],[41.500,13.500],[41.500,13.625],[41.500,13.750],[41.500,13.875],[41.500,14.000],[41.375,12.750],[41.375,12.875],[41.375,13.000],
                  [41.375,13.125],[41.375,13.250],[41.375,13.375],[41.375,13.500],[41.375,13.625],[41.375,13.750],[41.375,13.875],[41.250,13.000],[41.250,13.125],
                  [41.250,13.250],[41.250,13.375],[41.250,13.500],[41.250,13.625],[41.250,13.750],[41.250,13.875],[41.000,12.875],[41.000,13.000],[40.875,12.875],
                  [40.875,13.000],[40.750,13.500],[40.750,13.375],]#165
    avanzamento=0;elementi=len(coord_01_list)
    for coord in coord_01_list:
        latitudine=(coord[0])
        longitudine=(coord[1])
        dati_api, elev=api_01_dwd_global(latitudine, longitudine)
        
        avanzamento=avanzamento+1
        coordinate_per_poligono = ((longitudine-0.0625,latitudine+0.0625), (longitudine+0.0625,latitudine+0.0625),
        (longitudine+0.0625, latitudine-0.0625), (longitudine-0.0625, latitudine-0.0625),(longitudine-0.0625, latitudine+0.0625))

        for j in range(0,7):
                    data=dati_api["date"][j]
                    converti_giorno=datetime.date(data)
                    giorno = converti_giorno + timedelta(days=1)

                    pd_dataframe.loc[len(pd_dataframe)] = [giorno,
                                                           latitudine,
                                                           longitudine,
                                                           elev,
                                                           tronca(dati_api["temperature_2m_max"][j],1),
                                                           tronca(dati_api["wind_speed_10m_max"][j],1),
                                                           tronca(dati_api["snowfall_sum"][j],0),
                                                           tronca(dati_api["rain_sum"][j],0),
                                                           tronca(dati_api["precipitation_sum"][j],0),
                                                           dati_api["weather_code"][j],
                                                           dati_api["precipitation_hours"][j],
                                                           '',#river_discharge
                                                           '',#ts_discharge
                                                           '',#flood_factor
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           coordinate_per_poligono,
                                                           '',
                                                           tronca(dati_api["temperature_2m_max"][j],1),
                                                           tronca(dati_api["wind_speed_10m_max"][j],1),
                                                           tronca(dati_api["snowfall_sum"][j],0),
                                                           tronca(dati_api["precipitation_sum"][j],0),
                                                           tronca(dati_api["rain_sum"][j],0),
                                                           dati_api["weather_code"][j],
                                                           dati_api["precipitation_hours"][j],
                                                           '']
                    
        valore_bar=round((100/elementi)*avanzamento);bar.setValue(valore_bar)
    
    df_ordinato=pd_dataframe.sort_values(by=['giorno','lat','lon']).reset_index()
    #carica i confini regionali
    confini_regione = gpd.read_feather('./conf/confini/confini_regione_lazio.feather')
    geo_confini = gpd.GeoSeries(confini_regione["geometry"]).simplify(tolerance=0.001)
    df2 = gpd.GeoDataFrame({'geometry': geo_confini}, crs=4326)
    
    #calcola le intersezioni tra i confini regionali ed i poligoni 01 modello DWD ICON, popola il dataframe con i valori cdf    
    num_rows = len(df_ordinato)
    avanzamento=0;elementi=num_rows;bar.setValue(avanzamento)
    for i in range(0,num_rows):
           avanzamento=avanzamento+1
           poligono_coord=(df_ordinato.at[i,'poligono_01'])
           poligono_geometria = Polygon(poligono_coord)
           poligono=gpd.GeoSeries(poligono_geometria)
           df1 = gpd.GeoDataFrame({'geometry': poligono}, crs=4326)
           intersezione = df2.overlay(df1, how='intersection')
           df_ordinato.at[i,'geometry']=intersezione.at[0, 'geometry']
           df_ordinato.at[i,'index']=i

           df_ordinato.at[i,'hwdi']=calcola_hwdi(df_ordinato.at[i,'temperature_2m_max'],df_ordinato.at[i,'precipitation_sum'])
           df_ordinato.at[i,'hwdi_HM']=df_ordinato.at[i,'hwdi']/14
           df_ordinato.at[i,'prob_tralicci']=calcola_prob_tralicci(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_linea_esterna']=calcola_prob_linea_esterna(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'m_mm']=calcola_stima_m_ice(df_ordinato.at[i,'weather_code'],df_ordinato.at[i,'precipitation_hours'],df_ordinato.at[i,'wind_speed_10m_max'],df_ordinato.at[i,'precipitation_sum'])
           df_ordinato.at[i,'M_mm']=15
           df_ordinato.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(df_ordinato.at[i,'m_mm'],df_ordinato.at[i,'M_mm'])
           df_ordinato.at[i,'prob_pali_la_nuovi']=calcola_prob_pali_legnoacciaio_nuovi(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_20']=calcola_prob_pali_legno_20(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_40']=calcola_prob_pali_legno_40(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_60']=calcola_prob_pali_legno_60(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'tp65']=calcola_tp65(df_ordinato.at[i,'temperature_2m_max'])
           df_ordinato.at[i,'td65']=calcola_td65(df_ordinato.at[i,'temperature_2m_max'])
           valore_bar=round((100/elementi)*avanzamento);bar.setValue(valore_bar)

    #crea il geodataframe con le geometrie (overlay)      
    geo=gpd.GeoDataFrame(df_ordinato, geometry='geometry')
    if len(geo)==1155:
         geo.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
         geo.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')

         ct = datetime.now()
         timestamp = ct.timestamp()
         date_time = datetime.fromtimestamp(timestamp)
         data = date_time.strftime("%Y_%m_%d_%H%M%S_01deg")
         geo.to_feather('./scenari/' + 'Lazio_' + data + '.feather') #salva i dati nello storico
         abilita_elabora_scenario()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Errore")
        msg.setText("Dati incompleti/non disponibili sul server remoto. Riprovare all'inizio della prossima ora!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

#scarica i dati meteo richiamando l'api per ciascun valore di coordinata presente nella lista coord_002_list e crea il dataframe
#completo delle probabilità di failure richiamando le funzioni delle curve di fragilità
def pulsante_scarica_dati_meteo_002():
    pd_dataframe=pd.DataFrame(columns=['giorno',
                                       'lat',
                                       'lon',
                                       'elev',
                                       'temperature_2m_max',
                                       'wind_speed_10m_max',
                                       'snowfall_sum',
                                       'rain_sum',
                                       'precipitation_sum',
                                       'weather_code',
                                       'precipitation_hours',
                                       'river_discharge',
                                       'ts_discharge',
                                       'flood_factor',
                                       'hwdi',
                                       'hwdi_HM',
                                       'prob_tralicci',
                                       'prob_linea_esterna',
                                       'm_mm',
                                       'M_mm',
                                       'prob_linea_esterna_ice',
                                       'prob_pali_la_nuovi',
                                       'prob_pali_l_20',
                                       'prob_pali_l_40',
                                       'prob_pali_l_60',
                                       'tp65',
                                       'td65',
                                       'flood_warning',
                                       'flood_depth',
                                       'flood_risk_cabina',
                                       'poligono_002',
                                       'geometry',
                                       'bk_temperature_2m_max',
                                       'bk_wind_speed_10m_max',
                                       'bk_snowfall_sum',
                                       'bk_precipitation_sum',
                                       'bk_rain_sum',
                                       'bk_weather_code',
                                       'bk_precipitation_hours',
                                       'bk_river_discharge'])
    
    provincia=toolbar_combobox_scarica_dati_meteo_002_seleziona_provincia.currentText()

    if provincia=="Viterbo":
        confini_provincia = gpd.read_feather('./conf/confini/viterbo.feather')
        coord_002_list=[
            [42.24, 11.74],[42.24, 11.76],[42.24, 11.78],[42.24, 11.80],[42.24, 11.82],[42.24, 11.84],[42.24, 11.86],[42.24, 11.88],[42.24, 11.90],[42.24, 11.92],
            [42.24, 11.94],[42.24, 11.96],[42.24, 11.98],[42.24, 12.00],[42.24, 12.02],[42.24, 12.04],[42.24, 12.06],[42.24, 12.08],[42.24, 12.10],[42.24, 12.12],
            [42.24, 12.14],[42.24, 12.16],[42.24, 12.18],[42.24, 12.20],[42.24, 12.22],[42.24, 12.24],[42.26, 11.74],[42.26, 11.76],[42.26, 11.78],[42.26, 11.80],
            [42.26, 11.82],[42.26, 11.84],[42.26, 11.86],[42.26, 11.88],[42.26, 11.90],[42.26, 11.92],[42.26, 11.94],[42.26, 11.96],[42.26, 11.98],[42.26, 12.00],
            [42.26, 12.02],[42.26, 12.04],[42.26, 12.06],[42.26, 12.08],[42.26, 12.10],[42.26, 12.12],[42.26, 12.14],[42.26, 12.16],[42.26, 12.18],[42.26, 12.20],
            [42.26, 12.22],[42.26, 12.24],[42.28, 11.74],[42.28, 11.76],[42.28, 11.78],[42.28, 11.80],[42.28, 11.82],[42.28, 11.84],[42.28, 11.86],[42.28, 11.88],
            [42.28, 11.90],[42.28, 11.92],[42.28, 11.94],[42.28, 11.96],[42.28, 11.98],[42.28, 12.00],[42.28, 12.02],[42.28, 12.04],[42.28, 12.06],[42.28, 12.08],
            [42.28, 12.10],[42.28, 12.12],[42.28, 12.14],[42.28, 12.16],[42.28, 12.18],[42.28, 12.20],[42.28, 12.22],[42.28, 12.24],[42.30, 11.74],[42.30, 11.76],
            [42.30, 11.78],[42.30, 11.80],[42.30, 11.82],[42.30, 11.84],[42.30, 11.86],[42.30, 11.88],[42.30, 11.90],[42.30, 11.92],[42.30, 11.94],[42.30, 11.96],
            [42.30, 11.98],[42.30, 12.00],[42.30, 12.02],[42.30, 12.04],[42.30, 12.06],[42.30, 12.08],[42.30, 12.10],[42.30, 12.12],[42.30, 12.14],[42.30, 12.16],
            [42.30, 12.18],[42.30, 12.20],[42.30, 12.22],[42.30, 12.24],[42.32, 11.74],[42.32, 11.76],[42.32, 11.78],[42.32, 11.80],[42.32, 11.82],[42.32, 11.84],
            [42.32, 11.86],[42.32, 11.88],[42.32, 11.90],[42.32, 11.92],[42.32, 11.94],[42.32, 11.96],[42.32, 11.98],[42.32, 12.00],[42.32, 12.02],[42.32, 12.04],
            [42.32, 12.06],[42.32, 12.08],[42.32, 12.10],[42.32, 12.12],[42.32, 12.14],[42.32, 12.16],[42.32, 12.18],[42.32, 12.20],[42.32, 12.22],[42.32, 12.24],
            [42.34, 11.74],[42.34, 11.76],[42.34, 11.78],[42.34, 11.80],[42.34, 11.82],[42.34, 11.84],[42.34, 11.86],[42.34, 11.88],[42.34, 11.90],[42.34, 11.92],
            [42.34, 11.94],[42.34, 11.96],[42.34, 11.98],[42.34, 12.00],[42.34, 12.02],[42.34, 12.04],[42.34, 12.06],[42.34, 12.08],[42.34, 12.10],[42.34, 12.12],
            [42.34, 12.14],[42.34, 12.16],[42.34, 12.18],[42.34, 12.20],[42.34, 12.22],[42.34, 12.24],[42.36, 11.74],[42.36, 11.76],[42.36, 11.78],[42.36, 11.80],
            [42.36, 11.82],[42.36, 11.84],[42.36, 11.86],[42.36, 11.88],[42.36, 11.90],[42.36, 11.92],[42.36, 11.94],[42.36, 11.96],[42.36, 11.98],[42.36, 12.00],
            [42.36, 12.02],[42.36, 12.04],[42.36, 12.06],[42.36, 12.08],[42.36, 12.10],[42.36, 12.12],[42.36, 12.14],[42.36, 12.16],[42.36, 12.18],[42.36, 12.20],
            [42.36, 12.22],[42.36, 12.24],[42.38, 11.74],[42.38, 11.76],[42.38, 11.78],[42.38, 11.80],[42.38, 11.82],[42.38, 11.84],[42.38, 11.86],[42.38, 11.88],
            [42.38, 11.90],[42.38, 11.92],[42.38, 11.94],[42.38, 11.96],[42.38, 11.98],[42.38, 12.00],[42.38, 12.02],[42.38, 12.04],[42.38, 12.06],[42.38, 12.08],#200
            [42.38, 12.10],[42.38, 12.12],[42.38, 12.14],[42.38, 12.16],[42.38, 12.18],[42.38, 12.20],[42.38, 12.22],[42.38, 12.24],[42.40, 11.74],[42.40, 11.76],
            [42.40, 11.78],[42.40, 11.80],[42.40, 11.82],[42.40, 11.84],[42.40, 11.86],[42.40, 11.88],[42.40, 11.90],[42.40, 11.92],[42.40, 11.94],[42.40, 11.96],
            [42.40, 11.98],[42.40, 12.00],[42.40, 12.02],[42.40, 12.04],[42.40, 12.06],[42.40, 12.08],[42.40, 12.10],[42.40, 12.12],[42.40, 12.14],[42.40, 12.16],
            [42.40, 12.18],[42.40, 12.20],[42.40, 12.22],[42.40, 12.24],[42.42, 11.74],[42.42, 11.76],[42.42, 11.78],[42.42, 11.80],[42.42, 11.82],[42.42, 11.84],
            [42.42, 11.86],[42.42, 11.88],[42.42, 11.90],[42.42, 11.92],[42.42, 11.94],[42.42, 11.96],[42.42, 11.98],[42.42, 12.00],[42.42, 12.02],[42.42, 12.04],
            [42.42, 12.06],[42.42, 12.08],[42.42, 12.10],[42.42, 12.12],[42.42, 12.14],[42.42, 12.16],[42.42, 12.18],[42.42, 12.20],[42.42, 12.22],[42.42, 12.24],
            [42.44, 11.74],[42.44, 11.76],[42.44, 11.78],[42.44, 11.80],[42.44, 11.82],[42.44, 11.84],[42.44, 11.86],[42.44, 11.88],[42.44, 11.90],[42.44, 11.92],
            [42.44, 11.94],[42.44, 11.96],[42.44, 11.98],[42.44, 12.00],[42.44, 12.02],[42.44, 12.04],[42.44, 12.06],[42.44, 12.08],[42.44, 12.10],[42.44, 12.12],
            [42.44, 12.14],[42.44, 12.16],[42.44, 12.18],[42.44, 12.20],[42.44, 12.22],[42.44, 12.24],[42.46, 11.74],[42.46, 11.76],[42.46, 11.78],[42.46, 11.80],
            [42.46, 11.82],[42.46, 11.84],[42.46, 11.86],[42.46, 11.88],[42.46, 11.90],[42.46, 11.92],[42.46, 11.94],[42.46, 11.96],[42.46, 11.98],[42.46, 12.00],
            [42.46, 12.02],[42.46, 12.04],[42.46, 12.06],[42.46, 12.08],[42.46, 12.10],[42.46, 12.12],[42.46, 12.14],[42.46, 12.16],[42.46, 12.18],[42.46, 12.20],
            [42.46, 12.22],[42.46, 12.24],[42.48, 11.74],[42.48, 11.76],[42.48, 11.78],[42.48, 11.80],[42.48, 11.82],[42.48, 11.84],[42.48, 11.86],[42.48, 11.88],
            [42.48, 11.90],[42.48, 11.92],[42.48, 11.94],[42.48, 11.96],[42.48, 11.98],[42.48, 12.00],[42.48, 12.02],[42.48, 12.04],[42.48, 12.06],[42.48, 12.08],
            [42.48, 12.10],[42.48, 12.12],[42.48, 12.14],[42.48, 12.16],[42.48, 12.18],[42.48, 12.20],[42.48, 12.22],[42.48, 12.24],[42.50, 11.74],[42.50, 11.76],
            [42.50, 11.78],[42.50, 11.80],[42.50, 11.82],[42.50, 11.84],[42.50, 11.86],[42.50, 11.88],[42.50, 11.90],[42.50, 11.92],[42.50, 11.94],[42.50, 11.96],
            [42.50, 11.98],[42.50, 12.00],[42.50, 12.02],[42.50, 12.04],[42.50, 12.06],[42.50, 12.08],[42.50, 12.10],[42.50, 12.12],[42.50, 12.14],[42.50, 12.16],
            [42.50, 12.18],[42.50, 12.20],[42.50, 12.22],[42.50, 12.24],[42.52, 11.74],[42.52, 11.76],[42.52, 11.78],[42.52, 11.80],[42.52, 11.82],[42.52, 11.84],
            [42.52, 11.86],[42.52, 11.88],[42.52, 11.90],[42.52, 11.92],[42.52, 11.94],[42.52, 11.96],[42.52, 11.98],[42.52, 12.00],[42.52, 12.02],[42.52, 12.04],
            [42.52, 12.06],[42.52, 12.08],[42.52, 12.10],[42.52, 12.12],[42.52, 12.14],[42.52, 12.16],[42.52, 12.18],[42.52, 12.20],[42.52, 12.22],[42.52, 12.24],
            [42.54, 11.74],[42.54, 11.76],[42.54, 11.78],[42.54, 11.80],[42.54, 11.82],[42.54, 11.84],[42.54, 11.86],[42.54, 11.88],[42.54, 11.90],[42.54, 11.92],#400
            [42.54, 11.94],[42.54, 11.96],[42.54, 11.98],[42.54, 12.00],[42.54, 12.02],[42.54, 12.04],[42.54, 12.06],[42.54, 12.08],[42.54, 12.10],[42.54, 12.12],
            [42.54, 12.14],[42.54, 12.16],[42.54, 12.18],[42.54, 12.20],[42.54, 12.22],[42.54, 12.24],[42.56, 11.74],[42.56, 11.76],[42.56, 11.78],[42.56, 11.80],
            [42.56, 11.82],[42.56, 11.84],[42.56, 11.86],[42.56, 11.88],[42.56, 11.90],[42.56, 11.92],[42.56, 11.94],[42.56, 11.96],[42.56, 11.98],[42.56, 12.00],
            [42.56, 12.02],[42.56, 12.04],[42.56, 12.06],[42.56, 12.08],[42.56, 12.10],[42.56, 12.12],[42.56, 12.14],[42.56, 12.16],[42.56, 12.18],[42.56, 12.20],
            [42.56, 12.22],[42.56, 12.24],[42.58, 11.74],[42.58, 11.76],[42.58, 11.78],[42.58, 11.80],[42.58, 11.82],[42.58, 11.84],[42.58, 11.86],[42.58, 11.88],
            [42.58, 11.90],[42.58, 11.92],[42.58, 11.94],[42.58, 11.96],[42.58, 11.98],[42.58, 12.00],[42.58, 12.02],[42.58, 12.04],[42.58, 12.06],[42.58, 12.08],
            [42.58, 12.10],[42.58, 12.12],[42.58, 12.14],[42.58, 12.16],[42.58, 12.18],[42.58, 12.20],[42.58, 12.22],[42.58, 12.24],[42.60, 11.74],[42.60, 11.76],
            [42.60, 11.78],[42.60, 11.80],[42.60, 11.82],[42.60, 11.84],[42.60, 11.86],[42.60, 11.88],[42.60, 11.90],[42.60, 11.92],[42.60, 11.94],[42.60, 11.96],
            [42.60, 11.98],[42.60, 12.00],[42.60, 12.02],[42.60, 12.04],[42.60, 12.06],[42.60, 12.08],[42.60, 12.10],[42.60, 12.12],[42.60, 12.14],[42.60, 12.16],
            [42.60, 12.18],[42.60, 12.20],[42.60, 12.22],[42.60, 12.24],[42.62, 11.74],[42.62, 11.76],[42.62, 11.78],[42.62, 11.80],[42.62, 11.82],[42.62, 11.84],
            [42.62, 11.86],[42.62, 11.88],[42.62, 11.90],[42.62, 11.92],[42.62, 11.94],[42.62, 11.96],[42.62, 11.98],[42.62, 12.00],[42.62, 12.02],[42.62, 12.04],
            [42.62, 12.06],[42.62, 12.08],[42.62, 12.10],[42.62, 12.12],[42.62, 12.14],[42.62, 12.16],[42.62, 12.18],[42.62, 12.20],[42.62, 12.22],[42.62, 12.24],
            [42.24, 12.26],[42.24, 12.28],[42.24, 12.30],[42.24, 12.32],[42.24, 12.34],[42.24, 12.36],[42.24, 12.38],[42.24, 12.40],[42.24, 12.42],[42.26, 12.26],
            [42.26, 12.28],[42.26, 12.30],[42.26, 12.32],[42.26, 12.34],[42.26, 12.36],[42.26, 12.38],[42.26, 12.40],[42.26, 12.42],[42.28, 12.26],[42.28, 12.28],
            [42.28, 12.30],[42.28, 12.32],[42.28, 12.34],[42.28, 12.36],[42.28, 12.38],[42.28, 12.40],[42.28, 12.42],[42.30, 12.26],[42.30, 12.28],[42.30, 12.30],
            [42.30, 12.32],[42.30, 12.34],[42.30, 12.36],[42.30, 12.38],[42.30, 12.40],[42.30, 12.42],[42.32, 12.26],[42.32, 12.28],[42.32, 12.30],[42.32, 12.32],
            [42.32, 12.34],[42.32, 12.36],[42.32, 12.38],[42.32, 12.40],[42.32, 12.42],[42.34, 12.26],[42.34, 12.28],[42.34, 12.30],[42.34, 12.32],[42.34, 12.34],
            [42.34, 12.36],[42.34, 12.38],[42.34, 12.40],[42.34, 12.42],[42.36, 12.26],[42.36, 12.28],[42.36, 12.30],[42.36, 12.32],[42.36, 12.34],[42.36, 12.36],
            [42.36, 12.38],[42.36, 12.40],[42.36, 12.42],[42.38, 12.26],[42.38, 12.28],[42.38, 12.30],[42.38, 12.32],[42.38, 12.34],[42.38, 12.36],[42.38, 12.38],
            [42.38, 12.40],[42.38, 12.42],[42.40, 12.26],[42.40, 12.28],[42.40, 12.30],[42.40, 12.32],[42.40, 12.34],[42.40, 12.36],[42.40, 12.38],[42.40, 12.40],#600
            [42.40, 12.42],[42.42, 12.26],[42.42, 12.28],[42.42, 12.30],[42.42, 12.32],[42.42, 12.34],[42.42, 12.36],[42.42, 12.38],[42.42, 12.40],[42.42, 12.42],            
            [42.44, 12.26],[42.44, 12.28],[42.44, 12.30],[42.44, 12.32],[42.44, 12.34],[42.44, 12.36],[42.44, 12.38],[42.44, 12.40],[42.44, 12.42],[42.46, 12.26],
            [42.46, 12.28],[42.46, 12.30],[42.46, 12.32],[42.46, 12.34],[42.46, 12.36],[42.46, 12.38],[42.46, 12.40],[42.46, 12.42],[42.48, 12.26],[42.48, 12.28],
            [42.48, 12.30],[42.48, 12.32],[42.48, 12.34],[42.48, 12.36],[42.48, 12.38],[42.48, 12.40],[42.48, 12.42],[42.66, 11.82],[42.66, 11.84],[42.66, 11.86],
            [42.66, 11.88],[42.66, 11.90],[42.66, 11.92],[42.68, 11.82],[42.68, 11.84],[42.68, 11.86],[42.68, 11.88],[42.68, 11.90],[42.68, 11.92],[42.70, 11.82],
            [42.70, 11.84],[42.70, 11.86],[42.70, 11.88],[42.70, 11.90],[42.70, 11.92],[42.72, 11.82],[42.72, 11.84],[42.72, 11.86],[42.72, 11.88],[42.72, 11.90],
            [42.72, 11.92],[42.74, 11.82],[42.74, 11.84],[42.74, 11.86],[42.74, 11.88],[42.74, 11.90],[42.74, 11.92],[42.76, 11.82],[42.76, 11.84],[42.76, 11.86],
            [42.76, 11.88],[42.76, 11.90],[42.76, 11.92],[42.78, 11.82],[42.78, 11.84],[42.78, 11.86],[42.78, 11.88],[42.78, 11.90],[42.78, 11.92],[42.80, 11.82],
            [42.80, 11.84],[42.80, 11.86],[42.80, 11.88],[42.80, 11.90],[42.80, 11.92],[42.82, 11.82],[42.82, 11.84],[42.82, 11.86],[42.82, 11.88],[42.82, 11.90],
            [42.82, 11.92],[42.64, 11.76],[42.64, 11.78],[42.64, 11.80],[42.64, 11.82],[42.64, 11.84],[42.64, 11.86],[42.64, 11.88],[42.64, 11.90],[42.64, 11.92],#700
            [42.64, 11.94],[42.64, 11.96],[42.64, 11.98],[42.64, 12.00],[42.64, 12.02],[42.64, 12.04],[42.64, 12.06],[42.64, 12.08],[42.64, 12.10],[42.64, 12.12],
            [42.64, 12.14],[42.64, 12.16],[42.64, 12.18],[42.64, 12.20],[42.64, 12.22],[42.64, 12.24],[42.50, 12.26],[42.52, 12.26],[42.54, 12.26],[42.56, 12.26],
            [42.50, 12.28],[42.52, 12.28],[42.54, 12.28],[42.56, 12.28],[42.50, 12.30],[42.50, 12.32],[42.50, 12.34],[42.50, 12.38],[42.50, 12.40],[42.50, 12.42],
            [42.32, 11.62],[42.32, 11.64],[42.32, 11.66],[42.32, 11.68],[42.32, 11.70],[42.32, 11.72],[42.34, 11.62],[42.34, 11.64],[42.34, 11.66],[42.34, 11.68],
            [42.34, 11.70],[42.34, 11.72],[42.36, 11.62],[42.36, 11.64],[42.36, 11.66],[42.36, 11.68],[42.36, 11.70],[42.36, 11.72],[42.38, 11.62],[42.38, 11.64],
            [42.38, 11.66],[42.38, 11.68],[42.38, 11.70],[42.38, 11.72],[42.40, 11.62],[42.40, 11.64],[42.40, 11.66],[42.40, 11.68],[42.40, 11.70],[42.40, 11.72],
            [42.42, 11.62],[42.42, 11.64],[42.42, 11.66],[42.42, 11.68],[42.42, 11.70],[42.42, 11.72],[42.44, 11.62],[42.44, 11.64],[42.44, 11.66],[42.44, 11.68],
            [42.44, 11.70],[42.44, 11.72],[42.46, 11.62],[42.46, 11.64],[42.46, 11.66],[42.46, 11.68],[42.46, 11.70],[42.46, 11.72],[42.48, 11.62],[42.48, 11.64],
            [42.48, 11.66],[42.48, 11.68],[42.48, 11.70],[42.48, 11.72],[42.50, 11.62],[42.50, 11.64],[42.50, 11.66],[42.50, 11.68],[42.50, 11.70],[42.50, 11.72],
            [42.52, 11.62],[42.52, 11.64],[42.52, 11.66],[42.52, 11.68],[42.52, 11.70],[42.52, 11.72],[42.54, 11.62],[42.54, 11.64],[42.54, 11.66],[42.54, 11.68],#800
            [42.54, 11.70],[42.54, 11.72],[42.56, 11.62],[42.56, 11.64],[42.56, 11.66],[42.56, 11.68],[42.56, 11.70],[42.56, 11.72],[42.36, 11.48],[42.36, 11.50],
            [42.36, 11.52],[42.36, 11.54],[42.36, 11.56],[42.36, 11.58],[42.36, 11.60],[42.38, 11.48],[42.38, 11.50],[42.38, 11.52],[42.38, 11.54],[42.38, 11.56],
            [42.38, 11.58],[42.38, 11.60],[42.40, 11.48],[42.40, 11.50],[42.40, 11.52],[42.40, 11.54],[42.40, 11.56],[42.40, 11.58],[42.40, 11.60],[42.42, 11.48],
            [42.42, 11.50],[42.42, 11.52],[42.42, 11.54],[42.42, 11.56],[42.42, 11.58],[42.42, 11.60],[42.44, 11.48],[42.44, 11.50],[42.44, 11.52],[42.44, 11.54],
            [42.44, 11.56],[42.44, 11.58],[42.44, 11.60],[42.18, 11.74],[42.18, 11.76],[42.18, 11.78],[42.18, 11.80],[42.18, 11.82],[42.18, 11.84],[42.18, 11.86],
            [42.20, 11.74],[42.20, 11.76],[42.20, 11.78],[42.20, 11.80],[42.20, 11.82],[42.20, 11.84],[42.20, 11.86],[42.22, 11.74],[42.22, 11.76],[42.22, 11.78],
            [42.22, 11.80],[42.22, 11.82],[42.22, 11.84],[42.22, 11.86],[42.16, 12.00],[42.16, 12.02],[42.16, 12.04],[42.16, 12.06],[42.16, 12.08],[42.16, 12.10],
            [42.16, 12.12],[42.16, 12.14],[42.16, 12.16],[42.16, 12.30],[42.16, 12.32],[42.16, 12.34],[42.16, 12.36],[42.18, 12.00],[42.18, 12.02],[42.18, 12.04],#880_ok
            [42.18, 12.06],[42.18, 12.08],[42.18, 12.10],[42.18, 12.12],[42.18, 12.14],[42.18, 12.16],[42.18, 12.18],[42.18, 12.20],[42.18, 12.22],[42.18, 12.24],
            [42.18, 12.26],[42.18, 12.28],[42.18, 12.30],[42.18, 12.32],[42.18, 12.34],[42.18, 12.36],[42.18, 12.38],[42.22, 11.88],[42.22, 11.94],[42.22, 11.96],
            [42.22, 11.98],[42.22, 12.00],[42.22, 12.02],[42.22, 12.04],[42.22, 12.06],[42.22, 12.08],[42.22, 12.10],[42.22, 12.12],[42.22, 12.14],[42.22, 12.16],
            [42.22, 12.18],[42.22, 12.20],[42.22, 12.22],[42.22, 12.24],[42.22, 12.26],[42.22, 12.28],[42.22, 12.30],[42.22, 12.32],[42.22, 12.34],[42.22, 12.36],
            [42.22, 12.38],[42.22, 12.40],[42.22, 12.42],[42.22, 12.44],[42.22, 12.46],[42.20, 11.98],[42.20, 12.00],[42.20, 12.02],[42.20, 12.04],[42.20, 12.06],
            [42.20, 12.08],[42.20, 12.10],[42.20, 12.12],[42.20, 12.14],[42.20, 12.16],[42.20, 12.18],[42.20, 12.20],[42.20, 12.22],[42.20, 12.24],[42.20, 12.26],
            [42.20, 12.28],[42.20, 12.30],[42.20, 12.32],[42.20, 12.34],[42.20, 12.36],[42.20, 12.38],[42.20, 12.42],[42.20, 12.44],[42.20, 12.46],[42.24, 12.44],
            [42.24, 12.46],[42.24, 12.48],[42.26, 12.44],[42.26, 12.46],[42.26, 12.48],[42.28, 12.44],[42.42, 12.46],[42.28, 12.46],[42.28, 12.48],[42.30, 12.44],
            [42.30, 12.46],[42.30, 12.48],[42.32, 12.44],[42.32, 12.46],[42.32, 12.48],[42.34, 12.44],[42.34, 12.46],[42.34, 12.48],[42.36, 12.44],[42.36, 12.46],
            [42.36, 12.48],[42.38, 12.44],[42.38, 12.46],[42.38, 12.48],[42.40, 12.44],[42.40, 12.46],[42.40, 12.48],[42.42, 12.44],[42.30, 12.50],[42.30, 12.52],
            [42.28, 12.50],[42.28, 12.52],[42.18, 12.42],[42.18, 12.44],[42.14, 12.32],[42.16, 11.74],[42.16, 11.76],[42.16, 11.78],[42.16, 11.80],[42.16, 11.82],
            [42.14, 11.82],[42.18, 11.72],[42.20, 11.72],[42.22, 11.72],[42.24, 11.72],[42.26, 11.72],[42.28, 11.72],[42.30, 11.72],[42.22, 11.70],[42.24, 11.70],#1000
            [42.26, 11.70],[42.28, 11.70],[42.30, 11.70],[42.24, 11.68],[42.26, 11.68],[42.28, 11.68],[42.30, 11.68],[42.26, 11.66],[42.28, 11.66],[42.30, 11.66],
            [42.28, 11.64],[42.30, 11.64],[42.30, 11.62],[42.30, 11.60],[42.34, 11.54],[42.34, 11.56],[42.34, 11.58],[42.34, 11.60],[42.66, 12.22],[42.66, 12.20],
            [42.32, 11.58],[42.32, 11.60],[42.38, 11.46],[42.40, 11.46],[42.50, 11.58],[42.50, 11.60],[42.52, 11.56],[42.52, 11.58],[42.52, 11.60],[42.54, 11.56],
            [42.54, 11.58],[42.54, 11.60],[42.56, 11.58],[42.56, 11.60],[42.58, 11.66],[42.58, 11.68],[42.58, 11.70],[42.58, 11.72],[42.60, 11.68],[42.60, 11.70],
            [42.60, 11.72],[42.66, 11.80],[42.68, 11.78],[42.68, 11.80],[42.70, 11.78],[42.70, 11.80],[42.72, 11.80],[42.76, 11.78],[42.76, 11.80],[42.78, 11.76],
            [42.78, 11.78],[42.78, 11.80],[42.80, 11.76],[42.80, 11.78],[42.80, 11.80],[42.82, 11.76],[42.82, 11.78],[42.82, 11.80],[42.78, 11.74],[42.84, 11.84],
            [42.84, 11.86],[42.84, 11.88],[42.84, 11.90],[42.72, 11.94],[42.72, 11.96],[42.74, 11.94],[42.74, 11.96],[42.76, 11.94],[42.76, 11.96],[42.78, 11.94],
            [42.78, 11.96],[42.74, 11.98],[42.76, 11.98],[42.70, 11.94],[42.68, 11.94],[42.68, 11.96],[42.68, 11.98],[42.66, 11.94],[42.66, 11.96],[42.66, 11.98],
            [42.66, 12.00],[42.66, 12.02],[42.66, 12.06],[42.66, 12.08],[42.66, 12.10],[42.66, 12.12],[42.66, 12.14],[42.66, 12.16],[42.66, 12.18],[42.68, 12.16],
            [42.68, 12.18]#1091
            ]
                    


    if provincia=="Latina":
        confini_provincia = gpd.read_feather('./conf/confini/latina.feather')
        coord_002_list=[
            [41.72, 12.94],[41.42, 12.78],[41.42, 12.80],[41.42, 12.82],[41.42, 12.84],[41.42, 12.86],[41.42, 12.88],[41.42, 12.90],[41.42, 12.92],[41.42, 12.94],
            [41.42, 12.96],[41.42, 12.98],[41.42, 13.00],[41.42, 13.02],[41.42, 13.04],[41.42, 13.06],[41.42, 13.08],[41.42, 13.10],[41.42, 13.12],[41.42, 13.14],
            [41.42, 13.16],[41.42, 13.18],[41.42, 13.20],[41.44, 12.78],[41.44, 12.80],[41.44, 12.82],[41.44, 12.84],[41.44, 12.86],[41.44, 12.88],[41.44, 12.90],
            [41.44, 12.92],[41.44, 12.94],[41.44, 12.96],[41.44, 12.98],[41.44, 13.00],[41.44, 13.02],[41.44, 13.04],[41.44, 13.06],[41.44, 13.08],[41.44, 13.10],
            [41.44, 13.12],[41.44, 13.14],[41.44, 13.16],[41.44, 13.18],[41.44, 13.20],[41.46, 12.78],[41.46, 12.80],[41.46, 12.82],[41.46, 12.84],[41.46, 12.86],
            [41.46, 12.88],[41.46, 12.90],[41.46, 12.92],[41.46, 12.94],[41.46, 12.96],[41.46, 12.98],[41.46, 13.00],[41.46, 13.02],[41.46, 13.04],[41.46, 13.06],
            [41.46, 13.08],[41.46, 13.10],[41.46, 13.12],[41.46, 13.14],[41.46, 13.16],[41.46, 13.18],[41.46, 13.20],[41.48, 12.78],[41.48, 12.80],[41.48, 12.82],
            [41.48, 12.84],[41.48, 12.86],[41.48, 12.88],[41.48, 12.90],[41.48, 12.92],[41.48, 12.94],[41.48, 12.96],[41.48, 12.98],[41.48, 13.00],[41.48, 13.02],
            [41.48, 13.04],[41.48, 13.06],[41.48, 13.08],[41.48, 13.10],[41.48, 13.12],[41.48, 13.14],[41.48, 13.16],[41.48, 13.18],[41.48, 13.20],[41.50, 12.78],
            [41.50, 12.80],[41.50, 12.82],[41.50, 12.84],[41.50, 12.86],[41.50, 12.88],[41.50, 12.90],[41.50, 12.92],[41.50, 12.94],[41.50, 12.96],[41.50, 12.98],
            [41.50, 13.00],[41.50, 13.02],[41.50, 13.04],[41.50, 13.06],[41.50, 13.08],[41.50, 13.10],[41.50, 13.12],[41.50, 13.14],[41.50, 13.16],[41.50, 13.18],
            [41.50, 13.20],[41.52, 12.78],[41.52, 12.80],[41.52, 12.82],[41.52, 12.84],[41.52, 12.86],[41.52, 12.88],[41.52, 12.90],[41.52, 12.92],[41.52, 12.94],
            [41.52, 12.96],[41.52, 12.98],[41.52, 13.00],[41.52, 13.02],[41.52, 13.04],[41.52, 13.06],[41.52, 13.08],[41.52, 13.10],[41.52, 13.12],[41.52, 13.14],
            [41.52, 13.16],[41.52, 13.18],[41.52, 13.20],[41.54, 12.78],[41.54, 12.80],[41.54, 12.82],[41.54, 12.84],[41.54, 12.86],[41.54, 12.88],[41.54, 12.90],
            [41.54, 12.92],[41.54, 12.94],[41.54, 12.96],[41.54, 12.98],[41.54, 13.00],[41.54, 13.02],[41.54, 13.04],[41.54, 13.06],[41.54, 13.08],[41.54, 13.10],
            [41.54, 13.12],[41.54, 13.14],[41.54, 13.16],[41.54, 13.18],[41.54, 13.20],[41.56, 12.78],[41.56, 12.80],[41.56, 12.82],[41.56, 12.84],[41.56, 12.86],
            [41.56, 12.88],[41.56, 12.90],[41.56, 12.92],[41.56, 12.94],[41.56, 12.96],[41.56, 12.98],[41.56, 13.00],[41.56, 13.02],[41.56, 13.04],[41.56, 13.06],
            [41.56, 13.08],[41.56, 13.10],[41.56, 13.12],[41.56, 13.14],[41.56, 13.16],[41.56, 13.18],[41.56, 13.20],[41.30, 13.02],[41.30, 13.04],[41.30, 13.06],
            [41.30, 13.08],[41.30, 13.10],[41.30, 13.12],[41.30, 13.14],[41.30, 13.16],[41.30, 13.18],[41.30, 13.20],[41.30, 13.22],[41.30, 13.24],[41.30, 13.26],
            [41.30, 13.28],[41.30, 13.30],[41.30, 13.32],[41.30, 13.34],[41.30, 13.36],[41.30, 13.38],[41.30, 13.40],[41.30, 13.42],[41.30, 13.44],[41.30, 13.46],#200
            [41.30, 13.48],[41.30, 13.50],[41.30, 13.52],[41.30, 13.54],[41.30, 13.56],[41.30, 13.58],[41.32, 13.02],[41.32, 13.04],[41.32, 13.06],[41.32, 13.08],
            [41.32, 13.10],[41.32, 13.12],[41.32, 13.14],[41.32, 13.16],[41.32, 13.18],[41.32, 13.20],[41.32, 13.22],[41.32, 13.24],[41.32, 13.26],[41.32, 13.28],
            [41.32, 13.30],[41.32, 13.32],[41.32, 13.34],[41.32, 13.36],[41.32, 13.38],[41.32, 13.40],[41.32, 13.42],[41.32, 13.44],[41.32, 13.46],[41.32, 13.48],
            [41.32, 13.50],[41.32, 13.52],[41.32, 13.54],[41.32, 13.56],[41.32, 13.58],[41.34, 13.02],[41.34, 13.04],[41.34, 13.06],[41.34, 13.08],[41.34, 13.10],
            [41.34, 13.12],[41.34, 13.14],[41.34, 13.16],[41.34, 13.18],[41.34, 13.20],[41.34, 13.22],[41.34, 13.24],[41.34, 13.26],[41.34, 13.28],[41.34, 13.30],
            [41.34, 13.32],[41.34, 13.34],[41.34, 13.36],[41.34, 13.38],[41.34, 13.40],[41.34, 13.42],[41.34, 13.44],[41.34, 13.46],[41.34, 13.48],[41.34, 13.50],
            [41.34, 13.52],[41.34, 13.54],[41.34, 13.56],[41.34, 13.58],[41.36, 13.02],[41.36, 13.04],[41.36, 13.06],[41.36, 13.08],[41.36, 13.10],[41.36, 13.12],
            [41.36, 13.14],[41.36, 13.16],[41.36, 13.18],[41.36, 13.20],[41.36, 13.22],[41.36, 13.24],[41.36, 13.26],[41.36, 13.28],[41.36, 13.30],[41.36, 13.32],
            [41.36, 13.34],[41.36, 13.36],[41.36, 13.38],[41.36, 13.40],[41.36, 13.42],[41.36, 13.44],[41.36, 13.46],[41.36, 13.48],[41.36, 13.50],[41.36, 13.52],
            [41.36, 13.54],[41.36, 13.56],[41.36, 13.58],[41.38, 13.02],[41.38, 13.04],[41.38, 13.06],[41.38, 13.08],[41.38, 13.10],[41.38, 13.12],[41.38, 13.14],#300
            [41.38, 13.16],[41.38, 13.18],[41.38, 13.20],[41.38, 13.22],[41.38, 13.24],[41.38, 13.26],[41.38, 13.28],[41.38, 13.30],[41.38, 13.32],[41.38, 13.34],
            [41.38, 13.36],[41.38, 13.38],[41.38, 13.40],[41.38, 13.42],[41.38, 13.44],[41.38, 13.46],[41.38, 13.48],[41.38, 13.50],[41.38, 13.52],[41.38, 13.54],
            [41.38, 13.56],[41.38, 13.58],[41.40, 13.02],[41.40, 13.04],[41.40, 13.06],[41.40, 13.08],[41.40, 13.10],[41.40, 13.12],[41.40, 13.14],[41.40, 13.16],
            [41.40, 13.18],[41.40, 13.20],[41.40, 13.22],[41.40, 13.24],[41.40, 13.26],[41.40, 13.28],[41.40, 13.30],[41.40, 13.32],[41.40, 13.34],[41.40, 13.36],
            [41.40, 13.38],[41.40, 13.40],[41.40, 13.42],[41.40, 13.44],[41.40, 13.46],[41.40, 13.48],[41.40, 13.50],[41.40, 13.52],[41.40, 13.54],[41.40, 13.56],
            [41.40, 13.58],[41.66, 12.60],[41.66, 12.62],[41.66, 12.64],[41.66, 12.66],[41.64, 12.58],[41.64, 12.60],[41.64, 12.62],[41.64, 12.64],[40.78, 13.40],
            [41.64, 12.66],[41.62, 12.56],[41.62, 12.58],[41.62, 12.60],[41.62, 12.62],[41.62, 12.64],[41.62, 12.66],[41.60, 12.54],[41.60, 12.56],[41.60, 12.58],
            [41.60, 12.60],[41.60, 12.62],[41.60, 12.64],[41.60, 12.66],[41.60, 12.68],[41.60, 12.70],[41.60, 12.72],[41.60, 12.74],[41.58, 12.56],[41.58, 12.58],
            [41.58, 12.60],[41.58, 12.62],[41.58, 12.64],[41.58, 12.66],[41.58, 12.68],[41.58, 12.70],[41.58, 12.72],[41.58, 12.74],[41.58, 12.76],[41.56, 12.58],
            [41.56, 12.60],[41.56, 12.62],[41.56, 12.64],[41.56, 12.66],[41.56, 12.68],[41.56, 12.70],[41.56, 12.72],[41.56, 12.74],[41.56, 12.76],[41.54, 12.58],
            [41.54, 12.60],[41.54, 12.62],[41.54, 12.64],[41.54, 12.66],[41.54, 12.68],[41.54, 12.70],[41.54, 12.72],[41.54, 12.74],[41.54, 12.76],[41.52, 12.66],
            [41.52, 12.68],[41.52, 12.70],[41.52, 12.72],[41.52, 12.74],[41.52, 12.76],[41.50, 12.68],[41.50, 12.70],[41.50, 12.72],[41.50, 12.74],[41.50, 12.76],
            [41.48, 12.72],[41.48, 12.74],[41.48, 12.76],[41.46, 12.74],[41.46, 12.76],[41.58, 13.04],[41.58, 13.06],[41.58, 12.78],[41.58, 12.80],[41.58, 12.82],
            [41.58, 12.84],[41.58, 12.86],[41.58, 12.88],[41.58, 12.90],[41.58, 12.92],[41.58, 12.94],[41.58, 12.96],[41.58, 12.98],[41.58, 13.00],[41.58, 13.02],
            [41.60, 12.78],[41.60, 12.80],[41.60, 12.82],[41.60, 12.84],[41.60, 12.86],[41.60, 12.88],[41.60, 12.90],[41.60, 12.92],[41.60, 12.94],[41.60, 12.96],
            [41.60, 12.98],[41.60, 13.00],[41.60, 13.02],[41.62, 12.78],[41.62, 12.80],[41.62, 12.82],[41.62, 12.84],[41.62, 12.86],[41.62, 12.88],[41.62, 12.90],
            [41.62, 12.92],[41.62, 12.94],[41.62, 12.96],[41.62, 12.98],[41.62, 13.00],[41.62, 13.02],[41.64, 12.82],[41.64, 12.84],[41.64, 12.86],[41.64, 12.88],
            [41.64, 12.90],[41.64, 12.92],[41.64, 12.94],[41.64, 12.96],[41.64, 12.98],[41.64, 13.00],[41.66, 12.82],[41.66, 12.84],[41.66, 12.86],[41.66, 12.88],
            [41.66, 12.90],[41.66, 12.92],[41.66, 12.94],[41.66, 12.96],[41.66, 12.98],[41.68, 12.86],[41.68, 12.88],[41.68, 12.90],[41.68, 12.92],[41.68, 12.94],
            [41.70, 12.84],[41.70, 12.86],[41.70, 12.88],[41.70, 12.90],[41.70, 12.92],[41.70, 12.94],[41.72, 12.84],[41.72, 12.86],[40.78, 13.42],[41.72, 12.90],#500            
            [41.72, 12.92],[41.58, 13.16],[41.58, 13.18],[41.58, 13.20],[41.42, 13.22],[41.42, 13.24],[41.42, 13.26],[41.42, 13.28],[41.44, 13.22],[41.44, 13.24],
            [41.44, 13.26],[41.46, 13.22],[41.46, 13.24],[41.46, 13.26],[41.46, 13.28],[41.48, 13.22],[41.48, 13.24],[41.48, 13.26],[41.48, 13.28],[41.50, 13.22],
            [41.50, 13.24],[41.50, 13.26],[41.50, 13.28],[41.52, 13.22],[41.52, 13.24],[41.52, 13.26],[41.52, 13.28],[41.54, 13.22],[41.54, 13.24],[41.54, 13.26],
            [41.48, 13.30],[41.46, 13.30],[41.42, 13.30],[41.46, 13.42],[41.46, 13.44],[41.46, 13.46],[41.44, 13.44],[41.44, 13.46],[41.44, 13.48],[41.44, 13.50],
            [41.42, 13.44],[41.42, 13.46],[41.42, 13.48],[41.42, 13.50],[41.42, 13.52],[41.42, 13.54],[41.42, 13.56],[41.40, 12.86],[41.40, 12.88],[41.40, 12.90],#550
            [41.40, 12.92],[41.40, 12.94],[41.40, 12.96],[41.40, 12.98],[41.40, 13.00],[41.38, 12.90],[41.38, 12.92],[41.38, 12.94],[41.38, 12.96],[41.38, 12.98],
            [41.38, 13.00],[41.36, 12.94],[41.36, 12.96],[41.36, 12.98],[41.36, 13.00],[41.34, 12.96],[41.34, 12.98],[41.34, 13.00],[41.32, 12.98],[41.32, 13.00],
            [41.30, 13.00],[41.28, 13.02],[41.28, 13.04],[41.28, 13.06],[41.28, 13.08],[41.28, 13.10],[41.28, 13.12],[41.28, 13.14],[41.28, 13.16],[41.28, 13.18],
            [41.28, 13.20],[41.28, 13.22],[41.28, 13.24],[41.28, 13.26],[41.26, 13.02],[41.26, 13.04],[41.26, 13.06],[41.26, 13.08],[41.26, 13.10],[41.26, 13.12],
            [41.26, 13.14],[41.26, 13.16],[41.24, 13.04],[41.24, 13.06],[41.24, 13.08],[41.24, 13.10],[41.24, 13.12],[41.22, 13.04],[41.22, 13.06],[41.22, 13.08],#600
            [40.80, 13.44],[41.36, 13.70],[41.36, 13.72],[41.34, 13.60],[41.34, 13.66],[41.34, 13.68],[41.34, 13.70],[41.34, 13.72],[41.34, 13.82],[41.34, 13.84],
            [41.34, 13.86],[41.34, 13.88],[41.32, 13.60],[41.32, 13.62],[41.32, 13.64],[41.32, 13.66],[41.32, 13.68],[41.32, 13.70],[41.32, 13.72],[41.32, 13.74],            
            [41.28, 13.66],[41.28, 13.68],[41.28, 13.70],[41.28, 13.72],[41.28, 13.74],[41.28, 13.76],[41.28, 13.78],[41.28, 13.80],[41.28, 13.82],[41.28, 13.84],
            [41.26, 13.42],[41.26, 13.44],[41.26, 13.46],[41.26, 13.48],[41.26, 13.50],[41.26, 13.52],[41.26, 13.54],[41.26, 13.56],[41.26, 13.58],[40.78, 13.46],
            [41.26, 13.60],[41.26, 13.62],[41.26, 13.64],[41.26, 13.66],[41.26, 13.68],[41.26, 13.70],[41.26, 13.72],[41.26, 13.74],[41.26, 13.76],[41.26, 13.78],
            [41.26, 13.80],[41.26, 13.82],[41.26, 13.84],[41.24, 13.46],[41.24, 13.48],[41.24, 13.50],[41.24, 13.52],[41.24, 13.54],[41.24, 13.56],[41.24, 13.58],
            [41.24, 13.68],[41.24, 13.72],[41.24, 13.74],[41.24, 13.76],[41.24, 13.78],[41.24, 13.80],[41.24, 13.82],[41.22, 13.50],[41.22, 13.52],[41.22, 13.54],
            [41.22, 13.56],[41.22, 13.58],[41.22, 13.76],[41.20, 13.56],[41.20, 13.58],[40.94, 12.84],[40.94, 12.86],[40.92, 12.84],[40.92, 12.86],[40.80, 13.46],
            [40.94, 12.98],[40.94, 13.00],[40.92, 12.94],[40.92, 12.96],[40.92, 12.98],[40.90, 12.94],[40.90, 12.96],[40.88, 12.94],[40.88, 12.96],[40.98, 13.04],
            [41.30, 13.64],[41.30, 13.66],[41.30, 13.68],[41.30, 13.70],[41.30, 13.72],[41.30, 13.74],[41.30, 13.76],[41.30, 13.78],[41.30, 13.80],[41.30, 13.82],
            [41.30, 13.84],[41.30, 13.86],[41.30, 13.88],[41.30, 13.90],[41.28, 13.34],[41.28, 13.36],[41.28, 13.38],[41.28, 13.40],[41.28, 13.42],[41.28, 13.44],
            [41.28, 13.46],[41.28, 13.48],[41.28, 13.50],[41.28, 13.52],[41.28, 13.54],[41.28, 13.56],[41.28, 13.58],[41.28, 13.60],[41.28, 13.62],[41.28, 13.64],#720
            [40.98, 13.06],[40.96, 13.04],[40.96, 13.06],[41.30, 13.60],[41.30, 13.62],[41.32, 13.76],[41.32, 13.80],[41.32, 13.82],[41.32, 13.84],[41.32, 13.86],
            [41.32, 13.88],[41.32, 13.90],[41.44, 12.74],[41.44, 12.76],[41.22, 13.10]#735
            ]
                        
            

    if provincia=="Roma":
        confini_provincia = gpd.read_feather('./conf/confini/roma.feather')
        coord_002_list=[
            [42.16, 11.74],[41.74, 12.22],[41.74, 12.24],[41.74, 12.26],[41.74, 12.28],[41.74, 12.30],[41.74, 12.32],[41.74, 12.34],[41.74, 12.36],[41.74, 12.38],
            [41.74, 12.40],[41.74, 12.42],[41.74, 12.44],[41.74, 12.46],[41.74, 12.48],[41.74, 12.50],[41.74, 12.52],[41.74, 12.54],[41.74, 12.56],[41.74, 12.58],
            [41.74, 12.60],[41.74, 12.62],[41.74, 12.64],[41.74, 12.66],[41.74, 12.68],[41.74, 12.70],[41.74, 12.72],[41.74, 12.74],[41.74, 12.76],[41.74, 12.78],
            [41.74, 12.80],[41.74, 12.82],[41.74, 12.84],[41.76, 12.22],[41.76, 12.24],[41.76, 12.26],[41.76, 12.28],[41.76, 12.30],[41.76, 12.32],[41.76, 12.34],
            [41.76, 12.36],[41.76, 12.38],[41.76, 12.40],[41.76, 12.42],[41.76, 12.44],[41.76, 12.46],[41.76, 12.48],[41.76, 12.50],[41.76, 12.52],[41.76, 12.54],
            [41.76, 12.56],[41.76, 12.58],[41.76, 12.60],[41.76, 12.62],[41.76, 12.64],[41.76, 12.66],[41.76, 12.68],[41.76, 12.70],[41.76, 12.72],[41.76, 12.74],
            [41.76, 12.76],[41.76, 12.78],[41.76, 12.80],[41.76, 12.82],[41.76, 12.84],[41.78, 12.22],[41.78, 12.24],[41.78, 12.26],[41.78, 12.28],[41.78, 12.30],
            [41.78, 12.32],[41.78, 12.34],[41.78, 12.36],[41.78, 12.38],[41.78, 12.40],[41.78, 12.42],[41.78, 12.44],[41.78, 12.46],[41.78, 12.48],[41.78, 12.50],
            [41.78, 12.52],[41.78, 12.54],[41.78, 12.56],[41.78, 12.58],[41.78, 12.60],[41.78, 12.62],[41.78, 12.64],[41.78, 12.66],[41.78, 12.68],[41.78, 12.70],
            [41.78, 12.72],[41.78, 12.74],[41.78, 12.76],[41.78, 12.78],[41.78, 12.80],[41.78, 12.82],[41.78, 12.84],[41.80, 12.22],[41.80, 12.24],[41.80, 12.26],
            [41.80, 12.28],[41.80, 12.30],[41.80, 12.32],[41.80, 12.34],[41.80, 12.36],[41.80, 12.38],[41.80, 12.40],[41.80, 12.42],[41.80, 12.44],[41.80, 12.46],
            [41.80, 12.48],[41.80, 12.50],[41.80, 12.52],[41.80, 12.54],[41.80, 12.56],[41.80, 12.58],[41.80, 12.60],[41.80, 12.62],[41.80, 12.64],[41.80, 12.66],
            [41.80, 12.68],[41.80, 12.70],[41.80, 12.72],[41.80, 12.74],[41.80, 12.76],[41.80, 12.78],[41.80, 12.80],[41.80, 12.82],[41.80, 12.84],[41.82, 12.22],
            [41.82, 12.24],[41.82, 12.26],[41.82, 12.28],[41.82, 12.30],[41.82, 12.32],[41.82, 12.34],[41.82, 12.36],[41.82, 12.38],[41.82, 12.40],[41.82, 12.42],
            [41.82, 12.44],[41.82, 12.46],[41.82, 12.48],[41.82, 12.50],[41.82, 12.52],[41.82, 12.54],[41.82, 12.56],[41.82, 12.58],[41.82, 12.60],[41.82, 12.62],
            [41.82, 12.64],[41.82, 12.66],[41.82, 12.68],[41.82, 12.70],[41.82, 12.72],[41.82, 12.74],[41.82, 12.76],[41.82, 12.78],[41.82, 12.80],[41.82, 12.82],
            [41.82, 12.84],[41.84, 12.22],[41.84, 12.24],[41.84, 12.26],[41.84, 12.28],[41.84, 12.30],[41.84, 12.32],[41.84, 12.34],[41.84, 12.36],[41.84, 12.38],
            [41.84, 12.40],[41.84, 12.42],[41.84, 12.44],[41.84, 12.46],[41.84, 12.48],[41.84, 12.50],[41.84, 12.52],[41.84, 12.54],[41.84, 12.56],[41.84, 12.58],
            [41.84, 12.60],[41.84, 12.62],[41.84, 12.64],[41.84, 12.66],[41.84, 12.68],[41.84, 12.70],[41.84, 12.72],[41.84, 12.74],[41.84, 12.76],[41.84, 12.78],
            [41.84, 12.80],[41.84, 12.82],[41.84, 12.84],[41.86, 12.22],[41.86, 12.24],[41.86, 12.26],[41.86, 12.28],[41.86, 12.30],[41.86, 12.32],[41.86, 12.34],#200
            [41.86, 12.36],[41.86, 12.38],[41.86, 12.40],[41.86, 12.42],[41.86, 12.44],[41.86, 12.46],[41.86, 12.48],[41.86, 12.50],[41.86, 12.52],[41.86, 12.54],
            [41.86, 12.56],[41.86, 12.58],[41.86, 12.60],[41.86, 12.62],[41.86, 12.64],[41.86, 12.66],[41.86, 12.68],[41.86, 12.70],[41.86, 12.72],[41.86, 12.74],
            [41.86, 12.76],[41.86, 12.78],[41.86, 12.80],[41.86, 12.82],[41.86, 12.84],[41.88, 12.22],[41.88, 12.24],[41.88, 12.26],[41.88, 12.28],[41.88, 12.30],
            [41.88, 12.32],[41.88, 12.34],[41.88, 12.36],[41.88, 12.38],[41.88, 12.40],[41.88, 12.42],[41.88, 12.44],[41.88, 12.46],[41.88, 12.48],[41.88, 12.50],
            [41.88, 12.52],[41.88, 12.54],[41.88, 12.56],[41.88, 12.58],[41.88, 12.60],[41.88, 12.62],[41.88, 12.64],[41.88, 12.66],[41.88, 12.68],[41.88, 12.70],
            [41.88, 12.72],[41.88, 12.74],[41.88, 12.76],[41.88, 12.78],[41.88, 12.80],[41.88, 12.82],[41.88, 12.84],[41.90, 12.22],[41.90, 12.24],[41.90, 12.26],
            [41.90, 12.28],[41.90, 12.30],[41.90, 12.32],[41.90, 12.34],[41.90, 12.36],[41.90, 12.38],[41.90, 12.40],[41.90, 12.42],[41.90, 12.44],[41.90, 12.46],
            [41.90, 12.48],[41.90, 12.50],[41.90, 12.52],[41.90, 12.54],[41.90, 12.56],[41.90, 12.58],[41.90, 12.60],[41.90, 12.62],[41.90, 12.64],[41.90, 12.66],
            [41.90, 12.68],[41.90, 12.70],[41.90, 12.72],[41.90, 12.74],[41.90, 12.76],[41.90, 12.78],[41.90, 12.80],[41.90, 12.82],[41.90, 12.84],[41.92, 12.22],
            [41.92, 12.24],[41.92, 12.26],[41.92, 12.28],[41.92, 12.30],[41.92, 12.32],[41.92, 12.34],[41.92, 12.36],[41.92, 12.38],[41.92, 12.40],[41.92, 12.42],
            [41.92, 12.44],[41.92, 12.46],[41.92, 12.48],[41.92, 12.50],[41.92, 12.52],[41.92, 12.54],[41.92, 12.56],[41.92, 12.58],[41.92, 12.60],[41.92, 12.62],
            [41.92, 12.64],[41.92, 12.66],[41.92, 12.68],[41.92, 12.70],[41.92, 12.72],[41.92, 12.74],[41.92, 12.76],[41.92, 12.78],[41.92, 12.80],[41.92, 12.82],
            [41.92, 12.84],[41.94, 12.22],[41.94, 12.24],[41.94, 12.26],[41.94, 12.28],[41.94, 12.30],[41.94, 12.32],[41.94, 12.34],[41.94, 12.36],[41.94, 12.38],
            [41.94, 12.40],[41.94, 12.42],[41.94, 12.44],[41.94, 12.46],[41.94, 12.48],[41.94, 12.50],[41.94, 12.52],[41.94, 12.54],[41.94, 12.56],[41.94, 12.58],
            [41.94, 12.60],[41.94, 12.62],[41.94, 12.64],[41.94, 12.66],[41.94, 12.68],[41.94, 12.70],[41.94, 12.72],[41.94, 12.74],[41.94, 12.76],[41.94, 12.78],
            [41.94, 12.80],[41.94, 12.82],[41.94, 12.84],[41.96, 12.22],[41.96, 12.24],[41.96, 12.26],[41.96, 12.28],[41.96, 12.30],[41.96, 12.32],[41.96, 12.34],
            [41.96, 12.36],[41.96, 12.38],[41.96, 12.40],[41.96, 12.42],[41.96, 12.44],[41.96, 12.46],[41.96, 12.48],[41.96, 12.50],[41.96, 12.52],[41.96, 12.54],
            [41.96, 12.56],[41.96, 12.58],[41.96, 12.60],[41.96, 12.62],[41.96, 12.64],[41.96, 12.66],[41.96, 12.68],[41.96, 12.70],[41.96, 12.72],[41.96, 12.74],
            [41.96, 12.76],[41.96, 12.78],[41.96, 12.80],[41.96, 12.82],[41.96, 12.84],[41.98, 12.22],[41.98, 12.24],[41.98, 12.26],[41.98, 12.28],[41.98, 12.30],
            [41.98, 12.32],[41.98, 12.34],[41.98, 12.36],[41.98, 12.38],[41.98, 12.40],[41.98, 12.42],[41.98, 12.44],[41.98, 12.46],[41.98, 12.48],[41.98, 12.50],#400
            [41.98, 12.52],[41.98, 12.54],[41.98, 12.56],[41.98, 12.58],[41.98, 12.60],[41.98, 12.62],[41.98, 12.64],[41.98, 12.66],[41.98, 12.68],[41.98, 12.70],
            [41.98, 12.72],[41.98, 12.74],[41.98, 12.76],[41.98, 12.78],[41.98, 12.80],[41.98, 12.82],[41.98, 12.84],[42.00, 12.22],[42.00, 12.24],[42.00, 12.26],
            [42.00, 12.28],[42.00, 12.30],[42.00, 12.32],[42.00, 12.34],[42.00, 12.36],[42.00, 12.38],[42.00, 12.40],[42.00, 12.42],[42.00, 12.44],[42.00, 12.46],
            [42.00, 12.48],[42.00, 12.50],[42.00, 12.52],[42.00, 12.54],[42.00, 12.56],[42.00, 12.58],[42.00, 12.60],[42.00, 12.62],[42.00, 12.64],[42.00, 12.66],
            [42.00, 12.68],[42.00, 12.70],[42.00, 12.72],[42.00, 12.74],[42.00, 12.76],[42.00, 12.78],[42.00, 12.80],[42.00, 12.82],[42.00, 12.84],[42.02, 12.22],
            [42.02, 12.24],[42.02, 12.26],[42.02, 12.28],[42.02, 12.30],[42.02, 12.32],[42.02, 12.34],[42.02, 12.36],[42.02, 12.38],[42.02, 12.40],[42.02, 12.42],
            [42.02, 12.44],[42.02, 12.46],[42.02, 12.48],[42.02, 12.50],[42.02, 12.52],[42.02, 12.54],[42.02, 12.56],[42.02, 12.58],[42.02, 12.60],[42.02, 12.62],
            [42.02, 12.64],[42.02, 12.66],[42.02, 12.68],[42.02, 12.70],[42.02, 12.72],[42.02, 12.74],[42.02, 12.76],[42.02, 12.78],[42.02, 12.80],[42.02, 12.82],
            [42.02, 12.84],[42.04, 12.22],[42.04, 12.24],[42.04, 12.26],[42.04, 12.28],[42.04, 12.30],[42.04, 12.32],[42.04, 12.34],[42.04, 12.36],[42.04, 12.38],
            [42.04, 12.40],[42.04, 12.42],[42.04, 12.44],[42.04, 12.46],[42.04, 12.48],[42.04, 12.50],[42.04, 12.52],[42.04, 12.54],[42.04, 12.56],[42.04, 12.58],
            [42.04, 12.60],[42.04, 12.62],[42.04, 12.64],[42.04, 12.66],[42.04, 12.68],[42.04, 12.70],[42.04, 12.72],[42.04, 12.74],[42.04, 12.76],[42.04, 12.78],
            [42.04, 12.80],[42.04, 12.82],[42.04, 12.84],[42.06, 12.22],[42.06, 12.24],[42.06, 12.26],[42.06, 12.28],[42.06, 12.30],[42.06, 12.32],[42.06, 12.34],
            [42.06, 12.36],[42.06, 12.38],[42.06, 12.40],[42.06, 12.42],[42.06, 12.44],[42.06, 12.46],[42.06, 12.48],[42.06, 12.50],[42.06, 12.52],[42.06, 12.54],
            [42.06, 12.56],[42.06, 12.58],[42.06, 12.60],[42.06, 12.62],[42.06, 12.64],[42.06, 12.66],[42.06, 12.68],[42.06, 12.70],[42.06, 12.72],[42.06, 12.74],
            [42.06, 12.76],[42.06, 12.78],[42.06, 12.80],[42.06, 12.82],[42.06, 12.84],[42.08, 12.22],[42.08, 12.24],[42.08, 12.26],[42.08, 12.28],[42.08, 12.30],
            [42.08, 12.32],[42.08, 12.34],[42.08, 12.36],[42.08, 12.38],[42.08, 12.40],[42.08, 12.42],[42.08, 12.44],[42.08, 12.46],[42.08, 12.48],[42.08, 12.50],
            [42.08, 12.52],[42.08, 12.54],[42.08, 12.56],[42.08, 12.58],[42.08, 12.60],[42.08, 12.62],[42.08, 12.64],[42.08, 12.66],[42.08, 12.68],[42.08, 12.70],
            [42.08, 12.72],[42.08, 12.74],[42.08, 12.76],[42.08, 12.78],[42.08, 12.80],[42.08, 12.82],[42.08, 12.84],[42.10, 12.22],[42.10, 12.24],[42.10, 12.26],
            [42.10, 12.28],[42.10, 12.30],[42.10, 12.32],[42.10, 12.34],[42.10, 12.36],[42.10, 12.38],[42.10, 12.40],[42.10, 12.42],[42.10, 12.44],[42.10, 12.46],
            [42.10, 12.48],[42.10, 12.50],[42.10, 12.52],[42.10, 12.54],[42.10, 12.56],[42.10, 12.58],[42.10, 12.60],[42.10, 12.62],[42.10, 12.64],[42.10, 12.66],#600
            [42.10, 12.68],[42.10, 12.70],[42.10, 12.72],[42.10, 12.74],[42.10, 12.76],[42.10, 12.78],[42.10, 12.80],[42.10, 12.82],[42.10, 12.84],[42.12, 12.22],
            [42.12, 12.24],[42.12, 12.26],[42.12, 12.28],[42.12, 12.30],[42.12, 12.32],[42.12, 12.34],[42.12, 12.36],[42.12, 12.38],[42.12, 12.40],[42.12, 12.42],
            [42.12, 12.44],[42.12, 12.46],[42.12, 12.48],[42.12, 12.50],[42.12, 12.52],[42.12, 12.54],[42.12, 12.56],[42.12, 12.58],[42.12, 12.60],[42.12, 12.62],
            [42.12, 12.64],[42.12, 12.66],[42.12, 12.68],[42.12, 12.70],[42.12, 12.72],[42.12, 12.74],[42.12, 12.76],[42.12, 12.78],[42.12, 12.80],[42.12, 12.82],
            [42.12, 12.84],[41.94, 12.08],[41.94, 12.10],[41.94, 12.12],[41.94, 12.14],[41.94, 12.16],[41.94, 12.18],[41.94, 12.20],[41.96, 12.08],[41.96, 12.10],
            [41.96, 12.12],[41.96, 12.14],[41.96, 12.16],[41.96, 12.18],[41.96, 12.20],[41.98, 12.08],[41.98, 12.10],[41.98, 12.12],[41.98, 12.14],[41.98, 12.16],
            [41.98, 12.18],[41.98, 12.20],[42.00, 12.08],[42.00, 12.10],[42.00, 12.12],[42.00, 12.14],[42.00, 12.16],[42.00, 12.18],[42.00, 12.20],[42.02, 12.08],
            [42.02, 12.10],[42.02, 12.12],[42.02, 12.14],[42.02, 12.16],[42.02, 12.18],[42.02, 12.20],[42.04, 12.08],[42.04, 12.10],[42.04, 12.12],[42.04, 12.14],
            [42.04, 12.16],[42.04, 12.18],[42.04, 12.20],[42.06, 12.08],[42.06, 12.10],[42.06, 12.12],[42.06, 12.14],[42.06, 12.16],[42.06, 12.18],[42.06, 12.20],
            [42.08, 12.08],[42.08, 12.10],[42.08, 12.12],[42.08, 12.14],[42.08, 12.16],[42.08, 12.18],[42.08, 12.20],[42.10, 12.08],[42.10, 12.10],[42.10, 12.12],
            [42.10, 12.14],[42.10, 12.16],[42.10, 12.18],[42.10, 12.20],[42.12, 12.08],[42.12, 12.10],[42.12, 12.12],[42.12, 12.14],[42.12, 12.16],[42.12, 12.18],
            [42.12, 12.20],[42.14, 12.08],[42.14, 12.10],[42.14, 12.12],[42.14, 12.14],[42.14, 12.16],[42.14, 12.18],[42.14, 12.20],[42.16, 12.08],[42.16, 12.10],
            [42.16, 12.12],[42.16, 12.14],[42.16, 12.16],[42.16, 12.18],[42.16, 12.20],[41.92, 12.12],[41.92, 12.14],[41.92, 12.16],[41.92, 12.18],[41.92, 12.20],
            [41.90, 12.14],[41.90, 12.16],[41.90, 12.18],[41.90, 12.20],[41.88, 12.16],[41.88, 12.18],[41.88, 12.20],[41.86, 12.18],[41.86, 12.20],[41.84, 12.20],            
            [42.02, 11.96],[42.02, 11.98],[42.02, 12.00],[42.02, 12.02],[42.02, 12.04],[42.02, 12.06],[42.00, 11.96],[42.00, 11.98],[42.00, 12.00],[42.00, 12.02],
            [42.00, 12.04],[42.00, 12.06],[41.98, 12.02],[41.98, 12.04],[41.98, 12.06],[41.96, 12.04],[41.96, 12.06],[42.04, 11.84],[42.04, 11.86],[42.04, 11.88],
            [42.04, 11.90],[42.04, 11.92],[42.04, 11.94],[42.04, 11.96],[42.04, 11.98],[42.04, 12.00],[42.04, 12.02],[42.04, 12.04],[42.04, 12.06],[42.06, 11.84],
            [42.06, 11.86],[42.06, 11.88],[42.06, 11.90],[42.06, 11.92],[42.06, 11.94],[42.06, 11.96],[42.06, 11.98],[42.06, 12.00],[42.06, 12.02],[42.06, 12.04],
            [42.06, 12.06],[42.08, 11.84],[42.08, 11.86],[42.08, 11.88],[42.08, 11.90],[42.08, 11.92],[42.08, 11.94],[42.08, 11.96],[42.08, 11.98],[42.08, 12.00],
            [42.08, 12.02],[42.08, 12.04],[42.08, 12.06],[42.10, 11.84],[42.10, 11.86],[42.10, 11.88],[42.10, 11.90],[42.10, 11.92],[42.10, 11.94],[42.10, 11.96],#800
            [42.10, 11.98],[42.10, 12.00],[42.10, 12.02],[42.10, 12.04],[42.10, 12.06],[42.12, 11.84],[42.12, 11.86],[42.12, 11.88],[42.12, 11.90],[42.12, 11.92],
            [42.12, 11.94],[42.12, 11.96],[42.12, 11.98],[42.12, 12.00],[42.12, 12.02],[42.12, 12.04],[42.12, 12.06],[42.14, 11.84],[42.14, 11.86],[42.14, 11.88],
            [42.14, 11.90],[42.14, 11.92],[42.14, 11.94],[42.14, 11.96],[42.14, 11.98],[42.14, 12.00],[42.14, 12.02],[42.14, 12.04],[42.14, 12.06],[42.16, 11.84],
            [42.16, 11.86],[42.16, 11.88],[42.16, 11.90],[42.16, 11.92],[42.16, 11.94],[42.16, 11.96],[42.16, 11.98],[42.16, 12.00],[42.16, 12.02],[42.16, 12.04],
            [42.16, 12.06],[42.18, 11.84],[42.18, 11.86],[42.18, 11.88],[42.18, 11.90],[42.18, 11.92],[42.18, 11.94],[42.18, 11.96],[42.18, 11.98],[42.18, 12.00],
            [42.20, 11.86],[42.20, 11.88],[42.20, 11.90],[42.20, 11.92],[42.20, 11.94],[42.20, 11.96],[42.20, 11.98],[42.22, 11.88],[42.22, 11.90],[42.22, 11.92],
            [42.22, 11.94],[42.22, 11.96],[42.22, 11.98],[42.24, 11.90],[42.24, 11.92],[42.16, 11.76],[42.16, 11.78],[42.16, 11.80],[42.16, 11.82],[42.14, 11.74],
            [42.14, 11.76],[42.14, 11.78],[42.14, 11.80],[42.14, 11.82],[42.12, 11.76],[42.12, 11.78],[42.12, 11.80],[42.12, 11.82],[42.10, 11.78],[42.10, 11.80],
            [42.10, 11.82],[42.08, 11.80],[42.08, 11.82],[42.06, 11.82],[42.04, 11.82],[42.18, 12.18],[42.18, 12.20],[42.14, 12.22],[42.14, 12.24],[42.14, 12.26],
            [42.14, 12.28],[42.16, 12.22],[42.16, 12.24],[42.16, 12.26],[42.16, 12.28],[42.18, 12.22],[42.18, 12.24],[42.18, 12.26],[42.18, 12.28],[42.16, 12.30],
            [42.14, 12.30],[42.14, 12.32],[42.16, 12.34],[42.14, 12.34],[42.18, 12.36],[42.16, 12.36],[42.14, 12.36],[42.22, 12.38],[42.20, 12.38],[42.18, 12.38],
            [42.16, 12.38],[42.14, 12.38],[42.14, 12.40],[42.14, 12.42],[42.16, 12.40],[42.16, 12.42],[42.18, 12.40],[42.18, 12.42],[42.20, 12.40],[42.20, 12.42],
            [42.22, 12.40],[42.22, 12.42],[42.24, 12.40],[42.24, 12.42],[42.26, 12.40],[42.26, 12.42],[42.14, 12.44],[42.14, 12.46],[42.16, 12.44],[42.16, 12.46],
            [42.18, 12.44],[42.18, 12.46],[42.20, 12.44],[42.20, 12.46],[42.22, 12.46],[42.30, 12.52],[42.30, 12.54],[42.30, 12.56],[42.28, 12.50],[42.28, 12.52],
            [42.28, 12.54],[42.28, 12.56],[42.28, 12.58],[42.28, 12.60],[42.14, 12.48],[42.14, 12.50],[42.14, 12.52],[42.14, 12.54],[42.14, 12.56],[42.14, 12.58],
            [42.14, 12.60],[42.14, 12.62],[42.14, 12.64],[42.16, 12.48],[42.16, 12.50],[42.16, 12.52],[42.16, 12.54],[42.16, 12.56],[42.16, 12.58],[42.16, 12.60],
            [42.16, 12.62],[42.16, 12.64],[42.18, 12.48],[42.18, 12.50],[42.18, 12.52],[42.18, 12.54],[42.18, 12.56],[42.18, 12.58],[42.18, 12.60],[42.18, 12.62],
            [42.26, 12.62],[42.20, 12.48],[42.20, 12.50],[42.20, 12.52],[42.20, 12.54],[42.20, 12.56],[42.20, 12.58],[42.20, 12.60],[42.20, 12.62],[42.20, 12.64],
            [42.22, 12.48],[42.22, 12.50],[42.22, 12.52],[42.22, 12.54],[42.22, 12.56],[42.22, 12.58],[42.22, 12.60],[42.22, 12.62],[42.22, 12.64],[42.24, 12.48],
            [42.24, 12.50],[42.24, 12.52],[42.24, 12.54],[42.24, 12.56],[42.24, 12.58],[42.24, 12.60],[42.24, 12.62],[42.24, 12.64],[42.26, 12.48],[42.26, 12.50],#1000
            [42.26, 12.52],[42.26, 12.54],[42.26, 12.56],[42.26, 12.58],[42.26, 12.60],[42.18, 12.74],[42.18, 12.76],[42.18, 12.78],[42.18, 12.80],[42.16, 12.66],
            [42.16, 12.68],[42.16, 12.70],[42.16, 12.72],[42.16, 12.74],[42.16, 12.76],[42.16, 12.78],[42.16, 12.80],[42.16, 12.82],[42.14, 12.66],[42.14, 12.68],
            [42.14, 12.70],[42.14, 12.72],[42.14, 12.74],[42.14, 12.76],[42.14, 12.78],[42.14, 12.80],[42.14, 12.82],[42.14, 12.84],[42.14, 12.86],[42.12, 12.86],
            [42.12, 12.90],[42.12, 12.92],[42.12, 12.96],[42.12, 12.98],[42.12, 13.00],[42.12, 13.02],[42.10, 12.86],[42.10, 12.88],[42.10, 12.90],[42.10, 12.92],
            [42.10, 12.94],[42.10, 12.96],[42.10, 12.98],[42.10, 13.00],[42.10, 13.02],[41.82, 12.86],[41.82, 12.88],[41.82, 12.90],[41.82, 12.92],[41.82, 12.94],
            [41.82, 12.96],[41.82, 12.98],[41.82, 13.00],[41.82, 13.02],[41.84, 12.86],[41.84, 12.88],[41.84, 12.90],[41.84, 12.92],[41.84, 12.94],[41.84, 12.96],
            [41.84, 12.98],[41.84, 13.00],[41.84, 13.02],[41.86, 12.86],[41.86, 12.88],[41.86, 12.90],[41.86, 12.92],[41.86, 12.94],[41.86, 12.96],[41.86, 12.98],
            [41.86, 13.00],[41.86, 13.02],[41.88, 12.86],[41.88, 12.88],[41.88, 12.90],[41.88, 12.92],[41.88, 12.94],[41.88, 12.96],[41.88, 12.98],[41.88, 13.00],
            [41.88, 13.02],[41.90, 12.86],[41.90, 12.88],[41.90, 12.90],[41.90, 12.92],[41.90, 12.94],[41.90, 12.96],[41.90, 12.98],[41.90, 13.00],[41.90, 13.02],
            [41.92, 12.86],[41.92, 12.88],[41.92, 12.90],[41.92, 12.92],[41.92, 12.94],[41.92, 12.96],[41.92, 12.98],[41.92, 13.00],[41.92, 13.02],[41.94, 12.86],
            [41.94, 12.88],[41.94, 12.90],[41.94, 12.92],[41.94, 12.94],[41.94, 12.96],[41.94, 12.98],[41.94, 13.00],[41.94, 13.02],[41.96, 12.86],[41.96, 12.88],
            [41.96, 12.90],[41.96, 12.92],[41.96, 12.94],[41.96, 12.96],[41.96, 12.98],[41.96, 13.00],[41.96, 13.02],[41.98, 12.86],[41.98, 12.88],[41.98, 12.90],
            [41.98, 12.92],[41.98, 12.94],[41.98, 12.96],[41.98, 12.98],[41.98, 13.00],[41.98, 13.02],[42.00, 12.86],[42.00, 12.88],[42.00, 12.90],[42.00, 12.92],
            [42.00, 12.94],[42.00, 12.96],[42.00, 12.98],[42.00, 13.00],[42.00, 13.02],[42.02, 12.86],[42.02, 12.88],[42.02, 12.90],[42.02, 12.92],[42.02, 12.94],
            [42.02, 12.96],[42.02, 12.98],[42.02, 13.00],[42.02, 13.02],[42.04, 12.86],[42.04, 12.88],[42.04, 12.90],[42.04, 12.92],[42.04, 12.94],[42.04, 12.96],
            [42.04, 12.98],[42.04, 13.00],[42.04, 13.02],[42.06, 12.86],[42.06, 12.88],[42.06, 12.90],[42.06, 12.92],[42.06, 12.94],[42.06, 12.96],[42.06, 12.98],
            [42.06, 13.00],[42.06, 13.02],[42.08, 12.86],[42.08, 12.88],[42.08, 12.90],[42.08, 12.92],[42.08, 12.94],[42.08, 12.96],[42.08, 12.98],[42.08, 13.00],
            [42.08, 13.02],[42.04, 13.04],[42.02, 13.04],[42.02, 13.06],[42.02, 13.08],[42.02, 13.10],[42.02, 13.12],[42.02, 13.14],[41.84, 13.04],[41.84, 13.06],
            [41.84, 13.12],[41.84, 13.14],[41.84, 13.16],[41.84, 13.18],[41.86, 13.04],[41.86, 13.06],[41.86, 13.08],[41.86, 13.10],[42.00, 13.16],[42.00, 13.18],
            [41.86, 13.12],[41.86, 13.14],[41.86, 13.16],[41.86, 13.18],[41.88, 13.04],[41.88, 13.06],[41.88, 13.08],[41.88, 13.10],[41.88, 13.12],[41.88, 13.14],#1200
            [41.88, 13.16],[41.88, 13.18],[41.90, 13.04],[41.90, 13.06],[41.90, 13.08],[41.90, 13.10],[41.90, 13.12],[41.90, 13.14],[41.90, 13.16],[41.90, 13.18],
            [41.92, 13.04],[41.92, 13.06],[41.92, 13.08],[41.92, 13.10],[41.92, 13.12],[41.92, 13.14],[41.92, 13.16],[41.92, 13.18],[41.94, 13.04],[41.94, 13.06],
            [41.94, 13.08],[41.94, 13.10],[41.94, 13.12],[41.94, 13.14],[41.94, 13.16],[41.94, 13.18],[41.96, 13.04],[41.96, 13.06],[41.96, 13.08],[41.96, 13.10],
            [41.96, 13.12],[41.96, 13.14],[41.96, 13.16],[41.96, 13.18],[41.98, 13.04],[41.98, 13.06],[41.98, 13.08],[41.98, 13.10],[41.98, 13.12],[41.98, 13.14],
            [41.98, 13.16],[41.98, 13.18],[42.00, 13.04],[42.00, 13.06],[42.00, 13.08],[42.00, 13.10],[42.00, 13.12],[42.00, 13.14],[41.98, 13.20],[41.98, 13.22],
            [41.98, 13.24],[41.96, 13.20],[41.96, 13.22],[41.96, 13.24],[41.96, 13.26],[41.96, 13.28],[41.94, 13.20],[41.94, 13.22],[41.94, 13.24],[41.94, 13.26],
            [41.94, 13.28],[41.94, 13.30],[41.92, 13.20],[41.92, 13.22],[41.92, 13.24],[41.92, 13.26],[41.92, 13.28],[41.90, 13.20],[41.90, 13.22],[41.90, 13.24],
            [41.88, 13.20],[41.88, 13.22],[41.88, 13.24],[41.86, 13.20],[41.76, 13.02],[41.74, 13.02],[41.74, 13.04],[41.74, 13.06],[41.72, 13.02],[41.72, 13.04],
            [41.72, 13.06],[41.72, 13.08],[41.72, 12.86],[41.72, 12.88],[41.72, 12.90],[41.72, 12.92],[41.72, 12.94],[41.72, 12.96],[41.72, 12.98],[41.72, 13.00],
            [41.74, 12.86],[41.74, 12.88],[41.74, 12.90],[41.74, 12.92],[41.74, 12.94],[41.74, 12.96],[41.74, 12.98],[41.74, 13.00],[41.76, 12.86],[41.76, 12.88],
            [41.76, 12.90],[41.76, 12.92],[41.76, 12.94],[41.76, 12.96],[41.76, 12.98],[41.76, 13.00],[41.78, 12.86],[41.78, 12.88],[41.78, 12.90],[41.78, 12.92],
            [41.78, 12.94],[41.78, 12.96],[41.78, 12.98],[41.78, 13.00],[41.80, 12.86],[41.80, 12.88],[41.80, 12.90],[41.80, 12.92],[41.80, 12.94],[41.80, 12.96],
            [41.80, 12.98],[41.80, 13.00],[41.70, 12.94],[41.70, 12.96],[41.70, 12.98],[41.70, 13.00],[41.70, 13.02],[41.70, 13.04],[41.70, 13.06],[41.70, 13.08],
            [41.70, 13.10],[41.68, 12.94],[41.68, 12.96],[41.68, 12.98],[41.68, 13.00],[41.68, 13.02],[41.68, 13.04],[41.68, 13.06],[41.68, 13.08],[41.68, 13.10],
            [41.66, 12.96],[41.66, 12.98],[41.66, 13.00],[41.66, 13.02],[41.66, 13.04],[41.66, 13.06],[41.66, 13.08],[41.66, 13.10],[41.66, 13.12],[41.66, 13.14],
            [41.66, 13.16],[41.64, 12.98],[41.64, 13.00],[41.64, 13.02],[41.64, 13.04],[41.64, 13.06],[41.64, 13.08],[41.64, 13.10],[41.64, 13.12],[41.64, 13.14],
            [41.64, 13.16],[41.62, 13.00],[41.62, 13.02],[41.62, 13.04],[41.62, 13.06],[41.62, 13.08],[41.62, 13.10],[41.62, 13.12],[41.62, 13.14],[41.62, 13.16],
            [41.60, 13.02],[41.60, 13.04],[41.60, 13.06],[41.60, 13.08],[41.60, 13.10],[41.60, 13.12],[41.60, 13.14],[41.60, 13.16],[41.58, 13.02],[41.58, 13.04],
            [41.58, 13.06],[41.58, 13.08],[41.58, 13.10],[41.58, 13.12],[41.58, 13.14],[41.58, 13.16],[41.58, 13.18],[41.56, 13.08],[41.56, 13.10],[41.56, 13.12],
            [41.56, 13.14],[41.56, 13.16],[41.54, 13.10],[41.72, 12.28],[41.72, 12.30],[41.72, 12.32],[41.72, 12.34],[41.72, 12.36],[41.72, 12.38],[41.72, 12.40],#1400
            [41.72, 12.42],[41.72, 12.44],[41.72, 12.46],[41.72, 12.48],[41.72, 12.50],[41.72, 12.52],[41.72, 12.54],[41.72, 12.56],[41.72, 12.58],[41.72, 12.60],
            [41.72, 12.62],[41.72, 12.64],[41.72, 12.66],[41.72, 12.68],[41.72, 12.70],[41.72, 12.72],[41.72, 12.74],[41.72, 12.76],[41.72, 12.78],[41.72, 12.80],
            [41.72, 12.82],[41.72, 12.84],[41.70, 12.32],[41.70, 12.34],[41.70, 12.36],[41.70, 12.38],[41.70, 12.40],[41.70, 12.42],[41.70, 12.44],[41.70, 12.46],
            [41.70, 12.48],[41.70, 12.50],[41.70, 12.52],[41.70, 12.54],[41.70, 12.56],[41.70, 12.58],[41.70, 12.60],[41.70, 12.62],[41.70, 12.64],[41.70, 12.66],
            [41.70, 12.68],[41.70, 12.70],[41.70, 12.72],[41.70, 12.74],[41.70, 12.76],[41.70, 12.78],[41.70, 12.80],[41.70, 12.82],[41.70, 12.84],[41.70, 12.86],
            [41.70, 12.88],[41.68, 12.36],[41.68, 12.38],[41.68, 12.40],[41.68, 12.42],[41.68, 12.44],[41.68, 12.46],[41.68, 12.48],[41.68, 12.50],[41.68, 12.52],
            [41.68, 12.54],[41.68, 12.56],[41.68, 12.58],[41.68, 12.60],[41.68, 12.62],[41.68, 12.64],[41.68, 12.66],[41.68, 12.68],[41.68, 12.70],[41.68, 12.72],
            [41.68, 12.74],[41.68, 12.76],[41.68, 12.78],[41.68, 12.80],[41.68, 12.82],[41.68, 12.84],[41.68, 12.86],[41.66, 12.40],[41.66, 12.42],[41.66, 12.44],
            [41.66, 12.46],[41.66, 12.48],[41.66, 12.50],[41.66, 12.52],[41.66, 12.54],[41.66, 12.56],[41.66, 12.58],[41.66, 12.60],[41.66, 12.62],[41.66, 12.64],
            [41.66, 12.66],[41.66, 12.68],[41.66, 12.70],[41.66, 12.72],[41.66, 12.74],[41.66, 12.76],[41.66, 12.78],[41.66, 12.80],[41.66, 12.82],[41.66, 12.84],
            [41.64, 12.42],[41.64, 12.44],[41.64, 12.46],[41.64, 12.48],[41.64, 12.50],[41.64, 12.52],[41.64, 12.54],[41.64, 12.56],[41.64, 12.58],[41.64, 12.60],
            [41.64, 12.66],[41.64, 12.68],[41.64, 12.70],[41.64, 12.72],[41.64, 12.74],[41.64, 12.76],[41.64, 12.78],[41.64, 12.80],[41.64, 12.82],[41.62, 12.46],
            [41.62, 12.48],[41.62, 12.50],[41.62, 12.52],[41.62, 12.54],[41.62, 12.56],[41.62, 12.66],[41.62, 12.68],[41.62, 12.70],[41.62, 12.72],[41.62, 12.74],
            [41.62, 12.76],[41.62, 12.78],[41.62, 12.80],[41.60, 12.48],[41.60, 12.50],[41.60, 12.52],[41.60, 12.54],[41.60, 12.56],[41.60, 12.66],[41.60, 12.68],
            [41.60, 12.70],[41.60, 12.72],[41.60, 12.74],[41.60, 12.76],[41.60, 12.78],[41.58, 12.50],[41.58, 12.52],[41.58, 12.54],[41.58, 12.56],[41.58, 12.58],
            [41.58, 12.74],[41.58, 12.76],[41.56, 12.52],[41.56, 12.54],[41.56, 12.56],[41.56, 12.58],[41.54, 12.54],[41.54, 12.56],[41.54, 12.58],[41.54, 12.60],
            [41.54, 12.62],[41.54, 12.64],[41.54, 12.66],[41.52, 12.56],[41.52, 12.58],[41.52, 12.60],[41.52, 12.62],[41.52, 12.64],[41.52, 12.66],[41.52, 12.68],
            [41.50, 12.58],[41.50, 12.60],[41.50, 12.62],[41.50, 12.64],[41.50, 12.66],[41.50, 12.68],[41.50, 12.70],[41.50, 12.72],[41.48, 12.58],[41.48, 12.60],
            [41.48, 12.62],[41.48, 12.64],[41.48, 12.66],[41.48, 12.68],[41.48, 12.70],[41.48, 12.72],[41.48, 12.74],[41.46, 12.60],[41.46, 12.62],[41.46, 12.64],
            [41.46, 12.66],[41.46, 12.68],[41.46, 12.70],[41.46, 12.72],[41.46, 12.74],[41.44, 12.62],[41.44, 12.64],[41.44, 12.70],[41.44, 12.72],[41.44, 12.74],#1600
            [41.44, 12.76],[41.42, 12.74],[41.42, 12.76],[41.42, 12.78],[41.82, 12.20],[42.02, 11.94]#1606
        ]
    
    
    if provincia=="Frosinone":
        confini_provincia = gpd.read_feather('./conf/confini/frosinone.feather')
        coord_002_list=[
            [41.72, 13.78],[41.72, 13.80],[41.46, 13.38],[41.46, 13.40],[41.46, 13.42],[41.46, 13.44],[41.46, 13.46],[41.46, 13.48],[41.46, 13.50],[41.46, 13.52],
            [41.46, 13.54],[41.46, 13.56],[41.46, 13.58],[41.46, 13.60],[41.46, 13.62],[41.46, 13.64],[41.46, 13.66],[41.46, 13.68],[41.46, 13.70],[41.46, 13.72],
            [41.46, 13.74],[41.46, 13.76],[41.46, 13.78],[41.46, 13.80],[41.46, 13.82],[41.48, 13.38],[41.48, 13.40],[41.48, 13.42],[41.48, 13.44],[41.48, 13.46],
            [41.48, 13.48],[41.48, 13.50],[41.48, 13.52],[41.48, 13.54],[41.48, 13.56],[41.48, 13.58],[41.48, 13.60],[41.48, 13.62],[41.48, 13.64],[41.48, 13.66],
            [41.48, 13.68],[41.48, 13.70],[41.48, 13.72],[41.48, 13.74],[41.48, 13.76],[41.48, 13.78],[41.48, 13.80],[41.48, 13.82],[41.50, 13.38],[41.50, 13.40],
            [41.50, 13.42],[41.50, 13.44],[41.50, 13.46],[41.50, 13.48],[41.50, 13.50],[41.50, 13.52],[41.50, 13.54],[41.50, 13.56],[41.50, 13.58],[41.50, 13.60],
            [41.50, 13.62],[41.50, 13.64],[41.50, 13.66],[41.50, 13.68],[41.50, 13.70],[41.50, 13.72],[41.50, 13.74],[41.50, 13.76],[41.50, 13.78],[41.50, 13.80],
            [41.50, 13.82],[41.52, 13.38],[41.52, 13.40],[41.52, 13.42],[41.52, 13.44],[41.52, 13.46],[41.52, 13.48],[41.52, 13.50],[41.52, 13.52],[41.52, 13.54],
            [41.52, 13.56],[41.52, 13.58],[41.52, 13.60],[41.52, 13.62],[41.52, 13.64],[41.52, 13.66],[41.52, 13.68],[41.52, 13.70],[41.52, 13.72],[41.52, 13.74],
            [41.52, 13.76],[41.52, 13.78],[41.52, 13.80],[41.52, 13.82],[41.54, 13.38],[41.54, 13.40],[41.54, 13.42],[41.54, 13.44],[41.54, 13.46],[41.54, 13.48],
            [41.54, 13.50],[41.54, 13.52],[41.54, 13.54],[41.54, 13.56],[41.54, 13.58],[41.54, 13.60],[41.54, 13.62],[41.54, 13.64],[41.54, 13.66],[41.54, 13.68],
            [41.54, 13.70],[41.54, 13.72],[41.54, 13.74],[41.54, 13.76],[41.54, 13.78],[41.54, 13.80],[41.54, 13.82],[41.56, 13.38],[41.56, 13.40],[41.56, 13.42],
            [41.56, 13.44],[41.56, 13.46],[41.56, 13.48],[41.56, 13.50],[41.56, 13.52],[41.56, 13.54],[41.56, 13.56],[41.56, 13.58],[41.56, 13.60],[41.56, 13.62],
            [41.56, 13.64],[41.56, 13.66],[41.56, 13.68],[41.56, 13.70],[41.56, 13.72],[41.56, 13.74],[41.56, 13.76],[41.56, 13.78],[41.56, 13.80],[41.56, 13.82],
            [41.58, 13.38],[41.58, 13.40],[41.58, 13.42],[41.58, 13.44],[41.58, 13.46],[41.58, 13.48],[41.58, 13.50],[41.58, 13.52],[41.58, 13.54],[41.58, 13.56],
            [41.58, 13.58],[41.58, 13.60],[41.58, 13.62],[41.58, 13.64],[41.58, 13.66],[41.58, 13.68],[41.58, 13.70],[41.58, 13.72],[41.58, 13.74],[41.58, 13.76],
            [41.58, 13.78],[41.58, 13.80],[41.58, 13.82],[41.60, 13.38],[41.60, 13.40],[41.60, 13.42],[41.60, 13.44],[41.60, 13.46],[41.60, 13.48],[41.60, 13.50],
            [41.60, 13.52],[41.60, 13.54],[41.60, 13.56],[41.60, 13.58],[41.60, 13.60],[41.60, 13.62],[41.60, 13.64],[41.60, 13.66],[41.60, 13.68],[41.60, 13.70],
            [41.60, 13.72],[41.60, 13.74],[41.60, 13.76],[41.60, 13.78],[41.60, 13.80],[41.60, 13.82],[41.62, 13.38],[41.62, 13.40],[41.62, 13.42],[41.62, 13.44],
            [41.62, 13.46],[41.62, 13.48],[41.62, 13.50],[41.62, 13.52],[41.62, 13.54],[41.62, 13.56],[41.62, 13.58],[41.62, 13.60],[41.62, 13.62],[41.62, 13.64],
            [41.62, 13.66],[41.62, 13.68],[41.62, 13.70],[41.62, 13.72],[41.62, 13.74],[41.62, 13.76],[41.62, 13.78],[41.62, 13.80],[41.62, 13.82],[41.64, 13.38],
            [41.64, 13.40],[41.64, 13.42],[41.64, 13.44],[41.64, 13.46],[41.64, 13.48],[41.64, 13.50],[41.64, 13.52],[41.64, 13.54],[41.64, 13.56],[41.64, 13.58],
            [41.64, 13.60],[41.64, 13.62],[41.64, 13.64],[41.64, 13.66],[41.64, 13.68],[41.64, 13.70],[41.64, 13.72],[41.64, 13.74],[41.64, 13.76],[41.64, 13.78],
            [41.64, 13.80],[41.64, 13.82],[41.66, 13.38],[41.66, 13.40],[41.66, 13.42],[41.66, 13.44],[41.66, 13.46],[41.66, 13.48],[41.66, 13.50],[41.66, 13.52],
            [41.66, 13.54],[41.66, 13.56],[41.66, 13.58],[41.66, 13.60],[41.66, 13.62],[41.66, 13.64],[41.66, 13.66],[41.66, 13.68],[41.66, 13.70],[41.66, 13.72],
            [41.66, 13.74],[41.66, 13.76],[41.66, 13.78],[41.66, 13.80],[41.66, 13.82],[41.68, 13.38],[41.68, 13.40],[41.68, 13.42],[41.68, 13.44],[41.68, 13.46],
            [41.68, 13.48],[41.68, 13.50],[41.68, 13.52],[41.68, 13.54],[41.68, 13.56],[41.68, 13.58],[41.68, 13.60],[41.68, 13.62],[41.68, 13.64],[41.68, 13.66],
            [41.68, 13.68],[41.68, 13.70],[41.68, 13.72],[41.68, 13.74],[41.68, 13.76],[41.68, 13.78],[41.68, 13.80],[41.68, 13.82],[41.70, 13.38],[41.70, 13.40],
            [41.70, 13.42],[41.70, 13.44],[41.70, 13.46],[41.70, 13.48],[41.70, 13.50],[41.70, 13.52],[41.70, 13.54],[41.70, 13.56],[41.70, 13.58],[41.70, 13.60],
            [41.70, 13.62],[41.70, 13.64],[41.70, 13.66],[41.70, 13.68],[41.70, 13.70],[41.70, 13.72],[41.70, 13.74],[41.70, 13.76],[41.70, 13.78],[41.70, 13.80],#300
            [41.70, 13.82],[41.72, 13.38],[41.72, 13.40],[41.72, 13.42],[41.72, 13.44],[41.72, 13.46],[41.72, 13.48],[41.72, 13.50],[41.72, 13.52],[41.72, 13.54],
            [41.72, 13.56],[41.72, 13.58],[41.72, 13.60],[41.72, 13.62],[41.72, 13.64],[41.72, 13.66],[41.72, 13.68],[41.72, 13.70],[41.72, 13.72],[41.72, 13.74],
            [41.72, 13.76],[41.72, 13.82],[41.60, 13.16],[41.60, 13.18],[41.60, 13.20],[41.60, 13.22],[41.60, 13.24],[41.60, 13.26],[41.60, 13.28],[41.60, 13.30],
            [41.60, 13.32],[41.60, 13.34],[41.62, 13.16],[41.62, 13.18],[41.62, 13.20],[41.62, 13.22],[41.62, 13.24],[41.62, 13.26],[41.62, 13.28],[41.62, 13.30],
            [41.62, 13.32],[41.62, 13.34],[41.64, 13.16],[41.64, 13.18],[41.64, 13.20],[41.64, 13.22],[41.64, 13.24],[41.64, 13.26],[41.64, 13.28],[41.64, 13.30],
            [41.64, 13.32],[41.64, 13.34],[41.66, 13.16],[41.66, 13.18],[41.66, 13.20],[41.66, 13.22],[41.66, 13.24],[41.66, 13.26],[41.66, 13.28],[41.66, 13.30],
            [41.66, 13.32],[41.66, 13.34],[41.68, 13.16],[41.68, 13.18],[41.68, 13.20],[41.68, 13.22],[41.68, 13.24],[41.68, 13.26],[41.68, 13.28],[41.68, 13.30],
            [41.68, 13.32],[41.68, 13.34],[41.70, 13.16],[41.70, 13.18],[41.70, 13.20],[41.70, 13.22],[41.70, 13.24],[41.70, 13.26],[41.70, 13.28],[41.70, 13.30],
            [41.70, 13.32],[41.70, 13.34],[41.72, 13.16],[41.72, 13.18],[41.72, 13.20],[41.72, 13.22],[41.72, 13.24],[41.72, 13.26],[41.72, 13.28],[41.72, 13.30],
            [41.72, 13.32],[41.72, 13.34],[41.74, 13.16],[41.74, 13.18],[41.74, 13.20],[41.74, 13.22],[41.74, 13.24],[41.74, 13.26],[41.74, 13.28],[41.74, 13.30],#400
            [41.74, 13.32],[41.74, 13.34],[41.76, 13.16],[41.76, 13.18],[41.76, 13.20],[41.76, 13.22],[41.76, 13.24],[41.76, 13.26],[41.76, 13.28],[41.76, 13.30],
            [41.76, 13.32],[41.76, 13.34],[41.78, 13.16],[41.78, 13.18],[41.78, 13.20],[41.78, 13.22],[41.78, 13.24],[41.78, 13.26],[41.78, 13.28],[41.78, 13.30],
            [41.78, 13.32],[41.78, 13.34],[41.80, 13.16],[41.80, 13.18],[41.80, 13.20],[41.80, 13.22],[41.80, 13.24],[41.80, 13.26],[41.80, 13.28],[41.80, 13.30],
            [41.80, 13.32],[41.80, 13.34],[41.82, 13.16],[41.82, 13.18],[41.82, 13.20],[41.82, 13.22],[41.82, 13.24],[41.82, 13.26],[41.82, 13.28],[41.82, 13.30],
            [41.82, 13.32],[41.82, 13.34],[41.40, 13.36],[41.42, 13.36],[41.44, 13.36],[41.46, 13.36],[41.48, 13.36],[41.50, 13.36],[41.52, 13.36],[41.54, 13.36],
            [41.56, 13.36],[41.58, 13.36],[41.60, 13.36],[41.62, 13.36],[41.64, 13.36],[41.66, 13.36],[41.68, 13.36],[41.70, 13.36],[41.72, 13.36],[41.74, 13.36],
            [41.76, 13.36],[41.78, 13.36],[41.80, 13.36],[41.82, 13.36],[41.84, 13.36],[41.86, 13.36],[41.88, 13.36],[41.90, 13.36],[41.92, 13.36],[41.96, 13.30],
            [41.94, 13.28],[41.94, 13.30],[41.94, 13.32],[41.94, 13.34],[41.92, 13.24],[41.92, 13.26],[41.92, 13.28],[41.92, 13.30],[41.92, 13.32],[41.92, 13.34],
            [41.92, 13.38],[41.90, 13.38],[41.88, 13.38],[41.84, 13.24],[41.84, 13.26],[41.84, 13.28],[41.84, 13.30],[41.84, 13.32],[41.84, 13.34],[41.86, 13.24],
            [41.86, 13.26],[41.86, 13.28],[41.86, 13.30],[41.86, 13.32],[41.86, 13.34],[41.88, 13.24],[41.88, 13.26],[41.88, 13.28],[41.88, 13.30],[41.88, 13.32],#500
            [41.88, 13.34],[41.90, 13.24],[41.90, 13.26],[41.90, 13.28],[41.90, 13.30],[41.90, 13.32],[41.90, 13.34],[41.88, 13.22],[41.86, 13.22],[41.84, 13.22],
            [41.88, 13.20],[41.86, 13.20],[41.84, 13.20],[41.84, 13.18],[41.84, 13.16],[41.84, 13.14],[41.84, 13.12],[41.84, 13.10],[41.84, 13.08],[41.84, 13.06],
            [41.84, 13.04],[41.86, 13.08],[41.86, 13.10],[41.86, 13.10],[41.76, 13.00],[41.76, 13.02],[41.76, 13.04],[41.76, 13.06],[41.76, 13.08],[41.76, 13.10],
            [41.76, 13.12],[41.76, 13.14],[41.78, 13.00],[41.78, 13.02],[41.78, 13.04],[41.78, 13.06],[41.78, 13.08],[41.78, 13.10],[41.78, 13.12],[41.78, 13.14],
            [41.80, 13.00],[41.80, 13.02],[41.80, 13.04],[41.80, 13.06],[41.80, 13.08],[41.80, 13.10],[41.80, 13.12],[41.80, 13.14],[41.82, 13.00],[41.82, 13.02],
            [41.82, 13.04],[41.82, 13.06],[41.82, 13.08],[41.82, 13.10],[41.82, 13.12],[41.82, 13.14],[41.74, 13.02],[41.74, 13.04],[41.74, 13.06],[41.74, 13.08],
            [41.74, 13.10],[41.74, 13.12],[41.74, 13.14],[41.72, 13.06],[41.72, 13.08],[41.72, 13.10],[41.72, 13.12],[41.72, 13.14],[41.70, 13.10],[41.70, 13.12],
            [41.70, 13.14],[41.68, 13.10],[41.68, 13.12],[41.68, 13.14],[41.66, 13.12],[41.66, 13.14],[41.84, 13.40],[41.84, 13.42],[41.82, 13.38],[41.82, 13.40],
            [41.82, 13.42],[41.82, 13.44],[41.82, 13.46],[41.74, 13.38],[41.74, 13.40],[41.74, 13.42],[41.74, 13.44],[41.74, 13.46],[41.74, 13.48],[41.74, 13.50],
            [41.76, 13.38],[41.76, 13.40],[41.76, 13.42],[41.76, 13.44],[41.76, 13.46],[41.76, 13.48],[41.76, 13.50],[41.78, 13.38],[41.78, 13.40],[41.78, 13.42],#600
            [41.78, 13.44],[41.78, 13.46],[41.78, 13.48],[41.78, 13.50],[41.80, 13.38],[41.80, 13.40],[41.80, 13.42],[41.80, 13.44],[41.80, 13.46],[41.80, 13.48],
            [41.80, 13.50],[41.78, 13.52],[41.74, 13.52],[41.74, 13.54],[41.74, 13.56],[41.74, 13.58],[41.74, 13.60],[41.74, 13.62],[41.74, 13.64],[41.74, 13.66],
            [41.74, 13.68],[41.74, 13.70],[41.74, 13.72],[41.74, 13.74],[41.74, 13.76],[41.76, 13.52],[41.76, 13.54],[41.76, 13.56],[41.76, 13.58],[41.76, 13.60],
            [41.76, 13.62],[41.76, 13.64],[41.76, 13.66],[41.76, 13.68],[41.76, 13.70],[41.76, 13.72],[41.76, 13.74],[41.76, 13.76],[41.78, 13.60],[41.78, 13.62],
            [41.78, 13.64],[41.78, 13.66],[41.78, 13.68],[41.78, 13.70],[41.78, 13.72],[41.78, 13.74],[41.80, 13.64],[41.80, 13.66],[41.80, 13.68],[41.80, 13.72],
            [41.74, 13.78],[41.74, 13.80],[41.74, 13.82],[41.74, 13.84],[41.74, 13.86],[41.74, 13.88],[41.74, 13.90],[41.76, 13.80],[41.76, 13.82],[41.46, 13.84],
            [41.46, 13.86],[41.46, 13.88],[41.46, 13.90],[41.46, 13.92],[41.48, 13.84],[41.48, 13.86],[41.48, 13.88],[41.48, 13.90],[41.48, 13.92],[41.50, 13.84],
            [41.50, 13.86],[41.50, 13.88],[41.50, 13.90],[41.50, 13.92],[41.52, 13.84],[41.52, 13.86],[41.52, 13.88],[41.52, 13.90],[41.52, 13.92],[41.54, 13.84],
            [41.54, 13.86],[41.54, 13.88],[41.54, 13.90],[41.54, 13.92],[41.56, 13.84],[41.56, 13.86],[41.56, 13.88],[41.56, 13.90],[41.56, 13.92],[41.58, 13.84],
            [41.58, 13.86],[41.58, 13.88],[41.58, 13.90],[41.58, 13.92],[41.60, 13.84],[41.60, 13.86],[41.60, 13.88],[41.60, 13.90],[41.60, 13.92],[41.62, 13.84],#700
            [41.62, 13.86],[41.62, 13.88],[41.62, 13.90],[41.62, 13.92],[41.64, 13.84],[41.64, 13.86],[41.64, 13.88],[41.64, 13.90],[41.64, 13.92],[41.66, 13.84],
            [41.66, 13.86],[41.66, 13.88],[41.66, 13.90],[41.66, 13.92],[41.68, 13.84],[41.68, 13.86],[41.68, 13.88],[41.68, 13.90],[41.68, 13.92],[41.70, 13.84],
            [41.70, 13.86],[41.70, 13.88],[41.70, 13.90],[41.70, 13.92],[41.72, 13.84],[41.72, 13.86],[41.72, 13.88],[41.72, 13.90],[41.72, 13.92],[41.46, 13.94],
            [41.48, 13.94],[41.50, 13.94],[41.52, 13.94],[41.54, 13.94],[41.56, 13.94],[41.58, 13.94],[41.60, 13.94],[41.62, 13.94],[41.64, 13.94],[41.66, 13.94],
            [41.68, 13.94],[41.70, 13.94],[41.46, 13.96],[41.48, 13.96],[41.50, 13.96],[41.52, 13.96],[41.54, 13.96],[41.56, 13.96],[41.58, 13.96],[41.60, 13.96],
            [41.62, 13.96],[41.64, 13.96],[41.66, 13.96],[41.68, 13.96],[41.46, 13.98],[41.48, 13.98],[41.50, 13.98],[41.52, 13.98],[41.54, 13.98],[41.56, 13.98],
            [41.58, 13.98],[41.60, 13.98],[41.62, 13.98],[41.64, 13.98],[41.66, 13.98],[41.52, 14.00],[41.54, 14.00],[41.56, 14.00],[41.58, 14.00],[41.60, 14.00],
            [41.62, 14.00],[41.64, 14.00],[41.52, 14.02],[41.54, 14.02],[41.56, 14.02],[41.40, 13.30],[41.40, 13.32],[41.40, 13.34],[41.42, 13.30],[41.42, 13.32],
            [41.42, 13.34],[41.44, 13.30],[41.44, 13.32],[41.44, 13.34],[41.46, 13.30],[41.46, 13.32],[41.46, 13.34],[41.48, 13.30],[41.48, 13.32],[41.48, 13.34],
            [41.50, 13.30],[41.50, 13.32],[41.50, 13.34],[41.52, 13.30],[41.52, 13.32],[41.52, 13.34],[41.54, 13.30],[41.54, 13.32],[41.54, 13.34],[41.56, 13.30],#800
            [41.56, 13.32],[41.56, 13.34],[41.58, 13.30],[41.58, 13.32],[41.58, 13.34],[41.58, 13.16],[41.58, 13.18],[41.58, 13.20],[41.58, 13.22],[41.58, 13.24],
            [41.58, 13.26],[41.58, 13.28],[41.56, 13.20],[41.56, 13.22],[41.56, 13.24],[41.56, 13.26],[41.56, 13.28],[41.54, 13.20],[41.54, 13.22],[41.54, 13.24],
            [41.54, 13.26],[41.54, 13.28],[41.52, 13.26],[41.52, 13.28],[41.50, 13.28],[41.46, 13.26],[41.46, 13.28],[41.44, 13.26],[41.44, 13.28],[41.42, 13.28],
            [41.44, 13.38],[41.44, 13.40],[41.44, 13.42],[41.44, 13.44],[41.42, 13.38],[41.42, 13.40],[41.42, 13.42],[41.42, 13.44],[41.40, 13.38],[41.40, 13.40],
            [41.40, 13.42],[41.40, 13.44],[41.44, 13.46],[41.44, 13.48],[41.44, 13.50],[41.44, 13.52],[41.44, 13.54],[41.44, 13.56],[41.44, 13.58],[41.44, 13.60],
            [41.44, 13.62],[41.44, 13.64],[41.44, 13.66],[41.44, 13.68],[41.44, 13.70],[41.44, 13.72],[41.44, 13.74],[41.44, 13.76],[41.44, 13.78],[41.44, 13.80],
            [41.44, 13.82],[41.44, 13.84],[41.44, 13.86],[41.44, 13.88],[41.44, 13.90],[41.44, 13.92],[41.44, 13.94],[41.42, 13.52],[41.42, 13.54],[41.42, 13.56],
            [41.42, 13.58],[41.42, 13.60],[41.42, 13.62],[41.42, 13.64],[41.42, 13.66],[41.42, 13.68],[41.42, 13.70],[41.42, 13.72],[41.42, 13.74],[41.42, 13.76],
            [41.42, 13.78],[41.42, 13.80],[41.42, 13.82],[41.42, 13.84],[41.42, 13.86],[41.42, 13.88],[41.42, 13.90],[41.40, 13.56],[41.40, 13.58],[41.40, 13.60],
            [41.40, 13.62],[41.40, 13.64],[41.40, 13.66],[41.40, 13.68],[41.40, 13.70],[41.40, 13.72],[41.40, 13.74],[41.40, 13.76],[41.40, 13.78],[41.40, 13.80],#900
            [41.40, 13.82],[41.40, 13.84],[41.40, 13.86],[41.40, 13.88],[41.38, 13.56],[41.38, 13.58],[41.38, 13.60],[41.38, 13.62],[41.38, 13.64],[41.38, 13.66],
            [41.38, 13.68],[41.38, 13.70],[41.38, 13.72],[41.38, 13.74],[41.38, 13.76],[41.38, 13.78],[41.38, 13.80],[41.38, 13.82],[41.38, 13.84],[41.38, 13.86],
            [41.38, 13.88],[41.36, 13.56],[41.36, 13.58],[41.36, 13.60],[41.36, 13.62],[41.36, 13.64],[41.36, 13.66],[41.36, 13.68],[41.36, 13.70],[41.36, 13.72],
            [41.36, 13.74],[41.36, 13.76],[41.36, 13.78],[41.36, 13.80],[41.36, 13.82],[41.36, 13.84],[41.36, 13.86],[41.36, 13.88],[41.34, 13.60],[41.34, 13.62],
            [41.34, 13.64],[41.34, 13.66],[41.34, 13.68],[41.34, 13.70],[41.34, 13.72],[41.34, 13.74],[41.34, 13.76],[41.34, 13.78],[41.34, 13.80],[41.34, 13.82],
            [41.34, 13.84],[41.34, 13.86],[41.34, 13.88],[41.32, 13.62],[41.32, 13.64],[41.32, 13.66],[41.32, 13.74],[41.32, 13.76],[41.32, 13.78],[41.32, 13.80],
            [41.32, 13.82],[41.30, 13.76],[41.30, 13.78]#963            
            ]
        
    if provincia=="Rieti":
        confini_provincia = gpd.read_feather('./conf/confini/rieti.feather')
        coord_002_list=[
            [42.74, 13.28],[42.60, 13.20],[42.60, 13.22],[42.60, 13.24],[42.60, 13.26],[42.60, 13.28],[42.60, 13.30],[42.60, 13.32],[42.62, 13.20],[42.62, 13.22],
            [42.62, 13.24],[42.62, 13.26],[42.62, 13.28],[42.62, 13.30],[42.62, 13.32],[42.64, 13.20],[42.64, 13.22],[42.64, 13.24],[42.64, 13.26],[42.64, 13.28],
            [42.64, 13.30],[42.64, 13.32],[42.66, 13.20],[42.66, 13.22],[42.66, 13.24],[42.66, 13.26],[42.66, 13.28],[42.66, 13.30],[42.66, 13.32],[42.68, 13.20],
            [42.68, 13.22],[42.68, 13.24],[42.68, 13.26],[42.68, 13.28],[42.68, 13.30],[42.68, 13.32],[42.70, 13.20],[42.70, 13.22],[42.70, 13.24],[42.70, 13.26],
            [42.70, 13.28],[42.70, 13.30],[42.70, 13.32],[42.72, 13.20],[42.72, 13.22],[42.72, 13.24],[42.72, 13.26],[42.72, 13.28],[42.72, 13.30],[42.72, 13.32],
            [42.18, 12.92],[42.18, 12.94],[42.18, 12.96],[42.18, 12.98],[42.18, 13.00],[42.18, 13.02],[42.18, 13.04],[42.18, 13.06],[42.18, 13.08],[42.18, 13.10],
            [42.18, 13.12],[42.20, 12.92],[42.20, 12.94],[42.20, 12.96],[42.20, 12.98],[42.20, 13.00],[42.20, 13.02],[42.20, 13.04],[42.20, 13.06],[42.20, 13.08],
            [42.20, 13.10],[42.20, 13.12],[42.22, 12.92],[42.22, 12.94],[42.22, 12.96],[42.22, 12.98],[42.22, 13.00],[42.44, 12.84],[42.44, 12.86],[42.44, 12.88],
            [42.22, 13.02],[42.22, 13.04],[42.22, 13.06],[42.22, 13.08],[42.22, 13.10],[42.22, 13.12],[42.24, 12.92],[42.24, 12.94],[42.24, 12.96],[42.44, 12.82],
            [42.24, 12.98],[42.24, 13.00],[42.24, 13.02],[42.24, 13.04],[42.24, 13.06],[42.24, 13.08],[42.24, 13.10],[42.24, 13.12],[42.26, 12.92],[42.44, 12.80],
            [42.26, 12.94],[42.26, 12.96],[42.26, 12.98],[42.26, 13.00],[42.26, 13.02],[42.26, 13.04],[42.26, 13.06],[42.26, 13.08],[42.26, 13.10],[42.26, 13.12],
            [42.28, 12.90],[42.28, 12.92],[42.28, 12.94],[42.28, 12.96],[42.28, 12.98],[42.28, 13.00],[42.28, 13.02],[42.28, 13.04],[42.28, 13.06],[42.28, 13.08],
            [42.28, 13.10],[42.28, 13.12],[42.30, 12.90],[42.30, 12.92],[42.30, 12.94],[42.30, 12.96],[42.30, 12.98],[42.30, 13.00],[42.30, 13.02],[42.30, 13.04],
            [42.30, 13.06],[42.30, 13.08],[42.30, 13.10],[42.30, 13.12],[42.32, 12.90],[42.32, 12.92],[42.32, 12.94],[42.32, 12.96],[42.32, 12.98],[42.32, 13.00],
            [42.32, 13.02],[42.32, 13.04],[42.32, 13.06],[42.32, 13.08],[42.32, 13.10],[42.32, 13.12],[42.34, 12.90],[42.34, 12.92],[42.34, 12.94],[42.34, 12.96],
            [42.34, 12.98],[42.34, 13.00],[42.34, 13.02],[42.34, 13.04],[42.34, 13.06],[42.34, 13.08],[42.34, 13.10],[42.34, 13.12],[42.36, 12.90],[42.36, 12.92],
            [42.36, 12.94],[42.36, 12.96],[42.36, 12.98],[42.36, 13.00],[42.36, 13.02],[42.36, 13.04],[42.36, 13.06],[42.36, 13.08],[42.36, 13.10],[42.36, 13.12],
            [42.38, 12.90],[42.38, 12.92],[42.38, 12.94],[42.38, 12.96],[42.38, 12.98],[42.38, 13.00],[42.38, 13.02],[42.38, 13.04],[42.38, 13.06],[42.38, 13.08],
            [42.38, 13.10],[42.38, 13.12],[42.40, 12.90],[42.40, 12.92],[42.40, 12.94],[42.40, 12.96],[42.40, 12.98],[42.40, 13.00],[42.40, 13.02],[42.40, 13.04],
            [42.40, 13.06],[42.40, 13.08],[42.40, 13.10],[42.40, 13.12],[42.42, 12.90],[42.42, 12.92],[42.42, 12.94],[42.42, 12.96],[42.42, 12.98],[42.42, 13.00],#200
            [42.42, 13.02],[42.42, 13.04],[42.42, 13.06],[42.42, 13.08],[42.42, 13.10],[42.42, 13.12],[42.44, 12.90],[42.44, 12.92],[42.44, 12.94],[42.44, 12.96],
            [42.44, 12.98],[42.44, 13.00],[42.44, 13.02],[42.44, 13.04],[42.44, 13.06],[42.44, 13.08],[42.44, 13.10],[42.44, 13.12],[42.46, 12.90],[42.46, 12.92],
            [42.46, 12.94],[42.46, 12.96],[42.46, 12.98],[42.46, 13.00],[42.46, 13.02],[42.46, 13.04],[42.46, 13.06],[42.46, 13.08],[42.46, 13.10],[42.46, 13.12],
            [42.48, 12.90],[42.48, 12.92],[42.48, 12.94],[42.48, 12.96],[42.48, 12.98],[42.48, 13.00],[42.48, 13.02],[42.48, 13.04],[42.48, 13.06],[42.48, 13.08],
            [42.48, 13.10],[42.48, 13.12],[42.50, 12.90],[42.50, 12.92],[42.50, 12.94],[42.50, 12.96],[42.50, 12.98],[42.50, 13.00],[42.50, 13.02],[42.50, 13.04],
            [42.50, 13.06],[42.50, 13.08],[42.50, 13.10],[42.50, 13.12],[42.52, 12.90],[42.52, 12.92],[42.52, 12.94],[42.52, 12.96],[42.52, 12.98],[42.52, 13.00],
            [42.52, 13.02],[42.52, 13.04],[42.52, 13.06],[42.52, 13.08],[42.52, 13.10],[42.52, 13.12],[42.54, 12.90],[42.54, 12.92],[42.54, 12.94],[42.54, 12.96],
            [42.54, 12.98],[42.54, 13.00],[42.54, 13.02],[42.54, 13.04],[42.54, 13.06],[42.54, 13.08],[42.54, 13.10],[42.54, 13.12],[42.56, 12.90],[42.56, 12.92],
            [42.56, 12.94],[42.56, 12.96],[42.56, 12.98],[42.56, 13.00],[42.56, 13.02],[42.56, 13.04],[42.56, 13.06],[42.56, 13.08],[42.56, 13.10],[42.56, 13.12],
            [42.58, 12.90],[42.58, 12.92],[42.58, 12.94],[42.58, 12.96],[42.58, 12.98],[42.58, 13.00],[42.58, 13.02],[42.58, 13.04],[42.58, 13.06],[42.58, 13.08],
            [42.58, 13.10],[42.58, 13.12],[42.60, 12.90],[42.60, 12.92],[42.60, 12.94],[42.60, 12.96],[42.60, 12.98],[42.60, 13.00],[42.60, 13.02],[42.60, 13.04],
            [42.60, 13.06],[42.60, 13.08],[42.60, 13.10],[42.60, 13.12],[42.18, 12.64],[42.18, 12.66],[42.18, 12.68],[42.18, 12.70],[42.18, 12.72],[42.18, 12.74],
            [42.18, 12.76],[42.18, 12.78],[42.18, 12.80],[42.18, 12.82],[42.18, 12.84],[42.18, 12.86],[42.18, 12.88],[42.18, 12.90],[42.20, 12.64],[42.20, 12.66],
            [42.20, 12.68],[42.20, 12.70],[42.20, 12.72],[42.20, 12.74],[42.20, 12.76],[42.20, 12.78],[42.20, 12.80],[42.20, 12.82],[42.20, 12.84],[42.20, 12.86],
            [42.20, 12.88],[42.20, 12.90],[42.22, 12.64],[42.22, 12.66],[42.22, 12.68],[42.22, 12.70],[42.22, 12.72],[42.22, 12.74],[42.22, 12.76],[42.22, 12.78],
            [42.22, 12.80],[42.22, 12.82],[42.22, 12.84],[42.22, 12.86],[42.22, 12.88],[42.22, 12.90],[42.24, 12.64],[42.24, 12.66],[42.24, 12.68],[42.24, 12.70],
            [42.24, 12.72],[42.24, 12.74],[42.24, 12.76],[42.24, 12.78],[42.24, 12.80],[42.24, 12.82],[42.24, 12.84],[42.24, 12.86],[42.24, 12.88],[42.24, 12.90],
            [42.26, 12.64],[42.26, 12.66],[42.26, 12.68],[42.26, 12.70],[42.26, 12.72],[42.26, 12.74],[42.26, 12.76],[42.26, 12.78],[42.26, 12.80],[42.26, 12.82],
            [42.26, 12.84],[42.26, 12.86],[42.26, 12.88],[42.26, 12.90],[42.28, 12.64],[42.28, 12.66],[42.28, 12.68],[42.28, 12.70],[42.28, 12.72],[42.28, 12.74],
            [42.28, 12.76],[42.28, 12.78],[42.28, 12.80],[42.28, 12.82],[42.28, 12.84],[42.28, 12.86],[42.28, 12.88],[42.30, 12.64],[42.30, 12.66],[42.44, 12.78],#400
            [42.30, 12.68],[42.30, 12.70],[42.30, 12.72],[42.30, 12.74],[42.30, 12.76],[42.30, 12.78],[42.30, 12.80],[42.30, 12.82],[42.30, 12.84],[42.30, 12.86],
            [42.30, 12.88],[42.32, 12.64],[42.32, 12.66],[42.32, 12.68],[42.32, 12.70],[42.32, 12.72],[42.32, 12.74],[42.32, 12.76],[42.32, 12.78],[42.44, 12.76],
            [42.32, 12.80],[42.32, 12.82],[42.32, 12.84],[42.32, 12.86],[42.32, 12.88],[42.34, 12.64],[42.34, 12.66],[42.34, 12.68],[42.34, 12.70],[42.44, 12.74],
            [42.34, 12.72],[42.34, 12.74],[42.34, 12.76],[42.34, 12.78],[42.34, 12.80],[42.34, 12.82],[42.34, 12.84],[42.34, 12.86],[42.34, 12.88],[42.44, 12.72],
            [42.36, 12.64],[42.36, 12.66],[42.36, 12.68],[42.36, 12.70],[42.36, 12.72],[42.36, 12.74],[42.36, 12.76],[42.36, 12.78],[42.36, 12.80],[42.36, 12.82],
            [42.36, 12.84],[42.36, 12.86],[42.36, 12.88],[42.38, 12.64],[42.38, 12.66],[42.38, 12.68],[42.38, 12.70],[42.38, 12.72],[42.38, 12.74],[42.44, 12.70],
            [42.38, 12.76],[42.38, 12.78],[42.38, 12.80],[42.38, 12.82],[42.38, 12.84],[42.38, 12.86],[42.38, 12.88],[42.40, 12.64],[42.40, 12.66],[42.44, 12.68],
            [42.40, 12.68],[42.40, 12.70],[42.40, 12.72],[42.40, 12.74],[42.40, 12.76],[42.40, 12.78],[42.40, 12.80],[42.40, 12.82],[42.40, 12.84],[42.40, 12.86],
            [42.40, 12.88],[42.42, 12.64],[42.42, 12.66],[42.42, 12.68],[42.42, 12.70],[42.42, 12.72],[42.42, 12.74],[42.42, 12.76],[42.42, 12.78],[42.44, 12.66],
            [42.42, 12.80],[42.42, 12.82],[42.42, 12.84],[42.42, 12.86],[42.42, 12.88],[42.44, 12.64],[42.18, 13.14],[42.18, 13.16],[42.18, 13.18],[42.18, 13.20],#500
            [42.18, 13.22],[42.20, 13.14],[42.20, 13.16],[42.20, 13.18],[42.20, 13.20],[42.20, 13.22],[42.22, 13.14],[42.22, 13.16],[42.22, 13.18],[42.22, 13.20],
            [42.22, 13.22],[42.24, 13.14],[42.24, 13.16],[42.24, 13.18],[42.24, 13.20],[42.24, 13.22],[42.26, 13.14],[42.26, 13.16],[42.26, 13.18],[42.26, 13.20],
            [42.26, 13.22],[42.28, 13.14],[42.28, 13.16],[42.28, 13.18],[42.28, 13.20],[42.28, 13.22],[42.30, 13.14],[42.30, 13.16],[42.30, 13.18],[42.30, 13.20],
            [42.30, 13.22],[42.32, 13.14],[42.32, 13.16],[42.32, 13.18],[42.32, 13.20],[42.32, 13.22],[42.46, 12.72],[42.46, 12.74],[42.46, 12.76],[42.46, 12.78],
            [42.46, 12.80],[42.46, 12.82],[42.46, 12.84],[42.46, 12.86],[42.46, 12.88],[42.48, 12.72],[42.48, 12.74],[42.48, 12.76],[42.48, 12.78],[42.48, 12.80],
            [42.48, 12.82],[42.48, 12.84],[42.48, 12.86],[42.48, 12.88],[42.50, 12.72],[42.50, 12.74],[42.50, 12.76],[42.50, 12.78],[42.50, 12.80],[42.50, 12.82],
            [42.50, 12.84],[42.50, 12.86],[42.50, 12.88],[42.14, 12.84],[42.14, 12.86],[42.14, 12.88],[42.14, 12.90],[42.14, 12.92],[42.14, 12.94],[42.14, 12.96],
            [42.14, 12.98],[42.14, 13.00],[42.14, 13.02],[42.14, 13.04],[42.14, 13.06],[42.14, 13.08],[42.16, 12.84],[42.16, 12.86],[42.16, 12.88],[42.16, 12.90],
            [42.16, 12.92],[42.16, 12.94],[42.16, 12.96],[42.16, 12.98],[42.16, 13.00],[42.16, 13.02],[42.16, 13.04],[42.16, 13.06],[42.16, 13.08],[42.52, 12.76],
            [42.52, 12.78],[42.52, 12.80],[42.52, 12.82],[42.52, 12.84],[42.52, 12.86],[42.52, 12.88],[42.54, 12.78],[42.54, 12.80],[42.54, 12.82],[42.54, 12.84],
            [42.54, 12.86],[42.54, 12.88],[42.56, 12.84],[42.56, 12.86],[42.56, 12.88],[42.60, 12.88],[42.74, 13.20],[42.74, 13.26],[42.62, 12.88],[42.62, 12.90],
            [42.62, 12.92],[42.62, 12.94],[42.62, 12.96],[42.62, 12.98],[42.62, 13.00],[42.62, 13.02],[42.62, 13.04],[42.62, 13.06],[42.62, 13.08],[42.62, 13.10],
            [42.62, 13.12],[42.62, 13.14],[42.62, 13.16],[42.62, 13.18],[42.64, 13.02],[42.64, 13.04],[42.64, 13.08],[42.64, 13.10],[42.64, 13.12],[42.64, 13.14],
            [42.64, 13.16],[42.64, 13.18],[42.66, 13.12],[42.66, 13.14],[42.66, 13.16],[42.66, 13.18],[42.68, 13.18],[42.70, 13.18],[42.70, 13.34],[42.70, 13.36],
            [42.68, 13.34],[42.68, 13.36],[42.66, 13.34],[42.66, 13.36],[42.64, 13.34],[42.64, 13.36],[42.64, 13.38],[42.64, 13.40],[42.62, 13.34],[42.62, 13.36],
            [42.62, 13.38],[42.62, 13.40],[42.60, 13.34],[42.60, 13.36],[42.60, 13.38],[42.60, 13.40],[42.60, 13.14],[42.60, 13.16],[42.60, 13.18],[42.58, 13.14],
            [42.58, 13.16],[42.58, 13.18],[42.58, 13.20],[42.58, 13.22],[42.58, 13.24],[42.58, 13.26],[42.58, 13.28],[42.58, 13.30],[42.58, 13.32],[42.58, 13.34],
            [42.58, 13.36],[42.58, 13.38],[42.56, 13.14],[42.56, 13.16],[42.56, 13.18],[42.54, 13.14],[42.54, 13.16],[42.54, 13.18],[42.52, 13.14],[42.52, 13.16],
            [42.52, 13.18],[42.50, 13.14],[42.50, 13.16],[42.50, 13.18],[42.48, 13.14],[42.48, 13.16],[42.48, 13.18],[42.46, 13.14],[42.46, 13.16],[42.44, 13.14],
            [42.42, 13.14],[42.40, 13.14],[42.40, 13.16],[42.40, 13.18],[42.40, 13.20],[42.38, 13.14],[42.38, 13.16],[42.38, 13.18],[42.38, 13.20],[42.36, 13.14],#700
            [42.36, 13.16],[42.34, 13.14],[42.34, 13.16],[42.34, 13.18],[42.28, 13.24],[42.26, 13.24],[42.26, 13.26],[42.24, 13.24],[42.24, 13.26],[42.24, 13.28],
            [42.24, 13.30],[42.22, 13.24],[42.22, 13.26],[42.22, 13.28],[42.22, 13.30],[42.22, 13.32],[42.22, 13.34],[42.20, 13.24],[42.20, 13.26],[42.20, 13.28],
            [42.20, 13.30],[42.20, 13.32],[42.20, 13.34],[42.18, 13.24],[42.18, 13.26],[42.18, 13.28],[42.18, 13.30],[42.18, 13.32],[42.18, 13.34],[42.18, 13.36],
            [42.18, 13.38],[42.16, 13.14],[42.16, 13.16],[42.16, 13.18],[42.16, 13.20],[42.16, 13.22],[42.16, 13.24],[42.16, 13.26],[42.16, 13.28],[42.16, 13.30],
            [42.16, 13.32],[42.16, 13.34],[42.16, 13.36],[42.14, 13.20],[42.14, 13.22],[42.14, 13.24],[42.14, 13.26],[42.14, 13.28],[42.14, 13.30],[42.12, 13.24],
            [42.12, 12.86],[42.12, 12.88],[42.12, 12.90],[42.12, 12.92],[42.12, 12.94],[42.12, 12.96],[42.12, 12.98],[42.12, 13.00],[42.12, 13.02],[42.12, 13.04],
            [42.12, 13.06],[42.10, 12.86],[42.10, 12.88],[42.10, 12.90],[42.10, 12.94],[42.10, 12.96],[42.20, 12.62],[42.18, 12.62],[42.16, 12.64],[42.16, 12.66],
            [42.16, 12.68],[42.16, 12.70],[42.16, 12.72],[42.16, 12.74],[42.46, 12.62],[42.46, 12.64],[42.46, 12.70],[42.44, 12.62],[42.42, 12.62],[42.40, 12.44],
            [42.40, 12.46],[42.40, 12.48],[42.40, 12.50],[42.40, 12.52],[42.40, 12.58],[42.40, 12.60],[42.40, 12.62],[42.38, 12.44],[42.38, 12.46],[42.38, 12.48],
            [42.38, 12.50],[42.38, 12.52],[42.38, 12.54],[42.38, 12.56],[42.38, 12.58],[42.38, 12.60],[42.38, 12.62],[42.36, 12.46],[42.36, 12.48],[42.36, 12.50],#800
            [42.36, 12.52],[42.36, 12.54],[42.36, 12.56],[42.36, 12.58],[42.36, 12.60],[42.36, 12.62],[42.34, 12.46],[42.34, 12.48],[42.34, 12.50],[42.34, 12.52],
            [42.34, 12.54],[42.34, 12.56],[42.34, 12.58],[42.34, 12.60],[42.34, 12.62],[42.32, 12.48],[42.32, 12.50],[42.32, 12.52],[42.32, 12.54],[42.32, 12.56],
            [42.32, 12.58],[42.32, 12.60],[42.32, 12.62],[42.30, 12.48],[42.30, 12.50],[42.30, 12.52],[42.30, 12.54],[42.30, 12.56],[42.30, 12.58],[42.30, 12.60],
            [42.30, 12.62],[42.28, 12.56],[42.28, 12.58],[42.28, 12.60],[42.28, 12.62],[42.26, 12.58],[42.26, 12.60],[42.26, 12.62],[42.24, 12.62],[42.20, 12.62],
            [42.16, 12.78],[42.16, 12.80],[42.16, 12.82]#843
            ]

    avanzamento=0; elementi=(len(coord_002_list))

    for coord in coord_002_list:
        latitudine=(coord[0])
        longitudine=(coord[1])
        dati_api, elev=api_002_arpae_icon_2i(latitudine, longitudine)
        river_discharge=api_005_glofas_v4(latitudine,longitudine)
        avanzamento=avanzamento+1
            
        coordinate_per_poligono = ((longitudine-0.01,latitudine+0.01), (longitudine+0.01,latitudine+0.01),
        (longitudine+0.01, latitudine-0.01), (longitudine-0.01, latitudine-0.01),(longitudine-0.01, latitudine+0.01))

        for j in range(0,3):
                    data=dati_api["date"][j]
                    converti_giorno=datetime.date(data)
                    giorno = converti_giorno + timedelta(days=1)

                    pd_dataframe.loc[len(pd_dataframe)] = [giorno, 
                                                           latitudine, 
                                                           longitudine, 
                                                           elev, 
                                                           tronca(dati_api["temperature_2m_max"][j],1),
                                                           tronca(dati_api["wind_speed_10m_max"][j],1),
                                                           tronca(dati_api["snowfall_sum"][j],0),
                                                           tronca(dati_api["rain_sum"][j],0),
                                                           tronca(dati_api["precipitation_sum"][j],0), 
                                                           dati_api["weather_code"][j],
                                                           dati_api["precipitation_hours"][j],
                                                           tronca(river_discharge["river_discharge"][j],1),
                                                           0,#ts_discharge
                                                           0,#flood_factor
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           '',
                                                           0,
                                                           0,
                                                           coordinate_per_poligono,
                                                           '',
                                                           tronca(dati_api["temperature_2m_max"][j],1),
                                                           tronca(dati_api["wind_speed_10m_max"][j],1),
                                                           tronca(dati_api["snowfall_sum"][j],0),
                                                           tronca(dati_api["precipitation_sum"][j],0),
                                                           tronca(dati_api["rain_sum"][j],0),
                                                           dati_api["weather_code"][j],
                                                           dati_api["precipitation_hours"][j],
                                                           tronca(river_discharge["river_discharge"][j],1)]
                    
        valore_bar=round((100/elementi)*avanzamento);bar.setValue(valore_bar)

    
    df_ordinato=pd_dataframe.sort_values(by=['giorno','lat','lon']).reset_index()
    #carica i confini provinciali    
    geo_confini = gpd.GeoSeries(confini_provincia["geometry"]).simplify(tolerance=0.001)
    df2 = gpd.GeoDataFrame({'geometry': geo_confini}, crs=4326)
    
    #calcola le intersezioni tra i confini provinciali ed i poligoni 002 modello ARPAE ICON2I, popola il dataframe con i valori cdf
    num_rows = len(df_ordinato)
    avanzamento=0;elementi=num_rows;bar.setValue(avanzamento)
    #carica le soglie di discharge
    if num_rows==2205: df = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_latina.xlsx')
    if num_rows==3273: df = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_viterbo.xlsx')
    if num_rows==2529: df = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_rieti.xlsx')
    if num_rows==4818: df = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_roma.xlsx')
    if num_rows==2889: df = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_frosinone.xlsx')
    for i in range(0,num_rows):
           avanzamento=avanzamento+1
           poligono_coord=(df_ordinato.at[i,'poligono_002'])
           poligono_geometria = Polygon(poligono_coord)
           poligono=gpd.GeoSeries(poligono_geometria)
           df1 = gpd.GeoDataFrame({'geometry': poligono}, crs=4326)
           intersezione = df2.overlay(df1, how='intersection')
           df_ordinato.at[i,'geometry']=intersezione.at[0, 'geometry']
           df_ordinato.at[i,'index']=i           

           df_ordinato.at[i,'ts_discharge']=df.at[i,'ts_discharge']
           df_ordinato.at[i,'flood_factor']=df.at[i,'flood_factor']
           df_ordinato.at[i,'flood_warning']=df.at[i,'flood_pericolo']
           df_ordinato.at[i,'hwdi']=calcola_hwdi(df_ordinato.at[i,'temperature_2m_max'],df_ordinato.at[i,'precipitation_sum'])
           df_ordinato.at[i,'hwdi_HM']=df_ordinato.at[i,'hwdi']/14
           df_ordinato.at[i,'prob_tralicci']=calcola_prob_tralicci(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_linea_esterna']=calcola_prob_linea_esterna(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_la_nuovi']=calcola_prob_pali_legnoacciaio_nuovi(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_20']=calcola_prob_pali_legno_20(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_40']=calcola_prob_pali_legno_40(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'prob_pali_l_60']=calcola_prob_pali_legno_60(df_ordinato.at[i,'wind_speed_10m_max'])
           df_ordinato.at[i,'tp65']=calcola_tp65(df_ordinato.at[i,'temperature_2m_max'])
           df_ordinato.at[i,'td65']=calcola_td65(df_ordinato.at[i,'temperature_2m_max'])
           df_ordinato.at[i,'flood_depth']=calcola_flood_depth(df_ordinato.at[i,'flood_warning'],df_ordinato.at[i,'river_discharge'],df_ordinato.at[i,'ts_discharge'],df_ordinato.at[i,'flood_factor'])
           df_ordinato.at[i,'flood_risk_cabina']=calcola_flood_failure_cabina(df_ordinato.at[i,'flood_depth'])
           valore_bar=round((100/elementi)*avanzamento);bar.setValue(valore_bar)

    #crea il geodataframe con le geometrie (overlay)      
    geo=gpd.GeoDataFrame(df_ordinato, geometry='geometry')
    if (len(geo)==2205 or len(geo)==3273 or len(geo)==2529 or len(geo)==4818 or len(geo)==2889):
        geo.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
        geo.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')

        ct = datetime.now()
        timestamp = ct.timestamp()
        date_time = datetime.fromtimestamp(timestamp)
        data = date_time.strftime("%Y_%m_%d_%H%M%S_002deg")
        geo.to_feather('./scenari/' + provincia +'_' + data + '.feather')
        abilita_elabora_scenario()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Errore")
        msg.setText("Dati incompleti/non disponibili sul server remoto. Riprovare all'inizio della prossima ora!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()


#aggiorna il dataframe ricaricando le soglie portata corsi d'acqua dei file xlsx, eventualmente modificate
def ricarica_soglie():
    geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    num_rows=len(geo_dataframe_corrente)
    if num_rows==2205:#provincia Latina
        df_soglie = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_latina.xlsx')
    if num_rows==2889:#provincia Frosinone
        df_soglie = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_frosinone.xlsx')
    if num_rows==4818:#provincia Roma
        df_soglie = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_roma.xlsx')
    if num_rows==2529:#provincia Rieti
        df_soglie = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_rieti.xlsx')
    if num_rows==3273:#provincia Viterbo
        df_soglie = pd.read_excel('./conf/aree_pericolo_alluvione/soglie_viterbo.xlsx')
    
    for i in range(0,num_rows):
        geo_dataframe_corrente.at[i,'ts_discharge']=df_soglie.at[i,'ts_discharge']
        geo_dataframe_corrente.at[i,'flood_warning']=df_soglie.at[i,'flood_pericolo']
        geo_dataframe_corrente.at[i,'flood_factor']=df_soglie.at[i,'flood_factor']
        geo_dataframe_corrente.at[i,'flood_depth']=calcola_flood_depth(geo_dataframe_corrente.at[i,'flood_warning'],geo_dataframe_corrente.at[i,'river_discharge'],geo_dataframe_corrente.at[i,'ts_discharge'],geo_dataframe_corrente.at[i,'flood_factor'])
        geo_dataframe_corrente.at[i,'flood_risk_cabina']=calcola_flood_failure_cabina(geo_dataframe_corrente.at[i,'flood_depth'])
    geo_dataframe_corrente.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    geo_dataframe_corrente.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')
    #abilita_elabora_scenario()
    global msg
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle("Soglie flood")
    msg.setText("Soglie alluvione aggiornate")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.show()


#salva la mappa dello scenario corrente in un file html, in modo da essere utilizzata in altre applicazioni
def pulsante_salva_mappa():
    global file_dialog_salva_mappa
    file_dialog_salva_mappa=QFileDialog()
    filename_mappa, _ = QFileDialog.getSaveFileName(file_dialog_salva_mappa,"Salva mappa","./scenari","File HTML (*.html)")
    if filename_mappa:
            shutil.copy('./conf/analisi_corrente/analisi_map.html', str(filename_mappa))

#apre il dataframe in excel
def apri_dataframe_excel():
    file = "E:\\0_Tesi\\tool\\conf\\analisi_corrente\\geo_dataframe_base.xlsx"
    os.startfile(file)

#apre il manuale html nel browser predefinito
def apri_manuale_html():
    fileguida="file:///" + path + "/conf/manuale/EWS_Elettro_Lazio_manuale.htm"
    webbrowser.open_new(fileguida)
  
#----------------------------------------------FINE FUNZIONI PULSANTI TOOLBAR-------------------------------------------------





















#ripristina i dati meteo originari e ricalcola le cdf (prob failure), nel caso fossero state apportate modifiche ai dati meteo 
# con le funzioni di simulazione e l'utente volesse tornare ai dati iniziali
def reset_dati():
    geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    num_rows = len(geo_dataframe_corrente)
    for i in range(0,num_rows):
        geo_dataframe_corrente.at[i,'temperature_2m_max']=geo_dataframe_corrente.at[i,'bk_temperature_2m_max']
        geo_dataframe_corrente.at[i,'wind_speed_10m_max']=geo_dataframe_corrente.at[i,'bk_wind_speed_10m_max']
        geo_dataframe_corrente.at[i,'rain_sum']=geo_dataframe_corrente.at[i,'bk_rain_sum']
        geo_dataframe_corrente.at[i,'snowfall_sum']=geo_dataframe_corrente.at[i,'bk_snowfall_sum']
        geo_dataframe_corrente.at[i,'precipitation_sum']=geo_dataframe_corrente.at[i,'bk_precipitation_sum']
        geo_dataframe_corrente.at[i,'weather_code']=geo_dataframe_corrente.at[i,'bk_weather_code']
        geo_dataframe_corrente.at[i,'precipitation_hours']=geo_dataframe_corrente.at[i,'bk_precipitation_hours']
        geo_dataframe_corrente.at[i,'river_discharge']=geo_dataframe_corrente.at[i,'bk_river_discharge']
        geo_dataframe_corrente.at[i,'M_mm']=15
        geo_dataframe_corrente.at[i,'m_mm']=calcola_stima_m_ice(geo_dataframe_corrente.at[i,'weather_code'], geo_dataframe_corrente.at[i,'precipitation_hours'], geo_dataframe_corrente.at[i,'wind_speed_10m_max'], geo_dataframe_corrente.at[i,'precipitation_sum'])
        geo_dataframe_corrente.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(geo_dataframe_corrente.at[i,'m_mm'],geo_dataframe_corrente.at[i,'M_mm'])
        geo_dataframe_corrente.at[i,'hwdi']=calcola_hwdi(geo_dataframe_corrente.at[i,'temperature_2m_max'],geo_dataframe_corrente.at[i,'precipitation_sum'])
        geo_dataframe_corrente.at[i,'hwdi_HM']=geo_dataframe_corrente.at[i,'hwdi']/14
        geo_dataframe_corrente.at[i,'prob_tralicci']=calcola_prob_tralicci(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
        geo_dataframe_corrente.at[i,'prob_linea_esterna']=calcola_prob_linea_esterna(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
        geo_dataframe_corrente.at[i,'prob_pali_la_nuovi']=calcola_prob_pali_legnoacciaio_nuovi(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
        geo_dataframe_corrente.at[i,'prob_pali_l_20']=calcola_prob_pali_legno_20(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
        geo_dataframe_corrente.at[i,'prob_pali_l_40']=calcola_prob_pali_legno_40(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
        geo_dataframe_corrente.at[i,'prob_pali_l_60']=calcola_prob_pali_legno_60(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
        geo_dataframe_corrente.at[i,'tp65']=calcola_tp65(geo_dataframe_corrente.at[i,'temperature_2m_max'])
        geo_dataframe_corrente.at[i,'td65']=calcola_td65(geo_dataframe_corrente.at[i,'temperature_2m_max'])
        if(geo_dataframe_corrente.columns[31]=="poligono_002"):
           geo_dataframe_corrente.at[i,'flood_depth']=calcola_flood_depth(geo_dataframe_corrente.at[i,'flood_warning'],geo_dataframe_corrente.at[i,'river_discharge'],geo_dataframe_corrente.at[i,'ts_discharge'],geo_dataframe_corrente.at[i,'flood_factor'])
           geo_dataframe_corrente.at[i,'flood_risk_cabina']=calcola_flood_failure_cabina(geo_dataframe_corrente.at[i,'flood_depth'])

    geo_dataframe_corrente.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    geo_dataframe_corrente.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')
    slider_temp.setValue(0);slider_vento.setValue(0);slider_precip.setValue(0);slider_neve.setValue(0); slider_discharge.setValue(0)
    radio_temp_off.setChecked(True)
    radio_vento_off.setChecked(True)
    radio_precip_off.setChecked(True)
    radio_neve_off.setChecked(True)
    radio_discharge_off.setChecked(True)
    global msg
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle("Simulazione")
    msg.setText("Reimpostati i dati meteo originari")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.show()


#applica i nuovi dati meteo e ricalcola le funzioni cdf (failure) dopo la modifica dei parametri meteo nel box simulazione
def applica_dati_simulazione():
    if (radio_temp_off.isChecked()==True) and (radio_vento_off.isChecked()==True) and (radio_precip_off.isChecked()==True) and (radio_neve_off.isChecked()==True) and\
       (radio_pioggia_off.isChecked()==True) and (radio_ghiaccio_jones_off.isChecked()==True) and (radio_ghiaccio_nojones_off.isChecked()==True) and\
        radio_discharge_off.isChecked()==True:
        slider_temp.setValue(0);slider_vento.setValue(0);slider_precip.setValue(0);slider_neve.setValue(0); slider_pioggia.setValue(0); slider_discharge.setValue(0)
        combobox_jones_ore.setCurrentText('1');combobox_jones_M.setCurrentText('15');combobox_nojones_m.setCurrentText('1');combobox_nojones_M.setCurrentText('15')
        radio_temp_off.setChecked(True)
        radio_vento_off.setChecked(True)
        radio_pioggia_off.setChecked(True)
        radio_precip_off.setChecked(True)
        radio_neve_off.setChecked(True)
        radio_discharge_off.setChecked(True)
        global msg
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Simulazione")
        msg.setText("Nessuna modifica apportata. Selezionare All o Delta.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
    else:
        geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
        num_rows = len(geo_dataframe_corrente)
        alert_precip=0
        alert_pioggia=0
        alert_vento=0
        alert_neve=0
        alert_ghiaccio=0
        alert_discharge=0
        for i in range(0,num_rows):
            if (radio_temp_all.isChecked()==True):
               geo_dataframe_corrente.at[i,'temperature_2m_max']=float(slider_temp.value())
               geo_dataframe_corrente.at[i,'hwdi']=calcola_hwdi(geo_dataframe_corrente.at[i,'temperature_2m_max'],geo_dataframe_corrente.at[i,'precipitation_sum'])
               geo_dataframe_corrente.at[i,'hwdi_HM']=geo_dataframe_corrente.at[i,'hwdi']/14
               geo_dataframe_corrente.at[i,'tp65']=calcola_tp65(geo_dataframe_corrente.at[i,'temperature_2m_max'])
               geo_dataframe_corrente.at[i,'td65']=calcola_td65(geo_dataframe_corrente.at[i,'temperature_2m_max'])
            if (radio_temp_delta.isChecked()==True):
               geo_dataframe_corrente.at[i,'temperature_2m_max']=geo_dataframe_corrente.at[i,'temperature_2m_max']+float(slider_temp.value())
               geo_dataframe_corrente.at[i,'hwdi']=calcola_hwdi(geo_dataframe_corrente.at[i,'temperature_2m_max'],geo_dataframe_corrente.at[i,'precipitation_sum'])
               geo_dataframe_corrente.at[i,'hwdi_HM']=geo_dataframe_corrente.at[i,'hwdi']/14
               geo_dataframe_corrente.at[i,'tp65']=calcola_tp65(geo_dataframe_corrente.at[i,'temperature_2m_max'])
               geo_dataframe_corrente.at[i,'td65']=calcola_td65(geo_dataframe_corrente.at[i,'temperature_2m_max'])
            if (radio_vento_all.isChecked()==True):
               geo_dataframe_corrente.at[i,'wind_speed_10m_max']=float(slider_vento.value())
               if (geo_dataframe_corrente.at[i,'wind_speed_10m_max'])<0:
                   geo_dataframe_corrente.at[i,'wind_speed_10m_max']=0
                   alert_vento=1
               geo_dataframe_corrente.at[i,'prob_tralicci']=calcola_prob_tralicci(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_linea_esterna']=calcola_prob_linea_esterna(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_la_nuovi']=calcola_prob_pali_legnoacciaio_nuovi(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_l_20']=calcola_prob_pali_legno_20(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_l_40']=calcola_prob_pali_legno_40(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_l_60']=calcola_prob_pali_legno_60(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
            if (radio_vento_delta.isChecked()==True):
               geo_dataframe_corrente.at[i,'wind_speed_10m_max']=geo_dataframe_corrente.at[i,'wind_speed_10m_max']+float(slider_vento.value())
               if (geo_dataframe_corrente.at[i,'wind_speed_10m_max'])<0:
                   geo_dataframe_corrente.at[i,'wind_speed_10m_max']=0
                   alert_vento=1
               geo_dataframe_corrente.at[i,'prob_tralicci']=calcola_prob_tralicci(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_linea_esterna']=calcola_prob_linea_esterna(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_la_nuovi']=calcola_prob_pali_legnoacciaio_nuovi(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_l_20']=calcola_prob_pali_legno_20(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_l_40']=calcola_prob_pali_legno_40(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
               geo_dataframe_corrente.at[i,'prob_pali_l_60']=calcola_prob_pali_legno_60(geo_dataframe_corrente.at[i,'wind_speed_10m_max'])
            if (radio_pioggia_all.isChecked()==True):
               geo_dataframe_corrente.at[i,'rain_sum']=float(slider_pioggia.value())
               if (geo_dataframe_corrente.at[i,'rain_sum'])<0:
                   geo_dataframe_corrente.at[i,'rain_sum']=0
                   alert_pioggia=1
            if (radio_pioggia_delta.isChecked()==True):
               geo_dataframe_corrente.at[i,'rain_sum']=geo_dataframe_corrente.at[i,'rain_sum']+float(slider_pioggia.value())
               if (geo_dataframe_corrente.at[i,'rain_sum'])<0:
                   geo_dataframe_corrente.at[i,'rain_sum']=0
                   alert_pioggia=1
            if (radio_precip_all.isChecked()==True):
               geo_dataframe_corrente.at[i,'precipitation_sum']=float(slider_precip.value())
               if (geo_dataframe_corrente.at[i,'precipitation_sum'])<0:
                   geo_dataframe_corrente.at[i,'precipitation_sum']=0
                   alert_precip=1
               geo_dataframe_corrente.at[i,'hwdi']=calcola_hwdi(geo_dataframe_corrente.at[i,'temperature_2m_max'],geo_dataframe_corrente.at[i,'precipitation_sum'])
               geo_dataframe_corrente.at[i,'hwdi_HM']=geo_dataframe_corrente.at[i,'hwdi']/14
            if (radio_precip_delta.isChecked()==True):
               geo_dataframe_corrente.at[i,'precipitation_sum']=geo_dataframe_corrente.at[i,'precipitation_sum']+float(slider_precip.value())
               if (geo_dataframe_corrente.at[i,'precipitation_sum'])<0:
                   geo_dataframe_corrente.at[i,'precipitation_sum']=0
                   alert_precip=1
               geo_dataframe_corrente.at[i,'hwdi']=calcola_hwdi(geo_dataframe_corrente.at[i,'temperature_2m_max'],geo_dataframe_corrente.at[i,'precipitation_sum'])
               geo_dataframe_corrente.at[i,'hwdi_HM']=geo_dataframe_corrente.at[i,'hwdi']/14
            if (radio_neve_all.isChecked()==True):
               geo_dataframe_corrente.at[i,'snowfall_sum']=float(slider_neve.value())
               if (geo_dataframe_corrente.at[i,'snowfall_sum'])<0:
                   geo_dataframe_corrente.at[i,'snowfall_sum']=0
                   alert_neve=1
            if (radio_neve_delta.isChecked()==True):
               geo_dataframe_corrente.at[i,'snowfall_sum']=geo_dataframe_corrente.at[i,'snowfall_sum']+float(slider_precip.value())
               if (geo_dataframe_corrente.at[i,'snowfall_sum'])<0:
                   geo_dataframe_corrente.at[i,'snowfall_sum']=0
                   alert_neve=1
            if (radio_ghiaccio_jones_off.isChecked()!=True and radio_ghiaccio_nojones_off.isChecked()!=True): alert_ghiaccio=1
            else:
                if (radio_ghiaccio_jones_delta.isChecked()==True):
                    if (geo_dataframe_corrente.at[i,'weather_code']==56 or geo_dataframe_corrente.at[i,'weather_code']==57 or \
                        geo_dataframe_corrente.at[i,'weather_code']==66 or geo_dataframe_corrente.at[i,'weather_code']==67):
                             geo_dataframe_corrente.at[i,'precipitation_hours']=int(combobox_jones_ore.currentText())
                             geo_dataframe_corrente.at[i,'M_mm']=int(combobox_jones_M.currentText())
                             geo_dataframe_corrente.at[i,'m_mm']=calcola_stima_m_ice(geo_dataframe_corrente.at[i,'weather_code'], 
                                                                                geo_dataframe_corrente.at[i,'precipitation_hours'], 
                                                                                geo_dataframe_corrente.at[i,'wind_speed_10m_max'], 
                                                                                geo_dataframe_corrente.at[i,'precipitation_sum'])
                             geo_dataframe_corrente.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(geo_dataframe_corrente.at[i,'m_mm'],geo_dataframe_corrente.at[i,'M_mm'])
                if (radio_ghiaccio_jones_all.isChecked()==True):
                             geo_dataframe_corrente.at[i,'weather_code']=56
                             geo_dataframe_corrente.at[i,'precipitation_hours']=int(combobox_jones_ore.currentText())
                             geo_dataframe_corrente.at[i,'M_mm']=int(combobox_jones_M.currentText())
                             geo_dataframe_corrente.at[i,'m_mm']=calcola_stima_m_ice(geo_dataframe_corrente.at[i,'weather_code'], 
                                                                                geo_dataframe_corrente.at[i,'precipitation_hours'], 
                                                                                geo_dataframe_corrente.at[i,'wind_speed_10m_max'], 
                                                                                geo_dataframe_corrente.at[i,'precipitation_sum'])
                             geo_dataframe_corrente.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(geo_dataframe_corrente.at[i,'m_mm'],geo_dataframe_corrente.at[i,'M_mm'])
                if (radio_ghiaccio_nojones_all.isChecked()==True):
                        geo_dataframe_corrente.at[i,'weather_code']=56
                        geo_dataframe_corrente.at[i,'M_mm']=int(combobox_nojones_M.currentText())
                        geo_dataframe_corrente.at[i,'m_mm']=int(combobox_nojones_m.currentText())
                        geo_dataframe_corrente.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(geo_dataframe_corrente.at[i,'m_mm'],geo_dataframe_corrente.at[i,'M_mm'])
                
                if (radio_ghiaccio_nojones_delta.isChecked()==True):
                   if (geo_dataframe_corrente.at[i,'weather_code']==56 or geo_dataframe_corrente.at[i,'weather_code']==57 or \
                        geo_dataframe_corrente.at[i,'weather_code']==66 or geo_dataframe_corrente.at[i,'weather_code']==67):
                             geo_dataframe_corrente.at[i,'M_mm']=int(combobox_nojones_M.currentText())
                             geo_dataframe_corrente.at[i,'m_mm']=int(combobox_nojones_m.currentText())
                             geo_dataframe_corrente.at[i,'prob_linea_esterna_ice']=calcola_prob_linea_esterna_ice(geo_dataframe_corrente.at[i,'m_mm'],geo_dataframe_corrente.at[i,'M_mm']) 
            if (radio_discharge_all.isChecked()==True):
                geo_dataframe_corrente.at[i,'river_discharge']=float(slider_discharge.value())
                if (geo_dataframe_corrente.at[i,'river_discharge'])<0:
                      geo_dataframe_corrente.at[i,'river_discharge']=0
                      alert_discharge=1
                geo_dataframe_corrente.at[i,'flood_depth']=calcola_flood_depth(geo_dataframe_corrente.at[i,'flood_warning'],geo_dataframe_corrente.at[i,'river_discharge'],geo_dataframe_corrente.at[i,'ts_discharge'],geo_dataframe_corrente.at[i,'flood_factor'])
                geo_dataframe_corrente.at[i,'flood_risk_cabina']=calcola_flood_failure_cabina(geo_dataframe_corrente.at[i,'flood_depth'])

            if (radio_discharge_delta.isChecked()==True):
                geo_dataframe_corrente.at[i,'river_discharge']=geo_dataframe_corrente.at[i,'river_discharge']+float(slider_discharge.value())
                if (geo_dataframe_corrente.at[i,'river_discharge'])<0:
                      geo_dataframe_corrente.at[i,'river_discharge']=0
                      alert_discharge=1
                geo_dataframe_corrente.at[i,'flood_depth']=calcola_flood_depth(geo_dataframe_corrente.at[i,'flood_warning'],geo_dataframe_corrente.at[i,'river_discharge'],geo_dataframe_corrente.at[i,'ts_discharge'],geo_dataframe_corrente.at[i,'flood_factor'])
                geo_dataframe_corrente.at[i,'flood_risk_cabina']=calcola_flood_failure_cabina(geo_dataframe_corrente.at[i,'flood_depth'])

        geo_dataframe_corrente.to_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
        geo_dataframe_corrente.to_excel('./conf/analisi_corrente/geo_dataframe_base.xlsx')
        radio_temp_off.setChecked(True)
        radio_vento_off.setChecked(True)
        radio_pioggia_off.setChecked(True)
        radio_precip_off.setChecked(True)
        radio_neve_off.setChecked(True)
        radio_discharge_off.setChecked(True)
        slider_precip.setValue(0)
        slider_pioggia.setValue(0)
        slider_vento.setValue(0)
        slider_temp.setValue(0)
        slider_neve.setValue(0)
        slider_discharge.setValue(0)
        combobox_jones_ore.setCurrentText('1')
        combobox_jones_M.setCurrentText('15')
        radio_ghiaccio_jones_off.setChecked(True)
        combobox_nojones_m.setCurrentText('1')
        combobox_nojones_M.setCurrentText('15')
        radio_ghiaccio_nojones_off.setChecked(True)
        if (alert_precip==1):
            global msg_alert_precip
            msg_alert_precip = QMessageBox()
            msg_alert_precip.setIcon(QMessageBox.Icon.Information)
            msg_alert_precip.setWindowTitle("Simulazione")
            msg_alert_precip.setText("Le precipitazioni non possono essere minori di 0 mm. I valori negativi sono stati valorizzati a 0 mm")
            msg_alert_precip.setStandardButtons(QMessageBox.Ok)
            msg_alert_precip.show()
        if (alert_vento==1):
            global msg_alert_vento
            msg_alert_vento = QMessageBox()
            msg_alert_vento.setIcon(QMessageBox.Icon.Information)
            msg_alert_vento.setWindowTitle("Simulazione")
            msg_alert_vento.setText("Il vento non può essere minore di 0 m/s. I valori negativi sono stati valorizzati a 0 m/s")
            msg_alert_vento.setStandardButtons(QMessageBox.Ok)
            msg_alert_vento.show()
        if (alert_pioggia==1):
            global msg_alert_pioggia
            msg_alert_pioggia = QMessageBox()
            msg_alert_pioggia.setIcon(QMessageBox.Icon.Information)
            msg_alert_pioggia.setWindowTitle("Simulazione")
            msg_alert_pioggia.setText("La pioggia non può essere minore di 0 mm. I valori negativi sono stati valorizzati a 0 mm")
            msg_alert_pioggia.setStandardButtons(QMessageBox.Ok)
            msg_alert_pioggia.show()
        if (alert_neve==1):
            global msg_alert_neve
            msg_alert_neve = QMessageBox()
            msg_alert_neve.setIcon(QMessageBox.Icon.Information)
            msg_alert_neve.setWindowTitle("Simulazione")
            msg_alert_neve.setText("La neve non può essere minore di 0 mm. I valori negativi sono stati valorizzati a 0 mm")
            msg_alert_neve.setStandardButtons(QMessageBox.Ok)
            msg_alert_neve.show()
        if (alert_ghiaccio==1):
            global msg_alert_ghiaccio
            msg_alert_ghiaccio = QMessageBox()
            msg_alert_ghiaccio.setIcon(QMessageBox.Icon.Information)
            msg_alert_ghiaccio.setWindowTitle("Simulazione")
            msg_alert_ghiaccio.setText("Attivare ice(Jones) o Ice, non entrambi")
            msg_alert_ghiaccio.setStandardButtons(QMessageBox.Ok)
            msg_alert_ghiaccio.show()
        if (alert_discharge==1):
            global msg_alert_discharge
            msg_alert_discharge = QMessageBox()
            msg_alert_discharge.setIcon(QMessageBox.Icon.Information)
            msg_alert_discharge.setWindowTitle("Simulazione")
            msg_alert_discharge.setText("La portata non può essere minore di 0 mc/s. I valori negativi sono stati valorizzati a 0 mc/s")
            msg_alert_discharge.setStandardButtons(QMessageBox.Ok)
            msg_alert_discharge.show()
        else:
            global msg_modifiche_ok
            msg_modifiche_ok = QMessageBox()
            msg_modifiche_ok.setIcon(QMessageBox.Icon.Information)
            msg_modifiche_ok.setWindowTitle("Simulazione")
            msg_modifiche_ok.setText("Dati modificati")
            msg_modifiche_ok.setStandardButtons(QMessageBox.Ok)
            msg_modifiche_ok.show()
    
        
#se il weather code corrisponde a piogge del tipo FREEZING, calcola la stima dello spessore del ghiaccio accumulato 
# sulle linee (tickness) con la formula di Jones. 
def calcola_stima_m_ice(cod_meteo, ore_freezing, vento, precipitazioni):
   if (cod_meteo==56 or cod_meteo==57 or cod_meteo==66 or cod_meteo==67) and precipitazioni>0:
      precipitation_rate=precipitazioni/ore_freezing
      di=0.9 #densità ghiaccio
      pi_greco=3.1415
      dw=1 #densità acqua
      lwc=0.067*(pow(precipitation_rate,0.846)) #liquid water content
      stima_m_ice=round((ore_freezing/(precipitation_rate/(di*pi_greco)))*math.sqrt(pow((precipitation_rate*dw),2)+pow((3.6+vento*lwc),2)))
   else:
      stima_m_ice=0
   return stima_m_ice

#calcola l'altezza dell'alluvione (solo se si tratta di una zona pericolosa, la portata non è nulla, è maggiore di zero ed è maggiore
#della soglia esondazione e la soglia esondazione non è zero)
def calcola_flood_depth(flood_pericolo,river_discharge, ts_discharge, flood_factor):
    if (flood_pericolo==0) or (river_discharge==0) or (river_discharge<=ts_discharge) or (ts_discharge==0) or (math.isnan(river_discharge)==True): 
        return 0
    else:
        var_percentuale=tronca((((river_discharge-ts_discharge)/ts_discharge)*100),0)
        flood=tronca((flood_factor*var_percentuale),1)
        return flood

#aggiorna le label degli slider con i nuovi valori 
def cambia_label_slider_temp():
    label_slider_temp.setText(str(slider_temp.value()))

def cambia_label_slider_vento():
    label_slider_vento.setText(str(slider_vento.value()))

def cambia_label_slider_pioggia():
    label_slider_pioggia.setText(str(slider_pioggia.value()))

def cambia_label_slider_precip():
    label_slider_precip.setText(str(slider_precip.value()))

def cambia_label_slider_neve():
    label_slider_neve.setText(str(slider_neve.value()))
    
def cambia_label_slider_discharge():
    label_slider_discharge.setText(str(slider_discharge.value()))



#########################################  INIZIO FUNZIONI CDF #############################################

def calcola_hwdi(temperatura, precipitazioni):
    hwdi=0
    if temperatura>33:
        hwdi=hwdi+1
    if precipitazioni==0:
        hwdi=hwdi+1
    return (hwdi)


def calcola_prob_tralicci(vento):
     mu= 80
     sd = 16
     v_critical=45
     v_collapse=150
     curva = lognorm(sd / mu, scale=mu)
     if vento<v_critical:
       prob_tralicci=0
     elif vento>=v_collapse:   
        prob_tralicci=1
     else:   
        prob_tralicci=curva.cdf(vento)
     return round(prob_tralicci*100)

def calcola_prob_linea_esterna(vento):
     mu= 40
     sd = 5
     v_critical=30
     v_collapse=60
     curva = lognorm(sd / mu, scale=mu)
     if vento<v_critical:
       prob_linea_esterna=0
     elif vento>=v_collapse:   
        prob_linea_esterna=1
     else:   
        prob_linea_esterna=curva.cdf(vento)
     return round(prob_linea_esterna*100)

def calcola_prob_linea_esterna_ice(m_mm,M_mm):
    if m_mm <= M_mm:
        prob_ice = 0
    elif m_mm >= (M_mm*5):
        prob_ice = 1
    else: 
        prob_ice = math.exp((0.6931*(m_mm-M_mm))/(4*M_mm))-1
    return int(round(prob_ice*100))

def calcola_prob_pali_legnoacciaio_nuovi(vento):
     mu= 58
     sd = 7
     v_critical=40
     v_collapse=80
     curva = lognorm(sd / mu, scale=mu)
     if vento<v_critical:
       prob_linea_pali=0
     elif vento>=v_collapse:   
        prob_linea_pali=1
     else:   
        prob_linea_pali=curva.cdf(vento)
     return round(prob_linea_pali*100)

def calcola_prob_pali_legno_20(vento):
     mu= 55
     sd = 4.5
     v_critical=36
     v_collapse=72
     curva = lognorm(sd / mu, scale=mu)
     if vento<v_critical:
       prob_linea_pali=0
     elif vento>=v_collapse:   
        prob_linea_pali=1
     else:   
        prob_linea_pali=curva.cdf(vento)
     return round(prob_linea_pali*100)

def calcola_prob_pali_legno_40(vento):
     mu= 42
     sd = 5
     v_critical=27
     v_collapse=60
     curva = lognorm(sd / mu, scale=mu)
     if vento<v_critical:
       prob_linea_pali=0
     elif vento>=v_collapse:   
        prob_linea_pali=1
     else:   
        prob_linea_pali=curva.cdf(vento)
     return round(prob_linea_pali*100)

def calcola_prob_pali_legno_60(vento):
     mu= 28
     sd = 5
     v_critical=17
     v_collapse=50
     curva = lognorm(sd / mu, scale=mu)
     if vento<v_critical:
       prob_linea_pali=0
     elif vento>=v_collapse:   
        prob_linea_pali=1
     else:   
        prob_linea_pali=curva.cdf(vento)
     return round(prob_linea_pali*100)

def calcola_tp65(temperatura):
     if temperatura<=30:
       percentuale_riduzione_vita=0              
     else:   
       esponente=(6972.15/(353+temperatura))-13.391
       decadimento_anni=(10**esponente)/8760
       percentuale_riduzione_vita=tronca(((7.4-decadimento_anni)/7.4)*100, 1)
     return round(percentuale_riduzione_vita)

def calcola_td65(temperatura):
     if temperatura<=30:
       percentuale_riduzione_vita=0              
     else:   
       esponente=(6328.80/(353+temperatura))-11.269
       decadimento_anni=(10**esponente)/8760
       percentuale_riduzione_vita=tronca(((20.5-decadimento_anni)/20.5)*100, 1)
     return round(percentuale_riduzione_vita)

def calcola_flood_failure_cabina(flood_depth):
     mu= 150
     sd = 28
     v_critical=50
     v_collapse=250
     curva = lognorm(sd / mu, scale=mu)
     if flood_depth<v_critical:
       prob_flood_cabina=0
     elif flood_depth>=v_collapse:   
        prob_flood_cabina=1
     else:   
        prob_flood_cabina=curva.cdf(flood_depth)
     return round(prob_flood_cabina*100)


#########################################  FINE FUNZIONI CDF  #############################################











#########################################  INIZIO FUNZIONI API  ########################################## 


#ECMWF Weather Forecast, modello IFS025, risoluzione 0.25 gradi, 7gg (da https://open-meteo.com)    
def api_025_ifs(lat, lon):
    import openmeteo_requests
    import requests_cache
    import pandas as pd
    from retry_requests import retry
    cache_session = requests_cache.CachedSession('.cache.sqlite', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": lat,
	"longitude": lon,
	"daily": ["temperature_2m_max", "wind_speed_10m_max", "snowfall_sum", "rain_sum", "precipitation_sum","weather_code", "precipitation_hours"],
	"models": "ecmwf_ifs025",
	"timezone": "auto",
	"wind_speed_unit": "ms"
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(1).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(2).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(3).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(4).ValuesAsNumpy()
    daily_weather_code=daily.Variables(5).ValuesAsNumpy()
    daily_precipitation_hours=daily.Variables(6).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
    )}    
    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["snowfall_sum"] = daily_snowfall_sum
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_data["weather_code"]=daily_weather_code
    daily_data["precipitation_hours"]=daily_precipitation_hours
    quota=response.Elevation()        
    return daily_data, quota

#German weather service DWD, modello ICON GLOBAL, risoluzione 0.1 gradi, 7gg (da https://open-meteo.com)
def api_01_dwd_global(lat, lon):
    import openmeteo_requests
    import requests_cache
    import pandas as pd
    from retry_requests import retry
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": lat,
	"longitude": lon,
	"daily": ["temperature_2m_max", "wind_speed_10m_max", "snowfall_sum", "rain_sum", "precipitation_sum","weather_code", "precipitation_hours"],
	"models": "icon_global",
	"timezone": "auto",
	"wind_speed_unit": "ms"
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(1).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(2).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(3).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(4).ValuesAsNumpy()
    daily_weather_code=daily.Variables(5).ValuesAsNumpy()
    daily_precipitation_hours=daily.Variables(6).ValuesAsNumpy()
    
    daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
    )}    
    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["snowfall_sum"] = daily_snowfall_sum
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_data["weather_code"]=daily_weather_code
    daily_data["precipitation_hours"]=daily_precipitation_hours
    quota=response.Elevation()        
    return daily_data, quota


#GLOFas v4 Forecast, risoluzione 0.05 gradi, 3gg (da https://open-meteo.com/en/docs/flood-api)
def api_005_glofas_v4(lat, lon):
    import openmeteo_requests
    import pandas as pd
    import requests_cache
    from retry_requests import retry
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    url = "https://flood-api.open-meteo.com/v1/flood"
    params = {
	"latitude": lat,
	"longitude": lon,
	"daily": "river_discharge",
	"models": "forecast_v4",
	"timezone": "auto",
	"forecast_days": 3
}
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()
    daily_river_discharge = daily.Variables(0).ValuesAsNumpy()
    daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left" )}

    daily_data["river_discharge"] = daily_river_discharge    
    daily_dataframe = pd.DataFrame(data = daily_data)
    return daily_data


#Italia Meteo ARPAE, modello ICON 2i, risoluzione 0.02 gradi, 3gg (da https://open-meteo.com)
def api_002_arpae_icon_2i(lat, lon):
    import openmeteo_requests
    import requests_cache
    import pandas as pd
    from retry_requests import retry
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": lat,
	"longitude": lon,
	"daily": ["temperature_2m_max", "wind_speed_10m_max", "snowfall_sum", "rain_sum", "precipitation_sum","weather_code", "precipitation_hours"],
	"models": "italia_meteo_arpae_icon_2i",
	"timezone": "auto",
	"wind_speed_unit": "ms"
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(1).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(2).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(3).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(4).ValuesAsNumpy()
    daily_weather_code=daily.Variables(5).ValuesAsNumpy()
    daily_precipitation_hours=daily.Variables(6).ValuesAsNumpy()
    
    daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
    )}    
    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["snowfall_sum"] = daily_snowfall_sum
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_data["weather_code"]=daily_weather_code
    daily_data["precipitation_hours"]=daily_precipitation_hours
    quota=response.Elevation()        
    return daily_data, quota


#########################################  FINE FUNZIONI API  ##########################################




################################### FUNZIONI CARICA IMMAGINE RISCHIO (box rischio in alto a dx) 
def carica_immagine_rischio_default():
    img_rischio.setDisabled(True)
    pixmap = QPixmap('./conf/img/transmission-tower.ico')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_vento_tralicci():
    img_rischio.setDisabled(False)
    pixmap = QPixmap('./conf/img/cdf_vento_tralicci.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_heat_wave():
    img_rischio.setDisabled(False)
    pixmap = QPixmap('./conf/img/hw_ondata_calore.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_vento_linea_esterna():
    img_rischio.setDisabled(False)
    pixmap = QPixmap('./conf/img/cdf_vento_linea_esterna.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

#la cdf del ghiaccio non è statica per cui dev'essere generata di volta in volta in base ai valori di m e M
def carica_immagine_rischio_ghiaccio_linea_esterna():
    img_rischio.setDisabled(False)
    geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    M=geo_dataframe_corrente.at[1,'M_mm']
    g = np.linspace(0, (M*5)+M, (M*5)+M)
    elementi=g.size
    y=np.array(['0.0'] * elementi, dtype='float')
    for i in range(elementi):
       if g[i]<=M:
          y[i]=0
       elif g[i]>=(M*5):   
          y[i]=1
       else:      
          y[i] = math.exp((0.6931*(g[i]-M))/(4*M)) -1
    plt.clf()
    plt.plot(g, y, color = 'blue')
    plt.grid()
    plt.title("curva fragilità ghiaccio")
    plt.xlabel("mm ghiaccio")
    plt.ylabel("probabilità guasto")
    plt.savefig('./conf/img/cdf_ghiaccio.png')
    pixmap = QPixmap('./conf/img/cdf_ghiaccio.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setScaledContents(True)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_vento_pali(tipo_palo, pali_anni):
    img_rischio.setDisabled(False)
    if (tipo_palo=="legno_acciaio" and pali_anni==0): pixmap = QPixmap('./conf/img/cdf_pali_0.png')
    if (tipo_palo=="legno" and pali_anni==20):pixmap = QPixmap('./conf/img/cdf_pali_20.png')
    if (tipo_palo=="legno" and pali_anni==40):pixmap = QPixmap('./conf/img/cdf_pali_40.png')
    if (tipo_palo=="legno" and pali_anni==60):pixmap = QPixmap('./conf/img/cdf_pali_60.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setScaledContents(True)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_heat_wave_trasformatore_p():
    img_rischio.setDisabled(False)
    pixmap = QPixmap('./conf/img/tp65rise.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_heat_wave_trasformatore_d():
    img_rischio.setDisabled(False)
    pixmap = QPixmap('./conf/img/td65rise.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

def carica_immagine_rischio_alluvione_cabine():
    img_rischio.setDisabled(False)
    pixmap = QPixmap('./conf/img/cdf_flood_cabine.png')
    logoLabel.setPixmap(pixmap)
    logoLabel.setFixedHeight(280)
    logoLabel.setFixedWidth(280)

################################### FINE FUNZIONI CARICA IMMAGINE RISCHIO (box rischio in alto a dx)





################################## FUNZIONI ABILITA/DISABILITA OGGETTI GUI  ##########################

def abilita_elabora_scenario():
    analisi.setDisabled(False)
    simulazione.setDisabled(False)    
    opzioni.setDisabled(False)
    dato_meteo.setDisabled(False)
    componente.setDisabled(True)
    img_rischio.setDisabled(True)
    toolbar_pulsante_salva_scenario.setDisabled(False)
    toolbar_pulsante_chiudi_scenario.setDisabled(False)
    toolbar_pulsante_dataframe_excel.setDisabled(False)
    toolbar_pulsante_elabora_scenario.setDisabled(False)
    geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    if(geo_dataframe_corrente.columns[31]=="poligono_002"):
        toolbar_pulsante_ricarica_soglie.setDisabled(False)#abilita il caricamento delle soglie discharge        
        radio_ghiaccio_jones_all.setDisabled(True)#disabilita tutte le funzionalità ghiaccio
        radio_ghiaccio_jones_delta.setDisabled(True)
        radio_ghiaccio_jones_off.setDisabled(True)
        label_ghiaccio_jones.setDisabled(True)
        label_ghiaccio_jones_M.setDisabled(True)
        label_ghiaccio_jones_ore.setDisabled(True)
        combobox_jones_M.setDisabled(True)
        combobox_jones_ore.setDisabled(True)
        radio_ghiaccio_nojones_all.setDisabled(True)
        radio_ghiaccio_nojones_delta.setDisabled(True)
        radio_ghiaccio_nojones_off.setDisabled(True)
        label_ghiaccio_nojones.setDisabled(True)
        label_ghiaccio_nojones_M.setDisabled(True)
        label_ghiaccio_nojones_m.setDisabled(True)
        combobox_nojones_M.setDisabled(True)
        combobox_nojones_m.setDisabled(True)
        radio_discharge_all.setDisabled(False)#abilita tutte le funzionalità discharge
        radio_discharge_delta.setDisabled(False)
        radio_discharge_off.setDisabled(False)
        label_discharge.setDisabled(False)
        slider_discharge.setDisabled(False)
        label_slider_discharge.setDisabled(False)
        radio_dato_discharge.setDisabled(False)
    else:
        toolbar_pulsante_ricarica_soglie.setDisabled(True)#disabilita il caricamento delle soglie discharge        
        radio_ghiaccio_jones_all.setDisabled(False)#abilita tutte le funzionalità ghiaccio
        radio_ghiaccio_jones_delta.setDisabled(False)
        radio_ghiaccio_jones_off.setDisabled(False)
        label_ghiaccio_jones.setDisabled(False)
        label_ghiaccio_jones_M.setDisabled(False)
        label_ghiaccio_jones_ore.setDisabled(False)
        combobox_jones_M.setDisabled(False)
        combobox_jones_ore.setDisabled(False)
        radio_ghiaccio_nojones_all.setDisabled(False)
        radio_ghiaccio_nojones_delta.setDisabled(False)
        radio_ghiaccio_nojones_off.setDisabled(False)
        label_ghiaccio_nojones.setDisabled(False)
        label_ghiaccio_nojones_M.setDisabled(False)
        label_ghiaccio_nojones_m.setDisabled(False)
        combobox_nojones_M.setDisabled(False)
        combobox_nojones_m.setDisabled(False)
        radio_discharge_all.setDisabled(True)#disabilita tutte le funzionalità discharge
        radio_discharge_delta.setDisabled(True)
        radio_discharge_off.setDisabled(True)
        label_discharge.setDisabled(True)
        slider_discharge.setDisabled(True)
        label_slider_discharge.setDisabled(True)
        radio_dato_discharge.setDisabled(True)

    toolbar_pulsante_salva_mappa.setDisabled(False)
    radio_analisi_meteo.setChecked(True)
    radio_dato_temp.setChecked(True)
    radio_evento_hw.setChecked(True)
    radio_componente_linea_interrata.setChecked(True)
    radio_analisi_meteo.toggled.connect(attiva_solo_meteo)
    radio_analisi_rischio.toggled.connect(attiva_analisi_rischio)    
    pulsante_elabora_modello.setDisabled(False)
    toolbar_pulsante_scarica_dati_meteo_025.setDisabled(True)
    toolbar_pulsante_scarica_dati_meteo_01.setDisabled(True)
    toolbar_pulsante_scarica_dati_meteo_002.setDisabled(True)
    toolbar_combobox_scarica_dati_meteo_002_seleziona_provincia.setDisabled(True)
    bar.setValue(0)
    
def attiva_analisi_rischio():
    opzioni.setDisabled(False)
    dato_meteo.setDisabled(True)
    evento_naturale.setDisabled(False)
    componente.setDisabled(False)
    radio_componente_tralicci.setChecked(False)
    radio_componente_tralicci.setDisabled(True)
    radio_componente_linea_esterna.setChecked(False)
    radio_componente_linea_esterna.setDisabled(True)
    radio_componente_linea_interrata.setChecked(True)
    radio_componente_linea_interrata.setDisabled(False)
    radio_componente_pali.setChecked(False)
    radio_componente_pali.setDisabled(True)
    radio_componente_trasformatore_p.setChecked(False)
    radio_componente_trasformatore_p.setDisabled(False)
    radio_componente_trasformatore_d.setChecked(False)
    radio_componente_trasformatore_d.setDisabled(False)
    radio_componente_cabina_primaria.setDisabled(True)
    radio_evento_hw.toggled.connect(attiva_hw)
    radio_evento_vento.toggled.connect(attiva_vento)
    radio_evento_ghiaccio.toggled.connect(attiva_ghiaccio)
    radio_evento_alluvione.toggled.connect(attiva_alluvione)
    
    geo_dataframe_corrente = gpd.read_feather('./conf/analisi_corrente/geo_dataframe_base.feather')
    if(geo_dataframe_corrente.columns[31]=="poligono_002"):
        radio_evento_alluvione.setDisabled(False)
        radio_evento_ghiaccio.setDisabled(True)
    else:
        radio_evento_alluvione.setDisabled(True)
        radio_evento_ghiaccio.setDisabled(False)
    

def attiva_solo_meteo():
    opzioni.setDisabled(False)
    dato_meteo.setDisabled(False)
    radio_dato_temp.setChecked(True)
    radio_evento_hw.setChecked(True)
    radio_componente_linea_interrata.setChecked(True)
    radio_componente_trasformatore_p.setChecked(True)
    radio_componente_trasformatore_d.setChecked(True)
    radio_componente_linea_interrata.setChecked(True)
    evento_naturale.setDisabled(True)
    componente.setDisabled(True)


def attiva_hw():
    radio_componente_tralicci.setChecked(False)
    radio_componente_tralicci.setDisabled(True)
    radio_componente_linea_esterna.setChecked(False)
    radio_componente_linea_esterna.setDisabled(True)
    radio_componente_linea_interrata.setChecked(True)
    radio_componente_linea_interrata.setDisabled(False)
    radio_componente_pali.setChecked(False)
    radio_componente_pali.setDisabled(True)
    radio_componente_trasformatore_p.setChecked(False)
    radio_componente_trasformatore_p.setDisabled(False)
    radio_componente_trasformatore_d.setChecked(False)
    radio_componente_trasformatore_d.setDisabled(False)
    radio_componente_cabina_primaria.setDisabled(True)

def attiva_vento():
    radio_componente_tralicci.setChecked(True)
    radio_componente_tralicci.setDisabled(False)
    radio_componente_linea_esterna.setChecked(False)
    radio_componente_linea_esterna.setDisabled(False)
    radio_componente_linea_interrata.setChecked(False)
    radio_componente_linea_interrata.setDisabled(True)
    radio_componente_pali.setChecked(False)
    radio_componente_pali.setDisabled(False)
    radio_componente_trasformatore_p.setChecked(False)
    radio_componente_trasformatore_p.setDisabled(True)
    radio_componente_trasformatore_d.setChecked(False)
    radio_componente_trasformatore_d.setDisabled(True)
    radio_componente_cabina_primaria.setDisabled(True)

def attiva_ghiaccio():
    radio_componente_tralicci.setChecked(False)
    radio_componente_tralicci.setDisabled(True)
    radio_componente_linea_esterna.setChecked(True)
    radio_componente_linea_esterna.setDisabled(False)
    radio_componente_linea_interrata.setChecked(False)
    radio_componente_linea_interrata.setDisabled(True)
    radio_componente_pali.setChecked(False)
    radio_componente_pali.setDisabled(True)
    radio_componente_trasformatore_p.setChecked(False)
    radio_componente_trasformatore_p.setDisabled(True)
    radio_componente_trasformatore_d.setChecked(False)
    radio_componente_trasformatore_d.setDisabled(True)
    radio_componente_cabina_primaria.setDisabled(True)
    
def attiva_alluvione():
    radio_componente_tralicci.setChecked(False)
    radio_componente_tralicci.setDisabled(True)
    radio_componente_linea_esterna.setChecked(False)
    radio_componente_linea_esterna.setDisabled(True)
    radio_componente_linea_interrata.setChecked(False)
    radio_componente_linea_interrata.setDisabled(True)
    radio_componente_pali.setChecked(False)
    radio_componente_pali.setDisabled(True)
    radio_componente_trasformatore_p.setChecked(False)
    radio_componente_trasformatore_p.setDisabled(True)
    radio_componente_trasformatore_d.setChecked(False)
    radio_componente_trasformatore_d.setDisabled(True)
    radio_componente_cabina_primaria.setChecked(True)
    radio_componente_cabina_primaria.setDisabled(False)

################################## FINE FUNZIONI ABILITA/DISABILITA OGGETTI GUI  ##########################




















    
 




############################################# GUI APPLICAZIONE #############################################

#CREA APPLICAZIONE E FINESTRA PRINCIPALE
applicazione=QApplication(sys.argv)
global file_dialog
finestra_principale = QMainWindow()
finestra_principale.setWindowIcon(QIcon('./conf/img/transmission-tower.ico'))
finestra_principale.setWindowTitle('EWS Elettro Lazio')
finestra_principale.statusBar().showMessage('Ready')
finestra_principale.setStyleSheet("background-color:darkgray;")

#CREA TOOLBAR E RELATIVI PULSANTI
toolbar = QToolBar("toolbar")
toolbar.setIconSize(QSize(32,32))
toolbar.setMovable(False)
finestra_principale.addToolBar(toolbar)#aggiunge la toolbar alla finestra principale dell'applicazione

toolbar_pulsante_apri_scenario = QAction(QIcon("./conf/img/scenario_carica.png"), "Apri scenario", toolbar)
toolbar_pulsante_apri_scenario.setStatusTip("Importa scenario")
toolbar_pulsante_apri_scenario.triggered.connect(pulsante_apri_scenario)
toolbar.addAction(toolbar_pulsante_apri_scenario)

toolbar_pulsante_salva_scenario = QAction(QIcon("./conf/img/scenario_salva.png"), "Salva scenario", toolbar)
toolbar_pulsante_salva_scenario.setStatusTip("Salva scenario")
toolbar_pulsante_salva_scenario.setDisabled(True)
toolbar_pulsante_salva_scenario.triggered.connect(pulsante_salva_scenario)
toolbar.addAction(toolbar_pulsante_salva_scenario)

toolbar_pulsante_elabora_scenario = QAction(QIcon("./conf/img/elabora_scenario.png"), "Elabora scenario", toolbar)
toolbar_pulsante_elabora_scenario.setStatusTip("Elabora scenario")
toolbar_pulsante_elabora_scenario.setDisabled(True)
toolbar_pulsante_elabora_scenario.triggered.connect(elabora)
toolbar.addAction(toolbar_pulsante_elabora_scenario)

toolbar_pulsante_chiudi_scenario = QAction(QIcon("./conf/img/scenario_chiudi.png"), "Chiudi scenario", toolbar)
toolbar_pulsante_chiudi_scenario.setStatusTip("Chiudi scenario")
toolbar_pulsante_chiudi_scenario.setDisabled(True)
toolbar_pulsante_chiudi_scenario.triggered.connect(pulsante_chiudi_scenario)
toolbar.addAction(toolbar_pulsante_chiudi_scenario)

toolbar_pulsante_scarica_dati_meteo_025 = QAction(QIcon("./conf/img/scarica_dati_meteo_025.png"), "Scarica dati meteo IFS_ECMWF (0.25deg)", toolbar)
toolbar_pulsante_scarica_dati_meteo_025.setStatusTip("Scarica dati meteo IFS_ECMWF (0.25deg)")
toolbar_pulsante_scarica_dati_meteo_025.triggered.connect(pulsante_scarica_dati_meteo_025)
toolbar.addAction(toolbar_pulsante_scarica_dati_meteo_025)

toolbar_pulsante_scarica_dati_meteo_01 = QAction(QIcon("./conf/img/scarica_dati_meteo_01.png"), "Scarica dati meteo DWD ICON Global (0.1deg)", toolbar)
toolbar_pulsante_scarica_dati_meteo_01.setStatusTip("Scarica dati meteo DWD ICON Global (0.1deg)")
toolbar_pulsante_scarica_dati_meteo_01.triggered.connect(pulsante_scarica_dati_meteo_01)
toolbar.addAction(toolbar_pulsante_scarica_dati_meteo_01)

toolbar_pulsante_scarica_dati_meteo_002 = QAction(QIcon("./conf/img/scarica_dati_meteo_002.png"), "Scarica dati meteo Italia-Meteo ARPAE (0.02deg)", toolbar)
toolbar_pulsante_scarica_dati_meteo_002.setStatusTip("Scarica dati meteo Italia-Meteo ARPAE (0.02deg)")
toolbar_pulsante_scarica_dati_meteo_002.triggered.connect(pulsante_scarica_dati_meteo_002)
toolbar.addAction(toolbar_pulsante_scarica_dati_meteo_002)

toolbar_combobox_scarica_dati_meteo_002_seleziona_provincia = QComboBox()
toolbar_combobox_scarica_dati_meteo_002_seleziona_provincia.addItems(["Frosinone", "Latina", "Rieti", "Roma", "Viterbo"])
toolbar.addWidget(toolbar_combobox_scarica_dati_meteo_002_seleziona_provincia)

toolbar_pulsante_dataframe_excel=QAction(QIcon("./conf/img/excel.png"), "Apri dataframe excel", toolbar)
toolbar_pulsante_dataframe_excel.setStatusTip("Apri dataframe excel")
toolbar_pulsante_dataframe_excel.setDisabled(True)
toolbar_pulsante_dataframe_excel.triggered.connect(apri_dataframe_excel)
toolbar.addAction(toolbar_pulsante_dataframe_excel)

toolbar_pulsante_ricarica_soglie=QAction(QIcon("./conf/img/soglie_flood.png"), "Ricarica soglie flood", toolbar)
toolbar_pulsante_ricarica_soglie.setStatusTip("Ricarica soglie flood")
toolbar_pulsante_ricarica_soglie.setDisabled(True)
toolbar_pulsante_ricarica_soglie.triggered.connect(ricarica_soglie)
toolbar.addAction(toolbar_pulsante_ricarica_soglie)

toolbar_pulsante_salva_mappa=QAction(QIcon("./conf/img/icona_lazio.png"), "Esporta mappa come pagina web", toolbar)
toolbar_pulsante_salva_mappa.setStatusTip("Esporta mappa come pagina web")
toolbar_pulsante_salva_mappa.setDisabled(True)
toolbar_pulsante_salva_mappa.triggered.connect(pulsante_salva_mappa)
toolbar.addAction(toolbar_pulsante_salva_mappa)

toolbar_pulsante_info = QAction(QIcon("./conf/img/guida.png"), "Guida", toolbar)
toolbar_pulsante_info.setStatusTip("Guida")
toolbar_pulsante_info.triggered.connect(apri_manuale_html)
toolbar.addAction(toolbar_pulsante_info)

widget_master=QWidget()#crea il widget principale dell'applicazione, quello che conterrà tutti gli altri widget
layout = QHBoxLayout()#crea il contenitore di box con orientamento orizzontale

#BLOCCO SX WIDGET LAYOUT CONTENENTE I BOX ANALISI,DATI METEO,EVENTO NATURALE e COMPONENTE (oltre al pulsante ELABORA SCENARIO)
blocco_selezione=QVBoxLayout()
layout.addLayout(blocco_selezione)

analisi=QGroupBox("ANALISI")
analisi.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; width: 250px;}")
blocco_selezione.addWidget(analisi)
vbox_analisi = QVBoxLayout()
analisi.setLayout(vbox_analisi)
radio_analisi_meteo = QRadioButton("Solo dati meteo")
radio_analisi_meteo.setChecked(True)
vbox_analisi.addWidget(radio_analisi_meteo)
radio_analisi_rischio = QRadioButton("Analisi rischio")
radio_analisi_rischio.setChecked(False)
vbox_analisi.addWidget(radio_analisi_rischio)
analisi.setDisabled(True)

dato_meteo=QGroupBox("DATI METEO")
dato_meteo.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; }")
blocco_selezione.addWidget(dato_meteo)
vbox_dato_meteo = QVBoxLayout()
dato_meteo.setLayout(vbox_dato_meteo)
radio_dato_temp = QRadioButton("Max temp giorno °C")
radio_dato_temp.setChecked(True)
vbox_dato_meteo.addWidget(radio_dato_temp)
radio_dato_vento = QRadioButton("Max velocità vento giorno m/s")
vbox_dato_meteo.addWidget(radio_dato_vento)
radio_dato_pioggia = QRadioButton("Tot pioggia giorno mm")
vbox_dato_meteo.addWidget(radio_dato_pioggia)
radio_dato_neve = QRadioButton("Tot neve giorno mm")
vbox_dato_meteo.addWidget(radio_dato_neve)
radio_dato_precip = QRadioButton("Tot precipitazioni giorno mm")
vbox_dato_meteo.addWidget(radio_dato_precip)
radio_dato_discharge = QRadioButton("Portata corsi d'acqua mc/sec")
vbox_dato_meteo.addWidget(radio_dato_discharge)
dato_meteo.setDisabled(True)

evento_naturale=QGroupBox("EVENTO NATURALE")
evento_naturale.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; }")
blocco_selezione.addWidget(evento_naturale)
vbox_evento_naturale = QVBoxLayout()
evento_naturale.setLayout(vbox_evento_naturale)
radio_evento_hw = QRadioButton("Ondata di calore")
radio_evento_hw.setChecked(True)
vbox_evento_naturale.addWidget(radio_evento_hw)
radio_evento_vento = QRadioButton("Vento")
vbox_evento_naturale.addWidget(radio_evento_vento)
radio_evento_ghiaccio = QRadioButton("Ghiaccio")
vbox_evento_naturale.addWidget(radio_evento_ghiaccio)
radio_evento_alluvione = QRadioButton("Alluvione")
vbox_evento_naturale.addWidget(radio_evento_alluvione)
evento_naturale.setDisabled(True)

componente=QGroupBox("COMPONENTE")
componente.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; max-width: 300px; }")
blocco_selezione.addWidget(componente)
vbox_componente = QVBoxLayout()
componente.setLayout(vbox_componente)
radio_componente_tralicci = QRadioButton("Tralicci")
radio_componente_tralicci.setChecked(True)
vbox_componente.addWidget(radio_componente_tralicci)
radio_componente_linea_esterna = QRadioButton("Linea esterna")
vbox_componente.addWidget(radio_componente_linea_esterna)
radio_componente_linea_interrata = QRadioButton("Linea interrata")
vbox_componente.addWidget(radio_componente_linea_interrata)
radio_componente_pali = QRadioButton("Pali di servizio")
vbox_componente.addWidget(radio_componente_pali)
radio_componente_trasformatore_p = QRadioButton("Trasformatore potenza")
vbox_componente.addWidget(radio_componente_trasformatore_p)
radio_componente_trasformatore_d = QRadioButton("Trasformatore distribuzione")
vbox_componente.addWidget(radio_componente_trasformatore_d)
radio_componente_cabina_primaria = QRadioButton("Cabina primaria")
vbox_componente.addWidget(radio_componente_cabina_primaria)
componente.setDisabled(True)

pulsante_elabora_modello=QPushButton("Elabora scenario")
pulsante_elabora_modello.setStyleSheet("QPushButton::hover" "{""background-color : lightskyblue;""}")
font=pulsante_elabora_modello.font(); font.setBold(True);font.setPointSize(12);pulsante_elabora_modello.setFont(font)
pulsante_elabora_modello.setToolTip("Genera la mappa")
pulsante_elabora_modello.setDisabled(True)
pulsante_elabora_modello.clicked.connect(elabora)
blocco_selezione.addWidget(pulsante_elabora_modello)




#BLOCCO CENTRALE WIDGET LAYOUT (contiene la MAPPA e la PROGRESS BAR)
blocco_mappa=QVBoxLayout()
layout.addLayout(blocco_mappa)

mappa=QMainWindow()
mappa.browser = QWebEngineView()
#mappa.browser.setUrl(QUrl("file:///E:/0_Tesi/tool/conf/img/start_map.html"))
mappa.browser.setUrl(QUrl("file:///" + path + "/conf/img/start_map.html"))
mappa.setCentralWidget(mappa.browser)
mappa.show()
blocco_mappa.addWidget(mappa)

bar=QProgressBar()
bar.setMinimum(0)
bar.setMaximum(100)
bar.setStyleSheet("""
                   QProgressBar {
                                 background-color: #C0C6CA;
                                 border: 0px;
                                 padding: 0px;
                                 height: 3px;
                                 }
""")
blocco_mappa.addWidget(bar)


#BLOCCO DX WIDGET LAYOUT CONTENENTE I BOX RISCHIO, SIMULAZIONE, OPZIONI 
blocco_simulazione=QVBoxLayout()
layout.addLayout(blocco_simulazione)

img_rischio=QGroupBox("RISCHIO")
img_rischio.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; max-width: 300px;}")
img_rischio.setDisabled(True)
blocco_simulazione.addWidget(img_rischio)
vbox_img_rischio = QVBoxLayout()
img_rischio.setLayout(vbox_img_rischio)
logoLabel = QLabel()
logoLabel.setFixedHeight(280)
logoLabel.setFixedWidth(280)
logoLabel.setScaledContents(True)
pixmap = QPixmap('./conf/img/transmission-tower.ico')
logoLabel.setPixmap(pixmap)
vbox_img_rischio.addWidget(logoLabel)

simulazione=QGroupBox("SIMULAZIONE")
simulazione.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; max-width: 300px;}")
simulazione.setDisabled(True)
blocco_simulazione.addWidget(simulazione)
layout1 = QVBoxLayout()
layout_head=QHBoxLayout()
layout_temp = QHBoxLayout()
layout_vento = QHBoxLayout()
layout_pioggia = QHBoxLayout()
layout_precip = QHBoxLayout()
layout_neve = QHBoxLayout()
layout_ghiaccio_jones = QHBoxLayout()
layout_ghiaccio_nojones = QHBoxLayout()
layout_discharge=QHBoxLayout()
layout_pulsanti = QHBoxLayout()
layout_head.addStretch()
label_all=QLabel("All")
label_delta=QLabel("(Δ)")
label_off=QLabel("Off")
layout_head.addWidget(label_all)
layout_head.addWidget(label_delta)
layout_head.addWidget(label_off)
layout1.addLayout(layout_head)

label_temp=QLabel("Temp °C"); label_temp.setFixedWidth(90)
label_slider_temp=QLabel("0"); label_slider_temp.setStyleSheet("border: 1px solid black;"); label_slider_temp.setFixedWidth(40)
slider_temp=QSlider(Qt.Horizontal); slider_temp.setStyleSheet("max-width: 50px;")
slider_temp.setRange(-50,50)
slider_temp.setSingleStep(1)
slider_temp.setValue(0)
slider_temp.valueChanged.connect(cambia_label_slider_temp)
radio_temp_group = QButtonGroup()
radio_temp_all=QRadioButton()
radio_temp_delta=QRadioButton()
radio_temp_off=QRadioButton(); radio_temp_off.setChecked(True)
radio_temp_group.addButton(radio_temp_all)
radio_temp_group.addButton(radio_temp_delta)
radio_temp_group.addButton(radio_temp_off)
layout_temp.addWidget(label_temp)#;layout_temp.setSpacing(20)
layout_temp.addWidget(label_slider_temp)
layout_temp.addWidget(slider_temp)
layout_temp.addWidget(radio_temp_all)
layout_temp.addWidget(radio_temp_delta)
layout_temp.addWidget(radio_temp_off)
layout1.addLayout(layout_temp)

label_vento=QLabel("Vento m/s");label_vento.setFixedWidth(90)
label_slider_vento=QLabel("0"); label_slider_vento.setStyleSheet("border: 1px solid black;"); label_slider_vento.setFixedWidth(40)
slider_vento=QSlider(Qt.Horizontal); slider_vento.setStyleSheet("max-width: 50px;")
slider_vento.setRange(-150,150)
slider_vento.setSingleStep(1)
slider_vento.setValue(0)
slider_vento.valueChanged.connect(cambia_label_slider_vento)
radio_vento_group = QButtonGroup()
radio_vento_all=QRadioButton()
radio_vento_delta=QRadioButton()
radio_vento_off=QRadioButton(); radio_vento_off.setChecked(True)
radio_vento_group.addButton(radio_vento_all)
radio_vento_group.addButton(radio_vento_delta)
radio_vento_group.addButton(radio_vento_off)
layout_vento.addWidget(label_vento)
layout_vento.addWidget(label_slider_vento)
layout_vento.addWidget(slider_vento)
layout_vento.addWidget(radio_vento_all)
layout_vento.addWidget(radio_vento_delta)
layout_vento.addWidget(radio_vento_off)
layout1.addLayout(layout_vento)

label_pioggia=QLabel("Pioggia  mm");label_pioggia.setFixedWidth(90)
label_slider_pioggia=QLabel("0"); label_slider_pioggia.setStyleSheet("border: 1px solid black;");label_slider_pioggia.setFixedWidth(40)
slider_pioggia=QSlider(Qt.Horizontal); slider_pioggia.setStyleSheet("max-width: 50px;")
slider_pioggia.setRange(-1000,1000)
slider_pioggia.setSingleStep(1)
slider_pioggia.setValue(0)
slider_pioggia.valueChanged.connect(cambia_label_slider_pioggia)
radio_pioggia_group = QButtonGroup()
radio_pioggia_all=QRadioButton()
radio_pioggia_delta=QRadioButton()
radio_pioggia_off=QRadioButton(); radio_pioggia_off.setChecked(True)
radio_pioggia_group.addButton(radio_pioggia_all)
radio_pioggia_group.addButton(radio_pioggia_delta)
radio_pioggia_group.addButton(radio_pioggia_off)
layout_pioggia.addWidget(label_pioggia)
layout_pioggia.addWidget(label_slider_pioggia)
layout_pioggia.addWidget(slider_pioggia)
layout_pioggia.addWidget(radio_pioggia_all)
layout_pioggia.addWidget(radio_pioggia_delta)
layout_pioggia.addWidget(radio_pioggia_off)
layout1.addLayout(layout_pioggia)

label_neve=QLabel("Neve  mm");label_neve.setFixedWidth(90)
label_slider_neve=QLabel("0"); label_slider_neve.setStyleSheet("border: 1px solid black;");label_slider_neve.setFixedWidth(40)
slider_neve=QSlider(Qt.Horizontal); slider_neve.setStyleSheet("max-width: 50px;")
slider_neve.setRange(-1000,1000)
slider_neve.setSingleStep(1)
slider_neve.setValue(0)
slider_neve.valueChanged.connect(cambia_label_slider_neve)
radio_neve_group = QButtonGroup()
radio_neve_all=QRadioButton()
radio_neve_delta=QRadioButton()
radio_neve_off=QRadioButton(); radio_neve_off.setChecked(True)
radio_neve_group.addButton(radio_neve_all)
radio_neve_group.addButton(radio_neve_delta)
radio_neve_group.addButton(radio_neve_off)
layout_neve.addWidget(label_neve)
layout_neve.addWidget(label_slider_neve)
layout_neve.addWidget(slider_neve)
layout_neve.addWidget(radio_neve_all)
layout_neve.addWidget(radio_neve_delta)
layout_neve.addWidget(radio_neve_off)
layout1.addLayout(layout_neve)

label_precip=QLabel("Precip mm");label_precip.setFixedWidth(90)
label_slider_precip=QLabel("0"); label_slider_precip.setStyleSheet("border: 1px solid black;");label_slider_precip.setFixedWidth(40)
slider_precip=QSlider(Qt.Horizontal); slider_precip.setStyleSheet("max-width: 50px;")
slider_precip.setRange(-1000,1000)
slider_precip.setSingleStep(1)
slider_precip.setValue(0)
slider_precip.valueChanged.connect(cambia_label_slider_precip)
radio_precip_group = QButtonGroup()
radio_precip_all=QRadioButton()
radio_precip_delta=QRadioButton()
radio_precip_off=QRadioButton(); radio_precip_off.setChecked(True)
radio_precip_group.addButton(radio_precip_all)
radio_precip_group.addButton(radio_precip_delta)
radio_precip_group.addButton(radio_precip_off)
layout_precip.addWidget(label_precip)
layout_precip.addWidget(label_slider_precip)
layout_precip.addWidget(slider_precip)
layout_precip.addWidget(radio_precip_all)
layout_precip.addWidget(radio_precip_delta)
layout_precip.addWidget(radio_precip_off)
layout1.addLayout(layout_precip)

label_discharge=QLabel("Portata mc/s");label_discharge.setFixedWidth(90)
label_slider_discharge=QLabel("0"); label_slider_discharge.setStyleSheet("border: 1px solid black;");label_slider_discharge.setFixedWidth(40)
slider_discharge=QSlider(Qt.Horizontal); slider_discharge.setStyleSheet("max-width: 50px;")
slider_discharge.setRange(-100,100)
slider_discharge.setSingleStep(1)
slider_discharge.setValue(0)
slider_discharge.valueChanged.connect(cambia_label_slider_discharge)
radio_discharge_group = QButtonGroup()
radio_discharge_all=QRadioButton()
radio_discharge_delta=QRadioButton()
radio_discharge_off=QRadioButton(); radio_discharge_off.setChecked(True)
radio_discharge_group.addButton(radio_discharge_all)
radio_discharge_group.addButton(radio_discharge_delta)
radio_discharge_group.addButton(radio_discharge_off)
layout_discharge.addWidget(label_discharge)
layout_discharge.addWidget(label_slider_discharge)
layout_discharge.addWidget(slider_discharge)
layout_discharge.addWidget(radio_discharge_all)
layout_discharge.addWidget(radio_discharge_delta)
layout_discharge.addWidget(radio_discharge_off)
layout1.addLayout(layout_discharge)

label_ghiaccio_jones=QLabel("Ice(J)");label_ghiaccio_jones.setFixedWidth(40)
label_ghiaccio_jones_ore=QLabel("h");label_ghiaccio_jones_ore.setFixedWidth(18)
combobox_jones_ore = QComboBox(); combobox_jones_ore.addItems(['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
combobox_jones_ore.setFixedWidth(50); combobox_jones_ore.setCurrentText('1')
label_ghiaccio_jones_M=QLabel("M");label_ghiaccio_jones_M.setFixedWidth(14)
combobox_jones_M = QComboBox(); combobox_jones_M.addItems(['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])
combobox_jones_M.setFixedWidth(50); combobox_jones_M.setCurrentText('15')
radio_ghiaccio_jones_group = QButtonGroup()
radio_ghiaccio_jones_all=QRadioButton()
radio_ghiaccio_jones_delta=QRadioButton()
radio_ghiaccio_jones_off=QRadioButton(); radio_ghiaccio_jones_off.setChecked(True)
radio_ghiaccio_jones_group.addButton(radio_ghiaccio_jones_all)
radio_ghiaccio_jones_group.addButton(radio_ghiaccio_jones_delta)
radio_ghiaccio_jones_group.addButton(radio_ghiaccio_jones_off)
layout_ghiaccio_jones.addWidget(label_ghiaccio_jones)
layout_ghiaccio_jones.addWidget(label_ghiaccio_jones_ore)
layout_ghiaccio_jones.addWidget(combobox_jones_ore)
layout_ghiaccio_jones.addWidget(label_ghiaccio_jones_M)
layout_ghiaccio_jones.addWidget(combobox_jones_M)
layout_ghiaccio_jones.addWidget(radio_ghiaccio_jones_all)
layout_ghiaccio_jones.addWidget(radio_ghiaccio_jones_delta)
layout_ghiaccio_jones.addWidget(radio_ghiaccio_jones_off)
layout1.addLayout(layout_ghiaccio_jones)

label_ghiaccio_nojones=QLabel("Ice");label_ghiaccio_nojones.setFixedWidth(40)
label_ghiaccio_nojones_m=QLabel("m");label_ghiaccio_nojones_m.setFixedWidth(18)
combobox_nojones_m = QComboBox(); combobox_nojones_m.addItems(['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',\
                                                               '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40',\
                                                                '41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60'])
combobox_nojones_m.setFixedWidth(50); combobox_nojones_m.setCurrentText('1')
label_ghiaccio_nojones_M=QLabel("M");label_ghiaccio_nojones_M.setFixedWidth(14)
combobox_nojones_M = QComboBox(); combobox_nojones_M.addItems(['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])
combobox_nojones_M.setFixedWidth(50); combobox_nojones_M.setCurrentText('15')
radio_ghiaccio_nojones_group = QButtonGroup()
radio_ghiaccio_nojones_all=QRadioButton()
radio_ghiaccio_nojones_delta=QRadioButton()
radio_ghiaccio_nojones_off=QRadioButton(); radio_ghiaccio_nojones_off.setChecked(True)
radio_ghiaccio_nojones_group.addButton(radio_ghiaccio_nojones_all)
radio_ghiaccio_nojones_group.addButton(radio_ghiaccio_nojones_delta)
radio_ghiaccio_nojones_group.addButton(radio_ghiaccio_nojones_off)
layout_ghiaccio_nojones.addWidget(label_ghiaccio_nojones)
layout_ghiaccio_nojones.addWidget(label_ghiaccio_nojones_m)
layout_ghiaccio_nojones.addWidget(combobox_nojones_m)
layout_ghiaccio_nojones.addWidget(label_ghiaccio_nojones_M)
layout_ghiaccio_nojones.addWidget(combobox_nojones_M)
layout_ghiaccio_nojones.addWidget(radio_ghiaccio_nojones_all)
layout_ghiaccio_nojones.addWidget(radio_ghiaccio_nojones_delta)
layout_ghiaccio_nojones.addWidget(radio_ghiaccio_nojones_off)
layout1.addLayout(layout_ghiaccio_nojones)

pulsante_salva_dati_simulazione=QPushButton("Applica")
pulsante_salva_dati_simulazione.setStyleSheet("QPushButton::hover" "{""background-color : lightskyblue;""}")
font=pulsante_salva_dati_simulazione.font(); font.setBold(True);font.setPointSize(7);pulsante_salva_dati_simulazione.setFont(font)
pulsante_salva_dati_simulazione.setMaximumSize(QSize(60,30))
pulsante_salva_dati_simulazione.setToolTip("Modifica dati meteo")
pulsante_salva_dati_simulazione.clicked.connect(applica_dati_simulazione) 
pulsante_ripristina_dati_simulazione=QPushButton("Reset")
pulsante_ripristina_dati_simulazione.setStyleSheet("QPushButton::hover" "{""background-color : lightskyblue;""}")
font=pulsante_ripristina_dati_simulazione.font(); font.setBold(True);font.setPointSize(7);pulsante_ripristina_dati_simulazione.setFont(font)
pulsante_ripristina_dati_simulazione.setMaximumSize(QSize(60,30))
pulsante_ripristina_dati_simulazione.setToolTip("Ripristina i dati meteo originari")
pulsante_ripristina_dati_simulazione.clicked.connect(reset_dati)
layout_pulsanti.addWidget(pulsante_salva_dati_simulazione)
layout_pulsanti.addWidget(pulsante_ripristina_dati_simulazione)
layout1.addLayout(layout_pulsanti)
simulazione.setLayout(layout1)

opzioni=QGroupBox("OPZIONI")
opzioni.setStyleSheet("QGroupBox { font-size: 18px; font-weight: bold; max-width: 300px;}")
blocco_simulazione.addWidget(opzioni)
vbox_opzioni = QVBoxLayout()
opzioni.setLayout(vbox_opzioni)   
checkbox_opzioni_rete = QCheckBox("Visualizza infrastruttura elettrica")
checkbox_opzioni_rete.setChecked(False)
vbox_opzioni.addWidget(checkbox_opzioni_rete)
layout_pali_legno = QHBoxLayout()
label_pali_legno=QLabel("Pali");label_pali_legno.setFixedWidth(70)
label_pali_legno_20=QLabel("20y");label_pali_legno_20.setFixedWidth(25)
label_pali_legno_40=QLabel("40y");label_pali_legno_40.setFixedWidth(25)
label_pali_legno_60=QLabel("60y");label_pali_legno_60.setFixedWidth(25)
label_pali_legno_off=QLabel("Off");label_pali_legno_off.setFixedWidth(25)
radio_pali_legno_group = QButtonGroup()
radio_pali_legno_20=QRadioButton(); radio_pali_legno_20.setFixedWidth(20)
radio_pali_legno_40=QRadioButton(); radio_pali_legno_40.setFixedWidth(20)
radio_pali_legno_60=QRadioButton(); radio_pali_legno_60.setFixedWidth(20)
radio_pali_legno_off=QRadioButton(); radio_pali_legno_off.setChecked(True);radio_pali_legno_off.setFixedWidth(20)
radio_pali_legno_group.addButton(radio_pali_legno_20)
radio_pali_legno_group.addButton(radio_pali_legno_40)
radio_pali_legno_group.addButton(radio_pali_legno_60)
radio_pali_legno_group.addButton(radio_pali_legno_off)
layout_pali_legno.addWidget(label_pali_legno)
layout_pali_legno.addWidget(label_pali_legno_20)
layout_pali_legno.addWidget(radio_pali_legno_20)
layout_pali_legno.addWidget(label_pali_legno_40)
layout_pali_legno.addWidget(radio_pali_legno_40)
layout_pali_legno.addWidget(label_pali_legno_60)
layout_pali_legno.addWidget(radio_pali_legno_60)
layout_pali_legno.addWidget(label_pali_legno_off)
layout_pali_legno.addWidget(radio_pali_legno_off)
vbox_opzioni.addLayout(layout_pali_legno)
opzioni.setDisabled(True)

widget_master.setLayout(layout)#aggiunge l'insieme dei widget presenti nel contenitore di box con orientamento orizzontale nel widget_master
finestra_principale.setCentralWidget(widget_master)#imposta widget_master come elemento centrale
finestra_principale.show()


sys.exit(applicazione.exec_())

