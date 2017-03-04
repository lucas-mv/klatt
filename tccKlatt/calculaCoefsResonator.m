%%Funcoes para os coeficientes dos filtros do sintetizador de Klatt
function [A, B, C] = calculaCoefsResonator(Fr, Ta, BW)
    C = -exp(-2*pi*BW*Ta);
    B = 2*exp(-pi*BW*Ta)*cos(2*pi*Fr*Ta);
    A = 1 -B -C;
end