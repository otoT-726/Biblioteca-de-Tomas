import random

puntaje = 0

# Preguntas para el juego
questions = [ "¿Qué función se usa para obtener la longitud de una cadena en Python?",
            "¿Cuál de las siguientes opciones es un número entero en Python?",
            "¿Cómo se solicita entrada del usuario en Python?",
            "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
            "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [("size()", "len()", "length()", "count()"),
            ("3.14", "'42'", "10", "True"),
            ("input()", "scan()", "read()", "ask()"),
            (
            "// Esto es un comentario",
            "/* Esto es un comentario */",
            "-- Esto es un comentario",
            "# Esto es un comentario",
            ),
            ("=", "==", "!=", "==="),]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = list(zip(questions, answers, correct_answers_index))

question_index = random.sample((0, 1, 2, 3), 3)

# El usuario deberá contestar 3 preguntas
for j in question_index:
    # Se selecciona una pregunta aleatoria
    # Se muestra la pregunta y las respuestas posibles
    print(questions_to_ask[j][0])
    for i, answer in enumerate(questions_to_ask[j][1]):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2): 
        user_answer = input("Respuesta: ")
        pos = ['1', '2', '3', '4']
        if user_answer not in pos:
            print('Respuesta no valida')
            exit()
        else:
            user_answer = int(user_answer) - 1
        # Se verifica si la respuesta es correcta
        if user_answer == questions_to_ask[j][2]:
            print("¡Correcto!")
            puntaje += 1
            break
    else:
# Si el usuario no responde correctamente después de 2 intentos,
# se muestra la respuesta correcta
        puntaje -= 0.5
        print("Incorrecto. La respuesta correcta es:")
        print(questions_to_ask[j][1][questions_to_ask[j][2]])

print('Puntaje final: ', puntaje)

# Se imprime un blanco al final de la pregunta
print()