import Paddle from '/src/paddle.js';
import InputHandler from '/src/input.js';
import Ball from '/src/ball.js';
import ballGame from '/src/manager.js';

let canvas = document.getElementById('gameScreen');
let ctx = canvas.getContext('2d');

const game_width = 800;
const game_height = 600;

let ballgame = new ballGame(game_width,game_height);

ballgame.start();

let lasttime = 0;



function gameloop(timestamp) {
    let dt = timestamp - lasttime
    lasttime = timestamp;

    ctx.clearRect(0,0,game_width,game_height);
    ballgame.update(dt)
    ballgame.draw(ctx)


    requestAnimationFrame(gameloop);
    }

requestAnimationFrame(gameloop);