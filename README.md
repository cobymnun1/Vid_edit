# Video to Shorts Editor

A web application that lets users upload long-form videos and create short-form clips automatically using ClipsAI.

## Project Structure

- **Backend**: Python FastAPI service using ClipsAI for video processing
- **Frontend**: Next.js React application for the user interface

## Setup Instructions

### Backend Deployment (Railway)

1. Create a Railway account at https://railway.app/
2. Install Railway CLI: `npm i -g @railway/cli`
3. Login: `railway login`
4. Initialize project: `cd backend && railway init`
5. Create a new project and add environment variables:
   - `PYANNOTE_AUTH_TOKEN=your_token_here`
   - (add other required tokens from your .env file)
6. Deploy: `railway up`

### Frontend Deployment (Vercel)

1. Create a Vercel account at https://vercel.com/
2. Install Vercel CLI: `npm i -g vercel`
3. Login: `vercel login`
4. Navigate to frontend directory: `cd frontend`
5. Deploy: `vercel`
6. During deployment, set the environment variable:
   - `NEXT_PUBLIC_API_URL=your_railway_app_url`

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Using the Application

1. Upload a video through the interface
2. Wait for the AI to process the video
3. View and save the generated short clips

## Technologies Used

- **ClipsAI**: AI-powered video processing
- **FastAPI**: Backend API framework
- **Next.js**: React framework for the frontend
- **Railway**: Backend hosting
- **Vercel**: Frontend hosting 