import os

# Define the folder/file structure
structure = {
    "backend": {
        "app": {
            "routers": {
                "__init__.py": "",
                "auth.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n",
                "sample.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get('/')\ndef read_items():\n    return [{'id': 1, 'name': 'Sample item'}]\n",
            },
            "models": {
                "__init__.py": "",
                "sample_model.py": "# Pydantic models go here\n",
            },
            "db": {
                "__init__.py": "",
                "database.py": "# Database connection logic goes here\n",
            },
            "core": {
                "__init__.py": "",
                "config.py": "# Configuration / environment settings\n",
                "security.py": "# Security / auth helpers (JWT, hashing, etc.)\n",
            },
            "services": {
                "__init__.py": "",
                "ml_service.py": "# Optional ML/DL service functions\n",
            },
            "__init__.py": "",
            "main.py": (
                "from fastapi import FastAPI\n"
                "from fastapi.middleware.cors import CORSMiddleware\n"
                "from app.routers import auth, sample\n\n"
                "app = FastAPI(title='Hackathon Platform')\n\n"
                "# CORS setup\n"
                "app.add_middleware(\n"
                "    CORSMiddleware,\n"
                "    allow_origins=['*'],\n"
                "    allow_credentials=True,\n"
                "    allow_methods=['*'],\n"
                "    allow_headers=['*'],\n"
                ")\n\n"
                "app.include_router(auth.router, prefix='/api/auth', tags=['Auth'])\n"
                "app.include_router(sample.router, prefix='/api/sample', tags=['Sample'])\n\n"
                "@app.get('/')\n"
                "def root():\n"
                "    return {'msg': 'Backend running successfully 🚀'}\n"
            ),
        },
        "requirements.txt": "fastapi\nuvicorn\n",
    },
    "frontend": {
        "index.html": (
            "<!DOCTYPE html>\n<html>\n<head>\n"
            "  <meta charset='UTF-8'>\n"
            "  <title>Hackathon Frontend</title>\n"
            "  <script src='js/app.js' defer></script>\n"
            "</head>\n<body>\n"
            "  <h1>Sample Data</h1>\n"
            "  <ul id='data-list'></ul>\n"
            "</body>\n</html>\n"
        ),
        "js": {
            "app.js": (
                "fetch('http://localhost:8000/api/sample')\n"
                "  .then(res => res.json())\n"
                "  .then(data => {\n"
                "    const list = document.getElementById('data-list');\n"
                "    data.forEach(item => {\n"
                "      const li = document.createElement('li');\n"
                "      li.textContent = `${item.name}`;\n"
                "      list.appendChild(li);\n"
                "    });\n"
                "  })\n"
                "  .catch(err => console.error('Error fetching data:', err));\n"
            )
        },
        "css": {
            "styles.css": "body { font-family: Arial, sans-serif; }\n",
        },
    },
    "README.md": "# Hackathon Platform Skeleton\n",
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    base = os.getcwd()
    create_structure(base, structure)
    print("✅ Project skeleton created successfully!")
