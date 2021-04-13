# https://ffmpeg.zeranoe.com/builds

"""
Script
ffmpeg -i "ENTRADA -i "LEGENDA" -c:v libx264 -crf 23 -present ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 a -map 1:0 -ss 00:00:00 -to 00:01:00 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg/ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:01:00'

caminho_origem = os.getcwd()
print(caminho_origem)
caminho_destino = os.getcwd()

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch('arquivo', '*.mkv'):
            continue
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i"{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        nome_novo_arquivo = nome_arquivo + 'NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i"{caminho_completo}" {input_legenda}' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}' \
            f'{debug} {map_legenda} "{arquivo_saida}"'

        print(comando)

        os.system(comando)