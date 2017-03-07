%%TESTE DE FUNCAO DE TRANSFERENCIA
clear
clc
pkg load control

fs = 8000;
f = 5;

f_filtro = (f*2*pi/fs);
num = f_filtro;
den = [1 f_filtro];
filtro = tf(num, den);

figure(1);
bode(filtro);

for i=1:fs
  x_senoide(i) = i;
  y_senoide(i) = sin(2*pi*f*x_senoide(i)/fs);
end

sim = lsim(filtro, y_senoide, x_senoide);

figure(2);
plot(x_senoide, y_senoide);

figure(3);
plot(sim);