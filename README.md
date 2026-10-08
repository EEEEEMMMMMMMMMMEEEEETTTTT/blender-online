# Blender Online

A small web app for uploading a Blender scene, rendering it in a headless Blender Linux container, and downloading the output image.

## Stack
- React frontend
- Flask API
- Docker Compose
- Blender 5.2.2 Linux

## Quick start

1. Clone the repo
2. Run:
   ```bash
   docker compose up --build
   ```
3. Open the frontend at:
   - http://localhost:5173
4. Upload a `.blend` file and render it.

## Architecture
- `frontend/` contains the React UI
- `backend/` contains the Flask API and Blender render invocation
- `Dockerfile` installs Blender 5.2.2 automatically from the official Blender mirror
- `docker-compose.yml` runs the frontend and backend together

## Blender download source
The Docker image uses the official Blender release mirror:
- https://download.blender.org/release/Blender5.2/blender-5.2.2-linux-x64.tar.xz

## Notes
This is a starter app, not a production cloud GPU service. It is designed to work locally and to be expanded for deployment to a cloud host when needed.
