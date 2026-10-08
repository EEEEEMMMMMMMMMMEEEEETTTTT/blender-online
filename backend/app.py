import os
import uuid
from pathlib import Path

from flask import Flask, jsonify, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

BLENDER_BIN = "/opt/blender/blender"


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/render")
def render_blend():
    if "blend_file" not in request.files:
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files["blend_file"]
    if file.filename == "":
        return jsonify({"error": "No selected file."}), 400

    filename = secure_filename(file.filename)
    if not filename.lower().endswith(".blend"):
        return jsonify({"error": "Only .blend files are allowed."}), 400

    job_id = str(uuid.uuid4())
    input_dir = UPLOAD_DIR / job_id
    output_dir = OUTPUT_DIR / job_id
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    blend_path = input_dir / filename
    file.save(blend_path)

    output_prefix = output_dir / "render_"

    command = [
        BLENDER_BIN,
        "-b",
        str(blend_path),
        "-o",
        str(output_prefix),
        "-F",
        "PNG",
        "-f",
        "1",
    ]

    try:
        import subprocess

        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return jsonify({
                "error": "Blender render failed",
                "stderr": result.stderr,
                "stdout": result.stdout,
            }), 500

        rendered_files = list(output_dir.glob("render_*.png"))
        if not rendered_files:
            return jsonify({"error": "Render completed but no PNG file was created."}), 500

        return jsonify({
            "job_id": job_id,
            "filename": filename,
            "rendered_file": rendered_files[0].name,
            "download_url": f"/api/download/{job_id}",
        })

    except FileNotFoundError:
        return jsonify({"error": f"Blender executable not found at {BLENDER_BIN}."}), 500


@app.get("/api/download/<job_id>")
def download_render(job_id):
    output_dir = OUTPUT_DIR / job_id
    files = sorted(output_dir.glob("render_*.png"))
    if not files:
        return jsonify({"error": "No render file found for this job."}), 404

    return send_file(files[0], as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
