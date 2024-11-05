# Atividade 04 - Compressão de Imagem Usando Wavelet
## Objetivo: 
Utilizar a transformada Wavelet para realizar a compressão de uma imagem, removendo componentes de alta frequência (detalhes) e reconstruindo a imagem comprimida.
## Instruções:
- Carregue uma imagem em escala de cinza.
- Aplique a transformada Wavelet (usando 'haar') para decompor a imagem em componentes: (LL, LH, HL, HH)
- Descarte os componentes de detalhes  (LH, HL, HH) e mantenha apenas o componente de baixa frequência (LL)
- Realize a reconstrução inversa usando apenas o componente LL e visualize a imagem reconstruída.
- Desafio: Compare a imagem original com a imagem reconstruída. Avalie a qualidade da imagem comprimida.
## Análise de Resultados:
- Aplicação da Transformada Wavelet, descarte dos componentes (LH, HL, HH), reconstrução utilizando só o LL: <br><br> ![image](https://github.com/user-attachments/assets/57301ed8-0498-4c7e-add0-b7b1b025b938)
- Comparação das Imagens: <br>
Conforme olharmos as duas imagens, na imagem original temos uma qualidade alta, depois de usarmos a Transformada Wavelet para comprimir a imagem, obtivemos uma imagem com uma qualidade mais baixa.
