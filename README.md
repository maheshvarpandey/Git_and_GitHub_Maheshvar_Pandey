# Git_and_GitHub_Maheshvar_Pandey

DevOps assignment – Git and GitHub workflow using a Flask project.

Repository: https://github.com/maheshvarpandey/Git_and_GitHub_Maheshvar_Pandey

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env   # add your MongoDB Atlas URI
flask --app app run --debug
```

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/api` | GET | Returns the JSON list from `data/api_data.json` |
| `/todo` | GET | To-Do form page |
| `/submittodoitem` | POST | Saves `itemName` and `itemDescription` to MongoDB |
