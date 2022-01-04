def maior(*núm):
    mai = 0
    for c in range(len(núm)):
        if c == 0:
            mai = núm[c]
        else:
            if núm[c] > mai:
                mai = núm[c]
    print(f'O maior valor informado foi: {mai}.')


maior(2, 6, 8, 4, 23, 5)
maior(1, 5, 2, 4, 4)
maior(6, 3, 7, 9, 1)
maior(6, 3, 7, 9, 1, 2, 6, 8, 4, -23, 5, 1, 5, 2, 4, 4)