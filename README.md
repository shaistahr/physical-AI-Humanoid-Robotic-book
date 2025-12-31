# Physical AI & Humanoid Robotics Book with RAG Chatbot

**First Physical Humanoid Robotics Educational Platform with Integrated RAG Chatbot**

By Shazz Khan

## 🚀 Features

- 📚 **Comprehensive Documentation**: Interactive Docusaurus website covering Physical AI & Humanoid Robotics
- 🤖 **RAG Chatbot**: Intelligent Q&A chatbot powered by Gemini AI
- 🎨 **Modern UI**: Beautiful blue and purple theme
- 💬 **Real-time Learning**: Get instant answers about robotics concepts
- 🔓 **Open Source**: Free and accessible to everyone

## 📋 Prerequisites

- **Node.js** >= 20.0
- **Python** >= 3.11
- **Git**
- **Gemini API Key** (or OpenAI API Key)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shaistahr/Physical-ai-robotics-book.git
cd Physical-ai-robotics-book
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your API keys
```

### 3. Website Setup

```bash
cd website
npm install
```

## 🎯 Running the Project

### Start Backend Server

```bash
cd backend
venv\Scripts\python main.py
```

The backend will run on `http://localhost:8000`

### Start Website

```bash
cd website
npm start
```

The website will run on `http://localhost:3000` (or `http://localhost:3001` if 3000 is busy)

## 🔧 Configuration

### Environment Variables (backend/.env)

```env
# AI Service
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Database
DATABASE_URL=sqlite:///./rag_chatbot.db

# Vector Database (Optional)
QDRANT_URL=http://localhost:6333

# Application
DEBUG=true
LOG_LEVEL=info
```

### Changing the Front Page Image

1. Add your image to: `website/static/img/`
2. Update the image path in `website/src/pages/index.js`:

```javascript
<img
  src="/img/your-image-name.jpg"  // Change this
  alt="Book"
  style={styles.bookImage}
/>
```

### Initializing the RAG Chatbot

To make the chatbot functional, you need to initialize it with content:

```bash
curl -X POST http://localhost:8000/api/initialize \
  -H "Content-Type: application/json" \
  -d '{"content_url": "https://your-documentation-url.com"}'
```

## 🎨 Theme Customization

The theme uses a blue and purple color scheme. To customize:

- Edit `website/src/css/custom.css` for global colors
- Edit `website/src/pages/index.js` for homepage styling

## 📦 Deployment

### Deploy to GitHub Pages

```bash
cd website
npm run build
GIT_USER=shaistahr npm run deploy
```

### Deploy Backend

For production deployment, consider:
- **Heroku**
- **Railway**
- **Render**
- **AWS/Azure/GCP**

## 📖 Project Structure

```
Physical-ai-robotics-book/
├── backend/              # FastAPI backend with RAG chatbot
│   ├── api/             # API endpoints
│   ├── services/        # Business logic
│   ├── models/          # Database models
│   └── main.py          # Entry point
├── website/             # Docusaurus frontend
│   ├── docs/            # Documentation content
│   ├── src/             # React components
│   │   ├── components/  # Chat components
│   │   ├── pages/       # Page components
│   │   └── css/         # Styling
│   └── static/          # Static assets
└── specs/               # Feature specifications

```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Shazz Khan**
- GitHub: [@shaistahr](https://github.com/shaistahr)

## 🙏 Acknowledgments

- Built with [Docusaurus](https://docusaurus.io/)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- AI by [Google Gemini](https://deepmind.google/technologies/gemini/)

---

**Note**: This is the first educational platform combining Physical AI & Humanoid Robotics content with an integrated RAG chatbot for interactive learning.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
