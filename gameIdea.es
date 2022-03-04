e-sharp.init;
Include Vector;
//Main game stuff
bgColor(720,480,(184,184,184));
//Variables
var running = true;
var playerX = 150;
var playerY = 150;
//Game loop
while (running){
    e-sharp.class(“player”){
        drawRect(playerX,playerY,100,50);
        onMouseRight(true){
            wHtml.alert("You clicked on me!");
        };
    };
    //If the project quits
    event.Quit(){
        e-sharp.gameQuit;
        e-sharp.stop;
    };
};
