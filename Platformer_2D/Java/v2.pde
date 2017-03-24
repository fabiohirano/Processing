int w = 800;
int h = 600;

int[][] blocks = {

  //boundary box
  {
    0, -21, w, 20, 1
  }
  , 
  {
    0, h, w, 20, 1
  }
  , 
  {
    -21, 0, 20, h, 1
  }
  , 
  {
    w, 0, 20, h, 1
  }
  , 


  /*platforms*/

  {
    200, 570, 400, 30, 1
  },
  
  {
    200, 250, 400, 30, 1
  }

  , 
  {
    250, 540, 50, 30, 1
  }
  , 
  {
    500, 540, 50, 30, 1
  }
  , 
  {
    300, 500, 200, 10, 1
  }
  ,
  {
    600, 480, 200, 20, 1
  }
  ,
  {
    0, 480, 200, 20, 1
  }
  ,
  {
    375, 560, 50, 40, 0
  }
  ,
  {
    70, 470, 30, 10, 0
  }
  ,
  {
    0, 430, 20, 10, 1
  }
  ,
  {
    700, 470, 30, 10, 0
  }
  ,
  {
    780, 430, 20, 10, 1
  }
  ,
  {
    110, 380, 200, 20, 0
  }
  ,
  {
    490, 380, 200, 20, 2
  }
  ,
};

void setup() {
  size(800, 600);

  noStroke();
  noSmooth();
  frameRate(60);
}

float psize=20;
float px=w-psize;
float py=h-psize;
float rx=px;
float ry=py;
float pxv=0;
float pyv=0;
float pspeed=2;
float gravity=0;

boolean dead = false;
boolean falling = true;
boolean win = false;

void blockUpdate() {
  for (int i = 0; i<blocks.length; i++) {

    fill(100);

    if (blocks[i][4]==0) {
      fill(0, 250, 0);
    }
    
    if (blocks[i][4]==2) {
      fill(0, 0, 255);
    }

    
    if (px+pxv+psize>blocks[i][0] && 
        px+pxv<blocks[i][0]+blocks[i][2] && 
        py+psize>blocks[i][1] && 
        py<blocks[i][1]+blocks[i][3]) {
      if (blocks[i][4]==0) {
        dead=true;
      }
      if (blocks[i][4]==2) {
        win=true;
      }
      pxv=0;
    }

    if (px+psize>blocks[i][0] && 
        px<blocks[i][0]+blocks[i][2] && 
        py+pyv+psize>blocks[i][1] && 
        py<blocks[i][1]+blocks[i][3]) {
      if (blocks[i][4]==0) {
        dead=true;
      }
      if (blocks[i][4]==2) {
        win=true;
      }

      pyv=0;
      gravity=0;
      falling = false;
    }

    if (px+psize>blocks[i][0] && 
        px<blocks[i][0]+blocks[i][2] && 
        py+psize>blocks[i][1] && 
        py+pyv<blocks[i][1]+blocks[i][3]) {
      if (blocks[i][4]==0) {
        dead=true;
      }
      if (blocks[i][4]==2) {
        win=true;
      }

      pyv=0;
      gravity=0;
    }

    rect(blocks[i][0], blocks[i][1], blocks[i][2], blocks[i][3]);
  }
}

boolean[] keys = new boolean[256];

void keyPressed() {
  keys[keyCode]=true;
};

void keyReleased() {
  keys[keyCode]=false;
};

void playerInput() {
  pxv=0;
  pyv=0;


  if (dead==false) {
    if (keys[UP] && falling==false) {
      gravity-=7;
    }
    if (keys[LEFT]) {
      pxv=-pspeed;
    }
    if (keys[RIGHT]) {
      pxv=pspeed;
    }
  }
  
  if(keys[82]){
    dead=false;
    px=rx;
    py=ry;
  }
  
  pyv+=gravity;
  gravity+=0.3;

  falling = true;
}
void playerUpdate() {
  px+=pxv;
  py+=pyv;
  
  fill(255, 0, 0);
  if(dead==true){
    fill(255,150,150);
  }
  if(win==true){
    fill(150,150,255);
  }

  rect(px, py, psize, psize);
}

void draw() {
  background(250);

  playerInput();
  blockUpdate();
  playerUpdate();

  fill(255, 0, 0);
  text(frameRate, 20, 20);
}
