import streamlit as st
from cryptography.fernet import Fernet

st.title("🔐 Secure Data Encryption System")
st.write("**By: Barirah Mansoor**")

mode = st.sidebar.selectbox("Choose Encryption Type", ["Caesar Cipher", "Fernet Encryption"])
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

key = st.session_state.get("fernet_key", Fernet.generate_key())
st.session_state["fernet_key"] = key
cipher = Fernet(key)

user_input = st.text_area("Enter your text:")
action = st.radio("Action", ["Encrypt", "Decrypt"])

if mode == "Caesar Cipher":
    shift = st.slider("Choose Shift", 1, 25, 3)
    if action == "Encrypt":
        result = caesar_encrypt(user_input, shift)
    else:
        result = caesar_decrypt(user_input, shift)

elif mode == "Fernet Encryption":
    if action == "Encrypt":
        result = cipher.encrypt(user_input.encode()).decode()
    else:
        try:
            result = cipher.decrypt(user_input.encode()).decode()
        except Exception as e:
            result = f"❌ Decryption failed: {str(e)}"

if user_input:
    st.subheader("🔎 Result:")
    st.code(result)

if mode == "Fernet Encryption":
    st.caption(f"Fernet Key (keep this secure!): `{key.decode()}`")
