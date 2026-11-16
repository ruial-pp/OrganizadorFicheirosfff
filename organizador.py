from pathlib import Path

pasta = Path.cwd()
total = 0

print("ORGANIZADOR DE FICHEIROS")
print("-----------------------")

for ficheiro in pasta.iterdir():
    if ficheiro.is_file():
        total += 1
        extensao = ficheiro.suffix.lower()

        if extensao == ".py":
            tipo = "Python"
        elif extensao == ".txt":
            tipo = "Texto"
        elif extensao == ".csv":
            tipo = "CSV"
        else:
            tipo = "Outro"

        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix or "Sem extensão")
        print("Tipo:", tipo)
        print("-----------------------")

if total == 0:
    print("A pasta não contém ficheiros.")

print("Total de ficheiros:", total)
