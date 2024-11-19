from flask import Flask, render_template
import uvicorn
from fastapi import FastAPI
import requests
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

app = FastAPI()


# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get('/teams/')
def get_team_data():
    url = f"https://api.balldontlie.io/v1/teams?per_page=100"
    headers = {"Authorization": "0989e1cc-d7f6-451b-a53c-d4e311b971b9"}  # Use your actual API key here
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        team_data = response.json()
        return team_data['data']
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

@app.get('/players/')
def get_player_data():
    url = f"https://api.balldontlie.io/v1/players?per_page=100"
    headers = {"Authorization": "0989e1cc-d7f6-451b-a53c-d4e311b971b9"}  # Use your actual API key here
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        player_data = response.json()
        return player_data['data']
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None



# Root route
@app.get('/')
def index():
    return "Welcome to the Basketball Data API! Visit."


# Route for visualizations
@app.get("/charts/", response_class=HTMLResponse)
def show_charts(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)  # Port should be an integer, not a string
