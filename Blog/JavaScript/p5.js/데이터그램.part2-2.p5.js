//**p5.js예제 코드입니다.

//**전역 변수(variables) 선언 영역

var y;                                            // --- Example4-1,2
y = 60; // y좌표값->원의 중심
var d = 80; // 지름

y = 100, d = 130                                  // --- Example4-2

var x = 25;                                       // --- Example4-4
var h = 20;
var y = 25;



//**셋업 함수 영역(한번만 실행 됨)

function setup(){
  createCanvas(480, 120);  

  fill(100, 100, 255);
  stroke(255, 100, 100);
  //strokeWeight(2);
  //noStroke();
  //480 = width, 120 = height 변수로 자동선언
}



//**드로우 함수 영역(반복해서 실행 됨)

function draw(){
  background(0);

  //**ellipse(x1, y1, 가로지름, 세로지름) 중심이 기준점
  //ellipse(75, y, d, d); // Left                    // --- Example4-1
  //ellipse(175, y, d, d); // Middle
  //ellipse(275, y, d, d); // Right
  //noFill();

  //**line(x1, y1, x2, y2) 시작점과 끝점의 좌표 입력
  //line(0, 0, width, height);                       // --- Example4-3
  //line(width, 0, 0, height);
  //ellipse(width/2, height/2, 60, 60);

  //** rect(x좌표, y좌표, 가로, 세로) 좌측상단이 기준점
  //x = 20;                                          // --- Example4-4
  //rect(x, y, 300, h); //Top
  //x = x + 100;
  //rect(x, y + h, 300, h); //Middle
  //x = x - 250;
  //rect(x, y + h*2, 300, h); //Bottom

  //재지정 된 x값을 rect함수 내에 바로 넣어도 됨
  //ex) rect(x - 250, y...)

  //line(20, 40, 80, 80);                            // --- Example4-5
  //line(80, 40, 140, 80);
  //line(140, 40, 200, 80);
  //line(200, 40, 260, 80);
  //line(260, 40, 320, 80);
  //line(320, 40, 380, 80);
  //line(380, 40, 440, 80);
  
  //for문 활용해서 루프 생성
  //for (var i = 20; i < 400; i += 20){
    //line(i, 40, i + 60, 80);                       // --- Example4-6,7     
    
    //line(i, 0, i + i/2, 80);                       // --- Example4-8,9
    
    //line(i + i/2, 80, i*1.2, 120)                  // --- Example4-9
  //}
  
  //for (var y = 0; y <= height; y += 40){           // --- Example4-10
    //for (var x = 0; x <= width; x += 40){
      //fill(255, 140, 100);
      //ellipse(x, y, 40, 40);
    //}
  //}
  
  //for (var y = 0; y < height + 45; y += 40){       // --- Example4-11
    //fill(255, 140,100, 100);
    //ellipse(0, y, 40, 40);    
  //}
  //for (var x = 0; x < width + 45; x += 40){
    //fill(255, 140, 150, 100);
    //ellipse(x, 0, 40, 40);
  //}  

  //2중 for 문
  for (var y = 20; y <= height-20; y += 20){           // --- Example4-12
    for (var x = 20; x <= width-20; x += 20){
      ellipse(x, y, 4, 4);
      line(x, y, 240, 60); //각 중심 - 캔버스 중심점을 잇는 선
      
      ellipse(x + y, y, 16 - y/10.0, 16 - y/10.0); // --- Example4-13

      x1 = mouseX;
      y1 = mouseY;
      ellipse(x + y, y, x1/20 - y/10.0 / 10, x1/20 - y/10.0)  // --- 추가연습
      fill(x1/4, y1/3, (x1+y1)/2)
    }
  }    
}


