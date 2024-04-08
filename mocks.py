pix_keywords=[
    {
    "phrase": "Transferência",
    "context": "pix"
    },
    {
    "phrase": "Instantâneo",
    "context": "pix"
    },
    {
    "phrase": "Chave",
    "context": "pix"
    },
    {
    "phrase": "QR Code",
    "context": "pix"
    },
    {
    "phrase": "Pagamento",
    "context": "pix"
    },
    {
    "phrase": "Transação",
    "context": "pix"
    },
    {
    "phrase": "Copia e Cola",
    "context": "pix"
    },
    {
    "phrase": "Conta",
    "context": "pix"
    },
    {
    "phrase": "CPF/CNPJ",
    "context": "pix"
    },
    {
    "phrase": "TED",
    "context": "pix"
    },
    {
    "phrase": "E-mail",
    "context": "pix"
    }
]

pix_questions= [
    {
    "phrase": "Como funciona o sistema de chaves no PIX?",
    "context": "pix"
    },
    {
    "phrase": "Quais são os limites de valor para transferências via PIX?",
    "context": "pix"
    },
    {
    "phrase": "É possível cancelar uma transação feita pelo PIX?",
    "context": "pix"
    },
    {
    "phrase": "Quais são os horários de funcionamento do PIX?",
    "context": "pix"
    },
    {
    "phrase": "Quais são as medidas de segurança adotadas pelo PIX?",
    "context": "pix"
    },
    {
    "phrase": "O PIX está disponível para quais tipos de conta?",
    "context": "pix"
    },
    {
    "phrase": "É possível agendar transferências pelo PIX?",
    "context": "pix"
    },
    {
    "phrase": "Como posso cadastrar minhas chaves no PIX?",
    "context": "pix"
    },
    {
    "phrase": "Quais são as tarifas associadas às transações feitas pelo PIX?",
    "context": "pix"
    },
    {
    "phrase": "Quais são as vantagens do PIX em comparação com outras formas de pagamento?",
    "context": "pix"
    },
]

boleto_keywords=[
    {
    "phrase": "Carnê",
    "context": "boleto"
    },
    {
    "phrase": "Comprovante",
    "context": "boleto"
    },
    {
    "phrase": "Juros",
    "context": "boleto"
    },
    {
    "phrase": "Multa",
    "context": "boleto"
    },
    {
    "phrase": "Desconto",
    "context": "boleto"
    },
    {
    "phrase": "Vencido",
    "context": "boleto"
    },
    {
    "phrase": "Protesto",
    "context": "boleto"
    },
    {
    "phrase": "Fatura",
    "context": "boleto"
    },
    {
    "phrase": "Pagável",
    "context": "boleto"
    },
    {
    "phrase": "Registrado",
    "context": "boleto"
    }
]

boleto_questions=[
    {
    "phrase": "Qual é a data de vencimento deste boleto?",
    "context": "boleto"
    },
    {
    "phrase": "Quais são os dados do beneficiário deste boleto?",
    "context": "boleto"
    },
    {
    "phrase": "Como posso fazer o pagamento deste boleto?",
    "context": "boleto"
    },
    {
    "phrase": "Este boleto possui alguma taxa adicional?",
    "context": "boleto"
    },
    {
    "phrase": "É possível pagar este boleto em qualquer banco",
    "context": "boleto"
    },
    {
    "phrase": "Onde posso encontrar o código de barras deste boleto?",
    "context": "boleto"
    },
    {
    "phrase": "Posso parcelar o pagamento deste boleto?",
    "context": "boleto"
    },
    {
    "phrase": "Este boleto pode ser pago após a data de vencimento?",
    "context": "boleto"
    },
    {
    "phrase": "Como faço para gerar a segunda via deste boleto?",
    "context": "boleto"
    },
    {
    "phrase": "Este boleto está registrado em meu CPF/CNPJ?",
    "context": "boleto"
    }  
]

pix = pix_keywords + pix_questions
boleto = boleto_keywords + boleto_questions

mock_question_context=  pix + boleto
