let count = 1000;
let arr = []; 
let emptyX, emptyY;  // Add these variables to keep track of the empty tile position
const directions = ['left', 'right', 'up', 'down'];

function initializeGame() {
    createBoard();
    shuffleBoard();
    updateBoard();
}

function createBoard() {
    const board = document.getElementById('board');
    board.innerHTML = ''; 

    for (let i = 0; i < 4; i++) {
        arr[i] = new Array(4);
        for (let j = 0; j < 4; j++) {
            const tile = document.createElement('div');
            tile.classList.add('tile');
            tile.id = `tile-${i}-${j}`; 
            board.appendChild(tile);
        }
    }
}

function shuffleBoard() {
    let numbers = [...Array(16).keys()]; 
    numbers.shift(); 

    for (let i = numbers.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
    }

    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            arr[i][j] = numbers.pop();
            if (arr[i][j] === 0) {
                emptyX = i;
                emptyY = j;
            }
        }
    }
}

function isValidMove(x, y, dir) {  // Update isValidMove to also take direction as an argument
    if (dir === 'left') {
        return y > 0;
    } else if (dir === 'right') {
        return y < 3;
    } else if (dir === 'up') {
        return x > 0;
    } else if (dir === 'down') {
        return x < 3;
    }
}

function moveTile(x, y, dir) {
  if (!isValidMove(x, y, dir)) {
      return; 
  }

  let newX, newY;
  if (dir === 'left') {
      newX = x;
      newY = y - 1;
  } else if (dir === 'right') {
      newX = x;
      newY = y + 1;
  } else if (dir === 'up') {
      newX = x - 1;
      newY = y;
  } else if (dir === 'down') {
      newX = x + 1;
      newY = y;
  }

  const temp = arr[x][y];
  arr[x][y] = arr[newX][newY];
  arr[newX][newY] = temp;
  emptyX = newX;
  emptyY = newY;

  updateBoard();
  count--;
  document.getElementById('steps-count').textContent = count;
  checkWin();
}


// The rest of the code remains the same...


function updateBoard() {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const tile = document.getElementById(`tile-${i}-${j}`);
            tile.textContent = arr[i][j] === 0 ? '' : arr[i][j];
        }
    }
}

function checkWin() {
    // Implementation to check if 'arr' matches the winning pattern
}

function tileClick(event) {
    const tileId = event.target.id;
    const [_, x, y] = tileId.split('-').map(Number); 

    for (const dir of directions) {
        if (isValidMove(x, y, dir)) {
            moveTile(x, y, dir);
            return; 
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
  initializeGame();
  const tiles = document.querySelectorAll('.tile');
  tiles.forEach(tile => tile.addEventListener('click', tileClick));

  document.getElementById('btn-left').addEventListener('click', () => {
      console.log("Left button clicked");
      moveTile(emptyX, emptyY, 'left');
  });

  document.getElementById('btn-right').addEventListener('click', () => {
      console.log("Right button clicked");
      moveTile(emptyX, emptyY, 'right');
  });

  document.getElementById('btn-up').addEventListener('click', () => {
      console.log("Up button clicked");
      moveTile(emptyX, emptyY, 'up');
  });

  document.getElementById('btn-down').addEventListener('click', () => {
      console.log("Down button clicked");
      moveTile(emptyX, emptyY, 'down');
  });
});

