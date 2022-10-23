import Paddle from '/src/paddle.js';
import InputHandler from '/src/input.js';
import Ball from '/src/ball.js';
export default class ballGame {
    constructor(gamewidth,gameheight){
        this.gamewidth = gamewidth;
        this.gameheight = gameheight;
    }

    start(){
        this.ball = new Ball(this);
        this.paddle = new Paddle(this);
        this.gameObjects = [this.ball, this.paddle];
        new InputHandler(this.paddle);
}
    update(dt) {
        
        this.gameObjects.forEach(object => object.update(dt))
        
    }

    draw(ctx) {

        this.gameObjects.forEach(object => object.draw(ctx))
    }
}