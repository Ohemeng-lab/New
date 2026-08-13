# Flask + Vercel + GitHub

A Flask application configured for deployment on Vercel using GitHub.

## 📁 Project Structure

```
your-repo/
├── api/
│   └── index.py          # Flask app
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🚀 Quick Start

### 1. Create GitHub Repository

```bash
# Create a new folder
mkdir my-flask-vercel
cd my-flask-vercel

# Initialize Git
git init
git branch -M main

# Add files (download from the provided files)
# Place api/index.py in an 'api' folder
# Place requirements.txt, vercel.json, .gitignore in root

# Commit and push
git add .
git commit -m "Initial commit: Flask setup for Vercel"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Connect to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click **"Add New Project"**
4. Select your repository from GitHub
5. Vercel auto-detects `vercel.json`
6. Click **"Deploy"** ✨

### 3. Your App is Live!

- **Main URL**: `https://your-project.vercel.app`
- **API Endpoint**: `https://your-project.vercel.app/api/hello`
- **Status Check**: `https://your-project.vercel.app/api/status`

## 🔧 Local Development

```bash
# Install Vercel CLI
npm install -g vercel

# Install Python dependencies
pip install -r requirements.txt

# Run locally with Vercel environment
vercel dev

# Visit http://localhost:3000
```

Or use Flask directly:
```bash
export FLASK_APP=api/index.py
export FLASK_ENV=development
python -m flask run
```

## 📝 Adding Routes

Edit `api/index.py`:

```python
@app.route('/api/custom')
def custom():
    return jsonify({"custom": "response"})
```

Push to GitHub and Vercel auto-deploys! 🎉

## 🔐 Environment Variables

1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add variables (e.g., `DATABASE_URL`, `API_KEY`)
3. Vercel auto-redeploys with new variables

Access in code:
```python
import os
secret = os.getenv('MY_SECRET_KEY')
```

## 📚 Useful Links

- [Flask Docs](https://flask.palletsprojects.com/)
- [Vercel Python Runtime](https://vercel.com/docs/runtimes/python)
- [Vercel Deployment Docs](https://vercel.com/docs/concepts/deployments/overview)

## ✅ Auto-Deploy from GitHub

Every push to `main` branch automatically redeploys:

```bash
git add .
git commit -m "Update Flask routes"
git push origin main  # ← Vercel redeploys automatically
```

Check deployment logs in Vercel Dashboard.

---

Happy coding! 🚀
