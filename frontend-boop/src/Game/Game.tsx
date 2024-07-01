import React, { useState, useEffect } from "react";
import { ReactComponent as Kitten1 } from "../svgs/kitten1.svg";
import { ReactComponent as Kitten2 } from "../svgs/kitten2.svg";
import { ReactComponent as Cat1 } from "../svgs/cat1.svg";
import { ReactComponent as Cat2 } from "../svgs/cat2.svg";
import axios from "axios";

export function Game() {
  const [board, setBoard] = useState<Array<Array<String>>>([
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
  ]);
  const [currentTurn, setCurrentTurn] = useState(1);
  const [numKittens, setNumKittens] = useState(0);
  const [numCats, setNumCats] = useState(0);
  const [catsToggled, setCatsToggled] = useState(false);
  const [winner, setWinner] = useState(null);
  const [error, setError] = useState<String | null>(null);

  useEffect(() => {
    fetchGameState();
  }, []);

  const fetchGameState = async () => {
    const response = await axios.get("http://localhost:8000/game_state");
    setBoard(response.data.board);
    setCurrentTurn(response.data.currentTurn);
    setNumKittens(response.data.numKittens);
    setNumCats(response.data.numCats);
  };

  const makeMove = async (row: number, col: number) => {
    if (!winner) {
      if (board[row][col] !== ".") {
        setError("That spot is taken. Please choose a different spot");
      } else {
        let piece;
        if (catsToggled) {
          piece = currentTurn === 1 ? "X" : "O";
        } else {
          piece = currentTurn === 1 ? "x" : "o";
        }
        const response = await axios.post("http://localhost:8000/make_move", {
          player_piece: piece,
          row,
          col,
        });
        setBoard(response.data.board);
        setWinner(response.data.winner);
        setError(null);
        fetchGameState();
      }
    }
  };

  const renderCat = (cell: String) => {
    if (cell === "x") {
      return <Kitten1 />;
    } else if (cell === "o") {
      return <Kitten2 />;
    } else if (cell === "X") {
      return <Cat1 />;
    } else if (cell === "O") {
      return <Cat2 />;
    } else {
      return cell;
    }
  };

  const renderBoard = (): JSX.Element[] => {
    return board.map((row: Array<String>, rowIndex) => (
      <div key={`r-${rowIndex}`} className="row">
        {row.map((cell, colIndex) => (
          <div
            key={`c-${colIndex}`}
            className="cell"
            onClick={() => makeMove(rowIndex, colIndex)}
          >
            {renderCat(cell)}
          </div>
        ))}
      </div>
    ));
  };

  const onToggleChange = () => {
    setCatsToggled(!catsToggled);
  };

  return (
    <div className="App">
      <h1>Boop Game</h1>
      {winner ? (
        <h2>Winner: Player {winner}</h2>
      ) : (
        <h2>Current Turn: {currentTurn}</h2>
      )}
      <h3>
        Kittens Available: {numKittens} | Cats Available: {numCats}
      </h3>
      <div className="kittenToggle">
        <p>Place a cat:</p>
        <label className="switch">
          <input type="checkbox" onChange={onToggleChange} />
          <span className="slider round"></span>
        </label>
      </div>
      <div className="board">{renderBoard()}</div>
      {error && <h4 className="ErrorText">{error}</h4>}
      {winner && <h2 className="WinnerText">Winner: Player {winner}</h2>}
    </div>
  );
}

export default Game;
