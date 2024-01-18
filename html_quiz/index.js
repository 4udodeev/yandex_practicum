const questions = [
    {
      type: 'single-choice',
      text: 'What is the capital of France?',
      options: ['Paris', 'Berlin', 'London', 'Madrid'],
      correctAnswer: 'Paris',
    },
    {
      type: 'multiple-choice',
      text: 'Which programming languages are used for web development?',
      options: ['Python', 'Java', 'JavaScript', 'C++'],
      correctAnswers: ['JavaScript'],
    },
    {
      type: 'ranking',
      text: 'Rank the following colors from most favorite to least favorite:',
      options: ['Red', 'Blue', 'Green', 'Yellow'],
      correctOrder: ['Blue', 'Green', 'Red', 'Yellow'],
    },
    {
      type: 'matching',
      text: 'Match the programming languages with their respective logo colors:',
      options: [
        { text: 'Python', matching_options: ['Yellow'] },
        { text: 'JavaScript', matching_options: ['Yellow'] },
        { text: 'Java', matching_options: ['Red'] },
        { text: 'Ruby', matching_options: ['Red'] },
      ],
    },
  ];

  let currentQuestionIndex = 0;
  let userAnswers = [];

  function showQuestion(question) {
    const questionElement = document.getElementById('question');
    const optionsContainer = document.getElementById('options-container');
    
    questionElement.textContent = question.text;
    optionsContainer.innerHTML = '';

    if (question.type === 'single-choice') {
      question.options.forEach((option) => {
        const li = document.createElement('li');
        li.className = 'option';
        li.textContent = option;
        li.onclick = () => selectSingleChoice(option);
        optionsContainer.appendChild(li);
      });
    } else if (question.type === 'multiple-choice') {
      question.options.forEach((option) => {
        const li = document.createElement('li');
        li.className = 'option';
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.value = option;
        checkbox.onchange = () => updateMultipleChoice();
        li.appendChild(checkbox);
        li.appendChild(document.createTextNode(option));
        optionsContainer.appendChild(li);
      });
    } else if (question.type === 'ranking') {
      question.options.forEach((option, index) => {
        const li = document.createElement('li');
        li.className = 'option';
        li.textContent = option;
        const input = document.createElement('input');
        input.type = 'number';
        input.min = 1;
        input.max = question.options.length;
        input.onchange = () => updateRanking();
        li.appendChild(input);
        optionsContainer.appendChild(li);
      });
    } else if (question.type === 'matching') {
      question.options.forEach((option) => {
        const li = document.createElement('li');
        li.className = 'option';
        li.textContent = option.text;
        const select = document.createElement('select');
        option.matching_options.forEach((match) => {
          const option = document.createElement('option');
          option.value = match;
          option.textContent = match;
          select.appendChild(option);
        });
        select.onchange = () => updateMatching();
        li.appendChild(select);
        optionsContainer.appendChild(li);
      });
    }
  }

  function selectSingleChoice(option) {
    userAnswers[currentQuestionIndex] = option;
  }

  function updateMultipleChoice() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    userAnswers[currentQuestionIndex] = Array.from(checkboxes).map((checkbox) => checkbox.value);
  }

  function updateRanking() {
    const inputs = document.querySelectorAll('input[type="number"]');
    userAnswers[currentQuestionIndex] = Array.from(inputs).map((input) => input.value);
  }

  function updateMatching() {
    const selects = document.querySelectorAll('select');
    userAnswers[currentQuestionIndex] = Array.from(selects).map((select) => select.value);
  }

  function nextQuestion() {
    currentQuestionIndex++;

    if (currentQuestionIndex < questions.length) {
      showQuestion(questions[currentQuestionIndex]);
    } else {
      showResults();
    }
  }

  function showResults() {
    const resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = '<h2>Quiz Finished!</h2>';
    resultContainer.innerHTML += `<p>Your score: ${calculateScore()}/${questions.length}</p>`;
    resultContainer.innerHTML += '<h3>Your Answers:</h3>';
    resultContainer.innerHTML += '<ul>';
    
    questions.forEach((question, index) => {
      resultContainer.innerHTML += `<li>${question.text} - Your answer: ${userAnswers[index]}</li>`;
    });

    resultContainer.innerHTML += '</ul>';
  }

  function calculateScore() {
    let score = 0;

    questions.forEach((question, index) => {
      if (areAnswersEqual(question, userAnswers[index])) {
        score++;
      }
    });

    return score;
  }

  function areAnswersEqual(question, userAnswer) {
    if (question.type === 'multiple-choice') {
      return arraysEqual(question.correctAnswers, userAnswer);
    } else if (question.type === 'ranking') {
      return arraysEqual(question.correctOrder, userAnswer);
    } else if (question.type === 'matching') {
      return arraysEqual(question.options.map((option) => option.matching_options), userAnswer);
    } else {
      return question.correctAnswer === userAnswer;
    }
  }

  function arraysEqual(arr1, arr2) {
    return JSON.stringify(arr1) === JSON.stringify(arr2);
  }

  document.addEventListener('DOMContentLoaded', () => {
    showQuestion(questions[currentQuestionIndex]);
  });