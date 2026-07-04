import subprocess
import json
import os


class VideoInfo:

    @staticmethod
    def get(video):

        cmd = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_streams",
            "-show_format",
            video
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        data = json.loads(result.stdout)

        stream = data["streams"][0]
        fmt = data["format"]

        fps = stream["r_frame_rate"]

        if "/" in fps:
            a, b = fps.split("/")
            fps = round(float(a) / float(b), 2)

        return {

            "arquivo": os.path.basename(video),

            "largura": stream["width"],

            "altura": stream["height"],

            "fps": fps,

            "duracao": round(float(fmt["duration"]), 1),

            "tamanho": round(int(fmt["size"]) / 1024 / 1024, 2)

        }