# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:33:57 2024

@author: LENOVO
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:11:55 2024

@author: LENOVO
"""

import numpy as np
import streamlit as st
from PIL import Image

import joblib
C=joblib.load("C:/Users/LENOVO/Downloads/archive (3)/car_price.joblib")

def car_price(input_data):
    
    
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float32)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    result = C.predict(input_data_reshaped)
    return result[0] if result[0] > 0 else "Enter valid car details"

def main():
    st.title("car price prediction website")
    image_path = "Documents/mercedes-benz-g-class.jpg"
    image = st.image(image_path, caption="Your Image Caption", use_column_width=True)
    car_names = []  # Add your car names here
    car_name_input = st.selectbox("Select the car name", car_names)
    fueltype=st.text_input("enter the 0 or 1 it mean 1 gas and 0 is diesel")
    doornumber=st.text_input("enter the 0 or 1 it mean 1 two door and 0 is four door")
    carbody=st.text_input("enter the 0 1 2 3 4 it mean 1 hardtop and 0 is convertible 2 is hatchback 3 is sedan 4 is wagon ")
    drivewheel=st.text_input("enter the 0 1 2 it mean 0 is 4wd 1 is fwd 2 is rwd")
    enginelocation=st.text_input("enter the 0 and 1 it mean 0 is front 1 is rear")
    wheelbase=st.text_input("enter the wheelbase like this 88.6,  94.5,  99.8,  99.4, 105.8,  99.5, 101.2")
    curbweight=st.text_input("enter the  the weight of the vehicle like this 2548, 2823, 2337, 2824, 2507, 2844, 2954, 3086")
    enginetype=st.text_input("enter the enginetype 0 is dohc 5 is ohcv is 3 ohc is 6 rotor 2 is ohcf 4 is dohcv")
    enginesize=st.text_input("enter the enginesize like this 130, 152, 109, 136, 131, 108, 164, 209,  90")
    boreratio=st.text_input("enter the boreratio like this 3.47, 2.68, 3.19, 3.13, 3.5 , 3.31, 3.62")
    stroke=st.text_input("enter the stroke like this 2.68 , 3.47 , 3.4  , 2.8  , 3.19 , 3.39")
    horsepower=st.text_input("enter the horsepower like this 111, 154, 102, 115, 110, 140, 160, 101, 121")
    peakrpm=st.text_input("enter the peakrpm like this 5000, 5500, 5800, 4250, 5400, 6000, 4800, 4650, 4200")
    citympg=st.text_input("enter the citympg 21, 19, 24, 18, 17, 16, 23, 20, 15, 38")
    highwaympg=st.text_input("enter the highwaympg 27, 26, 30, 22, 25, 20, 29, 28, 43, 41, 38")
    diagnosis=''
    
    if st.button("price"):
        diagnosis=car_price([CarName,	fueltype	,doornumber,	carbody,	drivewheel,	enginelocation,	wheelbase,	curbweight,	enginetype,	enginesize,	boreratio,	stroke,	horsepower	,peakrpm	,citympg,	highwaympg])
        st.success(diagnosis)


if __name__ == '__main__':
    main()
    
        

