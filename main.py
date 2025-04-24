import streamlit as st
from cryptography.fernet import Fernet

# Title
st.title("🔐 Secure Data Encryption System")
st.write("**By: Barirah Mansoor**")

# Sidebar for mode selection
mode = st.sidebar.selectbox("Choose Encryption Type", ["Caesar Cipher", "Fernet Encryption"])

# Caesar Cipher Functions
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fernet Encryption Key Setup
key = st.session_state.get("fernet_key", Fernet.generate_key())
st.session_state["fernet_key"] = key
fernet = Fernet(key)

# Input
user_input = st.text_area("Enter your text:")
action = st.radio("Action", ["Encrypt", "Decrypt"])

# Processing
if mode == "Caesar Cipher":
    shift = st.slider("Choose Shift", 1, 25, 3)
    if action == "Encrypt":
        result = caesar_encrypt(user_input, shift)
    else:
        result = caesar_decrypt(user_input, shift)

elif mode == "Fernet Encryption":
    if action == "Encrypt":
        result = fernet.encrypt(user_input.encode()).decode()
    else:
        try:
            result = fernet.decrypt(user_input.encode()).decode()
        except Exception as e:
            result = f"❌ Decryption failed: {str(e)}"

# Output
if user_input:
    st.subheader("🔎 Result:")
    st.code(result)

# Show Fernet key (for demonstration)
if mode == "Fernet Encryption":
    st.caption(f"Fernet Key (keep it secret!): `{key.decode()}`")
