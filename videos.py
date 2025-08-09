import yt_dlp
import subprocess

def verificar_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg está instalado correctamente.")
    except Exception:
        print("FFmpeg no está instalado o no está en el PATH. Descárgalo de https://ffmpeg.org/download.html y agrégalo al PATH.")

def listar_formatos(link):
    ydl_opts = {
        'listformats': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(link, download=False)

def descargar_video(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("Descarga Completa")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

verificar_ffmpeg()
link = str(input("Pega el link del video a descargar: ")).strip()

print("Listando formatos disponibles...")
listar_formatos(link)

descargar_video(link)