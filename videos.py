import yt_dlp

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

link = str(input("Pega el link del video a descargar: ")).strip()

print("Listando formatos disponibles...")
listar_formatos(link)

descargar_video(link)