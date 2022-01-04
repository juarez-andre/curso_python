def notas(* num, sit):
    """
    => Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação da turma.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = {}
    dicio["total"] = len(num)
    dicio["maior"] = max(num)
    dicio["menor"] = min(num)
    dicio["med"] = sum(num) / len(num)
    if sit:
        if dicio["med"] >= 7:
            dicio["situação"] = 'BOA'
        elif dicio["med"] >= 5:
            dicio["situação"] = 'RAZOÁVEL.'
        else:
            dicio["situação"] = 'RUIM.'
    print(dicio)


notas(3.5, 2, 6.5, sit=True)