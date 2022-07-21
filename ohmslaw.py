"""
Ohm's Law (in series)

"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Welcome to Emma's Ohm's Law Simulator")
st.caption("This simulator will calculate the current and voltage drops of an in-series circuit!")

voltage = st.slider("Please select your input voltage", 0, 50)
st.write('The selected voltage is ', voltage, 'V')

R_count = st.selectbox("Please select how many resistors you'd like:", [0,1,2,3])
Resistances = []

for i in range(R_count):
    R = st.number_input('Please enter a resistance for R'+str(i+1)+':',0.0, key=i)
    st.write('The selected resistance is ', round(R,2), 'Ω')
    Resistances.append(R)

r_total = sum(Resistances)

y = [voltage]

if r_total != 0:
    I = voltage/(r_total)
    st.write('\nThe current of the circuit is: ', round(I,2), 'A')
    
    V_drop_list = [0]

    for j in range(0, len(Resistances)):
        V_drop = (I*Resistances[j])
        st.write('The voltage drop over R'+str(j+1)+' is: ', round(V_drop,2),'V')
        V_drop_list.append(V_drop)
        tmp_drop = 0;
        for k in range(0, len(V_drop_list) - 1):
            tmp_drop += V_drop_list[k+1]
        V_total = voltage-(tmp_drop)
        y.append(V_total)

else:
    st.write("To have current and voltage drops calculated, please select more than 0 resistors")

y=np.array(y)
x=np.arange(0,len(y),1)

if r_total != 0:
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(x, y, 'red', linewidth=2)
    ax.set_title('Voltage at each resistor')
    ax.set_ylabel("Total circuit voltage (V)")
    ax.set_ylim(0,voltage+1)
    ax.set_xlabel("Resistor number")
    st.pyplot(fig)