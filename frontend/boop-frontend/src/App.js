import logo from "./logo.svg";
import React, { useState, useEffect } from "react";
import axios from "axios";

import "./App.css";

function App() {
  const [board, setBoard] = useState([]);
  const [currentTurn, setCurrentTurn] = useState(1);
  const [numKittens, setNumKittens] = useState(0);
  const [numCats, setNumCats] = useState(0);
  const [catsToggled, setCatsToggled] = useState(false)
  const [winner, setWinner] = useState(null);

  useEffect(() => {
    fetchGameState();
  }, []);

  const fetchGameState = async () => {
    const response = await axios.get("http://localhost:8000/game_state");
    setBoard(response.data.board);
    setCurrentTurn(response.data.currentTurn);
    setNumKittens(response.data.numKittens)
    setNumCats(response.data.numCats)
  };

  const makeMove = async (row, col) => {
    let piece 
    if (catsToggled) {
      piece = currentTurn === 1 ? "X" : "O"
    } else {
      piece = currentTurn === 1 ? "x" : "o"
    }
    const response = await axios.post("http://localhost:8000/make_move", {
      player_piece: piece,
      row,
      col,
    });
    setBoard(response.data.board);
    setWinner(response.data.winner);
    fetchGameState();
  };

  const renderBoard = () => {
    return board.map((row, rowIndex) => (
      <div key={rowIndex} className="row">
        {row.map((cell, colIndex) => (
          <div
            key={colIndex}
            className="cell"
            onClick={() =>
              makeMove(rowIndex, colIndex)
            }
          >
            {cell}
          </div>
        ))}
      </div>
    ));
  };

  const onToggleChange = () => {
    setCatsToggled(!catsToggled)
  } 

  return (
    <div className="App">
      <h1>Boop Game</h1>
      {winner ? (
        <h2>Winner: Player {winner}</h2>
      ) : (
        <h2>Current Turn: {currentTurn}</h2>
      )}
      <h3>Kittens Available: {numKittens} | Cats Available: {numCats}</h3>
      <div className="kittenToggle">
        <p>Place a cat:</p>
        <label class="switch">
          <input type="checkbox" onChange={onToggleChange}/>
          <span class="slider round"></span>
        </label>
      </div>
      <div className="board">{renderBoard()}</div>
    </div>
  );
}

export default App;
