import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(r'vehicles_us.csv') # leer los datos
hist_button = st.checkbox('Construir histograma') # crear un botón
scatter_button = st.checkbox('Constuir dispersión')

car_data['manufacturer'] = [model.split()[0] for model in car_data['model']]

st.header("Aplicación web sobre las ventas de vehículos de Estados Unidos")
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.header('Histograma') 

    st.write('Creación de histogramas para el conjunto de datos de anuncios de venta de coches') 
    
    fig = px.histogram(car_data, x="odometer",
                           title='Distribución del kilometraje de los vehículos.')
               
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    fig1 = px.histogram(car_data, x="manufacturer",color='transmission',title='Fabricantes con mayor registro')
    
    st.plotly_chart(fig1, use_container_width=True)
    
if scatter_button:
    
    st.header('Dispersión') 
    
    st.write('Creación de gráficas de dispersion de vehículos de Estados Unidos')
    
    fig = px.scatter(car_data, x="odometer", y="price", title='Precio de vehículos con respecto a su kilometraje',color='condition')
    
    st.plotly_chart(fig, use_container_width=True)
    
    fig1 = px.scatter(car_data.sort_values(by='date_posted',ascending=True),
           x='model_year',
           y='price',
           color='model_year',
           title='Precio de los vehículos con respecto al año de fabricación')
    
    st.plotly_chart(fig1, use_container_width=True)