var canvas = document.getElementById("myCanvas");
    var c = canvas.getContext("2d");
    var player = document.getElementById("player");
    var playerSide = document.getElementById("playerSide");
    var tree = document.getElementById("tree");

    let playerX = 540;
    let playerY = 335;
    let coin = {x:150,y:150,width:50,height:50};
    let playerHit = {x:playerX,y:playerY,width:100,height:100};
    let dead = false;
    let hitbox = false;
    let playerDIR = "right";
    let scene = 0;
    let titleY = 480/2
    let time = 0;

    let leftKeyPresed = false;
    let rightKeyPressed = false;
    let upKeyPressed = false;
    let downKeyPressed = false;
    let spaceKeyPressed = false;

    function redraw(){
        if(scene == 0){
            clear();
            title();
            lineDraw();
            drawInfo();
        }
        if(scene == 1){
            clear();
            coin = {x:250,y:250,width:50,height:50};
            playerHit = {x:playerX+35,y:playerY+30,width:50,height:50};   
            drawHitBox();
            drawPlayer();
            drawEnemy();
            drawTree();
            //Must be first unless cutscene
            lineDraw();
        }
    }
    function title(){
        c.fillStyle = "#115577";
        c.font = 'bold 48px sans serif';
        c.fillText("Farther",720/2,titleY);
        c.fillText("Early Alpha",720/2+10,titleY+40);
    }
    function drawInfo(){
        c.fillStyle = "#11cc77";
        c.font = 'bold 15px sans serif';
        c.fillText("Copyright 2022 ClassicMC",10,470); 
    }
    function clear(){
        if(scene == 0){
            c.fillStyle = "#000000";
            c.fillRect(0,0,720,480);
            c.drawImage(player,90,90,200,200);
        }
        else{
            c.fillStyle = "#000000";
            c.fillRect(0,0,720,480);
        }
    }
    function drawPlayer(){
        //c.fillStyle = "#ffffff";
        //c.fillRect(rect2.x,rect2.y,rect2.width,rect2.height);
        if(playerDIR == "right"){
            c.drawImage(player,playerX,playerY);
        }
        else if(playerDIR == "left"){
            c.drawImage(playerSide,playerX,playerY)
        }
    }
    function drawHitBox(){
        if(hitbox == true){
            c.fillStyle = "#00cc00";
            c.fillRect(playerX+35,playerY+30,50,50);
        }
    }
    function drawEnemy(){
        if(dead == false){
            c.fillStyle = "#ffffff";
            c.fillRect(coin.x,coin.y,coin.width,coin.height);
        }
    }
    function drawTree(){
        let treeX = 0;
        let treeY = -10;
        for (let step = 0; step < 3; step++) {
            c.drawImage(tree,treeX,treeY)
            treeX += 100;
        }
    }
    function checkCollisions(){
        if(coin.x < playerHit.x + playerHit.width &&
        coin.x + coin.width > playerHit.x &&
        coin.y < playerHit.y + playerHit.height &&
        coin.y + coin.height > playerHit.y){
            if(spaceKeyPressed == true){
                dead = true;
            }
        }  
    }
    function lineDraw(){
        c.fillStyle = "#000000";
        let lY = 10;
        for (let step = 0; step < 50; step++) {
            // Runs 5 times, with values of step 0 through 4.
            c.fillRect(0,lY,720,5);
            lY += 10;
        }
    }
    /*
    Just a whole buch of garbage to 
    get the movement working correctly
    */
    function keyPressed(evt){
        if(evt.keyCode == 37){
            leftKeyPressed = true;
        }
        if(evt.keyCode == 39){
            rightKeyPressed = true;
        }
        if(evt.keyCode == 38){
            upKeyPressed = true;
        }
        if(evt.keyCode == 40){
            downKeyPressed = true;
        }
        if(evt.keyCode == 32){
            spaceKeyPressed = true;
        }
    }
    function keyReleased(evt){
        if(evt.keyCode == 37){
            leftKeyPressed = false;
        }
        if(evt.keyCode == 39){
            rightKeyPressed = false;
        }
        if(evt.keyCode == 38){
            upKeyPressed = false;
        }
        if(evt.keyCode == 40){
            downKeyPressed = false;
        }
        if(evt.keyCode == 32){
            spaceKeyPressed = false;
        }
    }
    function playerMove(){
        if(spaceKeyPressed == true){
            if(scene ==0){
            scene = 1;
            }
            spaceKeyPressed = false;
        }
        else if(leftKeyPressed == true){
            playerDIR = "left";
            playerX -= 5;
        }
        else if(rightKeyPressed == true){
            playerDIR = "right";
            playerX += 5;
        }
        else if(upKeyPressed == true){
            playerY -= 5;
        }
        else if(downKeyPressed == true){
            playerY += 5;
        }
    }
    clear();
    redraw();
    document.addEventListener('keydown',function  (evt){
        if(event.keyCode == 68){
            hitbox = true;
        }
    });
    //The acctual game
    window.main = function (){
        window.requestAnimationFrame( main );
        checkCollisions();
        redraw();
        document.addEventListener('keydown',keyPressed);
        document.addEventListener('keyup',keyReleased);
        //Updates title screen Y
        titleY += Math.sin(0+(time*-0.5)*0.5);
        time += 0.5;
        playerMove();
    }
    main();  