import yt_dlp

def descargar_video(link):
    ydl_opts={
        'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl':'%(title)s.%(ext)s',
        'merge_output_format':'mp4',

        'postprocessors':[
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
        print(f"Hubo un problema al descargar:  {e}")

link=str(input("pega el link del video a descargar: ")).strip()

descargar_video(link)