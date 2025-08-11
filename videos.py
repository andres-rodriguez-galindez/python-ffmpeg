import yt_dlp
import subprocess
import os

def verificar_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg está instalado correctamente.")
    except Exception:
        print("FFmpeg no está instalado o no está en el PATH. Descárgalo de https://ffmpeg.org/download.html y agrégalo al PATH.")

def listar_formatos(link):
    ydl_opts = {
        'listformats': True,
        'quiet': False
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(link, download=False)
    except Exception as e:
        print(f"No se pudieron listar los formatos: {e}")

def descargar_video(link):
    def mostrar_progreso(d):
        if d['status'] == 'downloading':
            # Mostrar progreso de descarga con porcentaje y velocidad
            if 'total_bytes' in d:
                porcentaje = d['downloaded_bytes']/d['total_bytes']*100
                print(f"\rDescargando: {porcentaje:.1f}% - Velocidad: {d.get('speed', 'N/A'):.1f} bytes/s", end='')
            else:
                print(f"\rDescargando... - Velocidad: {d.get('speed', 'N/A'):.1f} bytes/s", end='')
        elif d['status'] == 'finished':
            print("\nDescarga completada, procesando...")

    ydl_opts = {
        # Selecciona la mejor calidad absoluta sin restricciones
        'format': 'bestvideo+bestaudio',
        'outtmpl': '%(title)s.%(ext)s',
        # Sin restricciones de formato para mantener calidad original
        'postprocessors': [],
        'noplaylist': True,  # Descarga solo un video, no listas completas
        'quiet': False,
        'progress_hooks': [mostrar_progreso]
    }

    # Si existe cookies.txt, usarlo para evitar errores 403
    if os.path.exists('cookies.txt'):
        ydl_opts['cookiefile'] = 'cookies.txt'
    else:
        print("Advertencia: No se encontró 'cookies.txt'. Si tienes problemas de acceso, exporta tus cookies del navegador y guárdalas como 'cookies.txt' en esta carpeta.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([link])
            if result == 0:
                print("Descarga completa.")
            else:
                print("No se pudo descargar el video. Puede que no haya formatos compatibles.")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")


if __name__ == "__main__":
    verificar_ffmpeg()
    link = str(input("Pega el link del video a descargar: ")).strip()
    if not link:
        print("No se ingresó un enlace válido.")
    else:
        listar = input("¿Quieres listar los formatos disponibles antes de descargar? (s/n): ").strip().lower()
        if listar == 's':
            print("Listando formatos disponibles...")
            listar_formatos(link)
        descargar_video(link)