let count = 1000;
let arr = []; 
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
        }
    }
}

function isValidMove(x, y) {
    return x >= 0 && x < 4 && y >= 0 && y < 4;
}

function moveTile(x, y, dir) {
    if (!isValidMove(x, y)) {
        return; 
    }

    const newX = x + (dir === 'up' ? -1 : (dir === 'down' ? 1 : 0));
    const newY = y + (dir === 'left' ? -1 : (dir === 'right' ? 1 : 0));

    if (isValidMove(newX, newY)) {
        const temp = arr[x][y];
        arr[x][y] = arr[newX][newY];
        arr[newX][newY] = temp;
        updateBoard();
        count--;
        document.getElementById('steps-count').textContent = count;
        checkWin();
    }
}

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

    document.getElementById('btn-left').addEventListener('click', () => moveTile(emptyX, emptyY, 'left'));
    document.getElementById('btn-right').addEventListener('click', () => moveTile(emptyX, emptyY, 'right'));
    document.getElementById('btn-up').addEventListener('click', () => moveTile(emptyX, emptyY, 'up')); 
    document.getElementById('btn-down').addEventListener('click', () => moveTile(emptyX, emptyY, 'down'));
});
