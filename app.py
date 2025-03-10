from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global game state
game_board = [""] * 10  # Board positions 1-9 (0 is unused)
current_player = "X"
scores = {"X": 0, "O": 0}

def check_winner():
    """Check if there is a winner."""
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]
    
    for combo in winning_combinations:
        a, b, c = combo
        if game_board[a] == game_board[b] == game_board[c] and game_board[a] != "":
            return game_board[a]  # Returns "X" or "O"
    
    if "" not in game_board[1:]:  # Check for a draw
        return "draw"
    
    return None  # No winner yet

@app.route("/")
def index():
    """Render the game page."""
    return render_template("index.html")
@app.route("/play", methods=["POST"])
def play():
    """Handle a player's move."""
    global current_player

    data = request.json
    move = data.get("move")

    if not (1 <= move <= 9) or game_board[move] != "":  # Invalid move
        return jsonify({"status": "invalid", "board": game_board})

    # Update board before checking for winner
    game_board[move] = current_player
    winner = check_winner()  # Check winner after making the move

    if winner in ["X", "O"]:  # Someone won
        scores[winner] += 1
        loser = "O" if winner == "X" else "X"  # Determine loser
        return jsonify({
            "status": "win",
            "winner": winner,  # Correctly return the current player
            "loser" : loser,
            "board": game_board,
            "scores": scores
        })
    elif winner == "draw":  # Game is a draw
        return jsonify({"status": "draw", "board": game_board})

    # Switch player **only if no one won**
    current_player = "O" if current_player == "X" else "X"

    return jsonify({
        "status": "continue",
        "board": game_board,
        "next_player": current_player
    })

@app.route("/reset", methods=["POST"])
def reset():
    """Reset the game board but keep scores."""
    global game_board, current_player
    game_board = [""] * 10
    current_player = "X"

    return jsonify({"status": "reset", "board": game_board, "scores": scores})

if __name__ == "__main__":
    app.run(debug=True)
