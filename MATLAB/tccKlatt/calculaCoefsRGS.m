%%Funcoes para os coeficientes dos filtros do sintetizador de Klatt
function [A, B, C] = calculaCoefsRGS(AVS, Ta, BW)
    C = -exp(-2*pi*BW*Ta);
    %B = 2*exp(-pi*BW*Ta)*cos(2*pi*Fr*Ta);
    %A = 1 -B -C;
    A = AVS;
    B = 1 -A -C;
end