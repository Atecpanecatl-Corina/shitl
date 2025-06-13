Algoritmo JuegoDelGato
    Definir tablero[3,3] Como Caracter
    Definir fila, columna, turno, jugadas Como Entero
    Definir ganador Como Caracter
	
    // Inicializar el tablero con '-'
    Para fila <- 0 Hasta 2
        Para columna <- 0 Hasta 2
            tablero[fila, columna] <- "-"
        FinPara
    FinPara
	
    turno <- 1
    jugadas <- 0
    ganador <- "-"
	
    Repetir
        Limpiar Pantalla
        Escribir "Tablero actual:"
        Para fila <- 0 Hasta 2
            Para columna <- 0 Hasta 2
                Escribir Sin Saltar tablero[fila, columna], " "
            FinPara
            Escribir ""
        FinPara
		
        Si turno = 1 Entonces
            Escribir "Turno del jugador 1 (X)"
        Sino
            Escribir "Turno del jugador 2 (O)"
        FinSi
		
        // Validación de entrada
        Repetir
            Escribir "Ingrese la fila (0-2): "
            Leer fila
            Escribir "Ingrese la columna (0-2): "
            Leer columna
        Hasta Que fila >= 0 Y fila <= 2 Y columna >= 0 Y columna <= 2 Y tablero[fila, columna] = "-"
		
        Si turno = 1 Entonces
            tablero[fila, columna] <- "X"
            turno <- 2
        Sino
            tablero[fila, columna] <- "O"
            turno <- 1
        FinSi
		
        jugadas <- jugadas + 1
		
        // Verificación de ganador 0 Hasta 2
		Si tablero[i,0] <> "-" Y tablero[i,0] = tablero[i,1] Y tablero[i,1] = tablero[i,2] Entonces
			ganador <- tablero[i,0]
		FinSi
		Si tablero[0,i] <> "-" Y tablero[0,i] = tablero[1,i] Y tablero[1,i] = tablero[2,i] Entonces
			ganador <- tablero[0,i]
		FinSi
	FinPara
	
	Si tablero[0,0] <> "-" Y tablero[0,0] = tablero[1,1] Y tablero[1,1] = tablero[2,2] Entonces
		ganador <- tablero[0,0]
	FinSi
	Si tablero[0,2] <> "-" Y tablero[0,2] = tablero[1,1] Y tablero[1,1] = tablero[2,0] Entonces
		ganador <- tablero[0,2]
	FinSi
	
Hasta Que ganador <> "-" O jugadas = 9

Limpiar Pantalla
Escribir "Tablero final:"
Para fila <- 0 Hasta 2
	Para columna <- 0 Hasta 2
		Escribir Sin Saltar tablero[fila, columna], " "
	FinPara
	Escribir ""
FinPara

Si ganador = "-" Entonces
	Escribir "¡Empate!"
Sino
	Escribir "¡Ganó el jugador ", Si ganador = "X" Entonces "1" Sino "2", "!"
		FinSi
FinAlgoritmo