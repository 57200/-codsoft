// Tic-Tac-Toe Unbeatable AI
// Human = 'X' or 'O' (chosen from UI), AI plays the other mark.
// Two algorithms available: Minimax (plain) and Minimax with Alpha-Beta pruning.

const statusEl = document.getElementById('status');
const boardEl = document.getElementById('board');
const newGameBtn = document.getElementById('newGame');
const humanSelect = document.getElementById('humanMark');
const algoSelect = document.getElementById('algo');

let board, human, ai, gameOver;

// Initialize
function init() {
  board = Array(9).fill(null);
  gameOver = false;
  human = humanSelect.value;
  ai = human === 'X' ? 'O' : 'X';
  statusEl.textContent = human === 'X' ? 'Your turn.' : 'AI is thinking...';
  // Reset cells
  Array.from(boardEl.querySelectorAll('.cell')).forEach((c, i) => {
    c.textContent = '';
    c.disabled = false;
    c.classList.remove('win', 'lose');
  });
  // If AI goes first
  if (human === 'O') {
    setTimeout(aiMove, 250);
  }
}

function availableMoves(b) {
  const moves = [];
  for (let i = 0; i < 9; i++) if (!b[i]) moves.push(i);
  return moves;
}

function checkWinner(b) {
  const wins = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6],
  ];
  for (const [a,c,d] of wins) {
    if (b[a] && b[a] === b[c] && b[a] === b[d]) return {winner: b[a], line:[a,c,d]};
  }
  if (availableMoves(b).length === 0) return {winner: 'draw', line: []};
  return null;
}

function humanMove(idx) {
  if (gameOver || board[idx]) return;
  board[idx] = human;
  render();
  const res = checkWinner(board);
  if (res) return endGame(res);
  statusEl.textContent = 'AI is thinking...';
  setTimeout(aiMove, 120);
}

function aiMove() {
  if (gameOver) return;
  const idx = bestMove(board, ai, human, algoSelect.value === 'ab');
  board[idx] = ai;
  render();
  const res = checkWinner(board);
  if (res) return endGame(res);
  statusEl.textContent = 'Your turn.';
}

function render() {
  Array.from(boardEl.querySelectorAll('.cell')).forEach((c, i) => {
    c.textContent = board[i] ?? '';
    c.disabled = !!board[i] || gameOver;
  });
}

function scoreResult(result, depth) {
  // Prefer faster wins and slower losses
  if (result.winner === ai) return 10 - depth;
  if (result.winner === human) return depth - 10;
  return 0;
}

function bestMove(b, player, opponent, useAB) {
  let best = -Infinity, move = null;
  let alpha = -Infinity, beta = Infinity;
  for (const idx of availableMoves(b)) {
    b[idx] = player;
    const value = minimax(b, false, player, opponent, 1, useAB, alpha, beta);
    b[idx] = null;
    if (value > best) {
      best = value;
      move = idx;
    }
    if (useAB) {
      alpha = Math.max(alpha, best);
    }
  }
  return move;
}

function minimax(b, isMax, player, opponent, depth, useAB, alpha, beta) {
  const res = checkWinner(b);
  if (res) return scoreResult(res, depth);

  if (isMax) {
    let value = -Infinity;
    for (const idx of availableMoves(b)) {
      b[idx] = player;
      const child = minimax(b, false, player, opponent, depth + 1, useAB, alpha, beta);
      b[idx] = null;
      value = Math.max(value, child);
      if (useAB) {
        alpha = Math.max(alpha, value);
        if (beta <= alpha) break; // beta cut-off
      }
    }
    return value;
  } else {
    let value = Infinity;
    for (const idx of availableMoves(b)) {
      b[idx] = opponent;
      const child = minimax(b, true, player, opponent, depth + 1, useAB, alpha, beta);
      b[idx] = null;
      value = Math.min(value, child);
      if (useAB) {
        beta = Math.min(beta, value);
        if (beta <= alpha) break; // alpha cut-off
      }
    }
    return value;
  }
}

function endGame(res) {
  gameOver = true;
  Array.from(boardEl.querySelectorAll('.cell')).forEach(c => c.disabled = true);

  if (res.winner === 'draw') {
    statusEl.textContent = 'Draw!';
    return;
  }
  statusEl.textContent = (res.winner === human) ? 'You win!' : 'AI wins!';
  // highlight line
  for (const i of res.line) {
    const cell = boardEl.querySelector(`.cell[data-idx="${i}"]`);
    if (cell) cell.classList.add(res.winner === human ? 'win' : 'lose');
  }
}

// Wire up UI
boardEl.addEventListener('click', (e) => {
  if (!(e.target instanceof HTMLButtonElement)) return;
  const idx = +e.target.dataset.idx;
  humanMove(idx);
});

newGameBtn.addEventListener('click', init);
humanSelect.addEventListener('change', init);
algoSelect.addEventListener('change', () => {
  // restart to apply algorithm change cleanly
  init();
});

// Start
init();
