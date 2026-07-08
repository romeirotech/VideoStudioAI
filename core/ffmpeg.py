import subprocess
import os


class FFmpeg:

    @staticmethod
    def check():

        try:

            subprocess.run(
                ["ffmpeg", "-version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )

            return True

        except:

            return False

    @staticmethod
    def nvenc():

        try:

            resultado = subprocess.run(
                ["ffmpeg", "-encoders"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            return "h264_nvenc" in resultado.stdout

        except:

            return False

    @staticmethod
    def convert(input_file, output_file):

        comando = [

            "ffmpeg",

            "-y",

            "-hwaccel",
            "cuda",

            "-i",
            input_file,

            "-vf",
            "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",

            "-c:v",
            "h264_nvenc",

            "-preset",
            "p4",

            "-b:v",
            "8M",

            "-c:a",
            "aac",

            output_file

        ]

        subprocess.run(comando)