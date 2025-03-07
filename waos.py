import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

# Función para generar el diagrama de Venn
def generar_diagrama(A, B, C):
    # Si el conjunto C está vacío, usar solo A y B
    if not C:
        venn = venn2([A, B], set_labels=('A', 'B'))
        plt.title("Diagrama de Venn para los conjuntos A y B")
    else:
        # Crear el diagrama de Venn con los tres conjuntos
        venn = venn3([A, B, C], set_labels=('A', 'B', 'C'))
        plt.title("Diagrama de Venn para los conjuntos A, B y C")

    # Etiquetar cada sección con las operaciones matemáticas
    venn.get_label_by_id('100').set_text('\n'.join(map(str, A - B - C)))  # A - B - C
    venn.get_label_by_id('010').set_text('\n'.join(map(str, B - A - C)))  # B - A - C
    venn.get_label_by_id('001').set_text('\n'.join(map(str, C - A - B)))  # C - A - B
    venn.get_label_by_id('110').set_text('\n'.join(map(str, A & B - C)))  # A ∩ B - C
    venn.get_label_by_id('011').set_text('\n'.join(map(str, B & C - A)))  # B ∩ C - A
    venn.get_label_by_id('101').set_text('\n'.join(map(str, A & C - B)))  # A ∩ C - B
    venn.get_label_by_id('111').set_text('\n'.join(map(str, A & B & C)))  # A ∩ B ∩ C

    return plt

# Crear la interfaz de usuario
st.title("Generador de Diagrama de Venn")
st.subheader("Desarrolado por Kevin molina")


# Entradas de los conjuntos
A = set(st.text_input("Conjunto A (separado por comas):").split(','))
B = set(st.text_input("Conjunto B (separado por comas):").split(','))
C = set(st.text_input("Conjunto C (separado por comas):").split(','))

# Limpiar los conjuntos (eliminar espacios en blanco y elementos vacíos)
A = {x.strip() for x in A if x.strip()}
B = {x.strip() for x in B if x.strip()}
C = {x.strip() for x in C if x.strip()}

if st.button('Generar Diagrama'):
    fig = generar_diagrama(A, B, C)
    st.pyplot(fig)
