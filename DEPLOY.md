# Deployment Guide

This guide covers deploying **Blender Online** to various free cloud hosting services.

## Option 1: Render (Recommended)

**Render** is the easiest and most beginner-friendly option with a permanent free tier.

### Steps:

1. **Go to Render**: https://render.com
2. **Sign up** with your GitHub account
3. **Create new Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo (`blender-online`)
   - Select the repo and authorize
4. **Configure**:
   - **Name**: `blender-online`
   - **Environment**: `Docker`
   - **Region**: US (or closest to you)
   - **Plan**: Free
5. **Deploy**:
   - Click "Create Web Service"
   - Render will build and deploy automatically
   - Your app will be live at a URL like: `https://blender-online-xxxxx.onrender.com`

### Notes:
- Free tier apps sleep after 15 minutes of inactivity
- They wake up when you visit, but take a few seconds to start
- No credit card required (optional for paid upgrades)
- Automatic redeploys when you push to GitHub

---

## Option 2: Google Cloud Run

**Google Cloud Run** offers $300 free credit for 90 days and a permanent free tier (2M requests/month).

### Steps:

1. **Go to Google Cloud**: https://console.cloud.google.com
2. **Sign up** with your Google account
3. **Enable Cloud Run API**:
   - Search "Cloud Run" in the console
   - Click "Enable"
4. **Create Service**:
   - Click "Create Service"
   - Select "Continuously deploy from a Git repository"
   - Connect GitHub → select `blender-online` repo
   - Set runtime to `Docker`
5. **Configure**:
   - **Service name**: `blender-online`
   - **Region**: `us-central1`
   - **Autoscaling**: Min instances 0, Max 100
   - **Memory**: 512 MB
6. **Deploy**:
   - Click "Create"
   - Google will build and deploy
   - You get a live URL like: `https://blender-online-xxxxx.run.app`

### Notes:
- $300 credit covers most hobby projects indefinitely
- After 90 days, you only pay for what you use
- Free tier: 2M requests/month (usually free for small projects)
- Faster cold starts than Render
- Requires credit card (but no automatic charges)

---

## Option 3: Koyeb

**Koyeb** offers 2 free services permanently with no credit card required.

### Steps:

1. **Go to Koyeb**: https://www.koyeb.com
2. **Sign up** with GitHub
3. **Create App**:
   - Click "Create a new app"
   - Select "Docker" deployment
   - Connect to your GitHub repo
4. **Configure**:
   - **Repository**: `EEEEEMMMMMMMMMMEEEEETTTTT/blender-online`
   - **Branch**: `main`
   - **Dockerfile**: `./Dockerfile`
   - **Port**: `5000`
5. **Deploy**:
   - Click "Deploy"
   - Koyeb builds and deploys automatically
   - Your app is live at a URL like: `https://blender-online-xxxxx.koyeb.app`

### Notes:
- Permanent free tier (2 services)
- No credit card required
- Fast deployments, no cold starts
- Great documentation
- Automatic redeploys on push to GitHub

---

## Option 4: Fly.io

**Fly.io** provides free credits and global deployment with Docker support.

### Steps:

1. **Go to Fly.io**: https://fly.io
2. **Sign up** with GitHub
3. **Install Fly CLI** (or use web dashboard):
   - Visit https://fly.io/dashboard
4. **Create App**:
   - Click "Launch an app"
   - Connect GitHub repo
5. **Configure**:
   - **App name**: `blender-online`
   - **Region**: Closest to you
6. **Deploy**:
   - Click "Deploy"
   - Fly builds and launches your app
   - URL like: `https://blender-online.fly.dev`

### Notes:
- Free tier with generous credits
- Very fast deployments
- Global edge network (deploy near your users)
- CLI-based workflow (slightly more advanced)

---

## Option 5: AWS (Elastic Container Service / Lightsail)

**AWS** offers free tier with more setup but powerful features.

### Steps:

1. **Go to AWS**: https://aws.amazon.com
2. **Sign up** with email/account
3. **Use Elastic Container Service (ECS)**:
   - Navigate to ECS console
   - Create cluster → select Fargate (serverless)
   - Register task definition with your Docker image
   - Create service from task definition
4. **Alternative: AWS Lightsail**:
   - Simpler option for containers
   - Navigate to Lightsail → Containers
   - Create container service → connect GitHub repo
5. **Deploy**:
   - AWS builds and deploys
   - Public endpoint provided

### Notes:
- Free tier: 750 hours/month of compute
- Covers small hobby projects indefinitely
- More complex setup than others
- Powerful for scaling later
- Requires credit card

---

## Comparison Table

| Service | Free Tier | Credit Card | Setup Difficulty | Cold Start |
|---------|-----------|-------------|------------------|-----------|
| **Render** | Permanent | No | Very Easy | ~30s |
| **Google Cloud Run** | $300 credit (90 days) | Yes | Easy | Fast |
| **Koyeb** | Permanent (2 apps) | No | Very Easy | None |
| **Fly.io** | Free credits | No | Moderate | Fast |
| **AWS** | Free tier limited | Yes | Hard | Depends |

---

## Recommended Path for You

1. **Start with Render** (simplest, no credit card)
2. **Keep Koyeb as backup** (also no credit card)
3. **Use Google Cloud Run** if you want more power and have a credit card

---

## After Deployment

Once your app is live:

1. **Test it**:
   - Visit the live URL in your browser
   - Upload a `.blend` file
   - Click "Render scene"
   - Download the rendered PNG

2. **Troubleshoot**:
   - Check service logs in the dashboard
   - Common issues: port mismatch, missing environment variables, Blender not installing

3. **Update the app**:
   - Push changes to GitHub
   - Service auto-redeploys (usually within 1-5 minutes)

---

## Next Steps

Pick one service and follow the steps above. If you get stuck on any step, let me know the error message or what service you chose, and I can help debug!
