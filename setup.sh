mkdir -p ~/.streamlit
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

sudo apt install google-chrome-stable
sudo apt-get install firefox

seleniumbase install chromedriver
seleniumbase install geckodriver
