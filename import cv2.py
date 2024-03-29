import cv2

# Inicializa o objeto de captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Mostra o frame capturado
    cv2.imshow('Camera do Celular', frame)

    # Condição de saída do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o objeto de captura e fecha a janela
cap.release()
cv2.destroyAllWindows()

#como colocar um link nesse codigo para roda no meu celular  