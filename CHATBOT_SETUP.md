# RAG Chatbot Setup & Troubleshooting Guide

## ✅ What Was Fixed

### The Problem
The chatbot wasn't replying because:
1. **Not initialized** - No content loaded into the knowledge base
2. **Using OpenAI only** - System was hardcoded to use OpenAI API
3. **No Gemini support** - Your Gemini API key wasn't being used

### The Solution
1. ✅ **Added Gemini Support** - Now uses your Gemini API key for:
   - Text embeddings (`embedding-001` model)
   - Response generation (`gemini-pro` model)
2. ✅ **Auto-detect AI Service** - Automatically uses Gemini when Gemini API key is present
3. ✅ **Content Initialization** - Set up to load Wikipedia article about Humanoid Robots

## 🚀 How the Chatbot Works Now

### 1. Content Source
The chatbot is initialized with: `https://en.wikipedia.org/wiki/Humanoid_robot`

You can change this in `backend/.env`:
```env
CONTENT_URL=https://your-documentation-url.com
```

### 2. Initialization Process
When you run initialization, the system:
1. Scrapes content from the URL
2. Cleans and chunks the content
3. Generates Gemini embeddings for each chunk
4. Stores embeddings in Qdrant vector database
5. Makes the chatbot ready to answer questions

### 3. Query Process
When a user asks a question:
1. Question is converted to embedding (Gemini)
2. Similar content chunks are retrieved from vector DB
3. Gemini generates a response based on retrieved context
4. Response is returned with source links

## 📝 Manual Initialization

If needed, you can manually initialize:

```bash
# Navigate to backend
cd backend

# Run initialization script
python initialize_chatbot.py
```

Or via curl:
```bash
curl -X POST http://localhost:8000/api/initialize
```

## 🔍 Check Chatbot Status

```bash
curl http://localhost:8000/api/status
```

Expected response when ready:
```json
{
  "initialized": true,
  "content_source": "https://en.wikipedia.org/wiki/Humanoid_robot",
  "status": "completed"
}
```

## 🎨 Using Different Content Sources

### Option 1: Your Own Documentation
```env
CONTENT_URL=http://localhost:3001/docs/intro
```

### Option 2: External Documentation
```env
CONTENT_URL=https://docs.example.com/getting-started
```

### Option 3: GitHub README
```env
CONTENT_URL=https://raw.githubusercontent.com/shaistahr/Physical-ai-robotics-book/master/README.md
```

## 🐛 Troubleshooting

### Chatbot Still Not Responding

1. **Check backend is running:**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Check initialization status:**
   ```bash
   curl http://localhost:8000/api/status
   ```

3. **Check backend logs:**
   - Look at the terminal where backend is running
   - Check `backend/logs/` directory

### "Not Initialized" Error

Run initialization:
```bash
curl -X POST http://localhost:8000/api/initialize
```

Wait 1-2 minutes for it to complete.

### Gemini API Errors

1. **Check API key** in `backend/.env`
2. **Verify quota** at https://makersuite.google.com/app/apikey
3. **Check rate limits** - Gemini has usage limits

### Qdrant Connection Error

The system uses in-memory vector storage by default. If you see Qdrant errors, it will fallback gracefully.

## 🔑 API Keys

### Current Setup (Gemini)
```env
GEMINI_API_KEY=AIzaSyD2XWPb2pwhtoZE7N3kPVjAxpLFPwRUFw0
```

### Optional: Add OpenAI Support
```env
OPENAI_API_KEY=sk-your-real-key-here
```

System will prioritize Gemini if both are present.

## 📊 Testing the Chatbot

### Test via API
```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is a humanoid robot?"}'
```

### Test via Website
1. Open `http://localhost:3001`
2. Click the chat button (bottom right)
3. Ask: "What are humanoid robots?"

## 🎯 Expected Behavior

**First Query:** Might take 2-3 seconds (embedding generation)
**Subsequent Queries:** Should respond in <1 second
**Response Quality:** Based on content from the initialized URL

## 📈 Improving Response Quality

1. **Better Content Source:**
   - Use comprehensive documentation
   - Well-structured content works best

2. **More Content:**
   - Initialize with multiple URLs (modify initialization code)
   - Add more relevant documentation

3. **Better Prompts:**
   - Ask specific questions
   - Include context in your query

## 🔄 Reinitializing

To load new content:
1. Stop backend server (Ctrl+C)
2. Update `CONTENT_URL` in `.env`
3. Restart backend
4. Run initialization again

---

**Status:** Chatbot is now configured with Gemini and ready to use!

**Next Steps:**
1. Wait for current initialization to complete (~2 minutes)
2. Test with a query via the website
3. Optionally change CONTENT_URL to your own docs
