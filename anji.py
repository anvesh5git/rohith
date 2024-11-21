import streamlit as st

def norton_equivalent(resistances, currents):
    r_norton = sum(1 / r for r in resistances) ** -1
    i_norton = sum(currents)
    return r_norton, i_norton

def main():
    st.title("Norton's Theorem Calculator")
    
    num_sources = st.number_input("Number of sources", min_value=1, value=1)
    
    resistances = []
    currents = []
    
    for i in range(num_sources):
        st.header(f"Source {i+1}")
        resistance = st.number_input(f"Resistance (R{i+1})", min_value=0.0, value=1.0)
        current = st.number_input(f"Current (I{i+1})", min_value=0.0, value=1.0)
        resistances.append(resistance)
        currents.append(current)
    
    if st.button("Calculate Norton Equivalent"):
        r_norton, i_norton = norton_equivalent(resistances, currents)
        st.write(f"Norton Equivalent Resistance: {r_norton} Ω")
        st.write(f"Norton Equivalent Current: {i_norton} A")

if __name__ == "__main__":
    main()
