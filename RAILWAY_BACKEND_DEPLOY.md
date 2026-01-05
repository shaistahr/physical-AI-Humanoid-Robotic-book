# Deploy Backend to Railway - Step by Step

**Railway**: https://railway.app/new (Now open in your browser)

---

## 🚀 Quick Deployment Steps

### **Step 1: Sign In to Railway**

1. Click **"Login"** on Railway
2. Choose: **"Login with GitHub"**
3. Authorize Railway to access your repositories
4. You'll be redirected to Railway dashboard

---

### **Step 2: Create New Project**

1. Click **"New Project"**
2. Select: **"Deploy from GitHub repo"**
3. Find and select: `shaistahr/physical-AI-Humanoid-Robotic-book`
4. Click the repository to import it

---

### **Step 3: Configure Root Directory** ⚠️ CRITICAL

After selecting the repository:

1. Railway will start analyzing
2. Click **"Configure"** or **"Settings"**
3. Find **"Root Directory"** setting
4. Set it to: `backend`
5. Click **"Save"** or **"Update"**

**Why?** Your backend code is in the `backend/` folder, not the root.

---

### **Step 4: Set Environment Variables** 🔑

Railway needs your API keys and configuration:

1. Go to **"Variables"** tab
2. Click **"+ New Variable"**
3. Add each of these:

```env
GEMINI_API_KEY=AIzaSyD2XWPb2pwhtoZE7N3kPVjAxpLFPwRUFw0
DATABASE_URL=sqlite:///./rag_chatbot.db
CORS_ORIGINS=https://physical-ai-humanoid-robotic-book.vercel.app,http://localhost:3000
JWT_SECRET=railway-production-secret-change-this
DEBUG=false
LOG_LEVEL=info
CONTENT_URL=https://en.wikipedia.org/wiki/Humanoid_robot
```

**How to add**:
- Click "+ New Variable"
- Name: `GEMINI_API_KEY`
- Value: `AIzaSyD2XWPb2pwhtoZE7N3kPVjAxpLFPwRUFw0`
- Click "Add"
- Repeat for each variable

**Important**: Update `CORS_ORIGINS` with your actual Vercel URL!

---

### **Step 5: Deploy!**

1. Click **"Deploy"** button
2. Railway will:
   - ✅ Install Python dependencies
   - ✅ Set up the environment
   - ✅ Start your FastAPI server
   - ✅ Generate a public URL

3. **Wait** (5-10 minutes for first deployment)
4. Watch the build logs for any errors

---

### **Step 6: Get Your Backend URL**

After deployment succeeds:

1. Go to **"Settings"** tab
2. Find **"Domains"** section
3. Click **"Generate Domain"**
4. Railway will give you a URL like:
   ```
   https://your-project-name.up.railway.app
   ```
5. **Copy this URL!** You'll need it for the frontend.

---

## ✅ Checklist Before Deploying

- [ ] Signed in to Railway with GitHub
- [ ] Repository imported: `physical-AI-Humanoid-Robotic-book`
- [ ] Root directory set to: `backend`
- [ ] All environment variables added
- [ ] CORS_ORIGINS includes your Vercel URL
- [ ] Deployment started

---

## 🔧 After Deployment

### Test Your Backend

1. Open: `https://your-backend-url.railway.app/health`
2. Should see: `{"status":"healthy"}`

3. Test API docs: `https://your-backend-url.railway.app/docs`
4. Interactive Swagger UI should load

### Initialize the Chatbot

```bash
curl -X POST https://your-backend-url.railway.app/api/initialize
```

Wait ~2 minutes for it to process the content.

---

## 🌐 Update Frontend

After backend is deployed, update your frontend:

**File**: `website/src/rag-chatbot-config.js`

Change:
```javascript
apiBaseUrl: 'http://localhost:8000/api'
```

To:
```javascript
apiBaseUrl: 'https://your-backend-url.railway.app/api'
```

Then push to GitHub - Vercel will auto-deploy!

---

## 🆘 Troubleshooting

### Build Failed

**Check build logs**:
- Look for missing dependencies
- Python version issues
- Import errors

**Common fixes**:
- Ensure `requirements.txt` is correct
- Check Python version (should be 3.11+)
- Verify all imports work

### "Application Error"

**Check runtime logs**:
- Click "View Logs"
- Look for startup errors
- Check environment variables are set

### CORS Errors

Make sure `CORS_ORIGINS` includes:
- Your Vercel production URL
- `http://localhost:3000` for local testing

Format:
```
https://your-site.vercel.app,http://localhost:3000
```

### Database Issues

SQLite works but for production consider:
- PostgreSQL (Railway provides free)
- Update `DATABASE_URL` to Postgres URL

---

## 💾 Database Persistence

**Important**: Railway ephemeral storage means SQLite data can be lost.

**For production**:

1. In Railway dashboard, click "+ New"
2. Select "Database" → "PostgreSQL"
3. Railway creates a database
4. Copy the `DATABASE_URL`
5. Update your environment variable
6. Backend will automatically use PostgreSQL

---

## 📊 Monitoring

Railway provides:
- **Logs**: Real-time application logs
- **Metrics**: CPU, Memory, Network usage
- **Deployments**: History of all deployments

Access from your project dashboard.

---

## 💰 Pricing

**Free Tier**:
- $5 credit per month
- Enough for development/testing
- ~500 hours of runtime

**Pro Plan** ($20/month):
- More resources
- Better support
- Production workloads

Start with free tier, upgrade if needed!

---

## 🔄 Auto-Deployments

After initial setup:
- Every push to `master` = Auto-deploy
- Railway watches your GitHub repo
- Automatic builds and deployments

Same workflow as Vercel!

---

## 🎯 What to Tell Me

After each step:
- **"Signed in"** - Railway authentication done
- **"Project created"** - Repository imported
- **"Variables set"** - Environment configured
- **"Deployed"** - Build successful
- **"Got URL"** - Backend URL copied

Or if issues:
- **"Error: [describe what happened]"**

---

**Ready?** Open Railway and let's get started! 🚀

After deployment, come back with your Railway backend URL!
