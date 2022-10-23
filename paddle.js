export default class Paddle {
    constructor(ballgame) {
        this.width = 150;
        this.height = 35;
        this.maxSpeed = 5;
        this.speed = 0;
        this.gameWidth = ballgame.gamewidth
        this.position = {
            x: ballgame.gamewidth/2 - this.width/2,
            y: ballgame.gameheight - this.height - 10,
        };

    }
    moveLeft(){
        this.speed = -this.maxSpeed;
    }

    moveRight() {
        this.speed = this.maxSpeed;
    }
    stop() {
        this.speed = 0;
    }
    draw(ctx){
        ctx.fillStyle = 'red'
        ctx.fillRect(this.position.x, this.position.y, this.width, this.height);

    }

    update(dt){
        this.position.x += this.speed;

        if(this.position.x < 0) this.position.x = 0;
        if(this.position.x + this.width > this.gameWidth)
            this.position.x = this.gameWidth - this.width;
    }
}