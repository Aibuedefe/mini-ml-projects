import streamlit_authenticator as stauth
from pathlib import Path
import pickle

names  = ["Admin", "User"]
usernames = ["admin1", "user1"]
passwords = ["abc123","def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed1.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
  