from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import openai

# Set your OpenAI API key directly (you can secure this later with environment variables)
openai.api_key = ""
app = FastAPI(
    title="DocGenie",
    version="0.1.0",
    description="Generate code documentation with AI."
)

# Enable CORS for frontend apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder (for index.html, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_ui():
    return FileResponse("index.html")

# Input model
class CodeInput(BaseModel):
    code: str
    language: str

@app.post("/generate-doc")
async def generate_doc(input: CodeInput):
    if not input.code.strip():
        return JSONResponse(status_code=422, content={"error": "Code cannot be empty."})

    prompt = f"""
    Generate clean, well-formatted, and human-readable documentation for the following {input.language} code:

    {input.code}

    Make sure to include function descriptions, parameter details, return types, and usage examples if needed.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a senior software engineer who writes excellent code documentation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        doc = response.choices[0].message.content.strip()
        return {"documentation": doc}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
