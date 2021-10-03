
import streamlit as st
import pickle
import numpy as np

# loading the trained model
pickle_in = open('xgboost.pkl', 'rb')
classifier = pickle.load(pickle_in)
pickle_in.close()

print(classifier, type(classifier))

# # defining the function which will make the prediction using the data which the user inputs

@st.cache()
def prediction(battery_power, blue,clock_speed, dual_sim, fc, four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram, sc_h, sc_w,talk_time,three_g, touch_screen, wifi):

    if blue == "Yes":
        blue = 1
    elif (blue == 'No'):
        blue = 0

    if dual_sim == 'Yes':
        dual_sim = 1
    elif (dual_sim == 'No'):
        dual_sim = 0

    if four_g == 'Yes':
        four_g = 1
    elif (four_g == 'No'):
        four_g = 0

    if three_g == 'Yes':
        three_g = 1
    elif (three_g == 'No'):
        three_g = 0

    if touch_screen == 'Yes':
        touch_screen = 1
    elif (touch_screen == 'No'):
        touch_screen = 0

    if wifi == 'Yes':
        wifi = 1
    elif (wifi == 'No'):
        wifi = 0

    print([battery_power, blue,clock_speed, dual_sim, fc, four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram, sc_h, sc_w,talk_time,three_g, touch_screen, wifi])
    prediction = classifier.predict(
        np.array([[battery_power, blue,clock_speed, dual_sim, fc, four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram, sc_h, sc_w,talk_time,three_g, touch_screen, wifi]]))


    if prediction == 0:
        pred = 'price rs 5000'
    elif prediction ==1:
        pred = 'price rs 10000 '
    elif prediction == 2:
        pred = 'price rs 15000 '
    else:
        pred = 'price rs 20000'

    return pred


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    battery_power = st.number_input('Enter batter power: 500-1999', step=1)
    blue = st.selectbox('Bluetooth', ('Yes', 'No'))
    clock_speed = st.number_input('clock speed: 0.5-3', step=0.1)
    dual_sim = st.selectbox('Dual sim', ('Yes', 'No'))
    fc = st.number_input('Front Camera in mega pixels: 0-19', step=1)
    four_g = st.selectbox('4G', ('Yes', 'No'))
    int_memory = st.number_input('Internal memory: 2-64', step=1)
    m_dep = st.number_input('Mobile depth in cm: 0.1-1', step=0.1)
    mobile_wt = st.number_input('mobile weight: 80-200 gm', step=1)
    n_cores = st.number_input('Number of cores of processor: 1-8', step=1)
    pc = st.number_input('Primary camera in mega pixels: 0-20', step=1)
    px_height = st.number_input('px_resolution_height: 0-1907', step=1)
    px_width = st.number_input('px_width: 501-1998', step=1)
    ram = st.number_input('ram: 263-3989', step=1)
    sc_h = st.number_input('screen height: 5-19', step=1)
    sc_w = st.number_input('screen width: 0-18', step=1)
    talk_time = st.number_input('time battery charge 2-20', step=1)
    three_g = st.selectbox('3G', ("Yes",'No'))
    touch_screen = st.selectbox('touch_screen', ("Yes",'No'))
    wifi = st.selectbox('wifi', ("Yes",'No'))

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(battery_power, blue,clock_speed, dual_sim, fc, four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram, sc_h, sc_w,talk_time,three_g, touch_screen, wifi)
        st.success('Your mobile price is {}'.format(result))
        # print(LoanAmount)


if __name__ == '__main__':
    main()