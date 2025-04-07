import os
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from clipsai import Transcriber, ClipFinder, resize

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.post("/create_clips")
async def create_clips(video: UploadFile):
    try:
        # Save uploaded video temporarily
        temp_dir = "tmp"
        os.makedirs(temp_dir, exist_ok=True)
        video_path = f"{temp_dir}/{video.filename}"
        
        with open(video_path, "wb") as f:
            f.write(await video.read())

        # 1. Transcribe
        transcriber = Transcriber()
        transcription = transcriber.transcribe(audio_file_path=video_path)

        # 2. Find clips
        clipfinder = ClipFinder()
        clips = clipfinder.find_clips(transcription=transcription)

        # 3. Resize (optional)
        crops = resize(
            video_file_path=video_path,
            pyannote_auth_token=os.getenv("PYANNOTE_AUTH_TOKEN"),
            aspect_ratio=(9, 16)
        )

        # Cleanup
        os.remove(video_path)

        return JSONResponse({
            "clips": [{"start": clip.start_time, "end": clip.end_time} for clip in clips],
            "crops": crops.segments
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check
@app.get("/")
def health_check():
    return {"status": "running"}