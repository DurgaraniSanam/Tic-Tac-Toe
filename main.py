from helpers import draw_board, check_turn, check_for_win, get_input_with_timeout
import os
import time

def play_game():
    os.system('cls' if os.name == 'nt' else 'clear')

    player1 = input("Enter Player 1 Name: ")
    player2 = input("Enter Player 2 Name: ")

    scores = {player1: 0, player2: 0}  # Track wins

    while True:
        spots = {i: str(i) for i in range(1, 10)}
        playing = True
        turn = 0
        prev_turn = -1
        completed = False
        winner = None
        loser=None
        TIME_LIMIT = 10

        while playing:
            os.system('cls' if os.name == 'nt' else 'clear')
            draw_board(spots)

            current_player = player1 if turn % 2 == 0 else player2
            print(f"{current_player}'s turn: Pick your spot (1-9) or press 'q' to quit")

            if prev_turn == turn:
                print("Invalid spot selected! Pick another spot.")

            prev_turn = turn
            choice = get_input_with_timeout(TIME_LIMIT)

            if choice is None:
                print(f"⏳ Time's up! {current_player} missed the turn.")
                time.sleep(2)
                turn += 1
                continue

            if choice == 'q':
                print("Game ended. Thanks for playing!")
                return

            if choice.isdigit() and int(choice) in spots:
                if spots[int(choice)] not in {"X", "O"}:
                    spots[int(choice)] = check_turn(turn + 1)
                    turn += 1

            if check_for_win(spots):
                winner = player1 if check_turn(turn)=='X' else player2
                loser = player2 if winner==player1 else player1
                scores[winner] += 1
                completed = True
                playing = False

            if turn > 8:
                playing = False

        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)

        if completed:
            print(f"🎉 {winner} won the game! 🎊")
            print(f"👎 {loser} lost the game! 👎")
        else:
            print("Game Drawn!")

        print("\n🏆 Scores:")
        print(f"{player1}: {scores[player1]} wins")
        print(f"{player2}: {scores[player2]} wins")

        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for Playing! Final Scores:")
            print(f"{player1}: {scores[player1]} wins")
            print(f"{player2}: {scores[player2]} wins")
            break

play_game()
