from turtle import *;
#shape(colot)
color("blue", "red");
begin_fill(); #este metodo se llama antes de dibujar una forma que se va a rellenar
while True:
    forward(100);
    left(90);
    if abs(pos()) < 10:
        break;
end_fill();
done();
