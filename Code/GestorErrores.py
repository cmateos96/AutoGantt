def mensaje_error(i,id):
        switcher={
                1:"Falta el archivo de plantilla. \nCompruebe que en la carpeta /AutoGantt/Program_Files está el documento .csv generado por usted.",
                2:"Por favor, compruebe que en la carpeta /AutoGantt/Program_Files solo hay un documento .csv.",
                3:"El ID: " + id + " está duplicado, por favor, compruebe que ningún elemento de la columna ID del .csv sea igual a otro",
                4:"Por favor compruebe que no ha introducido ningún espacio en las subtareas o dependencias. Se produce el error cerca de \"" + id + "\"" ,
                5:"Alguna de las fechas no tiene el formato %YYYY-%mm-%dd o es una fecha imposible.",
                6:"La duración no tiene el formato deseado. \nFormatos válidos: "
                    +"\nNúmeros, expresados en días, Por ejemplo: 5"
                    +"\nNúmeros seguidos de \"d\" para días. Significa lo mismo que el anterior. Por ejemplo 15d"
                    +"\nNúmeros seguidos de \"w\" para semanas. Por ejemplo 6w"
                    +"\nNúmeros seguidos de \"m\" para meses. Por ejemplo 3m"
                    +"\nNúmeros seguidos de \"y\" para años. Por ejemplo 2y",
                7:"El ID: " + id + " no existe. \nPor favor compruebe que esté escrito igual que en la definicion",
                8:"El nombre de una tarea no puede ser nulo",
                9:"El id de la tarea tiene que empezar por letra o _ y estar compuesto por letras, dígitos y _. Por favor revise el id:" + id,
                10:"El id de un milestone no puede ser nulo",
                11:"El nombre de un milestone no puede ser nulo",
                12:"Cada milestone debe tener un detonante, ya sea una fecha de inicio, una o varias dependencias."
             }
        return switcher.get(i)

def reportar_error(i,id=""):
    print ("ERROR \n" + mensaje_error(i,id))
    exit(i)
