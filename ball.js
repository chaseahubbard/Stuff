export default class Ball {

    constructor(ballgame) {
      this.image = document.getElementById('img_ball_temp');  
      this.position = {x:80, y:10};
      this.speed = {x: 2, y: 3};
      this.size = {x: 16 , y:16};
      this.gamewidth = ballgame.gamewidth;
      this.gameheight = ballgame.gameheight;
      this.ballgame = ballgame;
    }
    draw(ctx) {
        ctx.drawImage(this.image,this.position.x,this.position.y,this.size.x,this.size.y);
    }

    update(dt){
        this.position.x += this.speed.x;
        this.position.y += this.speed.y;

        if (this.position.y + this.size.y > this.gameheight || this.position.y < 0) {
            this.speed.y = -this.speed.y;
        } 
        if (this.position.x + this.size.x > this.gamewidth || this.position.x < 0) {
            this.speed.x = -this.speed.x;
        } 

        let bottomball = this.position.y + this.size.y;
        let toppaddle = this.ballgame.paddle.position.y;
        let leftsideofpaddle = this.ballgame.paddle.position.x;
        let rightsideofpaddle = this.ballgame.paddle.width + this.ballgame.paddle.position.x;

        if (bottomball >= toppaddle &&
            this.position.x >= leftsideofpaddle &&
            this.position.x + this.size.x <= rightsideofpaddle
            ) {
            this.speed.y = -this.speed.y;
            this.position.y = this.ballgame.paddle.position.y - this.size.y;
        }
    }
} 