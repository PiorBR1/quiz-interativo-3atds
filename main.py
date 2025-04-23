# Importa a função 'executar_quiz' do módulo 'quiz'
from quiz import executar_quiz
# Importa o dicionário 'perguntas' do módulo 'perguntas'
from perguntas import perguntas

def main():
    # Função principal que inicia o quiz.
    # Chama a função 'executar_quiz' passando as perguntas importadas
    executar_quiz(perguntas)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal
