# ----------------  MODULO 1  --------------------
import csv

#A partir de la columna Close, al valor actual le voy restando todos hasta el quince, luego con el segundo le resto los 15 siguientes
def RestarLos14Siguientes(datasetNum, fileNameGenerated, fileNameToProces):
    datosActual = None
    columnsResults = ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11", "Col12", "Col13", "Col14", "Col15", "Col16"]

    with open(fileNameToProces, newline='') as File:
        with open(fileNameGenerated, 'w') as FileW:
            reader = csv.reader(File)
            writer = csv.writer(FileW, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(columnsResults)

            ubicacionDeColParaExtraer = 6 #Column Close
            cantidadDeColAgregar = 15
            cant = 0

            list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            listResult = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            for row in reader:
                dataActualList = row[0].split(";")
                if row[0].split(";")[0] != "<TICKER>":
                    if cant < cantidadDeColAgregar:
                        if datosActual is None:
                            datosActual = dataActualList

                        list[cant] = dataActualList[ubicacionDeColParaExtraer]
                        cant += 1

                    else:

                        # mover una posicion hacia atraz y eliminar el primero
                        listResult[0] = float(list[0]) - float(list[1])
                        listResult[1] = float(list[0]) - float(list[2])
                        listResult[2] = float(list[0]) - float(list[3])
                        listResult[3] = float(list[0]) - float(list[4])
                        listResult[4] = float(list[0]) - float(list[5])
                        listResult[5] = float(list[0]) - float(list[6])
                        listResult[6] = float(list[0]) - float(list[7])
                        listResult[7] = float(list[0]) - float(list[8])
                        listResult[8] = float(list[0]) - float(list[9])
                        listResult[9] = float(list[0]) - float(list[10])
                        listResult[10] = float(list[0]) - float(list[11])
                        listResult[11] = float(list[0]) - float(list[12])
                        listResult[12] = float(list[0]) - float(list[13])
                        listResult[13] = float(list[0]) - float(list[14])
                        listResult[14] = float(list[0]) - float(dataActualList[ubicacionDeColParaExtraer])

                        # asigno el resultado de la variacion del primero con el ultimo a la ultima posicion
                        listResult[15] = RetornarVariacionEntrePrimeraUltimaCol(float(listResult[0]), float(listResult[14]))

                        # mover los datos hacia atras
                        list[0] = list[1]
                        list[1] = list[2]
                        list[2] = list[3]
                        list[3] = list[4]
                        list[4] = list[5]
                        list[5] = list[6]
                        list[6] = list[7]
                        list[7] = list[8]
                        list[8] = list[9]
                        list[9] = list[10]
                        list[10] = list[11]
                        list[11] = list[12]
                        list[12] = list[13]
                        list[13] = list[14]
                        list[14] = dataActualList[ubicacionDeColParaExtraer]

                        # escribir en el archivo la list
                        print(listResult)
                        writer = csv.writer(FileW, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(listResult)

#---------------------------------------------------------------------------------------------------------------------
#toma cada precio de la columna Close y lista  los quince primeros precios (de la columna Close),
# esto es a partir del primer precio, es decir,
# lista el primero y luego los 14 siguientes (15 en total).
# Luego en el siguiente registro toma el segundo y los 14 siguientes precios y así sucesivamente.
# La ultima columna contiene la variacion del primero con el último                         # S si subió, I si quedó igual, B si bajó
def CopiarDe15(fileNameGenerated, fileNameToProces):
    datosActual = None
    columnsResults = ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11", "Col12", "Col13", "Col14", "Col15", "Class"]

    with open(fileNameToProces, newline='') as File:
        with open(fileNameGenerated, 'w') as FileW:

            reader = csv.reader(File)
            writer = csv.writer(FileW, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(columnsResults)

            ubicacionDeColParaExtraer = 6 #Column Close
            cantidadDeColAgregar = 15
            cant = 0

            list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            for row in reader:
                dataActualList = row[0].split(";")
                if row[0].split(";")[0] != "<TICKER>":
                    if cant < cantidadDeColAgregar:
                        if datosActual is None:
                            datosActual = dataActualList

                        list[cant] = dataActualList[ubicacionDeColParaExtraer]

                        # resto el primero con el ultimo para ver la variacion
                        # S si subió, I si quedó igual, B si bajó
                        if (list[0] != "" and list[14] != ""):
                            first = float(list[0])
                            last = float(list[14])

                            list[15] = '?'#RetornarVariacionEntrePrimeraUltimaCol(first, last)

                        cant += 1
                    else:
                        # escribir en el archivo la list
                        #datosActual += list
                        print(list)
                        #generalList.append(list)

                        writer = csv.writer(FileW, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(list)

                        # mover una posicion hacia atraz y eliminar el primero
                        list[0] = list[1]
                        list[1] = list[2]
                        list[2] = list[3]
                        list[3] = list[4]
                        list[4] = list[5]
                        list[5] = list[6]
                        list[6] = list[7]
                        list[7] = list[8]
                        list[8] = list[9]
                        list[9] = list[10]
                        list[10] = list[11]
                        list[11] = list[12]
                        list[12] = list[13]
                        list[13] = list[14]
                        list[14] = dataActualList[ubicacionDeColParaExtraer]

                        datosActual = dataActualList

                        # resto el primero con el ultimo para ver la variacion
                        # S si subió, I si quedó igual, B si bajó
                        first = float(list[0])
                        last = float(list[14])

                        # asigno el resultado de la variacion del primero con el ultimo a la ultima posicion
                        list[15] = '?'#RetornarVariacionEntrePrimeraUltimaCol(first, last)

# Retorna La ultima columna que contiene la variacion del primero con el último
# S si subió, I si quedó igual, B si bajó
def RetornarVariacionEntrePrimeraUltimaCol(primero, ultimo):
    if (primero == ultimo):
        return "I"
    elif (primero < ultimo):
        return "S"
    elif (primero > ultimo):
        return "B"

# Compara la primera con la ultima columna
# e inserta "+" si el ultimo es mayor al prmero y "-" si el ultimo es menor al primero
def RetornarMasOMenosEntrePrimerYUltimaCol(primero, ultimo):
    if (primero == ultimo or primero < ultimo):
        return "+"
    elif (primero > ultimo):
        return "-"

# FACTOR DE ESCALA
# Generar un dataset normalizado. Todos los valores van a quedar proporcionalmente
# distribuidos entre cero y uno. A esto se le llama cambio de escala
# (x1 - min)/(max - min) = un valor entre 0 y 1
# R = max - min (Rango)
def GenerarDatasetNormalizado(fileNameEnterFile, fileNameExitFile):
    cantColumns = 15
    max = -100
    men = 100

    # Busco el mayor y menor de todo el dataset
    with open(fileNameEnterFile, newline='') as File:
        reader = csv.reader(File)
        count = 0

        for row in reader:
            print(row)
            if (count != 0):
                countData = 0
                for data in row:
                    if (countData < cantColumns):
                        data = float(data)
                        if (data >= max):
                            max = data
                        if (data <= men):
                            men = data

                    countData = countData + 1

            count = count + 1

        print(max)
        print(men)

    # Aplico la formula de normalizacion para cada elemento del dataset
    rango = max - men

    with open(fileNameEnterFile, newline='') as File:
        with open(fileNameExitFile, 'w') as FileW:

            reader = csv.reader(File)
            columnsResults = ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11",
                              "Col12", "Col13", "Col14", "Col15"]
            listToSave = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            count = 0

            writer = csv.writer(FileW, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(columnsResults)

            for row in reader:
                #print(row)
                if (count != 0):
                    countData = 0
                    for data in row:
                        if (countData < cantColumns):
                            data = float(data)
                            dataToSave = (data - men) / (rango)
                            listToSave[countData] = round(dataToSave, 2)

                        countData = countData + 1

                    print(listToSave)
                    writer.writerow(listToSave)

                count = count + 1


# Metodo generico que llama a los demas metodos para generar los dataset del 1 al 3
def GenerarDataSet(datasetNum, fileNameGenerated, fileNameToProces):
    if (datasetNum == 1):
        CopiarDe15(fileNameGenerated, fileNameToProces)
    elif (datasetNum == 2):
        RestarLos14Siguientes(datasetNum, fileNameGenerated, fileNameToProces)
    elif (datasetNum == 3):
        GenerarDatasetNormalizado(fileNameToProces, fileNameGenerated)
    else:
        print("El número de dataset es incorrecto")


#           GENERAR DATASETS PARA TESTING

# Generar dataset para pruebas para el dataseet1.
# La ultima columna debe llamarse Class y no Col16 y debe tener como datos en toda la columna un ?
#GenerarDataSet(1, 'DataSet_1_Test.csv', 'DataSet_Inicial_Test.csv')

# Generar dataser para pruebas apartir del dataset2
# La ultima columna debe llamarse Class y no Col16 y debe tener como datos en toda la columna un ?
#GenerarDataSet(2, 'DataSet_2_Test.csv', 'DataSet_Inicial_Test.csv')

# Generar dataset final para testear generado del dataset2 y 3
# GenerarDataSet(3, 'DataSet_3_Test.csv', 'DataSet_2_Test.csv')

