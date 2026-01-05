# Vercel Deployment Guide

Complete guide to deploy your Physical AI Robotics Book to Vercel.

## Prerequisites

- GitHub account: `shaistahr`
- Vercel account (sign up at https://vercel.com)
- Git installed locally

---

## Step 1: Create GitHub Repository

### Option A: Create New Repository on GitHub

1. Go to https://github.com/new
2. **Repository name**: `Physical-ai-robotics-book`
3. **Description**: `Physical AI & Humanoid Robotics Educational Platform with RAG Chatbot`
4. **Visibility**: Public (recommended) or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **Create repository**

### Option B: If Repository Already Exists

If you already have the repository, you may need to update the remote URL:

```bash
git remote set-url origin https://github.com/shaistahr/Physical-ai-robotics-book.git
```

---

## Step 2: Push to GitHub

Once the repository is created on GitHub, push your code:

```bash
# Make sure you're in the project root
cd C:\Users\SHAZ\physical-AI-humanoid-Robotic-book

# Push to GitHub
git push -u origin master
```

If you encounter authentication issues:

```bash
# For Windows, you may need to set up Personal Access Token
# Go to: https://github.com/settings/tokens
# Generate new token with 'repo' permissions
# Use the token as password when prompted
```

---

## Step 3: Deploy to Vercel

### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Sign in to Vercel**
   - Go to https://vercel.com
   - Sign in with GitHub account

2. **Import Project**
   - Click **Add New Project**
   - Select **Import Git Repository**
   - Authorize Vercel to access your GitHub
   - Select repository: `shaistahr/Physical-ai-robotics-book`

3. **Configure Project**
   - **Framework Preset**: Docusaurus 2
   - **Root Directory**: `website` ⚠️ IMPORTANT!
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
   - **Install Command**: `npm install`

4. **Environment Variables** (Optional)
   - You can add these later if needed
   - For static site, no env vars needed initially

5. **Deploy**
   - Click **Deploy**
   - Wait for build to complete (2-3 minutes)
   - Your site will be live at: `https://physical-ai-robotics-book.vercel.app`

### Method 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Navigate to website directory
cd website

# Login to Vercel
vercel login

# Deploy
vercel

# For production deployment
vercel --prod
```

---

## Step 4: Configure Custom Domain (Optional)

1. In Vercel Dashboard, go to your project
2. Click **Settings** → **Domains**
3. Add your custom domain
4. Follow DNS configuration instructions

---

## Deployment Configuration Files

The following files have been created for optimal Vercel deployment:

### `vercel.json` (Root)
- Configures monorepo deployment
- Specifies build commands and output directories

### `website/vercel.json`
- Framework-specific configuration
- Optimized for Docusaurus 2

### `.vercelignore`
- Excludes backend, database, and unnecessary files
- Reduces deployment size and build time

---

## Environment Variables for Vercel

If you want to add backend API integration later:

```bash
# In Vercel Dashboard → Settings → Environment Variables
NEXT_PUBLIC_API_URL=https://your-backend-api.com
```

**Note**: The RAG chatbot backend needs separate deployment (see Backend Deployment section)

---

## Backend Deployment (Separate)

The backend (FastAPI) should be deployed separately:

### Recommended Platforms for Backend:
1. **Railway** (https://railway.app) - Easiest
2. **Render** (https://render.com) - Free tier available
3. **Heroku** (https://heroku.com)
4. **AWS/Azure/GCP** - Production scale

### Quick Backend Deployment to Railway:

1. Go to https://railway.app
2. Sign in with GitHub
3. New Project → Deploy from GitHub
4. Select repository: `Physical-ai-robotics-book`
5. Set **Root Directory**: `backend`
6. Railway will auto-detect Python/FastAPI
7. Add environment variables:
   - `GEMINI_API_KEY`
   - `DATABASE_URL`
   - `CORS_ORIGINS` (add your Vercel URL)
8. Deploy

Once backend is deployed, update frontend config:
- Edit `website/src/rag-chatbot-config.js`
- Change `apiBaseUrl` to your backend URL

---

## Automatic Deployments

Vercel automatically deploys:
- **Production**: When you push to `master` branch
- **Preview**: When you create a pull request

Every commit triggers a new deployment!

---

## Troubleshooting

### Build Fails

**Error: "Command failed: npm run build"**
- Check that `website/package.json` exists
- Verify root directory is set to `website`
- Check build logs for specific errors

### 404 Errors

- Ensure output directory is `build`
- Check that Docusaurus built successfully locally

### Slow Build Times

- Builds take 2-5 minutes normally
- Check for large dependencies
- Review `.vercelignore` to exclude unnecessary files

---

## Project URLs

After deployment, you'll have:

- **Production**: `https://physical-ai-robotics-book.vercel.app`
- **Preview**: `https://physical-ai-robotics-book-git-[branch].vercel.app`
- **GitHub**: `https://github.com/shaistahr/Physical-ai-robotics-book`

---

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Deploy to Vercel
3. 🔄 Deploy backend to Railway/Render
4. 🔄 Update frontend API URL
5. 🔄 Test chatbot functionality
6. 🔄 Add custom domain (optional)

---

## Support

- **Vercel Docs**: https://vercel.com/docs
- **Docusaurus Docs**: https://docusaurus.io/docs/deployment
- **GitHub Issues**: https://github.com/shaistahr/Physical-ai-robotics-book/issues

---

**Generated with Claude Code** 🤖
