function enterApp(){
  window.location.href = "main.html";
}

function calculate(){
  const expression = document.getElementById('expression').value;
  const base = document.getElementById('base').value;
  eel.calculate(expression, base)(function(result){
    document.getElementById('result').innerText = "Результат: " + result;
  });
}