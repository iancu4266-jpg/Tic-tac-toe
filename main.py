import os
import random

board = [" " for _ in range(9)]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear()
    print("🎮 TIC-TAC-TOE vs AI (Minimax) 🎮\n")
    
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    
    print("\n" + "="*20)
    print("   Pozițiile tale (1-9):")
    print(f"   {1} | {2} | {3} ")
    print("  ---+---+---")
    print(f"   {4} | {5} | {6} ")
    print("  ---+---+---")
    print(f"   {7} | {8} | {9} ")
    print("="*20 + "\n")

def check_winner(player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

def is_full():
    return " " not in board

def empty_positions():
    return [i for i, x in enumerate(board) if x == " "]

# Minimax - AI inteligent
def minimax(is_max):
    if check_winner("O"): return 1
    if check_winner("X"): return -1
    if is_full(): return 0

    if is_max:
        best = -float("inf")
        for pos in empty_positions():
            board[pos] = "O"
            best = max(best, minimax(False))
            board[pos] = " "
        return best
    else:
        best = float("inf")
        for pos in empty_positions():
            board[pos] = "X"
            best = min(best, minimax(True))
            board[pos] = " "
        return best

def ai_move():
    best_score = -float("inf")
    best_pos = None
    for pos in empty_positions():
        board[pos] = "O"
        score = minimax(False)
        board[pos] = " "
        if score > best_score:
            best_score = score
            best_pos = pos
    return best_pos

# Varianta Easy (mutare aleatorie)
def easy_ai_move():
    return random.choice(empty_positions())

def play():
    global board
    board = [" " for _ in range(9)]
    print("Alege dificultatea:")
    print("1. Easy (AI face greșeli)")
    print("2. Hard (AI imbatabil - Minimax)")
    
    while True:
        diff = input("Alege (1 sau 2): ")
        if diff in ["1", "2"]:
            break
        print("Te rog scrie 1 sau 2!")

    hard_mode = (diff == "2")
    
    print("\nTu joci cu X (începi tu). Introdu numărul de la 1 la 9.\n")
    
    while True:
        print_board()
        
        # Mutare jucător
        while True:
            try:
                move = int(input("Poziția ta (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = "X"
                    break
                print("Poziție invalidă!")
            except:
                print("Introdu un număr!")
        
        if check_winner("X"):
            print_board()
            print("🎉 Ai câștigat! Felicitări!")
            break
        if is_full():
            print_board()
            print("🤝 Egalitate!")
            break
        
        # Mutare AI
        print("Computerul gândește...")
        if hard_mode:
            move = ai_move()
        else:
            move = easy_ai_move()
        
        board[move] = "O"
        
        if check_winner("O"):
            print_board()
            print("💻 Computerul a câștigat!")
            break
        if is_full():
            print_board()
            print("🤝 Egalitate!")
            break

# Pornire
if __name__ == "__main__":
    while True:
        play()
        if input("\nVrei să joci din nou? (da/nu): ").lower() not in ["da", "d", "yes", "y"]:
            print("Mulțumesc pentru joc! 👋")
            break
