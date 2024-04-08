pix_keywords=[
    {
    "data": "Transferência",
    "context": "pix"
    },
    {
    "data": "Instantâneo",
    "context": "pix"
    },
    {
    "data": "Chave",
    "context": "pix"
    },
    {
    "data": "QR Code",
    "context": "pix"
    },
    {
    "data": "Pagamento",
    "context": "pix"
    },
    {
    "data": "Transação",
    "context": "pix"
    },
    {
    "data": "Copia e Cola",
    "context": "pix"
    },
    {
    "data": "Conta",
    "context": "pix"
    },
    {
    "data": "CPF/CNPJ",
    "context": "pix"
    },
    {
    "data": "TED",
    "context": "pix"
    },
    {
    "data": "E-mail",
    "context": "pix"
    }
]

pix_questions= [
    {
    "data": "Como funciona o sistema de chaves no PIX?",
    "context": "pix"
    },
    {
    "data": "Quais são os limites de valor para transferências via PIX?",
    "context": "pix"
    },
    {
    "data": "É possível cancelar uma transação feita pelo PIX?",
    "context": "pix"
    },
    {
    "data": "Quais são os horários de funcionamento do PIX?",
    "context": "pix"
    },
    {
    "data": "Quais são as medidas de segurança adotadas pelo PIX?",
    "context": "pix"
    },
    {
    "data": "O PIX está disponível para quais tipos de conta?",
    "context": "pix"
    },
    {
    "data": "É possível agendar transferências pelo PIX?",
    "context": "pix"
    },
    {
    "data": "Como posso cadastrar minhas chaves no PIX?",
    "context": "pix"
    },
    {
    "data": "Quais são as tarifas associadas às transações feitas pelo PIX?",
    "context": "pix"
    },
    {
    "data": "Quais são as vantagens do PIX em comparação com outras formas de pagamento?",
    "context": "pix"
    },
]

boleto_keywords=[
    {
    "data": "Carnê",
    "context": "boleto"
    },
    {
    "data": "Comprovante",
    "context": "boleto"
    },
    {
    "data": "Juros",
    "context": "boleto"
    },
    {
    "data": "Multa",
    "context": "boleto"
    },
    {
    "data": "Desconto",
    "context": "boleto"
    },
    {
    "data": "Vencido",
    "context": "boleto"
    },
    {
    "data": "Protesto",
    "context": "boleto"
    },
    {
    "data": "Fatura",
    "context": "boleto"
    },
    {
    "data": "Pagável",
    "context": "boleto"
    },
    {
    "data": "Registrado",
    "context": "boleto"
    }
]

boleto_questions=[
    {
    "data": "Qual é a data de vencimento deste boleto?",
    "context": "boleto"
    },
    {
    "data": "Quais são os dados do beneficiário deste boleto?",
    "context": "boleto"
    },
    {
    "data": "Como posso fazer o pagamento deste boleto?",
    "context": "boleto"
    },
    {
    "data": "Este boleto possui alguma taxa adicional?",
    "context": "boleto"
    },
    {
    "data": "É possível pagar este boleto em qualquer banco",
    "context": "boleto"
    },
    {
    "data": "Onde posso encontrar o código de barras deste boleto?",
    "context": "boleto"
    },
    {
    "data": "Posso parcelar o pagamento deste boleto?",
    "context": "boleto"
    },
    {
    "data": "Este boleto pode ser pago após a data de vencimento?",
    "context": "boleto"
    },
    {
    "data": "Como faço para gerar a segunda via deste boleto?",
    "context": "boleto"
    },
    {
    "data": "Este boleto está registrado em meu CPF/CNPJ?",
    "context": "boleto"
    }  
]

pix = pix_keywords + pix_questions
boleto = boleto_keywords + boleto_questions

mock_question_context=  pix + boleto
