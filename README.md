🧩 Tic Tac Toe – Python Edition
Un joc clasic de X și 0, implementat în Python. Proiectul este ideal pentru începători care vor să înțeleagă logica unui joc, lucrul cu funcții și structuri de date, dar și pentru cei care vor un mic proiect distractiv în consolă.

📌 Descriere
Acest proiect implementează jocul Tic Tac Toe pe o tablă 3×3, unde doi jucători introduc pe rând pozițiile dorite. Programul verifică automat câștigătorul, remiza și validează mutările.

🚀 Funcționalități
Joc pentru doi jucători (X și O)

Afișarea tablei după fiecare mutare

Verificarea automată a câștigătorului

Detectarea remizei

Validarea pozițiilor introduse

Cod simplu, ușor de înțeles și extins

🛠️ Tehnologii folosite
Python 3.x

📂 Structura proiectului
Dacă folosești o versiune simplă:

Code
tic-tac-toe/
│── README.md
└── main.py
Dacă ai o versiune modularizată:

Code
tic-tac-toe/
│── README.md
│── main.py
│── game.py
└── board.py
▶️ Cum rulezi jocul
Clonează repository-ul:

Code
git clone https://github.com/user/tic-tac-toe-python.git
Intră în director:

Code
cd tic-tac-toe-python
Rulează jocul:

Code
python main.py
🎮 Cum se joacă
Jucătorul 1 este X, jucătorul 2 este O

Fiecare introduce numărul poziției (1–9)

Programul actualizează tabla

Jocul se termină când:

un jucător are trei simboluri consecutive

toate pozițiile sunt ocupate → remiză

🧠 Exemplu de cod (main.py)
python
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(f" {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # linii
        [0,3,6], [1,4,7], [2,5,8],  # coloane
        [0,4,8], [2,4,6]            # diagonale
    ]
    return any(all(board[pos] == player for pos in cond) for cond in win_conditions)

def game():
    current = "X"
    moves = 0

    while True:
        print_board()
        try:
            pos = int(input(f"Jucătorul {current}, alege o poziție (1-9): ")) - 1
        except ValueError:
            print("Introduce un număr valid.")
            continue

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Mutare invalidă, încearcă din nou.")
            continue

        board[pos] = current
        moves += 1

        if check_winner(current):
            print_board()
            print(f"🎉 Jucătorul {current} a câștigat!")
            break

        if moves == 9:
            print_board()
            print("🤝 Remiză!")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    game()
📌 Îmbunătățiri posibile
Adăugarea unui AI (algoritmul Minimax)

Interfață grafică (Tkinter, Pygame)

Modul multiplayer online

Salvarea scorurilor

🤝 Contribuții
Orice contribuție este binevenită. Poți deschide un issue sau un pull request.

📜 Licență
Proiect distribuit sub licența MIT.
