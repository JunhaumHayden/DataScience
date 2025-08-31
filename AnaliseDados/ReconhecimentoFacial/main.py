import cv2
from cvzone.FaceDetectionModule import FaceDetector

# cv2: Este é o módulo principal da OpenCV, que é uma biblioteca popular de visão computacional. Ele fornece uma ampla gama de funções para processar imagens e vídeos, como leitura, exibição, manipulação e detecção de objetos.
# FaceDetector: Este é um módulo da biblioteca cvzone, que é uma coleção de ferramentas para facilitar a aplicação de técnicas de visão computacional. FaceDetector é utilizado para a detecção de rostos.

# # Inicializa a captura de vídeo
# Esta linha de código inicializa a captura de vídeo da webcam. O argumento 0 indica que a primeira câmera conectada ao sistema será utilizada (geralmente a webcam interna).
video = cv2.VideoCapture(0)

# # Verifica se a câmera foi aberta corretamente
# Adicionar verificações de erros, por exemplo, verificar se a câmera foi aberta corretamente:
if not video.isOpened():
    print("Erro ao abrir a câmera")
    exit()

# # Inicializa o detector de rostos
# Aqui, um objeto FaceDetector é instanciado para detectar rostos nas imagens capturadas.
detector = FaceDetector()

# # Loop para processar cada quadro de vídeo
# Captura de quadros:
# _, img = video.read() lê um quadro (imagem) da webcam. video.read() retorna dois valores: um booleano indicando sucesso ou falha na leitura, e o próprio quadro capturado.
# Detecção de rostos:
# imag, bboxes = detector.findFaces(img, draw=True) processa a imagem capturada para detectar rostos. Se draw=True, a função desenha caixas delimitadoras ao redor dos rostos detectados. bboxes contém as coordenadas das caixas delimitadoras dos rostos.
# Exibição do resultado:
# cv2.imshow("Resultado", img) exibe o quadro com os rostos detectados em uma janela chamada "Resultado".
# Controle para encerrar o loop:
# if cv2.waitKey(1) == 27: verifica se a tecla "Esc" (código 27) foi pressionada. Se sim, o loop é interrompido, encerrando a captura de vídeo e fechando as janelas.
while True:
    _, img = video.read()
    if img is None:
        print("Erro ao capturar o quadro")
        break

    img, bboxes = detector.findFaces(img, draw=True)
    cv2.imshow("Resultado", img)

    # Verifica se a tecla Esc foi pressionada para encerrar o loop
    if cv2.waitKey(1) == 27:
        break

# # Libera os recursos
# Ao finalizar o loop, é importante liberar os recursos da webcam e fechar todas as janelas abertas. Isso pode ser feito com:
video.release()
cv2.destroyAllWindows()
