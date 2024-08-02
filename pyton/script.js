const matrices = [
    [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49], [51, 53, 55, 57, 59]],
    [[2, 3, 6, 7, 10], [11, 14, 15, 18, 19], [22, 23, 26, 27, 30], [31, 34, 35, 38, 39], [42, 43, 46, 47, 50], [51, 54, 55, 58, 59]],
    [[4, 5, 6, 7, 11], [12, 13, 14, 15, 20], [21, 22, 23, 28, 29], [30, 31, 36, 37, 38], [39, 44, 45, 46, 47], [52, 53, 55, 60, ' ']],
    [[8, 9, 10, 11, 12], [13, 14, 15, 24, 25], [26, 27, 28, 29, 30], [31, 40, 41, 42, 43], [44, 45, 46, 47, 56], [57, 58, 59, 60, ' ']],
    [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 48, 49, 50, 51], [52, 53, 54, 55, 56], [57, 58, 59, 60, ' ']],
    [[32, 33, 34, 35, 36], [37, 38, 39, 40, 41], [42, 43, 44, 45, 46], [47, 48, 49, 50, 51], [52, 53, 54, 55, 56], [57, 58, 59, 60, ' ']]
  ];
  
  let currentMatrixIndex = 0;
  let guessedNumber = 0;
  
  function displayMatrix(matrix) {
    const matrixContainer = document.getElementById('matrix');
    matrixContainer.innerHTML = '';
  
    for (let row of matrix) {
      for (let num of row) {
        const numDiv = document.createElement('div');
        numDiv.classList.add('matrix-number');
        numDiv.textContent = num;
        matrixContainer.appendChild(numDiv);
      }
    }
  }
  
  function handleYesClick() {
    guessedNumber = guessedNumber+ matrices[currentMatrixIndex][0][0];
    currentMatrixIndex++;
    if (currentMatrixIndex < matrices.length) {
      displayMatrix(matrices[currentMatrixIndex]);
    } else {
      document.getElementById('result').textContent = `Your guessed number is: ${guessedNumber}`;
      disableButtons();
    }
  }
  
  function handleNoClick() {
    currentMatrixIndex++;
    if (currentMatrixIndex < matrices.length) {
      displayMatrix(matrices[currentMatrixIndex]);
    } else {
      document.getElementById('result').textContent = `Your guessed number is: ${guessedNumber}`;
      disableButtons();
    }
  }
  
  function disableButtons() {
    document.getElementById('yesBtn').disabled = true;
    document.getElementById('noBtn').disabled = true;
  }
  
  displayMatrix(matrices[currentMatrixIndex]);
  
  document.getElementById('yesBtn').addEventListener('click', handleYesClick);
  document.getElementById('noBtn').addEventListener('click', handleNoClick);