import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

score = 0

questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas

for pregunta, respuestas, respuestaCorrecta  in questions_to_ask:
    # Se selecciona una pregunta aleatoria
    #question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    
    print(pregunta)

    for i, p in enumerate(respuestas):
        print(f"{i+1}. {p}")


    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        
        # Verifico que la respuesta ingresada es valida en los rangos aceptables
        if user_answer.isnumeric() and 0 < int(user_answer) < 5:  
            # Se verifica si la respuesta es correcta
            if int(user_answer) - 1 == respuestaCorrecta:
                print("¡Correcto!")
                score += 1
                break
            else:
                score -= 0.5
        else:
            print("Respuesta no válida")
            sys.exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(respuestas[respuestaCorrecta])

    # no sabia que el for podia tener un else, tremendo
    
    
    
    # Se imprime un blanco al final de la pregunta
    print()
    
print(f"Puntaje final: {score}")
