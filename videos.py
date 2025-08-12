import yt_dlp
import os


def descargar_video_webm(link):
    def mostrar_progreso(d):
        if d['status'] == 'downloading':
            try:
                speed = d.get('speed', 0)
                if speed:
                    speed_mb = speed / (1024 * 1024)
                    speed_str = f"{speed_mb:.1f} MB/s"
                else:
                    speed_str = "-- MB/s"

                if 'total_bytes' in d and d['total_bytes']:
                    porcentaje = (d['downloaded_bytes'] / d['total_bytes']) * 100
                    print(f"\rDescargando: {porcentaje:.1f}% - {speed_str}", end='')
                else:
                    print(f"\rDescargando... - {speed_str}", end='')
            except:
                print("\rDescargando...", end='')
        elif d['status'] == 'finished':
            print(f"\n✅ Descarga completada!")

    # Configuración para WebM de alta calidad
    ydl_opts = {
        # Formato optimizado: mejor video WebM + mejor audio WebM, luego mejor WebM disponible
        'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]/bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'progress_hooks': [mostrar_progreso],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("🔍 Analizando video...")
            
            # Obtener info básica
            info = ydl.extract_info(link, download=False)
            if not info:
                print("❌ No se pudo obtener información del video")
                return
            
            title = info.get('title', 'Video')
            print(f"📹 {title}")
            
            # Descargar
            print("🚀 Descargando...")
            ydl.download([link])
            
            # Verificar archivo
            filename = ydl.prepare_filename(info)
            if os.path.exists(filename):
                size_mb = os.path.getsize(filename) / (1024 * 1024)
                ext = os.path.splitext(filename)[1]
                print(f"🎉 Listo: {os.path.basename(filename)} ({size_mb:.1f}MB)")
                print(f"📁 Formato: {ext}")
            else:
                print("🎉 Descarga completada")
                
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    print("🎬 DESCARGADOR WebM SIMPLE\n")
    
    link = input("🔗 Link del video: ").strip()
    if not link:
        print("❌ Link vacío")
        return
    
    descargar_video_webm(link)


if __name__ == "__main__":
    main()