import os
import subprocess


class Converter:

    @staticmethod
    def to_reels(video):

        pasta_saida = "output"

        os.makedirs(pasta_saida, exist_ok=True)

        nome = os.path.splitext(os.path.basename(video))[0]

        saida = os.path.join(
            pasta_saida,
            nome + "_REELS.mp4"
        )

        filtro = (
            "[0:v]split=2[fg][bg];"
            "[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
            "boxblur=20:10,"
            "crop=1080:1920[blur];"
            "[fg]scale=1080:1920:force_original_aspect_ratio=decrease[front];"
            "[blur][front]overlay=(W-w)/2:(H-h)/2"
        )

        comando = [

            "ffmpeg",

            "-y",

            "-i", video,

            "-filter_complex", filtro,

            "-c:v", "h264_nvenc",

            "-preset", "p4",

            "-b:v", "8M",

            "-c:a", "aac",

            "-b:a", "192k",

            saida

        ]

        subprocess.run(comando)

        return saida