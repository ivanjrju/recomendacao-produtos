def mensagem_oferta(produto):
    ofertas = {
        'casa_propria': "Já pensou em realizar o sonho da casa própria? Podemos te ajudar a conquistar o seu lar com condições especiais! Venha conferir!",
        'seguro_residencia': "Proteja o seu maior patrimônio com nosso Seguro Residência! Garantia de tranquilidade para você e sua família.",
        'carro': "Chegou a hora de acelerar seus sonhos! Que tal adquirir seu carro novo? Temos opções que cabem no seu bolso!",
        'seguro_auto': "Cuide bem do seu carro com nosso Seguro Auto. Oferecemos proteção completa e atendimento 24h para que você dirija sem preocupações!",
        'cartao': "Um cartão de crédito com benefícios exclusivos está esperando por você! Aproveite para fazer suas compras com mais praticidade.",
        'seguro_cartao': "Garanta mais segurança para suas transações com nosso Seguro Cartão. Cobertura em casos de perda ou roubo, para sua tranquilidade.",
        'poupanca': "Comece a poupar para o futuro com nossa conta poupança. É fácil, seguro, e seu dinheiro rende mais!",
        'renda_fixa': "Invista com segurança e tenha rentabilidade garantida! Conheça nossas opções de Renda Fixa e faça seu dinheiro crescer.",
        'credito_pessoal': "Precisa de um crédito rápido e sem burocracia? Nossas condições de Crédito Pessoal são ideais para realizar seus planos.",
        'scode_credito': "Quer melhorar seu score de crédito? Temos soluções para ajudar você a se organizar e aumentar suas chances de aprovação!"
    }
    
    return ofertas.get(produto, "Produto não encontrado")