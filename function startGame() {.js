const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const car = {
  x: canvas.width / 2 - 25,
  y: canvas.height - 100,
  width: 50,
  height: 80,
  speed: 0,
  maxSpeed: 8,
  acceleration: 0.3,
  friction: 0.95
};

const keys = {};

window.addEventListener('keydown', (e) => {
  keys[e.key] = true;
});

window.addEventListener('keyup', (e) => {
  keys[e.key] = false;
});

function drawCar() {
  ctx.fillStyle = 'red';
  ctx.fillRect(car.x, car.y, car.width, car.height);
  ctx.fillStyle = 'cyan';
  ctx.fillRect(car.x + 10, car.y + 10, 15, 25);
  ctx.fillRect(car.x + 25, car.y + 10, 15, 25);
}

function updateCar() {
  if (keys['ArrowLeft'] && car.x > 0) car.x -= 6;
  if (keys['ArrowRight'] && car.x < canvas.width - car.width) car.x += 6;
  if (keys['ArrowUp']) car.speed = Math.min(car.speed + car.acceleration, car.maxSpeed);
  else car.speed *= car.friction;
  
  car.y = Math.max(car.y - car.speed, 50);
}

function startGame() {
  function gameLoop() {
    ctx.fillStyle = 'darkgreen';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    updateCar();
    drawCar();
    requestAnimationFrame(gameLoop);
  }
  
  gameLoop();
}

startGame();