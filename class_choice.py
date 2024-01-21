import streamlit as st
import numpy as np

if 'random_seed' not in st.session_state:
    st.session_state['random_seed'] = np.random.randint(0, 10000)

# Set the random seed
np.random.seed(st.session_state['random_seed'])

sidebar_image_url = "https://i.ibb.co/TPQCzLd/diablo-4-v2.jpg"
st.image(sidebar_image_url, use_column_width=True)

# Function to generate class choice
def generate_class_choice():
    class_dictionary = {1: 'Barbarian', 2: 'Sorcerer', 3: 'Necromancer', 4: 'Rogue', 5: 'Druid'}
    random_number = np.random.randint(1, 6)
    return class_dictionary[random_number]

# Dictionary linking classes to their images
class_images = {
    'Barbarian': 'https://i.ibb.co/Qdx1fKx/Barbarian.jpg',
    'Sorcerer': 'https://i.ibb.co/2gfNS9B/sorcerer.jpg',
    'Necromancer': 'https://i.ibb.co/MGc932s/necromancer.jpg',
    'Rogue': 'https://i.ibb.co/GtqKdj7/rogue.jpg',
    'Druid': 'https://i.ibb.co/3dB0fjg/Druid.jpg'
}

# Streamlit app
st.title('Diablo 4 Season 3 Class Selector')

# Button to generate class
if st.button('Generate Class'):
    chosen_class = generate_class_choice()
    st.write(f"The class you will play is: {chosen_class}. Congratulations!")
    
    # Display the image of the chosen class
    image_path = class_images[chosen_class]
    st.image(image_path, caption=chosen_class, use_column_width=True)




footer_text = """Powered by Alptheone"""
st.markdown(footer_text)

