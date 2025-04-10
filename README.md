# 🧠 DocGenie

**DocGenie** is an AI-powered code documentation generator that automatically creates clean and intelligent documentation for your code in multiple programming languages. Whether you're working with Python, JavaScript, Java, C++, or C#, DocGenie helps you stay focused by handling the documentation process for you.

---

## 🌐 Live Preview

A modern web interface for developers to:

- Paste their code
- Choose a programming language
- Generate documentation with AI
- Download the result as a beautiful PDF

---

## 📁 Project Structure

```
docgenie/
├── main.py          # Backend - Flask server for AI documentation generation
├── templates/
│   └── index.html   # Frontend UI with responsive layout and PDF download support
├── static/          # (Optional) Static files (CSS, JS, logo etc.)
└── README.md        # Project documentation
```

---

## 🚀 Features

- 🔍 AI-based code analysis and documentation
- 🌐 Clean, responsive web interface
- 📅 One-click PDF download of the generated documentation
- 💡 Syntax highlighting for better readability
- 🧑‍💻 Supports multiple languages: Python, JavaScript, Java, C++, C#

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript, Highlight.js, Marked.js, html2pdf.js
- **Backend:** Python, Flask
- **AI Model:** OpenAI / Local LLM (You can plug your own)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/udaykonanki1/Docgenie.git
cd docgenie
```

### 2. Create and activate a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> Make sure you have access to an AI model or API like OpenAI.

### 4. Run the Flask server

```bash
python main.py
```

### 5. Open the app

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📄 API Endpoint

- **POST** `/generate-doc`\
  Accepts JSON with `code` and `language` fields and returns AI-generated documentation.

```json
{
  "code": "def hello(): print('Hello')",
  "language": "python"
}
```

Returns:

```json
{
  "documentation": "### Function: hello()\nThis function prints 'Hello' to the console..."
}
```

---

## 📅 Download PDF Feature

After generating documentation, click the **📅 Download** button to export your results as a PDF using `html2pdf.js`.

---

## 📸 Screenshots

> *(Include screenshots of UI here if available)*

---

## ✨ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📬 Contact

Made with ❤️ by [Uday](https://github.com/udaykonanki1/)

For suggestions, bugs, or feedback:\
📧 [your-email@example.com](mailto\:udaykumar.konanki@gmail.com)

